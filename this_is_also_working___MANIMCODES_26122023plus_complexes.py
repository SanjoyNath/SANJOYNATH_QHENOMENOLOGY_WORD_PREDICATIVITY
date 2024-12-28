from manim import *

class ComplexValueTrackerExample(Scene):
    def construct(self):
        tracker = ComplexValueTracker(-2+1j)
        dot = Dot().add_updater(
            lambda x: x.move_to(tracker.points)
        )

        self.add(NumberPlane(), dot)

        self.play(tracker.animate.set_value(3+2j))
        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.play(tracker.animate.set_value(tracker.get_value() - 2j))
        self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py complexes.py
# # # Manim Community v0.18.1

# # # [12/28/24 08:30:12] ERROR                                                                                                                                                                        module_ops.py:92
                                # # # complexes.py is not in the script

                    # # # INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ComplexValueTrackerExample\1185818338_2136721613_1593896308.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ComplexValueTrackerExample\624642324_3764747626_61291841.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ComplexValueTrackerExample\624642324_312063386_2832991474.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ComplexValueTrackerExample\624642324_3515548462_3785237943.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ComplexValueTrackerExample.mp4'

                    # # # INFO     Rendered ComplexValueTrackerExample                                                                                                                                     scene.py:247
                             # # # Played 4 animations
# # # [12/28/24 08:30:13] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ComplexValueTrackerExample.mp4'        		







from manim import *

class ValueTrackerExample___fornafecadsmipa(Scene):
    def construct(self):
        number_line = NumberLine()
        pointer = Vector(DOWN)
        label = MathTex("NAFECADMIPA").add_updater(lambda m: m.next_to(pointer, UP))

        tracker = ValueTracker(0)
        pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                    )
        )
        self.add(number_line, pointer,label)
        tracker += 1.5
        self.wait(1)
        tracker -= 4
        self.wait(0.5)
        self.play(tracker.animate.set_value(5))
        self.wait(0.5)
        self.play(tracker.animate.set_value(3))
        self.play(tracker.animate.increment_value(-2))
        self.wait(0.5)
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py ValueTrackerExample
# # # Manim Community v0.18.1

# # # [12/28/24 08:31:43] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample\1185818338_2268332985_1511752868.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample\624642324_1959358871_3334515175.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample\624642324_3861126409_3823107490.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample\624642324_1959358871_2979222991.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample\624642324_2536411555_3826291144.mp4'
                    # # # INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample\624642324_220584453_1965914227.mp4'
                    # # # INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample\624642324_1959358871_881938112.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ValueTrackerExample.mp4'

                    # # # INFO     Rendered ValueTrackerExample                                                                                                                                            scene.py:247
                             # # # Played 7 animations
# # # [12/28/24 08:31:44] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ValueTrackerExample.mp4'  








# # # from manim import *

# # # class ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY(Scene):
    # # # def construct(self):
        # # # number_line = NumberLine()
        # # # pointerDNS = Vector(DOWN)
        # # # pointerUPS = Vector(DOWN)		
        # # # label_DNS = MathTex("NAFECADMIPA").add_updater(lambda m: m.next_to(pointerDNS, UP))
        # # # label_UPS = MathTex("NAFECADMIPA").add_updater(lambda m: m.next_to(pointerUPS, DOWN))
        # # # tracker = ValueTracker(0)
        # # # tracker_ANOTHER = ValueTracker(tracker)		
        # # # pointerDNS.add_updater(
            # # # lambda m: m.next_to(
                        # # # number_line.n2p(tracker.get_value()),
                        # # # UP
                    # # # )
        # # # )
        # # # pointerUPS.add_updater(
            # # # lambda m: m.next_to(
                        # # # number_line.n2p(tracker_ANOTHER.get_value()),
                        # # # UP
                    # # # )
        # # # )		
        # # # self.add(number_line, pointerDNS,pointerUPS,label_DNS,label_UPS)
        # # # tracker += 1.5
        # # # tracker_ANOTHER -=3.3
        # # # self.wait(1)
        # # # tracker -= 4
        # # # self.wait(0.5)
        # # # self.play(tracker.animate.set_value(5))
        # # # self.play(tracker_ANOTHER.animate.set_value(5))		
        # # # self.wait(0.5)
        # # # self.play(tracker.animate.set_value(3))
        # # # self.play(tracker_ANOTHER.animate.set_value(3))		
        # # # self.play(tracker.animate.increment_value(-2))
        # # # self.play(tracker_ANOTHER.animate.increment_value(+6))		
        # # # self.wait(0.5)



from manim import *

class ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY(Scene):
    def construct(self):
        number_line = NumberLine()
        pointerDNS = Vector(DOWN)
        pointerUPS = Vector(UP)  # Corrected the direction of the second pointer
        label_DNS = MathTex("NAFECADMIPA").add_updater(lambda m: m.next_to(pointerDNS, UP))
        label_UPS = MathTex("NAFECADMIPA").add_updater(lambda m: m.next_to(pointerUPS, DOWN))
        tracker = ValueTracker(0)
        tracker_ANOTHER = ValueTracker(0)  # Initialized with 0 instead of tracker
        
        pointerDNS.add_updater(
            lambda m: m.next_to(
                number_line.n2p(tracker.get_value()),
                UP
            )
        )
        pointerUPS.add_updater(
            lambda m: m.next_to(
                number_line.n2p(tracker_ANOTHER.get_value()),
                DOWN  # Corrected the direction to DOWN
            )
        )
        
        self.add(number_line, pointerDNS, pointerUPS, label_DNS, label_UPS)
        
        self.play(tracker.animate.set_value(1.5))
        self.play(tracker_ANOTHER.animate.set_value(-3.3))
        self.wait(1)
        
        self.play(tracker.animate.set_value(-4))
        self.wait(0.5)
        
        self.play(tracker.animate.set_value(5))
        self.play(tracker_ANOTHER.animate.set_value(5))
        self.wait(0.5)
        
        self.play(tracker.animate.set_value(3))
        self.play(tracker_ANOTHER.animate.set_value(3))
        
        self.play(tracker.animate.increment_value(-2))
        self.play(tracker_ANOTHER.animate.increment_value(6))
        self.wait(0.5)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY()
# # # scene.render()

# # # print("ValueTracker animation has been rendered.")
                         		
								
								
# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY
# # # Manim Community v0.18.1

# # # [12/28/24 08:40:23] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\1185818338_387992690
                             # # # 0_3495978113.mp4'
# # # [12/28/24 08:40:24] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_2463611710
                             # # # _2500799121.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_3890345977
                             # # # _3919757925.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_3707994901
                             # # # _1337429041.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_1959358871
                             # # # _391956735.mp4'
                    # # # INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_3461007072
                             # # # _2948796896.mp4'
                    # # # INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_2339041819
                             # # # _2399597011.mp4'
                    # # # INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_1959358871
                             # # # _543329960.mp4'
# # # [12/28/24 08:40:25] INFO     Animation 8 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_2536411555
                             # # # _246658204.mp4'
                    # # # INFO     Animation 9 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_2536411555
                             # # # _828488448.mp4'
                    # # # INFO     Animation 10 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_220584453_
                             # # # 2799453218.mp4'
                    # # # INFO     Animation 11 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_767158850_
                             # # # 3764339718.mp4'
                    # # # INFO     Animation 12 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY\624642324_1959358871
                             # # # _1277205187.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY.mp4'

                    # # # INFO     Rendered ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY                                                                                                  scene.py:247
                             # # # Played 13 animations
# # # [12/28/24 08:40:26] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY.mp4'                           file_ops.py:231
								
from manim import *
import random

class ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats(Scene):
    def construct(self):
        # Create a text at the top that fits within the screen width
        text = Text("SANJOY NATH MANIMATIONS NAFECADMIPA ORDERING QHENOMENOLOGY").scale_to_fit_width(config.frame_width - 1).to_edge(UP)
        self.add(text)  # Ensure the text remains on the screen	
		###https://sanjoynathgeometrifyingtrigonometry.blogspot.com/2024/10/nafcadmipa-or-nafcaia.html
        # Create a text at the top that fits within the screen width
        textLINKS = Text("https://sanjoynathgeometrifyingtrigonometry.blogspot.com/2024/10/nafcadmipa-or-nafcaia.html").scale_to_fit_width(config.frame_width - 1).to_edge(DOWN)
        self.add(textLINKS)  # Ensure the text remains on the screen			
        number_line1 = NumberLine()
        number_line2 = NumberLine().shift(DOWN *1.1)
        pointerDNS = Vector(DOWN)
        pointerUPS = Vector(UP)
        label_DNS = MathTex("NAFECADMIPA(INDIVIDUAL)").add_updater(lambda m: m.next_to(pointerDNS, UP))
        label_UPS = MathTex("NAFECADMIPA(SOCIETY)").add_updater(lambda m: m.next_to(pointerUPS, DOWN))
        tracker = ValueTracker(0)
        tracker_ANOTHER = ValueTracker(0)
        
        pointerDNS.add_updater(
            lambda m: m.next_to(
                number_line1.n2p(tracker.get_value()),
                UP
            )
        )
        pointerUPS.add_updater(
            lambda m: m.next_to(
                number_line2.n2p(tracker_ANOTHER.get_value()),
                DOWN
            )
        )
        
        self.add(number_line1, number_line2, pointerDNS, pointerUPS, label_DNS, label_UPS)
        
        for _ in range(11):
            new_value1 = random.uniform(-10, 10)
            new_value2 = random.uniform(-10, 10)
            self.play(tracker.animate.set_value(new_value1))
            self.play(tracker_ANOTHER.animate.set_value(new_value2))
            self.wait(0.5)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY()
# # # scene.render()

# # # print("ValueTracker animation has been rendered and repeated 6 times with random values.")					









# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats
# # # Manim Community v0.18.1

# # # [12/28/24 08:52:04] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\118581833
                             # # # 8_3331278106_1051975373.mp4'
# # # [12/28/24 08:52:05] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _2899270682_3671875390.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_1206142195.mp4'
# # # [12/28/24 08:52:06] INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _3199016173_1425500855.mp4'
# # # [12/28/24 08:52:07] INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1655656308_360974846.mp4'
                    # # # INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_3563091768.mp4'
# # # [12/28/24 08:52:08] INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _2980030245_1628762785.mp4'
                    # # # INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _2850419891_2229887310.mp4'
# # # [12/28/24 08:52:09] INFO     Animation 8 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_2993227745.mp4'
                    # # # INFO     Animation 9 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _3374743960_2553335763.mp4'
# # # [12/28/24 08:52:10] INFO     Animation 10 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _709740027_3801769826.mp4'
# # # [12/28/24 08:52:11] INFO     Animation 11 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_3421905996.mp4'
                    # # # INFO     Animation 12 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _3375293720_2250424296.mp4'
# # # [12/28/24 08:52:12] INFO     Animation 13 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1789054941_3040082105.mp4'
                    # # # INFO     Animation 14 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_1969604620.mp4'
# # # [12/28/24 08:52:13] INFO     Animation 15 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1389809180_3568331133.mp4'
# # # [12/28/24 08:52:14] INFO     Animation 16 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _599013297_1988438494.mp4'
                    # # # INFO     Animation 17 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_3732436163.mp4'
# # # [12/28/24 08:52:15] INFO     Animation 18 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _2625843907_1152379449.mp4'
                    # # # INFO     Animation 19 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _953634472_458660878.mp4'
# # # [12/28/24 08:52:16] INFO     Animation 20 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_289101033.mp4'
                    # # # INFO     Animation 21 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _3962129394_1610801435.mp4'
# # # [12/28/24 08:52:17] INFO     Animation 22 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _3412393217_3913900604.mp4'
# # # [12/28/24 08:52:18] INFO     Animation 23 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_3264535116.mp4'
                    # # # INFO     Animation 24 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1059601070_3795734621.mp4'
# # # [12/28/24 08:52:19] INFO     Animation 25 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _2075544579_1687639267.mp4'
                    # # # INFO     Animation 26 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_2430234108.mp4'
# # # [12/28/24 08:52:20] INFO     Animation 27 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _2908344755_3542550604.mp4'
# # # [12/28/24 08:52:21] INFO     Animation 28 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1257788567_4015163448.mp4'
                    # # # INFO     Animation 29 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_2800230081.mp4'
# # # [12/28/24 08:52:22] INFO     Animation 30 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _3389532766_2228961538.mp4'
                    # # # INFO     Animation 31 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _2538345382_2084356615.mp4'
# # # [12/28/24 08:52:23] INFO     Animation 32 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats\624642324
                             # # # _1959358871_1030012576.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats.mp4'

                    # # # INFO     Rendered ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats                                                                                       scene.py:247
                             # # # Played 33 animations
# # # [12/28/24 08:52:24] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats.mp4'                file_ops.py:231			


from manim import *

class ValueTrackerExample(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        label = Dot(radius=3).add_updater(lambda x : x.set_x(tracker.get_value()))
        self.add(label)
        self.add(tracker)
        tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(2)
		
		
		
		
		
		
from manim import *

class BasicUsage___VECTORFIELDS(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(ArrowVectorField(func))		
		
		
	
		
from manim import *

class SizingAndSpacing____VECTORFIELDS(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        vf = ArrowVectorField(func, x_range=[-7, 7, 1])
        self.add(vf)
        self.wait()

        length_func = lambda x: x / 3
        vf2 = ArrowVectorField(func, x_range=[-7, 7, 1], length_func=length_func)
        self.play(vf.animate.become(vf2))
        self.wait()		









































		
# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py SizingAndSpacing____VECTORFIELDS
# # # Manim Community v0.18.1

# # # [12/28/24 09:32:27] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\SizingAndSpacing____VECTORFIELDS\1185818338_123554531_2633937126.mp4'
# # # [12/28/24 09:32:28] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\SizingAndSpacing____VECTORFIELDS\624642324_1305941099_946576386.mp4'
# # # [12/28/24 09:32:29] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\SizingAndSpacing____VECTORFIELDS\624642324_1704852926_3936589389.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\SizingAndSpacing____VECTORFIELDS.mp4'

                    # # # INFO     Rendered SizingAndSpacing____VECTORFIELDS                                                                                                                               scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\SizingAndSpacing____VECTORFIELDS.mp4'  		
		
		
		
		
from manim import *

class Coloring___VECTORFIELDS(Scene):
    def construct(self):
        func = lambda pos: pos - LEFT * 5
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        min_radius = Circle(radius=2, color=colors[0]).shift(LEFT * 5)
        max_radius = Circle(radius=10, color=colors[-1]).shift(LEFT * 5)
        vf = ArrowVectorField(
            func, min_color_scheme_value=2, max_color_scheme_value=10, colors=colors
        )
        self.add(vf, min_radius, max_radius)		
		
		
		
		
		
		
		
		
from manim import *

class BasicUsage___STREAMLINES_VECTORFIELDS(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        self.add(StreamLines(func))		
		
from manim import *

class SpawningAndFlowingArea(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0]) * UR + np.cos(pos[1]) * LEFT + pos / 5
        stream_lines = StreamLines(
            func, x_range=[-3, 3, 0.2], y_range=[-2, 2, 0.2], padding=1
        )

        spawning_area = Rectangle(width=6, height=4)
        flowing_area = Rectangle(width=8, height=6)
        labels = [Tex("Spawning Area"), Tex("Flowing Area").shift(DOWN * 2.5)]
        for lbl in labels:
            lbl.add_background_rectangle(opacity=0.6, buff=0.05)

        self.add(stream_lines, spawning_area, flowing_area, *labels)		
		
		
from manim import *

class StreamLineCreation___FORVECTORFIELDS(Scene):
    def construct(self):
        func = lambda pos: (pos[0] * UR + pos[1] * LEFT) - pos
        stream_lines = StreamLines(
            func,
            color=YELLOW,
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            stroke_width=3,
            virtual_time=1,  # use shorter lines
            max_anchors_per_line=5,  # better performance with fewer anchors
        )
        self.play(stream_lines.create())  # uses virtual_time as run_time
        self.wait()		
		























		
# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py StreamLineCreation___FORVECTORFIELDS
# # # Manim Community v0.18.1

# # # [12/28/24 09:35:31] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\StreamLineCreation___FORVECTORFIELDS\1185818338_1631509482_2358810818.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\StreamLineCreation___FORVECTORFIELDS\624642324_1704852926_1411973521.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
# # # [12/28/24 09:35:32] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\StreamLineCreation___FORVECTORFIELDS.mp4'

                    # # # INFO     Rendered StreamLineCreation___FORVECTORFIELDS                                                                                                                           scene.py:247
                             # # # Played 2 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\StreamLineCreation___FORVECTORFIELDS.mp4'                     		
		
		
		
		
		
		
		
		



from manim import *

class EndAnimation(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(
            func, stroke_width=3, max_anchors_per_line=5, virtual_time=1, color=BLUE
        )
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5, time_width=0.5)
        self.wait(1)
        self.play(stream_lines.end_animation())		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py EndAnimation
# # # Manim Community v0.18.1

# # # [12/28/24 09:36:31] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\EndAnimation\1185818338_361662931_1585318367.mp4'
# # # [12/28/24 09:36:33] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\EndAnimation\624642324_2604881203_4227516557.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\EndAnimation.mp4'

                    # # # INFO     Rendered EndAnimation                                                                                                                                                   scene.py:247
                             # # # Played 2 animations
# # # [12/28/24 09:36:34] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\EndAnimation.mp4'      		





from manim import *

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=3, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)

		
		
		
		
		
		
		
		
		
		
from manim import *

class Nudging_______________VECTORFIELDS(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP
        vector_field = ArrowVectorField(
            func, x_range=[-7, 7, 1], y_range=[-4, 4, 1], length_func=lambda x: x / 2
        )
        self.add(vector_field)
        circle = Circle(radius=2).shift(LEFT)
        self.add(circle.copy().set_color(GRAY))
        dot = Dot().move_to(circle)

        vector_field.nudge(circle, -2, 60, True)
        vector_field.nudge(dot, -2, 60)

        circle.add_updater(vector_field.get_nudge_updater(pointwise=True))
        dot.add_updater(vector_field.get_nudge_updater())
        self.add(circle, dot)
        self.wait(6)		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py Nudging_______________VECTORFIELDS
# # # Manim Community v0.18.1

# # # [12/28/24 09:38:14] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\Nudging_______________VECTORFIELDS\1185818338_2003472962_1595467338.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\Nudging_______________VECTORFIELDS.mp4'

                    # # # INFO     Rendered Nudging_______________VECTORFIELDS                                                                                                                             scene.py:247
                             # # # Played 1 animations
# # # [12/28/24 09:38:15] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\Nudging_______________VECTORFIELDS.mp4'                                                      file_ops.py:231
		
		
		
from manim import *

class ScaleVectorFieldFunction(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 0.5)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()		
		
		
		
		
		
		
		
		
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py ScaleVectorFieldFunction
# # # Manim Community v0.18.1

# # # [12/28/24 09:39:19] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ScaleVectorFieldFunction\1185818338_123554531_2349182197.mp4'
# # # [12/28/24 09:39:22] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ScaleVectorFieldFunction\624642324_610595201_946576386.mp4'
# # # [12/28/24 09:39:23] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ScaleVectorFieldFunction\624642324_1704852926_2601964802.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ScaleVectorFieldFunction.mp4'

                    # # # INFO     Rendered ScaleVectorFieldFunction                                                                                                                                       scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\ScaleVectorFieldFunction.mp4'    		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ChangingCameraWidthAndRestore___SCENES(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))		
		
from manim import *

class MovingCameraCenter___IMPORTANT(MovingCameraScene):
    def construct(self):
        s = Square(color=RED, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 * RIGHT)
        self.wait(0.3)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t))		
		
		
		
		
		
		
from manim import *

class MovingAndZoomingCamera(MovingCameraScene):
    def construct(self):
        s = Square(color=BLUE, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=YELLOW, fill_opacity=0.5).move_to(2 * RIGHT)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s).set(width=s.width*2))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t).set(width=t.width*2))

        self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))		
		
		
from manim import *

class MovingCameraOnGraph(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=WHITE, x_range=[0, 3 * PI])

        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))
        self.add(ax, graph, dot_1, dot_2)

        self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
        self.play(self.camera.frame.animate.move_to(dot_2))
        self.play(Restore(self.camera.frame))
        self.wait()		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class SCENES___SoundExample(Scene):
    # Source of sound under Creative Commons 0 License. https://freesound.org/people/Druminfected/sounds/250551/
    def construct(self):
        dot = Dot().set_color(GREEN)
        self.add_sound("click.wav")
        self.add(dot)
        self.wait()
        self.add_sound("click.wav")
        dot.set_color(BLUE)
        self.wait()
        self.add_sound("click.wav")
        dot.set_color(RED)
        self.wait()		
		
		
		
		
		
		
		
		
		
		
		
		



# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py SCENES___SoundExample
# # # Manim Community v0.18.1

# # # ╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
# # # │ C:\Users\Sanjoy                                                                                  │
# # # │ Nath\AppData\Roaming\Python\Python312\site-packages\manim\cli\render\commands.py:120 in render   │
# # # │                                                                                                  │
# # # │   117 │   │   │   try:                                                                           │
# # # │   118 │   │   │   │   with tempconfig({}):                                                       │
# # # │   119 │   │   │   │   │   scene = SceneClass()                                                   │
# # # │ ❱ 120 │   │   │   │   │   scene.render()                                                         │
# # # │   121 │   │   │   except Exception:                                                              │
# # # │   122 │   │   │   │   error_console.print_exception()                                            │
# # # │   123 │   │   │   │   sys.exit(1)                                                                │
# # # │                                                                                                  │
# # # │ C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\scene\scene.py:229 in  │
# # # │ render                                                                                           │
# # # │                                                                                                  │
# # # │    226 │   │   """                                                                               │
# # # │    227 │   │   self.setup()                                                                      │
# # # │    228 │   │   try:                                                                              │
# # # │ ❱  229 │   │   │   self.construct()                                                              │
# # # │    230 │   │   except EndSceneEarlyException:                                                    │
# # # │    231 │   │   │   pass                                                                          │
# # # │    232 │   │   except RerunSceneException as e:                                                  │
# # # │                                                                                                  │
# # # │ D:\SANJOY_NATH_MANIMS\complexes.py:859 in construct                                              │
# # # │                                                                                                  │
# # # │   856 │   # Source of sound under Creative Commons 0 License. https://freesound.org/people/Dru   │
# # # │   857 │   def construct(self):                                                                   │
# # # │   858 │   │   dot = Dot().set_color(GREEN)                                                       │
# # # │ ❱ 859 │   │   self.add_sound("click.wav")                                                        │
# # # │   860 │   │   self.add(dot)                                                                      │
# # # │   861 │   │   self.wait()                                                                        │
# # # │   862 │   │   self.add_sound("click.wav")                                                        │
# # # │                                                                                                  │
# # # │ C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\scene\scene.py:1601 in │
# # # │ add_sound                                                                                        │
# # # │                                                                                                  │
# # # │   1598 │   │   if self.renderer.skip_animations:                                                 │
# # # │   1599 │   │   │   return                                                                        │
# # # │   1600 │   │   time = self.renderer.time + time_offset                                           │
# # # │ ❱ 1601 │   │   self.renderer.file_writer.add_sound(sound_file, time, gain, **kwargs)             │
# # # │   1602 │                                                                                         │
# # # │   1603 │   def on_mouse_motion(self, point, d_point):                                            │
# # # │   1604 │   │   self.mouse_point.move_to(point)                                                   │
# # # │                                                                                                  │
# # # │ C:\Users\Sanjoy                                                                                  │
# # # │ Nath\AppData\Roaming\Python\Python312\site-packages\manim\scene\scene_file_writer.py:343 in      │
# # # │ add_sound                                                                                        │
# # # │                                                                                                  │
# # # │   340 │   │   │   used there can be referenced here.                                             │
# # # │   341 │   │                                                                                      │
# # # │   342 │   │   """                                                                                │
# # # │ ❱ 343 │   │   file_path = get_full_sound_file_path(sound_file)                                   │
# # # │   344 │   │   new_segment = AudioSegment.from_file(file_path)                                    │
# # # │   345 │   │   if gain:                                                                           │
# # # │   346 │   │   │   new_segment = new_segment.apply_gain(gain)                                     │
# # # │                                                                                                  │
# # # │ C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\sounds.py:16 in  │
# # # │ get_full_sound_file_path                                                                         │
# # # │                                                                                                  │
# # # │   13                                                                                             │
# # # │   14 # Still in use by add_sound() function in scene_file_writer.py                              │
# # # │   15 def get_full_sound_file_path(sound_file_name):                                              │
# # # │ ❱ 16 │   return seek_full_path_from_defaults(                                                    │
# # # │   17 │   │   sound_file_name,                                                                    │
# # # │   18 │   │   default_dir=config.get_dir("assets_dir"),                                           │
# # # │   19 │   │   extensions=[".wav", ".mp3"],                                                        │
# # # │                                                                                                  │
# # # │ C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\file_ops.py:175  │
# # # │ in seek_full_path_from_defaults                                                                  │
# # # │                                                                                                  │
# # # │   172 │   │   f"From: {Path.cwd()}, could not find {file_name} at either "                       │
# # # │   173 │   │   f"of these locations: {list(map(str, possible_paths))}"                            │
# # # │   174 │   )                                                                                      │
# # # │ ❱ 175 │   raise OSError(error)                                                                   │
# # # │   176                                                                                            │
# # # │   177                                                                                            │
# # # │   178 def modify_atime(file_path: str) -> None:                                                  │
# # # ╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
# # # OSError: From: D:\SANJOY_NATH_MANIMS, could not find click.wav at either of these locations: ['click.wav', 'click.wav', 'click.wav.wav', 'click.wav.mp3']		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py LinearTransformationSceneExample
# # # Manim Community v0.18.1

# # # [12/28/24 09:46:05] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\LinearTransformationSceneExample\1185818338_1361870435_158190875.mp4'
# # # [12/28/24 09:46:06] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\LinearTransformationSceneExample\624642324_1704852926_1952365528.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\LinearTransformationSceneExample.mp4'

                    # # # INFO     Rendered LinearTransformationSceneExample                                                                                                                               scene.py:247
                             # # # Played 2 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\LinearTransformationSceneExample.mp4'                                                        file_ops.py:231
		
		
		
		
		
		
		
		
		
		
from manim import *
import random

class ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats_complicated(Scene):
    def construct(self):
        # Create a text at the top that fits within the screen width
        text = Text("SANJOY NATH MANIMATIONS NAFECADMIPA ORDERING QHENOMENOLOGY").scale_to_fit_width(config.frame_width - 1).to_edge(UP)
        self.add(text)  # Ensure the text remains on the screen	
        # Create a text at the top that fits within the screen width
        text_below = Text("N>A>F>E>C>A>D>M>I>P>A (JUXTAPOSITION CREATES DIFFERENT ORDERS IN NUMBERING").scale_to_fit_width(config.frame_width - 1).to_edge(UP)#I NEED IT TO PLACE THIS BELOW THE  text
		
        self.add(text_below)  # Ensure the text remains on the screen			
		###https://sanjoynathgeometrifyingtrigonometry.blogspot.com/2024/10/nafcadmipa-or-nafcaia.html
        # Create a text at the top that fits within the screen width
        textLINKS = Text("https://sanjoynathgeometrifyingtrigonometry.blogspot.com/2024/10/nafcadmipa-or-nafcaia.html").scale_to_fit_width(config.frame_width - 1)###.to_edge(DOWN)
        self.add(textLINKS)  # Ensure the text remains on the screen			
        number_line1 = NumberLine()
        number_line2 = NumberLine().shift(DOWN *1.1)#I NEED THE NUMBERS TO SHOW THERE
        pointerDNS = Vector(DOWN)
        pointerUPS = Vector(UP)
        label_DNS = MathTex("NAFECADMIPA(INDIVIDUAL)").add_updater(lambda m: m.next_to(pointerDNS, UP))
        label_UPS = MathTex("NAFECADMIPA(SOCIETY)").add_updater(lambda m: m.next_to(pointerUPS, DOWN))
        tracker = ValueTracker(0)
        tracker_ANOTHER = ValueTracker(0)#I NEED THE DYNAMICS TO DIVERGE THEN CONVERGE THEN DIVERGE CALIBRATION WITH COMPLICATED SYSTEMS AND ALSO NEED A VECTOR FIELDS FLOW WITH (tracker,tracker_ANOTHER) AS THE CALIBRATIONS DIVERGANCES AGAIN CONVERGANCES LIKE SYSTEMS
        
        pointerDNS.add_updater(
            lambda m: m.next_to(
                number_line1.n2p(tracker.get_value()),
                UP
            )
        )
        pointerUPS.add_updater(
            lambda m: m.next_to(
                number_line2.n2p(tracker_ANOTHER.get_value()),
                DOWN
            )
        )
        
        self.add(number_line1, number_line2, pointerDNS, pointerUPS, label_DNS, label_UPS)
        
        for _ in range(11):
            new_value1 = random.uniform(-10, 10)
            new_value2 = random.uniform(-10, 10)
            self.play(tracker.animate.set_value(new_value1))
            self.play(tracker_ANOTHER.animate.set_value(new_value2))
            self.wait(0.5)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY()
# # # scene.render()
		
		
		
		
		
		
		
		
		
		
		
		
		








from manim import *
import random

class ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats_complicated_convergances(Scene):
    def construct(self):
        # Create a text at the top that fits within the screen width
        text = Text("SANJOY NATH MANIMATIONS NAFECADMIPA ORDERING QHENOMENOLOGY").scale_to_fit_width(config.frame_width - 1).to_edge(UP)
        self.add(text)  # Ensure the text remains on the screen
        
        # Create a text below the first text
        text_below = Text("N>A>F>E>C>A>D>M>I>P>A (JUXTAPOSITION CREATES DIFFERENT ORDERS IN NUMBERING)").scale_to_fit_width(config.frame_width - 1).next_to(text, DOWN)
        self.add(text_below)  # Ensure the text remains on the screen
        
        # Add a link text
        textLINKS = Text("https://sanjoynathgeometrifyingtrigonometry.blogspot.com/2024/10/nafcadmipa-or-nafcaia.html").scale_to_fit_width(config.frame_width - 1).next_to(text_below, DOWN)
        self.add(textLINKS)  # Ensure the text remains on the screen
        
        number_line1 = NumberLine(include_numbers=True)
        number_line2 = NumberLine(include_numbers=True).shift(DOWN * 2)  # Shifted down to make space for the second number line
        pointerDNS = Vector(DOWN)
        pointerUPS = Vector(UP)
        label_DNS = MathTex("NAFECADMIPA(INDIVIDUAL)").add_updater(lambda m: m.next_to(pointerDNS, UP))
        label_UPS = MathTex("NAFECADMIPA(SOCIETY)").add_updater(lambda m: m.next_to(pointerUPS, DOWN))
        tracker = ValueTracker(0)
        tracker_ANOTHER = ValueTracker(0)
        
        pointerDNS.add_updater(
            lambda m: m.next_to(
                number_line1.n2p(tracker.get_value()),
                UP
            )
        )
        pointerUPS.add_updater(
            lambda m: m.next_to(
                number_line2.n2p(tracker_ANOTHER.get_value()),
                DOWN
            )
        )
        
        self.add(number_line1, number_line2, pointerDNS, pointerUPS, label_DNS, label_UPS)
        
        for _ in range(30):
            new_value1 = random.uniform(-10, 10)
            new_value2 = random.uniform(-10, 10)
            self.play(tracker.animate.set_value(new_value1))
            self.wait(1.3)	#i need this to make more complicated with depending on some dynamic variable t1 and show this t1 	below text_below	
            self.play(tracker_ANOTHER.animate.set_value(new_value2))
            self.wait(1.1) #i need this to make more complicated with depending on some dynamic variable t2=f(t1) and show this t2 beside t1 (in same line) 	below text_below	

# # # # Create an instance of the scene to trigger the construct method
# # # scene = ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats_complicated()
# # # scene.render()

# # # print("ValueTracker animation has been rendered and repeated 11 times with random values.")		









from manim import *
import random

class ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__60repeats_complicated_society(Scene):
    def construct(self):
        # Create a text at the top that fits within the screen width
        text = Text("SANJOY NATH MANIMATIONS NAFECADMIPA ORDERING QHENOMENOLOGY").scale_to_fit_width(config.frame_width - 1).to_edge(UP)
        self.add(text)  # Ensure the text remains on the screen
        
        # Create a text below the first text
        text_below = Text("N>A>F>E>C>A>D>M>I>P>A (JUXTAPOSITION CREATES DIFFERENT ORDERS IN NUMBERING)").scale_to_fit_width(config.frame_width - 1).next_to(text, DOWN)
        self.add(text_below)  # Ensure the text remains on the screen
        
        # Add a link text
        textLINKS = Text("https://sanjoynathgeometrifyingtrigonometry.blogspot.com/2024/10/nafcadmipa-or-nafcaia.html").scale_to_fit_width(config.frame_width - 1).next_to(text_below, DOWN)
        self.add(textLINKS)  # Ensure the text remains on the screen
        
        number_line1 = NumberLine(include_numbers=True)
        number_line2 = NumberLine(include_numbers=True).shift(DOWN * 2)  # Shifted down to make space for the second number line
        pointerDNS = Vector(DOWN)
        pointerUPS = Vector(UP)
        label_DNS = MathTex("NAFECADMIPA(INDIVIDUAL)").add_updater(lambda m: m.next_to(pointerDNS, UP))
        label_UPS = MathTex("NAFECADMIPA(SOCIETY)").add_updater(lambda m: m.next_to(pointerUPS, DOWN))
        tracker = ValueTracker(0)
        tracker_ANOTHER = ValueTracker(0)
        
        pointerDNS.add_updater(
            lambda m: m.next_to(
                number_line1.n2p(tracker.get_value()),
                UP
            )
        )
        pointerUPS.add_updater(
            lambda m: m.next_to(
                number_line2.n2p(tracker_ANOTHER.get_value()),
                DOWN
            )
        )
        
        self.add(number_line1, number_line2, pointerDNS, pointerUPS, label_DNS, label_UPS)

        t1_tracker = ValueTracker(0)
        t2_tracker = ValueTracker(0)

        t1_label = always_redraw(lambda: MathTex(f"t1={t1_tracker.get_value():.2f}").next_to(text_below, DOWN))
        t2_label = always_redraw(lambda: MathTex(f"t2={t2_tracker.get_value():.2f}").next_to(t1_label, RIGHT))

        self.add(t1_label, t2_label)
        
        for _ in range(60):
            new_value1 = random.uniform(-10, 10)
            new_value2 = random.uniform(-10, 10)
            t1_value = random.uniform(0.5, 1.5)
            t2_value = t1_value * random.uniform(0.8, 1.2)

            self.play(tracker.animate.set_value(new_value1), run_time=t1_value)
            self.play(t1_tracker.animate.set_value(t1_value), run_time=0.5)
            self.wait(0.5)

            self.play(tracker_ANOTHER.animate.set_value(new_value2), run_time=t2_value)
            self.play(t2_tracker.animate.set_value(t2_value), run_time=0.5)
            self.wait(0.5)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = ValueTrackerExample___fornafecadsmipa_INDIVIDUALS_AND_SOCIETY__11repeats_complicated_convergances()
# # # scene.render()

# # # print("ValueTracker animation has been rendered and repeated with dynamic variables t1 and t2.")


from manim import *

class TextAlignment___kmeansclusterings(Scene):
    def construct(self):
        title = Text("K-means clustering and Logistic Regression", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

        t1 = Text("1. Measuring").set_color(WHITE)

        t2 = Text("2. Clustering").set_color(WHITE)

        t3 = Text("3. Regression").set_color(WHITE)

        t4 = Text("4. Prediction").set_color(WHITE)

        x = VGroup(t1, t2, t3, t4).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).next_to(ORIGIN,DR)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)
		
		
from manim import *

class HomotopyExample(Scene):
    def construct(self):
        # Create a square mobject
        square = Square()

        # Define the homotopy function
        def homotopy(x, y, z, t):
            # Example transformation: a spiral effect
            new_x = x * np.cos(2 * PI * t) - y * np.sin(2 * PI * t)
            new_y = x * np.sin(2 * PI * t) + y * np.cos(2 * PI * t)
            new_z = z
            return new_x, new_y, new_z

        # Create the homotopy animation
        homotopy_animation = Homotopy(homotopy, square, run_time=5)

        # Add the square to the scene
        self.add(square)

        # Play the homotopy animation
        self.play(homotopy_animation)
		
		
		
		
		

# # # # Create an instance of the scene to trigger the construct method
# # # scene = HomotopyExample()
# # # scene.render()

# # # print("Homotopy animation has been rendered.")		

# # # Here's an example of how to use the Homotopy class in Manim to create an animation that transforms a Square mobject using a custom homotopy function:

from manim import *

class HomotopyExample(Scene):
    def construct(self):
        # Create a square mobject
        square = Square()

        # Define the homotopy function
        def homotopy(x, y, z, t):
            # Example transformation: a spiral effect
            new_x = x * np.cos(2 * PI * t) - y * np.sin(2 * PI * t)
            new_y = x * np.sin(2 * PI * t) + y * np.cos(2 * PI * t)
            new_z = z
            return new_x, new_y, new_z

        # Create the homotopy animation
        homotopy_animation = Homotopy(homotopy, square, run_time=5)

        # Add the square to the scene
        self.add(square)

        # Play the homotopy animation
        self.play(homotopy_animation)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = HomotopyExample()
# # # scene.render()

# # # print("Homotopy animation has been rendered.")
# # # In this example:

# # # We create a Square mobject.
# # # We define a homotopy function that applies a spiral transformation to the points of the square over time.
# # # We create a Homotopy animation using this function and the square, with a run time of 5 seconds.
# # # We add the square to the scene and play the homotopy animation.
# # # This will create an animation where the square undergoes a spiral transformation. You can customize the homotopy function to achieve different effects. Let me know if you need any further adjustments or additional examples!


from manim import *

class HomotopyExamplecomplexes(Scene):
    def construct(self):
        # Create a square mobject
        square = Square()

        # Define the first homotopy function
        def homotopy1(x, y, z, t):
            # Example transformation: a more complicated effect
            new_x = x * np.cos(2 * PI * t) - y * np.sin(2 * PI * t) + 0.5 * np.sin(PI * x * t)
            new_y = x * np.sin(2 * PI * t) + y * np.cos(2 * PI * t) + 0.5 * np.cos(PI * y * t)
            new_z = z + 0.5 * np.sin(PI * z * t)
            return new_x, new_y, new_z

        # Create the first homotopy animation
        homotopy_animation1 = Homotopy(homotopy1, square, run_time=5)

        # Add the square to the scene
        self.add(square)

        # Play the first homotopy animation
        self.play(homotopy_animation1)
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py HomotopyExample
# # # Manim Community v0.18.1

# # # [12/28/24 12:39:25] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\HomotopyExample\1185818338_374262934_3256495558.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\HomotopyExample.mp4'

                    # # # INFO     Rendered HomotopyExample                                                                                                                                                scene.py:247
                             # # # Played 1 animations
# # # [12/28/24 12:39:26] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\HomotopyExample.mp4'                                                                         file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py HomotopyExamplecomplexes
# # # Manim Community v0.18.1

# # # [12/28/24 12:42:45] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\HomotopyExamplecomplexes\1185818338_3358259806_3256495558.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\HomotopyExamplecomplexes\624642324_2446411796_3256495558.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\HomotopyExamplecomplexes.mp4'

                    # # # INFO     Rendered HomotopyExamplecomplexes                                                                                                                                       scene.py:247
                             # # # Played 2 animations
# # # [12/28/24 12:42:46] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\HomotopyExamplecomplexes.mp4'     		

        # Define the second homotopy function
        def homotopy2(x, y, z, t):
            # Example transformation: a wave effect
            new_x = x + 0.5 * np.sin(2 * PI * y * t)
            new_y = y + 0.5 * np.cos(2 * PI * x * t)
            new_z = z + 0.5 * np.sin(2 * PI * z * t)
            return new_x, new_y, new_z

        # Create the second homotopy animation
        homotopy_animation2 = Homotopy(homotopy2, square, run_time=5)

        # Play the second homotopy animation
        self.play(homotopy_animation2)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = HomotopyExample()
# # # scene.render()

# # # print("Homotopy animation has been rendered.")
# # # In this example:


from manim import *

class HomotopyExample3D(ThreeDScene):
    def construct(self):
        # Create a cube mobject
        cube = Cube()

        # Define the first homotopy function
        def homotopy1(x, y, z, t):
            # Example transformation: a more complicated 3D effect
            new_x = x * np.cos(2 * PI * t) - y * np.sin(2 * PI * t) + 0.5 * np.sin(PI * x * t)
            new_y = x * np.sin(2 * PI * t) + y * np.cos(2 * PI * t) + 0.5 * np.cos(PI * y * t)
            new_z = z + 0.5 * np.sin(PI * z * t) + 0.5 * np.cos(PI * x * t)
            return new_x, new_y, new_z

        # Create the first homotopy animation
        homotopy_animation1 = Homotopy(homotopy1, cube, run_time=5)

        # Add the cube to the scene
        self.add(cube)

        # Set the camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Play the first homotopy animation
        self.play(homotopy_animation1)

        # Define the second homotopy function
        def homotopy2(x, y, z, t):
            # Example transformation: a wave effect in 3D
            new_x = x + 0.5 * np.sin(2 * PI * y * t)
            new_y = y + 0.5 * np.cos(2 * PI * x * t)
            new_z = z + 0.5 * np.sin(2 * PI * z * t) + 0.5 * np.cos(2 * PI * y * t)
            return new_x, new_y, new_z

        # Create the second homotopy animation
        homotopy_animation2 = Homotopy(homotopy2, cube, run_time=5)

        # Play the second homotopy animation
        self.play(homotopy_animation2)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = HomotopyExample3D()
# # # scene.render()

# # # print("Homotopy animation in 3D has been rendered.")




# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py HomotopyExample3D
# # # Manim Community v0.18.1

# # # [12/28/24 12:45:36] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\HomotopyExample3D\1121228674_1389630596_2549660379.mp4'
# # # [12/28/24 12:45:37] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\HomotopyExample3D\3953065503_2083553045_2549660379.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\HomotopyExample3D.mp4'

                    # # # INFO     Rendered HomotopyExample3D                                                                                                                                              scene.py:247
                             # # # Played 2 animations
# # # [12/28/24 12:45:38] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\HomotopyExample3D.mp4'                                                                       file_ops.py:231


















# # # from manim import *
# # # import numpy as np

# # # class MultiSceneAnimation(Scene):
    # # # def construct(self):
        # # # # Scene 1: ApplyComplexFunction
        # # # circle = Circle()
        # # # self.add(circle)
        # # # self.wait(1)
        
        # # # def complex_func(z):
            # # # return np.exp(z)
        
        # # # self.play(ApplyComplexFunction(complex_func, circle), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 2: ApplyFunction
        # # # square = Square()
        # # # self.add(square)
        # # # self.wait(1)
        
        # # # def func(mobject):
            # # # mobject.set_fill(RED, opacity=0.5)
            # # # return mobject
        
        # # # self.play(ApplyFunction(func, square), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 3: ApplyMatrix
        # # # triangle = Triangle()
        # # # self.add(triangle)
        # # # self.wait(1)
        
        # # # matrix = [[1, 0.5], [-0.5, 1]]
        
        # # # self.play(ApplyMatrix(matrix, triangle), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 4: ApplyMethod
        # # # dot = Dot()
        # # # self.add(dot)
        # # # self.wait(1)
        
        # # # self.play(ApplyMethod(dot.shift, RIGHT * 2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 5: ApplyPointwiseFunction
        # # # line = Line(LEFT, RIGHT)
        # # # self.add(line)
        # # # self.wait(1)
        
        # # # def pointwise_func(p):
            # # # return p + np.array([np.sin(p[0]), np.cos(p[1]), 0])
        
        # # # self.play(ApplyPointwiseFunction(pointwise_func, line), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 6: ApplyPointwiseFunctionToCenter
        # # # star = Star()
        # # # self.add(star)
        # # # self.wait(1)
        
        # # # def pointwise_func_to_center(p):
            # # # return p * 0.5
        
        # # # self.play(ApplyPointwiseFunctionToCenter(pointwise_func_to_center, star), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 7: CyclicReplace
        # # # square2 = Square()
        # # # circle2 = Circle()
        # # # self.add(square2)
        # # # self.wait(1)
        
        # # # self.play(CyclicReplace(square2, circle2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 8: FadeToColor
        # # # self.play(FadeToColor(square2, color=BLUE), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 9: FadeTransform
        # # # self.play(FadeTransform(square2, circle2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 10: MoveToTarget
        # # # square2.generate_target()
        # # # square2.target.shift(UP * 2)
        # # # self.play(MoveToTarget(square2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 11: ReplacementTransform
        # # # self.play(ReplacementTransform(square2, circle2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 12: Restore
        # # # self.play(Restore(square2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 13: ScaleInPlace
        # # # self.play(ScaleInPlace(circle2, 2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 14: ShrinkToCenter
        # # # self.play(ShrinkToCenter(circle2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 15: Swap
        # # # self.play(Swap(square2, circle2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 16: Transform
        # # # self.play(Transform(square2, circle2), run_time=6)
        # # # self.wait(1)
        
        # # # # Scene 17: TransformFromCopy
        # # # self.play(TransformFromCopy(square2, circle2), run_time=6)
        # # # self.wait(1)

# # # class MultiSceneAnimation3D(ThreeDScene):
    # # # def construct(self):
        # # # # Scene 18: ClockwiseTransform
        # # # cube = Cube()
        # # # sphere = Sphere()
        
        # # # self.add(cube)
        # # # self.wait(1)
        
        # # # self.play(ClockwiseTransform(cube, sphere), run_time=6)
        # # # self.wait(1)

        # # # # Scene 19: CounterclockwiseTransform
        # # # cylinder = Cylinder()
        
        # # # self.add(sphere)
        # # # self.wait(1)
        
        # # # self.play(CounterclockwiseTransform(sphere, cylinder), run_time=6)
        # # # self.wait(1)

# # # # # # # Create instances of the scenes to trigger the construct methods
# # # scene_2d = MultiSceneAnimation()
# # # scene_2d.render()

# # # scene_3d = MultiSceneAnimation3D()
# # # scene_3d.render()

# # # # # # print("Multi-scene animation has been rendered.")


from manim import *
import numpy as np

class MultiSceneAnimation(Scene):
    def construct(self):
        # Scene 1: ApplyComplexFunction
        circle = Circle()
        self.add(circle)
        self.wait(1)
        
        def complex_func(z):
            return np.exp(z)
        
        self.play(ApplyComplexFunction(complex_func, circle), run_time=6)
        self.wait(1)
        
        # Scene 2: ApplyFunction
        square = Square()
        self.add(square)
        self.wait(1)
        
        def func(mobject):
            mobject.set_fill(RED, opacity=0.5)
            return mobject
        
        self.play(ApplyFunction(func, square), run_time=6)
        self.wait(1)
        
        # Scene 3: ApplyMatrix
        triangle = Triangle()
        self.add(triangle)
        self.wait(1)
        
        matrix = [[1, 0.5], [-0.5, 1]]
        
        self.play(ApplyMatrix(matrix, triangle), run_time=6)
        self.wait(1)
        
        # Scene 4: ApplyMethod
        dot = Dot()
        self.add(dot)
        self.wait(1)
        
        self.play(ApplyMethod(dot.shift, RIGHT * 2), run_time=6)
        self.wait(1)
        
        # Scene 5: ApplyPointwiseFunction
        line = Line(LEFT, RIGHT)
        self.add(line)
        self.wait(1)
        
        def pointwise_func(p):
            return p + np.array([np.sin(p[0]), np.cos(p[1]), 0])
        
        self.play(ApplyPointwiseFunction(pointwise_func, line), run_time=6)
        self.wait(1)
        
        # Scene 6: ApplyPointwiseFunctionToCenter
        star = Star()
        self.add(star)
        self.wait(1)
        
        def pointwise_func_to_center(p):
            return p * 0.5
        
        self.play(star.animate.apply_function(pointwise_func_to_center), run_time=6)
        self.wait(1)
        
        # Scene 7: CyclicReplace
        square2 = Square()
        circle2 = Circle()
        self.add(square2)
        self.wait(1)
        
        self.play(CyclicReplace(square2, circle2), run_time=6)
        self.wait(1)
        
        # Scene 8: FadeToColor
        self.play(FadeToColor(square2, color=BLUE), run_time=6)
        self.wait(1)
        
        # Scene 9: FadeTransform
        self.play(FadeTransform(square2, circle2), run_time=6)
        self.wait(1)
        
        # Scene 10: MoveToTarget
        square2.generate_target()
        square2.target.shift(UP * 2)
        self.play(MoveToTarget(square2), run_time=6)
        self.wait(1)
        
        # Scene 11: ReplacementTransform
        self.play(ReplacementTransform(square2, circle2), run_time=6)
        self.wait(1)
        
        # Scene 12: Restore
        self.play(Restore(square2), run_time=6)
        self.wait(1)
        
        # Scene 13: ScaleInPlace
        self.play(ScaleInPlace(circle2, 2), run_time=6)
        self.wait(1)
        
        # Scene 14: ShrinkToCenter
        self.play(ShrinkToCenter(circle2), run_time=6)
        self.wait(1)
        
        # Scene 15: Swap
        self.play(Swap(square2, circle2), run_time=6)
        self.wait(1)
        
        # Scene 16: Transform
        self.play(Transform(square2, circle2), run_time=6)
        self.wait(1)
        
        # Scene 17: TransformFromCopy
        self.play(TransformFromCopy(square2, circle2), run_time=6)
        self.wait(1)

class MultiSceneAnimation3D(ThreeDScene):
    def construct(self):
        # Scene 18: ClockwiseTransform
        cube = Cube()
        sphere = Sphere()
        
        self.add(cube)
        self.wait(1)
        
        self.play(ClockwiseTransform(cube, sphere), run_time=6)
        self.wait(1)

        # Scene 19: CounterclockwiseTransform
        cylinder = Cylinder()
        
        self.add(sphere)
        self.wait(1)
        
        self.play(CounterclockwiseTransform(sphere, cylinder), run_time=6)
        self.wait(1)

# Create instances of the scenes to trigger the construct methods
scene_2d = MultiSceneAnimation()
scene_2d.render()

scene_3d = MultiSceneAnimation3D()
scene_3d.render()

###print("Multi-scene animation has been rendered.")



# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py MultiSceneAnimation
# # # Manim Community v0.18.1

# # # [12/28/24 13:33:58] INFO     Animation 0 : Using cached data (hash : 1185818338_2268332985_2060486491)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_63241171_1460023451)                                                                                          cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_3890345977_1043529420)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 3 : Using cached data (hash : 624642324_3890345977_3600282299)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 4 : Using cached data (hash : 624642324_2125777041_2415023254)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 5 : Using cached data (hash : 624642324_3890345977_886792461)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 6 : Using cached data (hash : 624642324_3890345977_1861001153)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 7 : Using cached data (hash : 624642324_1167715677_3106411273)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 8 : Using cached data (hash : 624642324_3890345977_2906073145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 9 : Using cached data (hash : 624642324_3890345977_941961985)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 10 : Using cached data (hash : 624642324_2350679632_799328855)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 11 : Using cached data (hash : 624642324_3890345977_217165145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 12 : Using cached data (hash : 624642324_3890345977_3513142638)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 13 : Using cached data (hash : 624642324_3436067318_3432709773)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 14 : Using cached data (hash : 624642324_3890345977_2408899354)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 15 : Using cached data (hash : 624642324_3890345977_238718090)                                                                                        cairo_renderer.py:88
# # # [12/28/24 13:33:59] INFO     Animation 16 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_398221284_717161843.mp4'
                    # # # INFO     Animation 17 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_2619114263.mp4'
                    # # # INFO     Animation 18 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_3084609313.mp4'
                    # # # INFO     Animation 19 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_2387690381_1927439422.mp4'
                    # # # INFO     Animation 20 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_2030747358.mp4'
                    # # # INFO     Animation 21 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_2118750530_127054679.mp4'
                    # # # INFO     Animation 22 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_1397751589.mp4'
# # # [12/28/24 13:34:00] INFO     Animation 23 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3409890605_161504147.mp4'
                    # # # INFO     Animation 24 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_400725032.mp4'
                    # # # INFO     Animation 25 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_927891157_1682000012.mp4'
                    # # # INFO     Animation 26 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_1063311697.mp4'
                    # # # INFO     Animation 27 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3264638863_2489752592.mp4'
                    # # # INFO     Animation 28 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_4165165893.mp4'
                    # # # INFO     Animation 29 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3387904903_580151393.mp4'
                    # # # INFO     Animation 30 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_1085775272.mp4'
# # # [12/28/24 13:34:01] INFO     Animation 31 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3298877490_4044041034.mp4'
                    # # # INFO     Animation 32 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_376259515.mp4'
                    # # # INFO     Animation 33 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_147712628_1063803792.mp4'
                    # # # INFO     Animation 34 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_2051298840.mp4'
                    # # # INFO     Animation 35 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_890465092_3206147009.mp4'
                    # # # INFO     Animation 36 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_954793410.mp4'
# # # [12/28/24 13:34:02] INFO     Animation 37 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_4465427_3945779336.mp4'
                    # # # INFO     Animation 38 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_1218773594.mp4'
                    # # # INFO     Animation 39 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_858943078_312165726.mp4'
                    # # # INFO     Animation 40 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_3890345977_957419685.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation                                                                                                                                            scene.py:247
                             # # # Played 41 animations
# # # [12/28/24 13:34:03] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231
                    # # # INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation3D\2550307886_4205520711_3191113035.mp4'
# # # [12/28/24 13:34:12] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation3D\2732211768_3677837834_2489902782.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation3D\2732211768_3438219438_763773924.mp4'
# # # [12/28/24 13:34:13] INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation3D\2732211768_3438219438_146634568.mp4'
# # # [12/28/24 13:34:25] INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation3D\2732211768_2480820327_157005399.mp4'
# # # [12/28/24 13:34:26] INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation3D\2732211768_3438219438_2074757775.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation3D                                                                                                                                          scene.py:247
                             # # # Played 6 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231
                    # # # INFO     Animation 0 : Using cached data (hash : 1185818338_2268332985_2060486491)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_729743218_1460023451.mp4'
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_3890345977_1043529420)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 3 : Using cached data (hash : 624642324_3890345977_3600282299)                                                                                        cairo_renderer.py:88
# # # [12/28/24 13:34:27] INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_110460379_2415023254.mp4'
                    # # # INFO     Animation 5 : Using cached data (hash : 624642324_3890345977_886792461)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 6 : Using cached data (hash : 624642324_3890345977_1861001153)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_1044838714_3106411273.mp4'
                    # # # INFO     Animation 8 : Using cached data (hash : 624642324_3890345977_2906073145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 9 : Using cached data (hash : 624642324_3890345977_941961985)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 10 : Using cached data (hash : 624642324_2350679632_799328855)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 11 : Using cached data (hash : 624642324_3890345977_217165145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 12 : Using cached data (hash : 624642324_3890345977_3513142638)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 13 : Using cached data (hash : 624642324_3436067318_3432709773)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 14 : Using cached data (hash : 624642324_3890345977_2408899354)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 15 : Using cached data (hash : 624642324_3890345977_238718090)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 16 : Using cached data (hash : 624642324_398221284_717161843)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 17 : Using cached data (hash : 624642324_3890345977_2619114263)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 18 : Using cached data (hash : 624642324_3890345977_3084609313)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 19 : Using cached data (hash : 624642324_2387690381_1927439422)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 20 : Using cached data (hash : 624642324_3890345977_2030747358)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 21 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\MultiSceneAnimation\624642324_1072402591_127054679.mp4'
                    # # # INFO     Animation 22 : Using cached data (hash : 624642324_3890345977_1397751589)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 23 : Using cached data (hash : 624642324_3409890605_161504147)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 24 : Using cached data (hash : 624642324_3890345977_400725032)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 25 : Using cached data (hash : 624642324_927891157_1682000012)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 26 : Using cached data (hash : 624642324_3890345977_1063311697)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 27 : Using cached data (hash : 624642324_3264638863_2489752592)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 28 : Using cached data (hash : 624642324_3890345977_4165165893)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 29 : Using cached data (hash : 624642324_3387904903_580151393)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 30 : Using cached data (hash : 624642324_3890345977_1085775272)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 31 : Using cached data (hash : 624642324_3298877490_4044041034)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 32 : Using cached data (hash : 624642324_3890345977_376259515)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 33 : Using cached data (hash : 624642324_147712628_1063803792)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 34 : Using cached data (hash : 624642324_3890345977_2051298840)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 35 : Using cached data (hash : 624642324_890465092_3206147009)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 36 : Using cached data (hash : 624642324_3890345977_954793410)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 37 : Using cached data (hash : 624642324_4465427_3945779336)                                                                                          cairo_renderer.py:88
# # # [12/28/24 13:34:28] INFO     Animation 38 : Using cached data (hash : 624642324_3890345977_1218773594)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 39 : Using cached data (hash : 624642324_858943078_312165726)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 40 : Using cached data (hash : 624642324_3890345977_957419685)                                                                                        cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation                                                                                                                                            scene.py:247
                             # # # Played 41 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py MultiSceneAnimation3D
# # # Manim Community v0.18.1

# # # [12/28/24 13:34:45] INFO     Animation 0 : Using cached data (hash : 1185818338_2268332985_2060486491)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_63241171_1460023451)                                                                                          cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_3890345977_1043529420)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 3 : Using cached data (hash : 624642324_3890345977_3600282299)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 4 : Using cached data (hash : 624642324_2125777041_2415023254)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 5 : Using cached data (hash : 624642324_3890345977_886792461)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 6 : Using cached data (hash : 624642324_3890345977_1861001153)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 7 : Using cached data (hash : 624642324_1167715677_3106411273)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 8 : Using cached data (hash : 624642324_3890345977_2906073145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 9 : Using cached data (hash : 624642324_3890345977_941961985)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 10 : Using cached data (hash : 624642324_2350679632_799328855)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 11 : Using cached data (hash : 624642324_3890345977_217165145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 12 : Using cached data (hash : 624642324_3890345977_3513142638)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 13 : Using cached data (hash : 624642324_3436067318_3432709773)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 14 : Using cached data (hash : 624642324_3890345977_2408899354)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 15 : Using cached data (hash : 624642324_3890345977_238718090)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 16 : Using cached data (hash : 624642324_398221284_717161843)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 17 : Using cached data (hash : 624642324_3890345977_2619114263)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 18 : Using cached data (hash : 624642324_3890345977_3084609313)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 19 : Using cached data (hash : 624642324_2387690381_1927439422)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 20 : Using cached data (hash : 624642324_3890345977_2030747358)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 21 : Using cached data (hash : 624642324_2118750530_127054679)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 22 : Using cached data (hash : 624642324_3890345977_1397751589)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 23 : Using cached data (hash : 624642324_3409890605_161504147)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 24 : Using cached data (hash : 624642324_3890345977_400725032)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 25 : Using cached data (hash : 624642324_927891157_1682000012)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 26 : Using cached data (hash : 624642324_3890345977_1063311697)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 27 : Using cached data (hash : 624642324_3264638863_2489752592)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 28 : Using cached data (hash : 624642324_3890345977_4165165893)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 29 : Using cached data (hash : 624642324_3387904903_580151393)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 30 : Using cached data (hash : 624642324_3890345977_1085775272)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 31 : Using cached data (hash : 624642324_3298877490_4044041034)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 32 : Using cached data (hash : 624642324_3890345977_376259515)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 33 : Using cached data (hash : 624642324_147712628_1063803792)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 34 : Using cached data (hash : 624642324_3890345977_2051298840)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 35 : Using cached data (hash : 624642324_890465092_3206147009)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 36 : Using cached data (hash : 624642324_3890345977_954793410)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 37 : Using cached data (hash : 624642324_4465427_3945779336)                                                                                          cairo_renderer.py:88
# # # [12/28/24 13:34:46] INFO     Animation 38 : Using cached data (hash : 624642324_3890345977_1218773594)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 39 : Using cached data (hash : 624642324_858943078_312165726)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 40 : Using cached data (hash : 624642324_3890345977_957419685)                                                                                        cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation                                                                                                                                            scene.py:247
                             # # # Played 41 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231
                    # # # INFO     Animation 0 : Using cached data (hash : 2550307886_4205520711_3191113035)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 2732211768_3677837834_2489902782)                                                                                       cairo_renderer.py:88
# # # [12/28/24 13:34:47] INFO     Animation 2 : Using cached data (hash : 2732211768_3438219438_763773924)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 3 : Using cached data (hash : 2732211768_3438219438_146634568)                                                                                        cairo_renderer.py:88
# # # [12/28/24 13:34:48] INFO     Animation 4 : Using cached data (hash : 2732211768_2480820327_157005399)                                                                                        cairo_renderer.py:88
# # # [12/28/24 13:34:49] INFO     Animation 5 : Using cached data (hash : 2732211768_3438219438_2074757775)                                                                                       cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation3D                                                                                                                                          scene.py:247
                             # # # Played 6 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231
                    # # # INFO     Animation 0 : Using cached data (hash : 2550307886_4205520711_3191113035)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 2732211768_3677837834_2489902782)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 2732211768_3438219438_763773924)                                                                                        cairo_renderer.py:88
# # # [12/28/24 13:34:50] INFO     Animation 3 : Using cached data (hash : 2732211768_3438219438_146634568)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 4 : Using cached data (hash : 2732211768_2480820327_157005399)                                                                                        cairo_renderer.py:88
# # # [12/28/24 13:34:51] INFO     Animation 5 : Using cached data (hash : 2732211768_3438219438_2074757775)                                                                                       cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation3D                                                                                                                                          scene.py:247
                             # # # Played 6 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>


from manim import *

class ThreeDCameraExample(ThreeDScene):
    def construct(self):
        # Set up the 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create 3D objects
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE).shift(LEFT * 2)
        cube = Cube(side_length=1, color=RED).shift(RIGHT * 2)
        cone = Cone(base_radius=1, height=2, direction=UP, color=GREEN).shift(UP * 2)

        # Add objects to the scene
        self.add(axes, sphere, cube, cone)

        # Rotate the camera around the objects
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()

        # Zoom in and out
        self.play(self.camera.frame.animate.scale(0.5), run_time=3)
        self.wait(1)
        self.play(self.camera.frame.animate.scale(2), run_time=3)
        self.wait(1)

        # Change camera orientation
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait(1)
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=3)
        self.wait(1)

# Create an instance of the scene to trigger the construct method
scene = ThreeDCameraExample()
scene.render()

###print("ThreeDCamera animation has been rendered.")








# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py ThreeDCameraExample
# # # Manim Community v0.18.1

# # # [12/28/24 13:56:43] INFO     Animation 0 : Using cached data (hash : 1185818338_2268332985_2060486491)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_63241171_1460023451)                                                                                          cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_3890345977_1043529420)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 3 : Using cached data (hash : 624642324_3890345977_3600282299)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 4 : Using cached data (hash : 624642324_2125777041_2415023254)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 5 : Using cached data (hash : 624642324_3890345977_886792461)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 6 : Using cached data (hash : 624642324_3890345977_1861001153)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 7 : Using cached data (hash : 624642324_1167715677_3106411273)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 8 : Using cached data (hash : 624642324_3890345977_2906073145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 9 : Using cached data (hash : 624642324_3890345977_941961985)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 10 : Using cached data (hash : 624642324_2350679632_799328855)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 11 : Using cached data (hash : 624642324_3890345977_217165145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 12 : Using cached data (hash : 624642324_3890345977_3513142638)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 13 : Using cached data (hash : 624642324_3436067318_3432709773)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 14 : Using cached data (hash : 624642324_3890345977_2408899354)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 15 : Using cached data (hash : 624642324_3890345977_238718090)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 16 : Using cached data (hash : 624642324_398221284_717161843)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 17 : Using cached data (hash : 624642324_3890345977_2619114263)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 18 : Using cached data (hash : 624642324_3890345977_3084609313)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 19 : Using cached data (hash : 624642324_2387690381_1927439422)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 20 : Using cached data (hash : 624642324_3890345977_2030747358)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 21 : Using cached data (hash : 624642324_2118750530_127054679)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 22 : Using cached data (hash : 624642324_3890345977_1397751589)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 23 : Using cached data (hash : 624642324_3409890605_161504147)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 24 : Using cached data (hash : 624642324_3890345977_400725032)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 25 : Using cached data (hash : 624642324_927891157_1682000012)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 26 : Using cached data (hash : 624642324_3890345977_1063311697)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 27 : Using cached data (hash : 624642324_3264638863_2489752592)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 28 : Using cached data (hash : 624642324_3890345977_4165165893)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 29 : Using cached data (hash : 624642324_3387904903_580151393)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 30 : Using cached data (hash : 624642324_3890345977_1085775272)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 31 : Using cached data (hash : 624642324_3298877490_4044041034)                                                                                       cairo_renderer.py:88
# # # [12/28/24 13:56:44] INFO     Animation 32 : Using cached data (hash : 624642324_3890345977_376259515)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 33 : Using cached data (hash : 624642324_147712628_1063803792)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 34 : Using cached data (hash : 624642324_3890345977_2051298840)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 35 : Using cached data (hash : 624642324_890465092_3206147009)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 36 : Using cached data (hash : 624642324_3890345977_954793410)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 37 : Using cached data (hash : 624642324_4465427_3945779336)                                                                                          cairo_renderer.py:88
                    # # # INFO     Animation 38 : Using cached data (hash : 624642324_3890345977_1218773594)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 39 : Using cached data (hash : 624642324_858943078_312165726)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 40 : Using cached data (hash : 624642324_3890345977_957419685)                                                                                        cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation                                                                                                                                            scene.py:247
                             # # # Played 41 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231
                    # # # INFO     Animation 0 : Using cached data (hash : 2550307886_4205520711_3191113035)                                                                                       cairo_renderer.py:88
# # # [12/28/24 13:56:45] INFO     Animation 1 : Using cached data (hash : 2732211768_3677837834_2489902782)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 2732211768_3438219438_763773924)                                                                                        cairo_renderer.py:88
# # # [12/28/24 13:56:46] INFO     Animation 3 : Using cached data (hash : 2732211768_3438219438_146634568)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 4 : Using cached data (hash : 2732211768_2480820327_157005399)                                                                                        cairo_renderer.py:88
# # # [12/28/24 13:56:47] INFO     Animation 5 : Using cached data (hash : 2732211768_3438219438_2074757775)                                                                                       cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation3D                                                                                                                                          scene.py:247
                             # # # Played 6 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231
# # # [12/28/24 13:57:17] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\partial_movie_files\ThreeDCameraExample\3799671348_2741840965_720704042.mp4'
# # # Traceback (most recent call last):
  # # # File "<frozen runpy>", line 198, in _run_module_as_main
  # # # File "<frozen runpy>", line 88, in _run_code
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\Scripts\manim.exe\__main__.py", line 7, in <module>
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1157, in __call__
    # # # return self.main(*args, **kwargs)
           # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1078, in main
    # # # rv = self.invoke(ctx)
         # # # ^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1688, in invoke
    # # # return _process_result(sub_ctx.command.invoke(sub_ctx))
                           # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1434, in invoke
    # # # return ctx.invoke(self.callback, **ctx.params)
           # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 783, in invoke
    # # # return __callback(*args, **kwargs)
           # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\cli\render\commands.py", line 116, in render
    # # # for SceneClass in scene_classes_from_file(file):
                      # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\module_ops.py", line 131, in scene_classes_from_file
    # # # module = get_module(file_path)
             # # # ^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\module_ops.py", line 54, in get_module
    # # # spec.loader.exec_module(module)
  # # # File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  # # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # # File "D:\SANJOY_NATH_MANIMS\complexes.py", line 2067, in <module>
    # # # scene.render()
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\scene\scene.py", line 229, in render
    # # # self.construct()
  # # # File "D:\SANJOY_NATH_MANIMS\complexes.py", line 2054, in construct
    # # # self.play(self.camera.frame.animate.scale(0.5), run_time=3)
              # # # ^^^^^^^^^^^^^^^^^
# # # AttributeError: 'ThreeDCamera' object has no attribute 'frame'

# # # D:\SANJOY_NATH_MANIMS>


from manim import *

class ThreeDVMobjectExample_saan(ThreeDScene):
    def construct(self):
        # Set up the 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create 3D objects with different styles
        sphere = Sphere(radius=1, color=BLUE).shift(LEFT * 3)
        cube = Cube(side_length=1, color=RED).shift(RIGHT * 3)
        cone = Cone(base_radius=1, height=2, direction=UP, color=GREEN).shift(UP * 2)
        torus = Torus(r1=1, r2=0.5, color=YELLOW).shift(DOWN * 2)

        # Add objects to the scene
        self.add(sphere, cube, cone, torus)

        # Rotate the camera around the objects
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()

        # Zoom in and out
        self.play(self.camera.frame.animate.scale(0.5), run_time=3)
        self.wait(1)
        self.play(self.camera.frame.animate.scale(2), run_time=3)
        self.wait(1)

        # Change camera orientation
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait(1)
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=3)
        self.wait(1)

# Create an instance of the scene to trigger the construct method
# # # scene = ThreeDVMobjectExample()
# # # scene.render()

###print("ThreeDVMobject animation has been rendered.")










# # # D:\SANJOY_NATH_MANIMS>manim -pql complexes.py ThreeDVMobjectExample_saan
# # # Manim Community v0.18.1

# # # [12/28/24 14:50:05] INFO     Animation 0 : Using cached data (hash : 1185818338_2268332985_2060486491)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_63241171_1460023451)                                                                                          cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_3890345977_1043529420)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 3 : Using cached data (hash : 624642324_3890345977_3600282299)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 4 : Using cached data (hash : 624642324_2125777041_2415023254)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 5 : Using cached data (hash : 624642324_3890345977_886792461)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 6 : Using cached data (hash : 624642324_3890345977_1861001153)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 7 : Using cached data (hash : 624642324_1167715677_3106411273)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 8 : Using cached data (hash : 624642324_3890345977_2906073145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 9 : Using cached data (hash : 624642324_3890345977_941961985)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 10 : Using cached data (hash : 624642324_2350679632_799328855)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 11 : Using cached data (hash : 624642324_3890345977_217165145)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 12 : Using cached data (hash : 624642324_3890345977_3513142638)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 13 : Using cached data (hash : 624642324_3436067318_3432709773)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 14 : Using cached data (hash : 624642324_3890345977_2408899354)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 15 : Using cached data (hash : 624642324_3890345977_238718090)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 16 : Using cached data (hash : 624642324_398221284_717161843)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 17 : Using cached data (hash : 624642324_3890345977_2619114263)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 18 : Using cached data (hash : 624642324_3890345977_3084609313)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 19 : Using cached data (hash : 624642324_2387690381_1927439422)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 20 : Using cached data (hash : 624642324_3890345977_2030747358)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 21 : Using cached data (hash : 624642324_2118750530_127054679)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 22 : Using cached data (hash : 624642324_3890345977_1397751589)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 23 : Using cached data (hash : 624642324_3409890605_161504147)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 24 : Using cached data (hash : 624642324_3890345977_400725032)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 25 : Using cached data (hash : 624642324_927891157_1682000012)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 26 : Using cached data (hash : 624642324_3890345977_1063311697)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 27 : Using cached data (hash : 624642324_3264638863_2489752592)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 28 : Using cached data (hash : 624642324_3890345977_4165165893)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 29 : Using cached data (hash : 624642324_3387904903_580151393)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 30 : Using cached data (hash : 624642324_3890345977_1085775272)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 31 : Using cached data (hash : 624642324_3298877490_4044041034)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 32 : Using cached data (hash : 624642324_3890345977_376259515)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 33 : Using cached data (hash : 624642324_147712628_1063803792)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 34 : Using cached data (hash : 624642324_3890345977_2051298840)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 35 : Using cached data (hash : 624642324_890465092_3206147009)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 36 : Using cached data (hash : 624642324_3890345977_954793410)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 37 : Using cached data (hash : 624642324_4465427_3945779336)                                                                                          cairo_renderer.py:88
                    # # # INFO     Animation 38 : Using cached data (hash : 624642324_3890345977_1218773594)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 39 : Using cached data (hash : 624642324_858943078_312165726)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 40 : Using cached data (hash : 624642324_3890345977_957419685)                                                                                        cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation                                                                                                                                            scene.py:247
                             # # # Played 41 animations
# # # [12/28/24 14:50:06] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231
                    # # # INFO     Animation 0 : Using cached data (hash : 2550307886_4205520711_3191113035)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 2732211768_3677837834_2489902782)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 2732211768_3438219438_763773924)                                                                                        cairo_renderer.py:88
# # # [12/28/24 14:50:07] INFO     Animation 3 : Using cached data (hash : 2732211768_3438219438_146634568)                                                                                        cairo_renderer.py:88
# # # [12/28/24 14:50:08] INFO     Animation 4 : Using cached data (hash : 2732211768_2480820327_157005399)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 5 : Using cached data (hash : 2732211768_3438219438_2074757775)                                                                                       cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
# # # [12/28/24 14:50:09] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'

                    # # # INFO     Rendered MultiSceneAnimation3D                                                                                                                                          scene.py:247
                             # # # Played 6 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\complexes\480p15\MultiSceneAnimation.mp4'                                                                     file_ops.py:231
# # # [12/28/24 14:50:10] INFO     Animation 0 : Using cached data (hash : 3799671348_2741840965_720704042)                                                                                        cairo_renderer.py:88
# # # Traceback (most recent call last):
  # # # File "<frozen runpy>", line 198, in _run_module_as_main
  # # # File "<frozen runpy>", line 88, in _run_code
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\Scripts\manim.exe\__main__.py", line 7, in <module>
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1157, in __call__
    # # # return self.main(*args, **kwargs)
           # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1078, in main
    # # # rv = self.invoke(ctx)
         # # # ^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1688, in invoke
    # # # return _process_result(sub_ctx.command.invoke(sub_ctx))
                           # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1434, in invoke
    # # # return ctx.invoke(self.callback, **ctx.params)
           # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 783, in invoke
    # # # return __callback(*args, **kwargs)
           # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\cli\render\commands.py", line 116, in render
    # # # for SceneClass in scene_classes_from_file(file):
                      # # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\module_ops.py", line 131, in scene_classes_from_file
    # # # module = get_module(file_path)
             # # # ^^^^^^^^^^^^^^^^^^^^^
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\module_ops.py", line 54, in get_module
    # # # spec.loader.exec_module(module)
  # # # File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  # # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # # File "D:\SANJOY_NATH_MANIMS\complexes.py", line 2067, in <module>
    # # # scene.render()
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\scene\scene.py", line 229, in render
    # # # self.construct()
  # # # File "D:\SANJOY_NATH_MANIMS\complexes.py", line 2054, in construct
    # # # self.play(self.camera.frame.animate.scale(0.5), run_time=3)
              # # # ^^^^^^^^^^^^^^^^^
# # # AttributeError: 'ThreeDCamera' object has no attribute 'frame'

# # # D:\SANJOY_NATH_MANIMS>


from manim import *

class LineGradientExample___Curvesasimplis(Scene):
    def construct(self):
        curve = ParametricFunction(lambda t: [t, np.sin(t), 0], t_range=[-PI, PI, 0.01], stroke_width=10)
        new_curve = CurvesAsSubmobjects(curve)
        new_curve.set_color_by_gradient(BLUE, RED)
        self.add(new_curve.shift(UP), curve)
		
		
		
		
		
		
from manim import *

class ComplexValueTrackerExample(Scene):
    def construct(self):
        tracker = ComplexValueTracker(0 + 0j)
        dot = Dot().add_updater(
            lambda x: x.move_to(complex_to_R3(tracker.get_value()))
        )

        self.add(NumberPlane(), dot)

        self.play(tracker.animate.set_value(3 + 2j))
        self.play(tracker.animate.set_value(tracker.get_value() * 1j))
        self.play(tracker.animate.set_value(tracker.get_value() - 2j))
        self.play(tracker.animate.set_value(tracker.get_value() / (-2 + 3j)))

class ThreeDVMobjectExample(ThreeDScene):
    def construct(self):
        # Set up the 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create 3D objects with different styles
        sphere = Sphere(radius=1, color=BLUE).shift(LEFT * 3)
        cube = Cube(side_length=1, color=RED).shift(RIGHT * 3)
        cone = Cone(base_radius=1, height=2, direction=UP, color=GREEN).shift(UP * 2)
        torus = Torus(r1=1, r2=0.5, color=YELLOW).shift(DOWN * 2)

        # Add objects to the scene
        self.add(sphere, cube, cone, torus)

        # Rotate the camera around the objects
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()

        # Zoom in and out
        self.play(self.camera.frame.animate.scale(0.5), run_time=3)
        self.wait(1)
        self.play(self.camera.frame.animate.scale(2), run_time=3)
        self.wait(1)

        # Change camera orientation
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait(1)
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=3)
        self.wait(1)

# # # # Create instances of the scenes to trigger the construct methods
# # # scene_2d = ComplexValueTrackerExample()
# # # scene_2d.render()

# # # scene_3d = ThreeDVMobjectExample()
# # # scene_3d.render()

# # # print("ComplexValueTracker and ThreeDVMobject animations have been rendered.")		


from manim import *
import mido
import tempfile
import os

class SoundExample_Automids(Scene):
    def construct(self):
        # Create a temporary MIDI file
        midi_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mid")
        midi_file.close()

        # Create a MIDI track
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        # Define the duration of each movement in seconds
        durations = [1, 1, 1]

        # Add MIDI notes corresponding to the movements
        for duration in durations:
            track.append(mido.Message('note_on', note=60, velocity=64, time=0))
            track.append(mido.Message('note_off', note=60, velocity=64, time=int(duration * 480)))

        # Save the MIDI file
        mid.save(midi_file.name)

        # Embed the MIDI file into the scene
        self.add_sound(midi_file.name)

        # Create and animate the dot
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(durations[0])
        
        self.add_sound(midi_file.name)
        dot.set_color(BLUE)
        self.wait(durations[1])
        
        self.add_sound(midi_file.name)
        dot.set_color(RED)
        self.wait(durations[2])

        # Clean up the temporary MIDI file
        os.remove(midi_file.name)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = SoundExample()
# # # scene.render()

# # # print("SoundExample animation with embedded MIDI file has been rendered.")

#####################yessssssssssssssssssssssssssssssssss generates the sounds
from manim import *
import mido
import tempfile
import os

class SoundExample_Automids(Scene):
    def construct(self):
        # Create a temporary MIDI file
        midi_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mid")
        midi_file.close()

        # Create a MIDI track
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)

        # Define the duration of each movement in seconds
        durations = [1, 1, 1]

        # Add MIDI notes corresponding to the movements
        for duration in durations:
            track.append(mido.Message('note_on', note=60, velocity=64, time=0))
            track.append(mido.Message('note_off', note=60, velocity=64, time=int(duration * 480)))

        # Save the MIDI file
        mid.save(midi_file.name)

        # Embed the MIDI file into the scene
        self.add_sound(midi_file.name)

        # Create and animate the dot
        dot = Dot().set_color(GREEN)
        self.add(dot)
        self.wait(durations[0])
        
        self.add_sound(midi_file.name)
        dot.set_color(BLUE)
        self.wait(durations[1])
        
        self.add_sound(midi_file.name)
        dot.set_color(RED)
        self.wait(durations[2])

        # Clean up the temporary MIDI file
        os.remove(midi_file.name)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = SoundExample()
# # # scene.render()

# # # print("SoundExample animation with embedded MIDI file has been rendered.")


# # # D:\SANJOY_NATH_MANIMS>manim -pql saansautomids.py SoundExample_Automids
# # # Manim Community v0.18.1

# # # [12/28/24 15:40:00] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\partial_movie_files\SoundExample_Automids\1185818338_2268332985_1279531144.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\partial_movie_files\SoundExample_Automids\624642324_3890345977_2352283492.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\partial_movie_files\SoundExample_Automids\624642324_3890345977_2392899484.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
# # # [12/28/24 15:40:01] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\SoundExample_Automids.mp4'

                    # # # INFO     Rendered SoundExample_Automids                                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\saansautomids\480p15\SoundExample_Automids.mp4'                                          