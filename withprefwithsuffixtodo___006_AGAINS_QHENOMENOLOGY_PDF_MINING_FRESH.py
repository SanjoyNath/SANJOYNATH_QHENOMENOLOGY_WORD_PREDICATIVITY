import fitz  # PyMuPDF
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from collections import Counter, defaultdict
from nltk import pos_tag, word_tokenize, ngrams
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
from tkinter import Tk, filedialog
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import io
import string
import logging  # Import for logging errors
from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer for stemming
stemmer = PorterStemmer()
# Initialize NLP tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
# Set up logging to log errors to a file named 'error.log'
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Define POS categories in WordNet
pos_categories___in_wordnet = [
    'Adj all', 'Adj pert', 'Adj ppl', 'Adv all', 'Noun act', 'Noun animal', 'Noun artifact',
    'Noun attribute', 'Noun body', 'Noun cognition', 'Noun communication', 'Noun event',
    'Noun feeling', 'Noun food', 'Noun group', 'Noun location', 'Noun motive', 'Noun object',
    'Noun person', 'Noun phenomenon', 'Noun plant', 'Noun possession', 'Noun process',
    'Noun quantity', 'Noun relation', 'Noun shape', 'Noun state', 'Noun substance',
    'Noun time', 'Noun tops', 'Verb body', 'Verb change', 'Verb cognition', 'Verb communication',
    'Verb competition', 'Verb consumption', 'Verb contact', 'Verb creation', 'Verb emotion',
    'Verb motion', 'Verb perception', 'Verb possession', 'Verb social', 'Verb stative',
    'Verb weather'
]

# Generate text dump from PDF file using PyMuPDF where each sentence is dumped in a new line with page number and sentence counter
def generate_text_dump_from_pdf_pymupdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            sentences = page.get_text("text").split('.')
            for sentence_counter, sentence in enumerate(sentences, start=1):
                text += f"Page {page_num + 1}, Sentence {sentence_counter}: {sentence.strip()}\n"
        return text
    except Exception as e:
        logging.error(f"Error reading PDF file: {e}")
        return ""

# Create a new PDF with each page sized 60000x60000 pixels and footer text
def create_custom_pdf_with_footer(output_pdf_path, input_text, footer_text):
    try:
        doc = fitz.open()
        page = doc.new_page(width=60000, height=60000)
        
        # Add the input text to the first page
        text_rect = fitz.Rect(0, 0, 60000, 59000)
        page.insert_textbox(text_rect, input_text)
        
        # Add the footer text to each page
        footer_rect = fitz.Rect(0, 59000, 60000, 60000)
        page.insert_textbox(footer_rect, footer_text)
        
        doc.save(output_pdf_path)
    except Exception as e:
        logging.error(f"Error creating custom PDF: {e}")

# Generate and save a word cloud as an SVG and embed it in the first page of the PDF
def generate_and_embed_wordcloud(text, output_svg_path, output_pdf_path):
    try:
        # Generate word cloud and save as SVG
        wordcloud = WordCloud(width=800, height=400).generate(text)
        wordcloud.to_file(output_svg_path)
        
        # Embed the word cloud SVG in the first page of the PDF
        doc = fitz.open(output_pdf_path)
        page = doc.load_page(0)
        
        svg_image = svg2rlg(output_svg_path)
        img_data = io.BytesIO()
        renderPDF.drawToFile(svg_image, img_data)
        
        img_rect = fitz.Rect(0, 0, 800, 400)
        page.insert_image(img_rect, stream=img_data.getvalue())
        
        doc.save(output_pdf_path)
    except Exception as e:
        logging.error(f"Error generating and embedding word cloud: {e}")

# Generate pivot table with POS categories and their relatedness frequencies
def generate_pos_relatedness_pivot(pos_tagged_words, filename='pos_relatedness_pivot.csv'):
    # Initialize the pivot table with zeros
    pivot_table = pd.DataFrame(0, index=pos_categories___in_wordnet, columns=pos_categories___in_wordnet)
    
    # Iterate through sentences and update the pivot table
    for sentence in pos_tagged_words:
        pos_tags = [pos for _, pos in sentence]
        for i, pos1 in enumerate(pos_tags):
            for j, pos2 in enumerate(pos_tags):
                if pos1 in pos_categories___in_wordnet and pos2 in pos_categories___in_wordnet:
                    pivot_table.at[pos1, pos2] += 1
    
    # Save the pivot table as CSV
    pivot_table.to_csv(filename)

# Preprocess the text: tokenize, stem, lemmatize, and remove stopwords/punctuation
def preprocess_text_with_stemming(text):
    if text is None:
        return [], []
    words = word_tokenize(text.lower())
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words and word not in string.punctuation]
    stemmed_words = [stemmer.stem(word) for word in words if word not in stop_words and word not in string.punctuation]
    return lemmatized_words, stemmed_words

# Split text into manageable chunks for analysis
def chunk_text(text, chunk_size=10000):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i + chunk_size])

# Analyze text and create visual outputs
def analyze_text(text, pdf_path=None):
    if not text:
        logging.warning("No text to analyze.")
        print("No text to analyze.")
        return
    
    try:
        all_words = []
        all_pos_tags = []
        pos_tagged_words = []
        
        for chunk in chunk_text(text):
            words, _ = preprocess_text_with_stemming(chunk)
            pos_tags = pos_tag(words)
            all_words.extend(words)
            all_pos_tags.extend([tag for _, tag in pos_tags])
            pos_tagged_words.append(pos_tags)
        
        print("Text preprocessing and POS tagging completed.")
        
        relatedness = calculate_word_relatedness(all_words, window_size=60)
        export_graph_data_to_csv(relatedness)
        export_pos_frequencies_to_csv(all_pos_tags)
        
        print("Word relatedness and POS frequencies exported.")
        
        # Generate separate noun-to-noun and noun-to-verb reports
        generate_noun_to_noun_pivot_report(pos_tagged_words, relatedness)
        generate_noun_to_verb_pivot_report(pos_tagged_words, relatedness)
        
        print("Noun-to-noun and noun-to-verb pivot reports generated.")
        
        # Create visualizations and generate general pivot report
        visualize_word_graph(relatedness, calculate_word_frequencies(all_words))
        generate_pivot_report(pos_tagged_words, [])
        
        print("Visualizations and general pivot report generated.")
        
        # Generate POS relatedness pivot table
        generate_pos_relatedness_pivot(pos_tagged_words)
        
        print("POS relatedness pivot table generated.")
        
        if pdf_path:
            convert_svg_to_pdf('wordcloud.svg', pdf_path)
            print("Word cloud SVG converted to PDF.")
    
    except Exception as e:
        logging.error(f"Error during text analysis: {e}")
        print(f"An error occurred during text analysis: {e}")

# Main program function to load and analyze a text file or PDF file
def main():
    root = Tk()
    root.withdraw()
    
    try:
        # Prompt user to select a text file or PDF file
        file_path = filedialog.askopenfilename(title="Select Text or PDF File",
                                               filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
        if not file_path:
            print("No file selected. Exiting.")
            return
        
        if file_path.endswith('.pdf'):
            text = generate_text_dump_from_pdf_pymupdf(file_path)
        else:
            text = read_text_from_file(file_path)
        
        analyze_text(text)
    
    except Exception as e:
        logging.error(f"Error in main program: {e}")
        print("An error occurred.")

if __name__ == "__main__":
    main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
# # # Root, Prefix or Suffix	Meaning	Examples
# # # a, ac, ad, af, ag, al, an, ap, as, at	to, toward, near, in addition to, by	aside, accompany, adjust, aggression, allocate, annihilate, affix, associate, attend, adverb
# # # a-, an-	not, without	apolitical, atheist, anarchy, anonymous, apathy, aphasia, anemia
# # # ab, abs	away from, off	absolve, abrupt, absent
# # # -able, -ible	Adjective: worth, ability	solvable, incredible
# # # acer, acid, acri	bitter, sour, sharp	acerbic, acidity, acrid, acrimony
# # # act, ag	do, act, drive	active, react, agent, active, agitate
# # # acu	sharp	acute, acupuncture, accurate
# # # -acy, -cy	Noun: state or quality	privacy, infancy, adequacy, intimacy, supremacy
# # # -ade	act, product, sweet drink	blockade, lemonade
# # # aer, aero	air, atmosphere, aviation	aerial, aerosol, aerodrome
# # # ag, agi, ig, act	do, move, go	agent, agenda, agitate, navigate, ambiguous, action
# # # -age	Noun: activity, or result of action	courage, suffrage, shrinkage, tonnage
# # # agri, agro	pertaining to fields or soil	agriculture, agroindustry
# # # -al	Noun: action, result of action	referral, disavowal, disposal, festival
# # # -al, -ial, -ical	Adjective: quality, relation	structural, territorial, categorical
# # # alb, albo	white, without pigment	albino, albite
# # # ali, allo, alter	other	alias, alibi, alien, alloy, alter, alter ego, altruism
# # # alt	high, deep	altimeter, altitude
# # # am, ami, amor	love, like, liking	amorous, amiable, amicable, enamoured
# # # ambi	both	ambidextrous
# # # ambul	to walk	ambulatory, amble, ambulance, somnambulist
# # # -an	Noun: person	artisan, guardian, historian, magician
# # # ana, ano	up, back, again, anew	anode, anagram, anagenetic
# # # -ance, -ence	Noun: action, state, quality or process	resistance, independence, extravagance, fraudulence
# # # -ancy, -ency	Noun: state, quality or capacity	vacancy, agency, truancy, latency
# # # andr, andro	male, characteristics of men	androcentric, android
# # # ang	angular	angle
# # # anim	mind, life, spirit, anger	animal, animate, animosity
# # # ann, annu, enni	yearly	annual, annual, annuity, anniversary, perrenial
# # # -ant, -ent	Noun: an agent, something that performs the action	disinfectant, dependent, fragrant
# # # -ant, -ent, -ient	Adjective: kind of agent, indication	important, dependent, convenient
# # # ante	before	anterior, anteroom, antebellum, antedate, antecedent antediluvian
# # # anthrop	man	anthropology, misanthrope, philanthropy
# # # anti, ant	against, opposite	antisocial, antiseptic, antithesis, antibody, antinomies, antifreeze, antipathy
# # # anti, antico	old	antique, antiquated, antiquity
# # # apo, ap, aph	away from, detached, formed	apology, apocalypse, aphagia
# # # aqu	water	aqueous
# # # -ar, -ary	Adjective: resembling, related to	spectacular, unitary
# # # arch	chief, first, rule	archangel, architect, archaic, monarchy, matriarchy, patriarchy, Archeozoic era
# # # -ard, -art	Noun: characterized	braggart, drunkard, wizard
# # # aster, astr	star	aster, asterisk, asteroid, astronomy, astronaut
# # # -ate	Noun: state, office, fuction	candidate, electorate, delegate
# # # -ate	Verb: cause to be	graduate, ameliorate, amputate, colligate
# # # -ate	Adjective: kind of state	inviolate
# # # -ation	Noun: action, resulting state	specialization, aggravation, alternation
# # # auc, aug, aut	to originate, to increase	augment , author, augment, auction
# # # aud, audi, aur, aus	to hear, listen	audience, audio, audible, auditorium, audiovisual, audition, auricular, ausculate
# # # aug, auc	increase	augur, augment, auction
# # # aut, auto	self	automobile, automatic, automotive, autograph, autonomous, autoimmune
# # # bar	weight, pressure	barometer
# # # be	on, around, over, about, excessively, make, cause, name, affect	berate, bedeck, bespeak, belittle, beleaguer
# # # belli	war	rebellion, belligerent, casus belli, bellicose
# # # bene	good, well, gentle	benefactor, beneficial, benevolent, benediction, beneficiary, benefit
# # # bi, bine	two	biped, bifurcate, biweekly, bivalve, biannual
# # # bibl, bibli, biblio	book	bibliophile, bibliography, Bible
# # # bio, bi	life	biography, biology, biometricsm biome, biosphere
# # # brev	short	abbreviate, brevity, brief
# # # cad, cap, cas, ceiv, cept, capt, cid, cip	to take, to seize, to hold	receive, deceive, capable, capacious, captive, accident, capture, occasion, concept, intercept, forceps, except, reciprocate
# # # cad, cas	to fall	cadaver, cadence, cascade
# # # -cade	procession	motorcade
# # # calor	heat	calorie, caloric, calorimeter
# # # capit, capt	head	decapitate, capital, captain, caption
# # # carn	flesh	carnivorous, incarnate, reincarnation, carnal
# # # cat, cata, cath	down, with	catalogue, category, catheter
# # # caus, caut	burn, heat	caustic, cauldron, cauterize
# # # cause, cuse, cus	cause, motive	because, excuse, accusation
# # # ceas, ced, cede, ceed, cess	to go, to yield, move, go, surrender	succeed, proceed, precede, recede, secession, exceed, succession
# # # cent	hundred	centennial, century, centipede
# # # centr, centri	center	eccentricity, centrifugal, concentric, eccentric
# # # chrom	color	chrome, chromosome, polychrome, chromatic
# # # chron	time	chronology, chronic, chronicle chronometer, anachronism, synchronize
# # # cide, cis, cise	to kill, to cut, cut down	fratricide, homicide, incision, incision, circumcision, scissors
# # # circum	around	circumnavigate, circumflex, circumstance, circumcision, circumference, circumorbital, circumlocution, circumvent, circumscribe, circulatory
# # # cit	call, start	incite, citation, cite
# # # civ	citizen	civic, civil, civilian, civilization
# # # clam, claim	cry out	exclamation, clamor, proclamation, reclamation, acclaim
# # # clin	lean, bend	decline, aclinic, inclination
# # # clud, clus claus	to close, shut	include, exclude, clause, claustrophobia, enclose, exclusive, reclusive, conclude
# # # co, cog, col, coll, con, com, cor	with, together	cohesiveness, cognate, collaborate, convene, commitment, compress, contemporary, converge, compact, confluence, convenient, concatenate, conjoin, combine, correct
# # # cogn, gnos	to know	recognize, cognizant, diagnose, agnostic, incognito, prognosis
# # # com, con	fully	complete, compel, conscious, condense, confess, confirm
# # # contr, contra, counter	against, opposite	contradict, counteract, contravene, contrary, counterspy, contrapuntal
# # # cord, cor, cardi	heart	cordial, concord, discord, courage, encourage
# # # corp	body	corporation, corporal punishment, corpse, corpulent, corpus luteum
# # # cort	correct	escort, cortage
# # # cosm	universe, world	cosmos, microcosm, cosmopolitan, cosmonaut
# # # cour, cur, curr, curs	run, course	occur, excursion, discourse, courier, course
# # # crat, cracy	rule	autocrat, aristocrat, theocracy, technocracy
# # # cre, cresc, cret, crease	grow	create, crescent, accretion, increase
# # # crea	create	creature, recreation, creation
# # # cred	believe	creed, credo, credence, credit, credulous, incredulous, incredible
# # # cresc, cret, crease, cru	rise, grow	crescendo, concrete, increase, decrease, accrue
# # # crit	separate, choose	critical, criterion, hypocrite
# # # cur, curs	run	current, concurrent, concur, incur, recur, occur, courier, precursor, cursive
# # # cura	care	curator, curative, manicure
# # # cycl, cyclo	wheel, circle, circular	Cyclops, unicycle, bicycle, cyclone, cyclic
# # # de-	from, down, away, to do the opposite, reverse, against	detach, deploy, derange, decrease, deodorize, devoid, deflate, degenerate
# # # dec, deca	ten, ten times	decimal, decade, decalogue, decimate, decathlon
# # # dec, dign	suitable	decent decorate dignity
# # # dei, div	God	divinity, divine, deity, divination, deify
# # # dem, demo	people, populace, population	democracy, demography, demagogue, epidemic
# # # dent, dont	tooth	dental, denture, orthodontist, periodontal
# # # derm	skin, covering	hypodermic, dermatology, epidermis, taxidermy
# # # di-, dy-	two, twice, double	divide, diverge, diglycerides
# # # dia	through, across, between	diameter, diagonal, dialogue dialect, dialectic, diagnosis, diachronic
# # # dic, dict, dit	say, speak	dictation, dictionary, dictate, dictator, Dictaphone, edict, predict, verdict, contradict, benediction
# # # dis, dif	not, opposite of, reverse, separate, deprive of, away	dismiss, differ, disallow, disperse, dissuade, divide, disconnect, disproportion, disrespect, distemper, disarray
# # # dit	give	credit, audit
# # # doc, doct	teach, prove	docile, doctor, doctrine, document, dogma, indoctrinate
# # # domin	master, that which is under control	dominate, dominion, predominant, domain
# # # don	give	donate, condone
# # # dorm	sleep	dormant, dormitory
# # # dox	thought, opinion, praise	orthodox, heterodox, paradox, doxology
# # # -drome	run, step	syndrome, aerodrome, velodrome
# # # duc, duct	to lead, pull	produce, abduct, product, transducer, viaduct, aqueduct, induct, deduct, reduce, induce
# # # dura	hard, lasting	durable, duration, endure
# # # dynam	power	dynamo, dynamic, dynamite, hydrodynamics
# # # dys-	bad, abnormal, difficult, impaired, unfavorable	dysfunctional, dyslexia, dyspathy
# # # e-	not, missing, out, fully, away, computer network related	emit, embed, eternal,ether, erase, email, e-tailer
# # # ec-	out of, outside	echo, eclipse, eclectic, ecesis, ecstasy, exzema
# # # eco-	household, environment, relating to ecology or economy	ecology, economize, ecospheres, ecomanagement
# # # ecto-	outside, external	ectomorph, ectoderm, ectoplasm
# # # -ed	Verb: past tense	dressed, faded, patted, closed, introduced
# # # -ed	Adjective: having the quality or characteristics of	winged, moneyed, dogged, tiered
# # # -en	Verb: to cause to become	lengthen, moisten, sharpen
# # # -en	Adjective: material	golden, woolen, silken
# # # en-, em-	put into, make, provide with, surround with	enamor, embolden, enslave, empower, entangle
# # # -ence, -ency	Noun: action or process, quality or state	reference, emergency, dependence, eminence, latency
# # # end-	inside, within	endorse, endocardial, endergonic, endoskeleton, endoscope, endogenous
# # # epi-	upon, close to, over, after, altered	epicenter, epicarp, epilogue, epigone, epidiorite
# # # equi-	equal	equidistant, equilateral, equilibrium, equinox, equation, equator
# # # -er, -ier	Adjective: comparative	better, brighter, sooner, hotter, happier
# # # -er, -or	Noun: person or thing that does something	flyer, reporter, player, member, fryer, collector, concentrator
# # # -er, -or	Verb: action	ponder, dishonor, clamor
# # # erg	work, effect	energy, erg, allergy, ergometer, ergograph, ergophobia
# # # -ery	collective qualities, art, practice, trade, collection, state, condition	snobbery, bakery, geenery, gallery, slavery
# # # -es, -ies	Noun: plural of most nouns ending in -ch, -s, -sh, -o and -z and some in -f and -y	passes, glasses, ladies, heroes
# # # -es, -ies	Verb: third person singular present indicative of verbs that end in -ch, -s, -sh, - and some in -y	blesses, hushes, fizzes, defies
# # # -ess	female	actress, goddess, poetess
# # # -est, -iest	Adjective or Adverb: superlative	latest, strongest, luckiest, lyingest
# # # ev-, et-	time, age	medieval, eternal
# # # ex-	out of, away from, lacking, former	exit, exhale, exclusive, exceed, explosion, ex-mayor
# # # exter-, extra-, extro-	outside of, beyond	external, extrinsic, extraordinary, extrapolate, extraneous, extrovert
# # # fa, fess	speak	fable, fabulous, fame, famous, confess, profess
# # # fac, fact, fec, fect, fic, fas, fea	do, make	difficult, fashion, feasible, feature, factory, fact, effect, manufacture, amplification, confection
# # # fall, fals	deceive	fallacy, falsify, fallacious
# # # femto	quadrillionth	femtosecond
# # # fer	bear, carry	ferry, coniferous, fertile, defer, infer, refer, transfer
# # # fic, feign, fain, fit, feat	shape, make, fashion	fiction, faint, feign
# # # fid	belief, faith	confide, diffident, fidelity
# # # fid, fide, feder	faith, trust	confidante, fidelity, confident, infidelity, infidel, federal, confederacy, semper fi
# # # fig	shape, form	figurem, effigy, figure, figment
# # # fila, fili	thread	filigree, filament, filter, filet, filibuster
# # # fin	end, ended, finished	final, finite, finish, confine, fine, refine, define, finale
# # # fix	repair, attach	fix, fixation, fixture, affix, prefix, suffix
# # # flex, flect	bend	flex, reflex, flexible, flexor, inflexibility, reflect, deflect,circumflex
# # # flict	strike	affliction, conflict, inflict
# # # flu, fluc, fluv, flux	flow	influence, fluid, flue, flush, fluently, fluctuate, reflux, influx
# # # -fold	Adverb: in a manner of, marked by	fourfold
# # # for, fore	before	forecast, fortune, foresee
# # # forc, fort	strength, strong	effort, fort, forte, fortifiable, fortify, forte, fortitude
# # # form	shape, resemble	form, format, conform, formulate, perform, formal, formula
# # # fract, frag, frai	break	fracture, infraction, fragile, fraction, refract, frail
# # # fuge	flee	subterfuge, refuge, centrifuge
# # # -ful	Noun: an amount or quanity that fills	mouthful
# # # -ful	Adjective: having, giving, marked by	fanciful
# # # fuse	pour	confuse, transfuse
# # # -fy	make, form into	falsify, dandify
# # # gam	marriage	bigamy, monogamy, polygamy
# # # gastr, gastro	stomach	gastric, gastronomic, gastritis, gastropod
# # # gen	kind	generous
# # # gen	birth, race, produce	genesis, genetics, eugenics, genealogy, generate, genetic, antigen, pathogen
# # # geo	earth	geometry, geography, geocentric, geology
# # # germ	vital part	germination, germ, germane
# # # gest	carry, bear	congest, gestation
# # # giga	billion	gigabyte, gigaflop
# # # gin	careful	gingerly
# # # gloss, glot	tongue	glossary, polyglot, epiglottis
# # # glu, glo	lump, bond, glue	glue, agglutinate, conglomerate
# # # gor	to gather, to bring together	category, categorize
# # # grad, gress, gree	to gather, to bring together, step, go	grade, degree, progress, gradual, graduate, egress
# # # graph, gram, graf	write, written, draw	graph, graphic, autograph, photography, graphite, telegram, polygraph, grammar, biography, lithograph, graphic
# # # grat	pleasing	congratulate, gratuity, grateful, ingrate
# # # grav	heavy, weighty	grave, gravity, aggravate, gravitate
# # # greg	herd	gregarious, congregation, segregate, gregarian
# # # hale, heal	make whole, sound	inhale, exhale, heal, healthy, healthiness
# # # helio	sun	heliograph, heliotrope, heliocentric
# # # hema, hemo	blood	hemorrhage, hemoglobin, hemophilia, hemostat
# # # her, here, hes	stick	adhere, cohere, cohesion, inherent, hereditary, hesitate
# # # hetero	other, different	heterodox, heterogeneous, heterosexual, heterodyne
# # # hex, ses, sex	six	hexagon, hexameter, sestet, sextuplets
# # # homo	same	homogenize, homosexual, homonym, homophone
# # # hum, human	earth, ground, man	humus, exhume, humane
# # # hydr, hydra, hydro	water	dehydrate, hydrant, hydraulic, hydraulics, hydrogen, hydrophobia
# # # hyper	over, above	hyperactive, hypertensive, hyperbolic, hypersensitive, hyperventilate, hyperkinetic
# # # hypn	sleep	hypnosis, hypnotherapy
# # # -ia	Noun: names, diseases	phobia
# # # -ian, an	Noun: related to, one that is	pedestrian, human
# # # -iatry	Noun: art of healing	psychiatry
# # # -ic	Adjective: quality, relation	generic
# # # -ic, ics	Noun: related to the arts and sciences	arithmetic, economics
# # # -ice	Noun: act	malice
# # # -ify	Verb: cause	specify
# # # ignis	fire	ignite, igneous, ignition
# # # -ile	Adjective: having the qualities of	projectile
# # # in, im	into, on, near, towards	instead, import
# # # in, im, il, ir	not	illegible, irresolute, inaction, inviolate, innocuous, intractable, innocent, impregnable, impossible, imposter
# # # infra	beneath	infrared, infrastructure
# # # -ing	Noun: material made for, activity, result of an activity	flooring, swimming, building
# # # -ing	Verb: present participle	depicting
# # # -ing	Adjective: activity	cohering
# # # inter	between, among	international, intercept, interject, intermission, internal, intermittent,
# # # intra	within, during, between layers, underneath	intramural, intranet, intranatal
# # # intro	into, within, inward	interoffice, introvert, introspection, introduce
# # # -ion	Noun: condition or action	abduction
# # # -ish	Adjective: having the character of	newish
# # # -ism	Noun: doctrine, belief, action or conduct	formalism
# # # -ist	Noun: person or member	podiatrist
# # # -ite	Noun: state or quality	graphite
# # # -ity, ty	Noun: state or quality	lucidity, novelty
# # # -ive	Noun: condition	native
# # # -ive, -ative, -itive	Adjective: having the quality of	festive, cooperative, sensitive
# # # -ize	Verb: cause	fantasize
# # # jac, ject	throw	reject, eject, project, trajectory, interject, dejected, inject, ejaculate, adjacent
# # # join, junct	join	adjoining, enjoin, juncture, conjunction, injunction, conjunction
# # # judice	judge	prejudice
# # # jug, junct, just	to join	junction, adjust, conjugal
# # # juven	young	juvenile, rejuvenate
# # # labor	work	laborious, belabor
# # # lau, lav, lot, lut	wash	launder, lavatory, lotion, ablution, dilute
# # # lect, leg, lig	choose, gather, select, read	collect, legible, eligible
# # # leg	law	legal, legislate, legislature, legitimize
# # # -less	Adjective: without, missing	motiveless
# # # levi	light	alleviate, levitate, levity
# # # lex, leag, leg	law	legal, college, league
# # # liber, liver	free	liberty, liberal, liberalize, deliverance
# # # lide	strike	collide, nuclide
# # # liter	letters	literary, literature, literal, alliteration, obliterate
# # # loc, loco	place, area	location, locally, locality, allocate, locomotion
# # # log, logo, ology	word, study, say, speech, reason, study	catalog, prologue, dialogue, zoology, logo
# # # loqu, locut	talk, speak	eloquent, loquacious, colloquial, circumlocution
# # # luc, lum, lun, lus, lust	light	translucent, luminary, luster, luna, illuminate, illustrate
# # # lude	play	prelude
# # # -ly	Adverb: in the manner of	fluently
# # # macr-, macer	lean	emaciated, meager
# # # magn	great	magnify, magnificent, magnanimous, magnate, magnitude, magnum
# # # main	strength, foremost	mainstream, mainsail, domain, remain
# # # mal	bad, badly	malformation, maladjusted, dismal, malady, malcontent,malfunction, malfeasance, maleficent
# # # man, manu	hand, make, do	manual, manage, manufacture, manacle, manicure, manifest, maneuver, emancipate, management
# # # mand	command	mandatory, remand, mandate
# # # mania	madness	mania, maniac, kleptomania, pyromania
# # # mar, mari, mer	sea, pool	marine, marsh, maritime, mermaid
# # # matri	mother	matrimony, maternal, matriarchate, matron
# # # medi	half, middle, between, halfway	mediate, medieval, Mediterranean, mediocre, medium
# # # mega	great, million	megaphone, megaton, megaflop, megalomaniac, megabyte, megalopolis
# # # mem	recall, remember	memo, commemoration, memento, memoir, memorable
# # # ment	mind	mental, mention
# # # -ment	Noun: condition or result	document
# # # meso	middle	mesomorph, mesoamerica, mesosphere
# # # meta	beyond, change	metaphor, metamorphosis, metabolism, metahistorical, metainformation
# # # meter	measure	meter, voltammeter, barometer, thermometer
# # # metr	admeasure, apportion	metrics, asymmetric, parametric, telemetry
# # # micro	small, millionth	microscope, microfilm, microcard, microwave, micrometer, microvolt
# # # migra	wander	migrate, emigrant, immigrate
# # # mill, kilo	thousand	millennium, kilobyte, kiloton
# # # milli	thousandth	millisecond, milligram, millivolt
# # # min	little, small	minute, minor, minuscule
# # # mis	wrong, bad, badly	misconduct, misinform, misinterpret, mispronounce, misnomer, mistake, misogynist
# # # mit, miss	send	emit, remit, submit, admit, commit, permit, transmit, omit, intermittent, mission, missile
# # # mob, mov, mot	move	motion, remove, mobile, motor
# # # mon	warn, remind	monument, admonition, monitor, premonition
# # # mono	one	monopoly, monotype, monologue, mononucleosis, monorail, monotheist,
# # # mor, mort	mortal, death	mortal, immortal, mortality, mortician, mortuary
# # # morph	shape, form	amorphous, dimorphic, metamorphosis, morphology, polymorphic, morpheme, amorphous
# # # multi	many, much	multifold, multilingual, multiped, multiply, multitude, multipurpose, multinational
# # # nano	billionth	nanosecond, nanobucks
# # # nasc, nat, gnant, nai	to be born	nascent, native, pregnant, naive
# # # nat, nasc	to be from, to spring forth	innate, natal, native, renaissance
# # # neo	new	Neolithic, nuveau riche, neologism, neophyte, neonate
# # # -ness	Noun: state, condition, quality	kindness
# # # neur	nerve	neuritis, neuropathic, neurologist, neural, neurotic
# # # nom	law, order	autonomy, astronomy, gastronomy, economy
# # # nom, nym	name	nominate, synonym
# # # nomen, nomin	name	nomenclature, nominate, ignominious
# # # non	nine	nonagon
# # # non	not	nonferrous, nonsense, nonabrasive, nondescript
# # # nov	new	novel, renovate, novice, nova, innovate
# # # nox, noc	night	nocturnal, equinox, noctilucent
# # # numer	number	numeral, numeration, enumerate, innumerable
# # # numisma	coin	numismatics
# # # ob, oc, of, op	toward, against, in the way	oppose, occur, offer, obtain
# # # oct	eight	octopus, octagon, octogenarian, octave
# # # oligo	few, little	Oligocene, oligosaccharide, oligotrophic, oligarchy
# # # omni	all, every	omnipotent, omniscient, omnipresent, omnivorous
# # # onym	name	anonymous, pseudonym, antonym, synonym
# # # oper	work	operate, cooperate, opus
# # # -or	Noun: condition or activity	valor, honor, humor, minor
# # # ortho	straight, correct	orthodox, orthodontist, orthopedic, unorthodox
# # # -ory	Noun: place for, serves for	territory, rectory
# # # -ous, -eous, -ose, -ious	Adjective: having the quality of, relating to	adventurous, courageous, verbose, fractious
# # # over	excessive, above	overwork, overall, overwork
# # # pac	peace	pacifist, pacify, pacific ocean
# # # pair, pare	arrange, assemblage, two	repair, impair, compare, prepare
# # # paleo	old	Paleozoic, Paleolithic, paleomagnetism, paleopsychology
# # # pan	all	Pan-American, pan-African, panacea, pandemonium (place of all the demons),
# # # para	beside	paradox, paraprofessional, paramedic, paraphrase, parachute
# # # pat, pass, path	feel, suffer	patient, passion, sympathy, pathology
# # # pater, patr	father	paternity, patriarch, patriot, patron, patronize
# # # path, pathy	feeling, suffering	pathos, sympathy, antipathy, apathy, telepathy
# # # ped, pod	foot	pedal, impede, pedestrian, centipede, tripod, podiatry, antipode, podium
# # # pedo	child	orthopedic, pedagogue, pediatrics
# # # pel, puls	drive, push, urge	compel, dispel, expel, repel, propel, pulse, impulse, pulsate, compulsory, expulsion, repulsive
# # # pend, pens, pond	hang, weigh	pendant, pendulum, suspend, appendage, pensive, append
# # # per	through, intensive	persecute, permit, perspire, perforate, persuade
# # # peri	around	periscope, perimeter, perigee, periodontal
# # # phage	eat	macrophage, bacteriophage
# # # phan, phas, phen, fan, phant, fant	show, make visible	phantom, fantasy
# # # phe	speak	blaspheme, cipher, phenomenon, philosopher
# # # phil	love	philosopher, philanthropy, philharmonic, bibliophile
# # # phlegma	inflammation	phlegm, phlegmatic
# # # phobia, phobos	fear	phobia, claustrophobia, acrophobia, aquaphobia, ergophobia, homophobia
# # # phon	sound	telephone, phonics, phonograph, phonetic, homophone, microphone, symphony, euphonious
# # # phot, photo	light	photograph, photoelectric, photogenic, photosynthesis, photon
# # # pico	trillionth	picofarad, picocurie, picovolt
# # # pict	paint, show, draw	picture, depict
# # # plac, plais	please	placid, placebo, placate, complacent
# # # pli, ply	fold	reply, implicate, ply
# # # plore	cry out, wail	implore, exploration, deploring
# # # plu, plur, plus	more	plural, pluralist, plus
# # # pneuma, pneumon	breath	pneumatic, pneumonia,
# # # pod	foot, feet	podiatry, tripod
# # # poli	city	metropolis, police, politics, Indianapolis, megalopolis, acropolis
# # # poly	many	polytheist, polygon, polygamy, polymorphous
# # # pon, pos, pound	place, put	postpone, component, opponent, proponent, expose, impose, deposit, posture, position, expound, impound
# # # pop	people	population, populous, popular
# # # port	carry	porter, portable, transport, report, export, import, support, transportation
# # # portion	part, share	portion, proportion
# # # post	after, behind	postpone, postdate
# # # pot	power	potential, potentate, impotent
# # # pre, pur	before	precede
# # # prehendere	seize, grasp	apprehend, comprehend, comprehensive, prehensile
# # # prin, prim, prime	first	primacy, prima donna, primitive, primary, primal, primeval, prince, principal
# # # pro	for, foward	propel
# # # proto	first	prototype, protocol, protagonist, protozoan, Proterozoic, protoindustrial
# # # psych	mind, soul	psyche, psychiatry, psychology, psychosis
# # # punct	point, dot	punctual, punctuation, puncture, acupuncture, punctuation
# # # pute	think	dispute, computer
# # # quat, quad	four	quadrangle, quadruplets
# # # quint, penta	five	quintet, quintuplets, pentagon, pentane, pentameter
# # # quip	ship	equip, equipment
# # # quir, quis, quest, quer	seek, ask	query, inquire, exquisite, quest
# # # re	back, again	report, realign, retract, revise, regain
# # # reg, recti	straighten	regiment, regular, rectify, correct, direct, rectangle
# # # retro	backwards	retrorocket, retrospect, retrogression, retroactive
# # # ri, ridi, risi	laughter	deride, ridicule, ridiculous, derision, risible
# # # rog, roga	ask	prerogative, interrogation, derogatory
# # # rupt	break	rupture, interrupt, abrupt, disrupt, ruptible
# # # sacr, sanc, secr	sacred	sacred, sacrosanct, sanction, consecrate, desecrate
# # # salv, salu	safe, healthy	salvation, salvage, salutation
# # # sanct	holy	sanctify, sanctuary, sanction, sanctimonious, sacrosanct
# # # sat, satis	enough	satient, saturate, satisfy
# # # sci, scio, scientia	know	science, conscious, omniscient, cognocienti
# # # scope	see, watch	telescope, microscope, kaleidoscope, periscope, stethoscope
# # # scrib, script	write	scribe, scribble, inscribe, describe, subscribe, prescribe, manuscript
# # # se	apart, move away from	secede
# # # sect, sec	cut	intersect, transect, dissect, secant, section
# # # sed, sess, sid	sit	sediment, session, obsession, possess, preside, president, reside, subside
# # # semi	half, partial	semifinal, semiconscious, semiannual, semimonthly, semicircle
# # # sen, scen	old, grow old	senior, senator, senile, senescence, evanescent
# # # sent, sens	feel, think	sentiment, consent, resent, dissent, sentimental, sense, sensation, sensitive, sensory, dissension
# # # sept	seven	septet, septennial
# # # sequ, secu, sue	follow	sequence, consequence, sequel, subsequent, prosecute, consecutive, second, ensue, pursue
# # # serv	save, serve, keep	servant, service, subservient, servitude, preserve, conserve, reservation, deserve, conservation, observe
# # # -ship	Noun: status, condition	relationship, friendship
# # # sign, signi	sign, mark, seal	signal, signature, design, insignia, significant
# # # simil, simul	like, resembling	similar, assimilate, simulate, simulacrum, simultaneous
# # # sist, sta, stit	stand, withstand, make up	assist, insist, persist, circumstance, stamina, status, state, static, stable, stationary, substitute
# # # soci	to join, companions	sociable, society
# # # sol, solus	alone	solo, soliloquy, solitaire, solitude, solitary, isolate
# # # solv, solu, solut	loosen, explain	solvent, solve, absolve, resolve, soluble, solution, resolution, resolute, dissolute, absolution
# # # somn	sleep	insomnia, somnambulist
# # # soph	wise	sophomore (wise fool), philosophy, sophisticated
# # # spec, spect, spi, spic	look, see	specimen, specific, spectator, spectacle, aspect, speculate, inspect, respect, prospect, retrospective, introspective, expect, conspicuous
# # # sper	render favorable	prosper
# # # sphere	ball, sphere	sphere, stratosphere, hemisphere, spheroid
# # # spir	breath	spirit, conspire, inspire, aspire, expire, perspire, respiration
# # # stand, stant, stab, stat, stan, sti, sta, st, stead	stand	stature, establish, stance
# # # -ster	person	mobster, monster
# # # strain, strict, string, stige	bind, pull, draw tight	stringent, strict, restrict, constrict, restrain, boa constrictor
# # # stru, struct, stroy, stry	build	construe, structure, construct, instruct, obstruct, destruction, destroy, industry, ministry
# # # sub, suc, suf, sup, sur, sus	under, below, from, secretly, instead of	sustain, survive, support, suffice, succeed, submerge, submarine, substandard, subnormal, subvert
# # # sume, sump	take, use, waste	consume, assume, sump, presumption
# # # super, supra	over, above	superior, suprarenal, superscript, supernatural, superimpose, supercede
# # # syn, sym	together, at the same time	sympathy, synthesis, synchronous, syndicate
# # # tact, tang, tag, tig, ting	touch	tactile, contact, intact, intangible, tangible, contagious, contiguous, contingent
# # # tain, ten, tent, tin	hold, keep, have	retain, continue, content, tenacious
# # # tect, teg	cover	detect, protect, tegular, tegument
# # # tele	distance, far, from afar	telephone, telegraph, telegram, telescope, television, telephoto, telecast, telepathy, telepathy
# # # tem, tempo	time	tempo, temporary, extemporaneously, contemporary, pro tem, temporal
# # # ten, tin, tain	hold	tenacious, tenant, tenure, untenable, detention, retentive, content, pertinent, continent, obstinate, contain, abstain, pertain, detain
# # # tend, tent, tens	stretch, strain	tendency, extend, intend, contend, pretend, superintend, tender, extent, tension, pretense
# # # tera	trillion	terabyte, teraflop
# # # term	end, boundary, limit	exterminate, terminal
# # # terr, terra	earth	terrain, terrarium, territory, terrestrial
# # # test	to bear witness	testament, detest, testimony, attest, testify
# # # the, theo	God, a god	monotheism, polytheism, atheism, theology
# # # therm	heat	thermometer, theorem, thermal, thermos bottle, thermostat, hypothermia
# # # thesis, thet	place, put	antithesis, hypothesis, synthesis, epithet
# # # tire	draw, pull	attire, retire, entire
# # # tom	cut	atom (not cutable), appendectomy, tonsillectomy, dichotomy, anatomy
# # # tor, tors, tort	twist	torture, retort, extort, distort, contort, torsion, tortuous, torturous
# # # tox	poison	toxic, intoxicate, antitoxin
# # # tract, tra, trai, treat	drag, draw, pull	attract, tractor, traction, extract, retract, protract, detract, subtract, contract, intractable
# # # trans	across, beyond, change	transform, transoceanic, transmit, transportation, transducer
# # # tri	three	tripod, triangle, trinity, trilateral
# # # trib	pay, bestow	tribute, contribute, attribute, retribution, tributary
# # # tribute	give	contribute, distribute, tributary
# # # turbo	disturb	turbulent, disturb, turbid, turmoil
# # # typ	print	type, prototype, typical, typography, typewriter, typology, typify
# # # ultima	last	ultimate, ultimatum
# # # umber, umbraticum	shadow	umbra, penumbra, (take) umbrage, adumbrate
# # # un	not, against, opposite	unceasing, unequal
# # # uni	one	uniform, unilateral, universal, unity, unanimous, unite, unison, unicorn
# # # -ure	Noun: act, condition, process, function	exposure, conjecture, measure
# # # vac	empty	vacate, vacuum, evacuate, vacation, vacant, vacuous
# # # vade	go	evade, invader
# # # vale, vali, valu	strength, worth	equivalent, valiant, validity, evaluate, value, valor
# # # veh, vect	to carry	vector, vehicle, convection, vehement
# # # ven, vent	come	convene, intervene, venue, convenient, avenue, circumvent, invent, convent, venture, event, advent, prevent
# # # ver, veri	true	very, aver, verdict, verity, verify, verisimilitude
# # # verb, verv	word	verify, veracity, verbalize, verve
# # # vert, vers	turn, change	convert, revert, advertise, versatile, vertigo, invert, reversion, extravert, introvert, diversion, introvert, convertible, reverse, controversy
# # # vi	way	viable, vibrate, vibrant
# # # vic, vicis	change, substitute	vicarious, vicar, vicissitude
# # # vict, vinc	conquer	victor, evict, convict, convince, invincible
# # # vid, vis	see	video, evident, provide, providence, visible, revise, supervise, vista, visit, vision, review, indivisible
# # # viv, vita, vivi	alive, life	revive, survive, vivid, vivacious, vitality, vivisection, vital, vitamins, revitalize
# # # voc, voke	call	vocation, avocation, convocation, invocation, evoke, provoke, revoke, advocate, provocative, vocal
# # # vol	will	malevolent, benevolent, volunteer, volition
# # # volcan	fire	volcano, vulcanize, Vulcan
# # # volv, volt, vol	turn about, roll	revolve, voluble, voluminous, convolution, revolt, evolution
# # # vor	eat greedily	voracious, carnivorous, herbivorous, omnivorous, devour
# # # -ward	Adverb: in a direction or manner	homeward
# # # -wise	Adverb: in the manner of, with regard to	timewise, clockwise, bitwise
# # # with	against	withhold, without, withdraw, forthwith
# # # -y	Noun: state, condition, result of an activity	society, victory
# # # -y	Adjective: marked by, having	hungry, angry, smeary, teary
# # # zo	animal	zoo (zoological garden), zoology, zodiac, protozoan