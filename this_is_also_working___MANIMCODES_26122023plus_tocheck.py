from manim import *
################################################not playing
class PointCloudDotExample2(Scene):
    def construct(self):
        plane = ComplexPlane()
        cloud = PointCloudDot(color=RED)
        self.add(
            plane, cloud
        )
        self.wait()
        self.play(
            cloud.animate.apply_complex_function(lambda z: np.exp(z))
        )	
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql tocheck.py PointCloudDotExample2
# # # Manim Community v0.18.1

# # # [12/28/24 08:19:59] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\PointCloudDotExample2\1185818338_123554531_1291582345.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\PointCloudDotExample2\624642324_1108809418_448977266.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\PointCloudDotExample2.mp4'

                    # # # INFO     Rendered PointCloudDotExample2                                                                                                                                          scene.py:247
                             # # # Played 2 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\PointCloudDotExample2.mp4'         




from manim import *

class ShapesWithVDict(Scene):
    def construct(self):
        square = Square().set_color(RED)
        circle = Circle().set_color(YELLOW).next_to(square, UP)

        # create dict from list of tuples each having key-mobject pair
        pairs = [("s", square), ("c", circle)]
        my_dict = VDict(pairs, show_keys=True)

        # display it just like a VGroup
        self.play(Create(my_dict))
        self.wait()

        text = Tex("Some text").set_color(GREEN).next_to(square, DOWN)

        # add a key-value pair by wrapping it in a single-element list of tuple
        # after attrs branch is merged, it will be easier like `.add(t=text)`
        my_dict.add([("t", text)])
        self.wait()

        rect = Rectangle().next_to(text, DOWN)
        # can also do key assignment like a python dict
        my_dict["r"] = rect

        # access submobjects like a python dict
        my_dict["t"].set_color(PURPLE)
        self.play(my_dict["t"].animate.scale(3))
        self.wait()

        # also supports python dict styled reassignment
        my_dict["t"] = Tex("Some other text").set_color(BLUE)
        self.wait()

        # remove submobject by key
        my_dict.remove("t")
        self.wait()

        self.play(Uncreate(my_dict["s"]))
        self.wait()

        self.play(FadeOut(my_dict["c"]))
        self.wait()

        self.play(FadeOut(my_dict["r"], shift=DOWN))
        self.wait()

        # you can also make a VDict from an existing dict of mobjects
        plain_dict = {
            1: Integer(1).shift(DOWN),
            2: Integer(2).shift(2 * DOWN),
            3: Integer(3).shift(3 * DOWN),
        }

        vdict_from_plain_dict = VDict(plain_dict)
        vdict_from_plain_dict.shift(1.5 * (UP + LEFT))
        self.play(Create(vdict_from_plain_dict))

        # you can even use zip
        vdict_using_zip = VDict(zip(["s", "c", "r"], [Square(), Circle(), Rectangle()]))
        vdict_using_zip.shift(1.5 * RIGHT)
        self.play(Create(vdict_using_zip))
        self.wait()			








D:\SANJOY_NATH_MANIMS>manim -pql tocheck.py ShapesWithVDict
Manim Community v0.18.1

[12/28/24 08:22:37] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\1185818338_2759395944_223132457.mp4'
                    INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_151333135.mp4'
                    INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_760794106.mp4'
                    INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_3821531530_2014154177.mp4'
                    INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_3923832781.mp4'
                    INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_2810894713.mp4'
                    INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_3605235151.mp4'
                    INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_2996143138_4067543713.mp4'
[12/28/24 08:22:38] INFO     Animation 8 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_853990248.mp4'
                    INFO     Animation 9 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_2889909005_367433180.mp4'
                    INFO     Animation 10 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_2284358977.mp4'
                    INFO     Animation 11 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_692431636_2809894269.mp4'
                    INFO     Animation 12 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_3864704535.mp4'
                    INFO     Animation 13 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_2327288063_691662086.mp4'
                    INFO     Animation 14 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_2052034747_1085555599.mp4'
                    INFO     Animation 15 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_2557559699.mp4'
                    INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    INFO                                                                                                                                                                 scene_file_writer.py:737
                             File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\ShapesWithVDict.mp4'

                    INFO     Rendered ShapesWithVDict                                                                                                                                                scene.py:247
                             Played 16 animations
[12/28/24 08:22:39] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\ShapesWithVDict.mp4'                                                                           file_ops.py:231
		