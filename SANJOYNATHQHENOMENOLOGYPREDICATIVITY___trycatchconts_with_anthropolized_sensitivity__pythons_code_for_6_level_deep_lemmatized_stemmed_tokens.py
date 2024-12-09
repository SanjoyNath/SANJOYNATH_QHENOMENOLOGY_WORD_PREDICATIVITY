import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict
from nltk.stem import WordNetLemmatizer, PorterStemmer
import pandas as pd
import re
import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

# Ensure you have the necessary NLTK data
try:
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('averaged_perceptron_tagger')
except Exception as e:
    logging.error(f"Error downloading NLTK data: {e}")

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Define sensitivity values for different POS categories
sensitivity_values = {
    'Adj all': 1, 'Adj pert': 2, 'Adj ppl': 3, 'Adv all': 4,
    'Noun act': 5, 'Noun animal': 6, 'Noun artifact': 7, 'Noun attribute': 8,
    'Noun body': 9, 'Noun cognition': 10, 'Noun communication': 11, 'Noun event': 12,
    'Noun feeling': 13, 'Noun food': 14, 'Noun group': 15, 'Noun location': 16,
    'Noun motive': 17, 'Noun object': 18, 'Noun person': 19, 'Noun phenomenon': 20,
    'Noun plant': 21, 'Noun possession': 22, 'Noun process': 23, 'Noun quantity': 24,
    'Noun relation': 25, 'Noun shape': 26, 'Noun state': 27, 'Noun substance': 28,
    'Noun time': 29, 'Noun tops': 30,
    'Verb body': 31, 'Verb change': 32, 'Verb cognition': 33, 'Verb communication': 34,
    'Verb competition': 35, 'Verb consumption': 36, 'Verb contact': 37, 'Verb creation': 38,
    'Verb emotion': 39, 'Verb motion': 40, 'Verb perception': 41, 'Verb possession': 42,
    'Verb social': 43, 'Verb stative': 44, 'Verb weather': 45
}

def tokenize_meaning(meaning):
    try:
        tokens = re.split(r'\W+', meaning.lower())
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        return lemmatized_tokens + stemmed_tokens
    except Exception as e:
        logging.error(f"Error in tokenize_meaning: {e}")
        return []

def recursive_token_analysis(word, depth=0, max_depth=6):
    if depth > max_depth:
        return 0
    try:
        synsets = wn.synsets(word)
        total_depth = 0
        counter = defaultdict(int)
        unique_tokens = set()
        
        for synset in synsets:
            tokens = tokenize_meaning(synset.definition())
            unique_tokens.update(tokens)
            for token in unique_tokens:
                total_depth += recursive_token_analysis(token, depth + 1, max_depth)
                counter[token] += sensitivity_values.get(synset.lexname(), 0)
        
        # Dump to text file at each depth stage
        try:
            with open(f"{word}_{depth}.txt", "w", encoding="utf-8") as f:
                f.write(f"Word: {word}\nDepth: {depth}\nTokens: {list(unique_tokens)}\nCounter: {dict(counter)}\n")
        except PermissionError as e:
            logging.error(f"Permission denied: {e}")
        except Exception as e:
            logging.error(f"Error writing to file: {e}")
        
        return total_depth + sum(counter.values())
    
    except Exception as e:
        logging.error(f"Error in recursive_token_analysis: {e}")
        return total_depth

def analyze_wordnet():
    try:
        words = set(lemma.name() for synset in wn.all_synsets() for lemma in synset.lemmas())
        word_depths = defaultdict(lambda: [0] * 7) # 7 levels of depth (0 to 6)
        
        for word in words:
            for depth in range(7):
                word_depths[word][depth] = recursive_token_analysis(word, depth, max_depth=6)
        
        return word_depths
    
    except Exception as e:
        logging.error(f"Error in analyze_wordnet: {e}")
        return {}

if __name__ == "__main__":
    try:
        word_depths = analyze_wordnet()
        
        with open("with_anthropology_sensitivity_weights_withcolabsrecursivedepthcheckingwordnets_py_depth_6_report_for_recursive_counters.txt", "w", encoding="utf-8") as f:
            for word, depths in word_depths.items():
                f.write(f"{word}###" + "###".join(map(str, depths)) + "\n")
        
        # Save to Excel
        df = pd.DataFrame.from_dict(word_depths, orient='index', columns=[f"Depth_{i}" for i in range(7)])
        df.index.name = "Word"
        df.reset_index(inplace=True)
        df.to_excel("with_anthropology_sensitivity_weights_withcolabsrecursivedepthcheckingwordnets_py_depth_6_report_for_recursive_counters.xlsx", index=False)
    
    except Exception as e:
        logging.error(f"Error in main execution: {e}")