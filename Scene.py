from manim import *

######use this command                      manim -pql scene.py CreateCircle

# # # D:\SANJOY_NATH_MANIMS>py Scene.py

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py CreateCircle
# # # Manim Community v0.18.1

# # # [12/19/24 21:01:05] INFO     Animation 0 : Partial movie file written in                        scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_fil
                             # # # es\CreateCircle\1185818338_41213021_223132457.mp4'
                    # # # INFO     Combining to Movie file.                                           scene_file_writer.py:617
                    # # # INFO                                                                        scene_file_writer.py:737
                             # # # File ready at
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\CreateCircle.mp4'

                    # # # INFO     Rendered CreateCircle                                                          scene.py:247
                             # # # Played 1 animations
# # # [12/19/24 21:01:06] INFO     Previewed File at:                                                          file_ops.py:231
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\CreateCircle.mp4'
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
		
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation		
		
		
###command is to run then is         manim -pql scene.py SquareToCircle		



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py SquareToCircle
# # # Manim Community v0.18.1

# # # [12/19/24 21:18:37] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SquareToCircle\1185818338_1063976082_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SquareToCircle\624642324_166878160_3256495558.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SquareToCircle\624642324_208288666_3256495558.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SquareToCircle.mp4'

                    # # # INFO     Rendered SquareToCircle                                                                                                                                                 scene.py:247
                             # # # Played 3 animations
# # # [12/19/24 21:18:38] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SquareToCircle.mp4'   





































class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen 
		
		
###then run the command manim -pql scene.py SquareAndCircle


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py SquareAndCircle
# # # Manim Community v0.18.1

# # # [12/19/24 21:20:20] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SquareAndCircle\1185818338_1180669753_223132457.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SquareAndCircle.mp4'

                    # # # INFO     Rendered SquareAndCircle                                                                                                                                                scene.py:247
                             # # # Played 1 animations
# # # [12/19/24 21:20:21] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SquareAndCircle.mp4'     


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen


### then running the commands  manim -pql scene.py AnimatedSquareToCircle





class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()


# # # ###then running the commands  manim -pql scene.py DifferentRotations	
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py SquareToCircle
# # # Manim Community v0.18.1

# # # [12/19/24 21:18:37] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SquareToCircle\1185818338_1063976082_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SquareToCircle\624642324_166878160_3256495558.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SquareToCircle\624642324_208288666_3256495558.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SquareToCircle.mp4'

                    # # # INFO     Rendered SquareToCircle                                                                                                                                                 scene.py:247
                             # # # Played 3 animations
# # # [12/19/24 21:18:38] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SquareToCircle.mp4'                                                                              file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py SquareAndCircle
# # # Manim Community v0.18.1

# # # [12/19/24 21:20:20] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SquareAndCircle\1185818338_1180669753_223132457.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SquareAndCircle.mp4'

                    # # # INFO     Rendered SquareAndCircle                                                                                                                                                scene.py:247
                             # # # Played 1 animations
# # # [12/19/24 21:20:21] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SquareAndCircle.mp4'                                                                             file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py AnimatedSquareToCircle
# # # Manim Community v0.18.1

# # # [12/19/24 21:22:12] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\AnimatedSquareToCircle\1185818338_1280228252_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\AnimatedSquareToCircle\624642324_886724217_3256495558.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\AnimatedSquareToCircle\624642324_792917952_3256495558.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\AnimatedSquareToCircle\624642324_3553665112_3256495558.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\AnimatedSquareToCircle.mp4'

                    # # # INFO     Rendered AnimatedSquareToCircle                                                                                                                                         scene.py:247
                             # # # Played 4 animations
# # # [12/19/24 21:22:13] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\AnimatedSquareToCircle.mp4'                                                                      file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py DifferentRotations
# # # Manim Community v0.18.1

# # # [12/19/24 21:23:32] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\DifferentRotations\1185818338_3163499937_2792856867.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\DifferentRotations\624642324_1704852926_4231444911.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\DifferentRotations.mp4'

                    # # # INFO     Rendered DifferentRotations                                                                                                                                             scene.py:247
                             # # # Played 2 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\DifferentRotations.mp4'                                                                          file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TwoTransforms
# # # Manim Community v0.18.1

# # # [12/19/24 21:25:45] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TwoTransforms\1185818338_3020532286_4272345035.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TwoTransforms\624642324_4116951727_4272345035.mp4'
# # # [12/19/24 21:25:46] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TwoTransforms\624642324_1046082076_4272345035.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TwoTransforms\624642324_1959358871_631829896.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TwoTransforms\624642324_224569774_889849732.mp4'
                    # # # INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TwoTransforms\624642324_4118105539_3548317080.mp4'
                    # # # INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TwoTransforms\624642324_4093562833_1601094618.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\TwoTransforms.mp4'

                    # # # INFO     Rendered TwoTransforms                                                                                                                                                  scene.py:247
                             # # # Played 7 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\TwoTransforms.mp4'         

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()	
		



from manim import *

class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene,py TransformCycle
# # # Manim Community v0.18.1

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
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\module_ops.py", line 57, in get_module
    # # # raise FileNotFoundError(f"{file_name} not found")
# # # FileNotFoundError: D:\SANJOY_NATH_MANIMS\scene,py not found


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TransformCycle
# # # Manim Community v0.18.1

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
  # # # File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  # # # File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  # # # File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  # # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # # File "D:\SANJOY_NATH_MANIMS\scene.py", line 284
    # # # D:\SANJOY_NATH_MANIMS>manim -pql scene,py TransformCycle
       # # # ^
# # # SyntaxError: unexpected character after line continuation character
			

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TransformCycle
# # # Manim Community v0.18.1

# # # [12/19/24 21:30:26] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TransformCycle\1185818338_123554531_2060486491.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TransformCycle\624642324_115351080_1460023451.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TransformCycle\624642324_4116951727_1460023451.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\TransformCycle.mp4'

                    # # # INFO     Rendered TransformCycle                                                                                                                                                 scene.py:247
                             # # # Played 3 animations
# # # [12/19/24 21:30:27] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\TransformCycle.mp4'                                                                              file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>		


from manim import *

class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        text = Text("SANJOY NATH GEOMETRIFYING TRIGONOMETRY QHENOMENOLOGY").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ChangingCameraWidthAndRestore
# # # Manim Community v0.18.1

# # # [12/19/24 21:35:31] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ChangingCameraWidthAndRestore\95310997_4661280_812137966.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ChangingCameraWidthAndRestore\2091185771_3156131044_1573342425.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ChangingCameraWidthAndRestore\2091185771_2144201532_1974136912.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ChangingCameraWidthAndRestore.mp4'

                    # # # INFO     Rendered ChangingCameraWidthAndRestore                                                                                                                                  scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ChangingCameraWidthAndRestore.mp4'   	


from manim import *

class TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY(MovingCameraScene):
    def construct(self):
        text = Text("SANJOY NATH GEOMETRIFYING TRIGONOMETRY QHENOMENOLOGY").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))					
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY
# # # Manim Community v0.18.1

# # # [12/19/24 21:37:24] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY\3207110929_1588480369_387384823.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY\2593657122_3156131044_1415416005.mp4'
# # # [12/19/24 21:37:25] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY\2593657122_2144201532_1427408234.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY.mp4'

                    # # # INFO     Rendered TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY                                                                                                                     scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY.mp4'  
	


from manim import *

class MovingCameraCenter(MovingCameraScene):
    def construct(self):
        s = Square(color=RED, fill_opacity=0.5).move_to(2 * LEFT)
        t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 * RIGHT)
        self.wait(0.3)
        self.add(s, t)
        self.play(self.camera.frame.animate.move_to(s))
        self.wait(0.3)
        self.play(self.camera.frame.animate.move_to(t))	
		
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingCameraCenter
# # # Manim Community v0.18.1

# # # [12/19/24 21:38:40] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingCameraCenter\3383164744_354233455_631829896.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingCameraCenter\3593883998_295094927_4177661008.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingCameraCenter\894920910_3156131044_2447821607.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingCameraCenter\3073931319_3548988089_1599536104.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingCameraCenter.mp4'

                    # # # INFO     Rendered MovingCameraCenter                                                                                                                                             scene.py:247
                             # # # Played 4 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingCameraCenter.mp4'                                                                          file_ops.py:231
		
		







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


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingAndZoomingCamera
# # # Manim Community v0.18.1

# # # [12/19/24 21:39:57] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAndZoomingCamera\4028643659_392016436_1979599971.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAndZoomingCamera\3319821646_3156131044_3769575808.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAndZoomingCamera\212054668_2006109817_899335350.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAndZoomingCamera\2646333718_1829605039_3302704521.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingAndZoomingCamera.mp4'

                    # # # INFO     Rendered MovingAndZoomingCamera                                                                                                                                         scene.py:247
                             # # # Played 4 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingAndZoomingCamera.mp4'        	


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






# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingCameraOnGraph
# # # Manim Community v0.18.1

# # # [12/19/24 21:41:24] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingCameraOnGraph\1179099625_748431935_2859216269.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingCameraOnGraph\3919637460_3212398593_790376805.mp4'
# # # [12/19/24 21:41:25] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingCameraOnGraph\942685399_2144201532_1242041937.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingCameraOnGraph\2616593765_4042641242_882514976.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingCameraOnGraph.mp4'

                    # # # INFO     Rendered MovingCameraOnGraph                                                                                                                                            scene.py:247
                             # # # Played 4 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingCameraOnGraph.mp4'               


from manim import *

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)			



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py CreatingMobjects
# # # Manim Community v0.18.1

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
  # # # File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  # # # File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  # # # File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  # # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # # File "D:\SANJOY_NATH_MANIMS\scene.py", line 541
    # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingCameraOnGraph
       # # # ^
# # # SyntaxError: unexpected character after line continuation character

from manim import *

class t2gExample(Scene):
    def construct(self):
        t2gindices = Text(
            'Hello',
            t2g={
                '[1:-1]': (RED,GREEN),
            },
        ).move_to(LEFT)
        t2gwords = Text(
            'World',
            t2g={
                'World':(RED,BLUE),
            },
        ).next_to(t2gindices, RIGHT)
        self.add(t2gindices, t2gwords)
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py t2gExample
# # # Manim Community v0.18.1

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
  # # # File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  # # # File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  # # # File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  # # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # # File "D:\SANJOY_NATH_MANIMS\scene.py", line 541
    # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingCameraOnGraph
       # # # ^
# # # SyntaxError: unexpected character after line continuation character		





# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py CreatingMobjects
# # # Manim Community v0.18.1

# # # [12/19/24 21:45:42] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\CreatingMobjects\1185818338_2268332985_2060486491.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\CreatingMobjects\624642324_3890345977_1071484169.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\CreatingMobjects.mp4'

                    # # # INFO     Rendered CreatingMobjects                                                                                                                                               scene.py:247
                             # # # Played 2 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\CreatingMobjects.mp4'                                                                            file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py t2gExample
# # # Manim Community v0.18.1

# # # # # # [12/19/24 21:45:58] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\t2gExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered t2gExample                                                                                                                                                     scene.py:247
                             # # # Played 0 animations
# # # [12/19/24 21:45:59] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\t2gExample_ManimCE_v0.18.1.png'          

from manim import *

class LineSpacing(Scene):
    def construct(self):
        a = Text("Hello\nWorld", line_spacing=1)
        b = Text("Hello\nWorld", line_spacing=4)
        self.add(Group(a,b).arrange(LEFT, buff=5))		
		
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LineSpacing
# # # Manim Community v0.18.1

# # # [12/19/24 21:47:21] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LineSpacing_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LineSpacing                                                                                                                                                    scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LineSpacing_ManimCE_v0.18.1.png'       





from manim import *

class DisableLigature(Scene):
    def construct(self):
        li = Text("fl ligature",font_size=96)
        nli = Text("fl ligature", disable_ligatures=True, font_size=96)
        self.add(Group(li, nli).arrange(DOWN, buff=.8))

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py DisableLigature
# # # Manim Community v0.18.1

# # # [12/19/24 21:49:13] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\DisableLigature_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered DisableLigature                                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\DisableLigature_ManimCE_v0.18.1.png'    
					
					
					
					
from manim import *

class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)				


from manim import *

class MarkupTest(Scene):
    def construct(self):
        text = MarkupText(
            f'<span underline="double" underline_color="green">double green underline</span> in red text<span fgcolor="{YELLOW}"> except this</span>',
            color=RED,
            font_size=34
        )
        self.add(text)



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MarkupTest
# # # Manim Community v0.18.1

# # # [12/19/24 22:51:40] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\MarkupTest_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered MarkupTest                                                                                                                                                     scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\MarkupTest_ManimCE_v0.18.1.png'         		
		
		
		
from manim import *

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py HelloLaTeX
# # # Manim Community v0.18.1

# # # [12/19/24 22:52:30] INFO     Writing \LaTeX to media\Tex\07fd8c4c1d6550a5.tex                                                                                                             tex_file_writing.py:109
# # # [12/19/24 22:53:05] INFO         
# # # instals the mikitex first. install the miktex first                                                                                                                                                        scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\HelloLaTeX_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered HelloLaTeX                                                                                                                                                     scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\HelloLaTeX_ManimCE_v0.18.1.png'         		



from manim import *

class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MathTeXDemo
# # # Manim Community v0.18.1

# # # [12/19/24 22:54:14] INFO     Writing \xrightarrow{x^6y^8} to media\Tex\097911b43a99d9cf.tex                                                                                               tex_file_writing.py:109
# # # [12/19/24 22:54:15] INFO     Writing $\xrightarrow{x^6y^8}$ to media\Tex\3edeba480ead3d34.tex                                                                                             tex_file_writing.py:109
# # # [12/19/24 22:54:16] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\MathTeXDemo_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered MathTeXDemo                                                                                                                                                    scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\MathTeXDemo_ManimCE_v0.18.1.png'   


from manim import *

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)


		# # # tested ok
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py AMSLaTeX
# # # Manim Community v0.18.1

# # # [12/19/24 22:55:01] INFO     Writing $\mathtt{H} \looparrowright$ \LaTeX to media\Tex\01f987757cc0c8ba.tex                                                                                tex_file_writing.py:109
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\AMSLaTeX_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered AMSLaTeX                                                                                                                                                       scene.py:247
                             # # # Played 0 animations
# # # [12/19/24 22:55:02] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\AMSLaTeX_ManimCE_v0.18.1.png'   


# # # from manim import *

# # # class LaTeXAttributes(Scene):
    # # # def construct(self):
        # # # tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        # # # self.add(tex)



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LaTeXAttributes
# # # Manim Community v0.18.1

# # # [12/19/24 22:56:08] INFO     Writing Hello \LaTeX to media\Tex\f00dac3c1d012e99.tex                                                                                                       tex_file_writing.py:109
# # # [12/19/24 22:56:09] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LaTeXAttributes_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LaTeXAttributes                                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LaTeXAttributes_ManimCE_v0.18.1.png'    		
					
					
# # # D:\SANJOY_NATH_MANIMS>manim -pql tocheckarbitraryfilesnames.py LaTeXAttributes
# # # Manim Community v0.18.1

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
  # # # File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  # # # File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  # # # File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  # # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # # File "D:\SANJOY_NATH_MANIMS\tocheckarbitraryfilesnames.py", line 859
    # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LaTeXAttributes
       # # # ^
# # # SyntaxError: unexpected character after line continuation character				


from manim import *

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ManimCELogo
# # # Manim Community v0.18.1

# # # [12/19/24 23:32:49] INFO     Writing \mathbb{M} to media\Tex\834e99f1e5f1676e.tex                                                                                                         tex_file_writing.py:109
# # # [12/19/24 23:32:50] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\ManimCELogo_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered ManimCELogo                                                                                                                                                    scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\ManimCELogo_ManimCE_v0.18.1.png'    



from manim import *

class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py BraceAnnotation
# # # Manim Community v0.18.1

# # # [12/19/24 23:33:50] INFO     Writing Horizontal distance to media\Tex\1c22c507eca0dfce.tex                                                                                                tex_file_writing.py:109
# # # [12/19/24 23:33:51] INFO     Writing x-x_1 to media\Tex\c7233a31a47769e5.tex                                                                                                              tex_file_writing.py:109
# # # [12/19/24 23:33:52] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\BraceAnnotation_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered BraceAnnotation                                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\BraceAnnotation_ManimCE_v0.18.1.png'   


from manim import *

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py VectorArrow
# # # Manim Community v0.18.1

# # # [12/19/24 23:34:56] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\VectorArrow_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered VectorArrow                                                                                                                                                    scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\VectorArrow_ManimCE_v0.18.1.png'      






from manim import *

class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, n)]
        )
        image = ImageMobject(imageArray).scale(2)
        image.background_rectangle = SurroundingRectangle(image, GREEN)
        self.add(image, image.background_rectangle)


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GradientImageFromArray
# # # Manim Community v0.18.1

# # # [12/19/24 23:36:25] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\GradientImageFromArray_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GradientImageFromArray                                                                                                                                         scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\GradientImageFromArray_ManimCE_v0.18.1.png'       		
					
					
from manim import *

class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))		

###great animations         https://docs.manim.community/en/stable/examples.html

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py BooleanOperations
# # # Manim Community v0.18.1

# # # [12/19/24 23:37:19] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\1185818338_1546283473_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\624642324_283232089_2945923452.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\624642324_3467268576_771430443.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\624642324_2843360282_2966542040.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\624642324_211828114_1408936434.mp4'
# # # [12/19/24 23:37:20] INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\624642324_2852714256_2313767923.mp4'
                    # # # INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\624642324_2962411128_2697291123.mp4'
                    # # # INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\624642324_3736041038_4112410612.mp4'
                    # # # INFO     Animation 8 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\BooleanOperations\624642324_1707004815_2400830724.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\BooleanOperations.mp4'

                    # # # INFO     Rendered BooleanOperations                                                                                                                                              scene.py:247
                             # # # Played 9 animations
# # # [12/19/24 23:37:21] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\BooleanOperations.mp4'    


from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PointMovingOnShapes
# # # Manim Community v0.18.1

# # # [12/19/24 23:38:35] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointMovingOnShapes\1185818338_22980905_4159515603.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointMovingOnShapes\624642324_3199290941_2799868931.mp4'
# # # [12/19/24 23:38:36] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointMovingOnShapes\624642324_3405673780_496602590.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointMovingOnShapes\624642324_3048896321_2799868931.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointMovingOnShapes\624642324_1704852926_2925915001.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\PointMovingOnShapes.mp4'

                    # # # INFO     Rendered PointMovingOnShapes                                                                                                                                            scene.py:247
                             # # # Played 5 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\PointMovingOnShapes.mp4'         


from manim import *

class MovingAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)

        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))				


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingAround
# # # Manim Community v0.18.1

# # # [12/19/24 23:39:28] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAround\1185818338_2735299807_1600157425.mp4'
# # # [12/19/24 23:39:29] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAround\624642324_310341572_1600157425.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAround\624642324_1070973442_1600157425.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAround\624642324_3111630521_1600157425.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingAround.mp4'

                    # # # INFO     Rendered MovingAround                                                                                                                                                   scene.py:247
                             # # # Played 4 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingAround.mp4'                           


from manim import *

class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, tex)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))					





		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingAngle
# # # Manim Community v0.18.1

# # # [12/19/24 23:40:16] INFO     Writing \theta to media\Tex\0cec1e994feab60e.tex                                                                                                             tex_file_writing.py:109
# # # [12/19/24 23:40:17] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAngle\1185818338_123554531_1652103794.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAngle\624642324_1844281646_79103077.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAngle\624642324_849294087_1731195912.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAngle\624642324_2588136312_2971457240.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingAngle\624642324_2506509665_2032314852.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingAngle.mp4'

                    # # # INFO     Rendered MovingAngle                                                                                                                                                    scene.py:247
                             # # # Played 5 animations
# # # [12/19/24 23:40:18] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingAngle.mp4'                                                                                 file_ops.py:231



from manim import *

class MovingDots(Scene):
    def construct(self):
        d1,d2=Dot(color=BLUE),Dot(color=GREEN)
        dg=VGroup(d1,d2).arrange(RIGHT,buff=1)
        l1=Line(d1.get_center(),d2.get_center()).set_color(RED)
        x=ValueTracker(0)
        y=ValueTracker(0)
        d1.add_updater(lambda z: z.set_x(x.get_value()))
        d2.add_updater(lambda z: z.set_y(y.get_value()))
        l1.add_updater(lambda z: z.become(Line(d1.get_center(),d2.get_center())))
        self.add(d1,d2,l1)
        self.play(x.animate.set_value(5))
        self.play(y.animate.set_value(4))
        self.wait()		
		
		





# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingDots
# # # Manim Community v0.18.1

# # # [12/19/24 23:41:23] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingDots\1185818338_1319928151_205659675.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingDots\624642324_2843732495_1123187806.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingDots\624642324_1704852926_1559560624.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingDots.mp4'

                    # # # INFO     Rendered MovingDots                                                                                                                                                     scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingDots.mp4'    	


from manim import *

class MovingGroupToDestination(Scene):
    def construct(self):
        group = VGroup(Dot(LEFT), Dot(ORIGIN), Dot(RIGHT, color=RED), Dot(2 * RIGHT)).scale(1.4)
        dest = Dot([4, 3, 0], color=YELLOW)
        self.add(group, dest)
        self.play(group.animate.shift(dest.get_center() - group[2].get_center()))
        self.wait(0.5)


# # # # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingGroupToDestination
# # # # # # Manim Community v0.18.1

# # # # # # [12/19/24 23:42:20] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingGroupToDestination\1185818338_4271005753_1374358632.mp4'
                    # # # # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingGroupToDestination\624642324_1959358871_1609572231.mp4'
                    # # # # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingGroupToDestination.mp4'

                    # # # # # # INFO     Rendered MovingGroupToDestination                                                                                                                                       scene.py:247
                             # # # # # # Played 2 animations
                    # # # # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingGroupToDestination.mp4'               	


from manim import *

class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()


		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingFrameBox
# # # Manim Community v0.18.1

# # # [12/19/24 23:44:21] INFO     Writing \frac{d}{dx}f(x)g(x)= f(x)\frac{d}{dx}g(x) + g(x)\frac{d}{dx}f(x) to media\Tex\7cd836c6069a1f6f.tex                                                  tex_file_writing.py:109
# # # [12/19/24 23:44:22] INFO     Writing \frac{d}{dx}f(x)g(x)= to media\Tex\f8c413854b774f69.tex                                                                                              tex_file_writing.py:109
# # # [12/19/24 23:44:23] INFO     Writing f(x)\frac{d}{dx}g(x) to media\Tex\166008daff52de9b.tex                                                                                               tex_file_writing.py:109
# # # [12/19/24 23:44:24] INFO     Writing + to media\Tex\9f38976a758de16a.tex                                                                                                                  tex_file_writing.py:109
                    # # # INFO     Writing g(x)\frac{d}{dx}f(x) to media\Tex\9a96c323d57521d5.tex                                                                                               tex_file_writing.py:109
# # # [12/19/24 23:44:26] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingFrameBox\1185818338_2138901128_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingFrameBox\624642324_271042858_833714077.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingFrameBox\624642324_1704852926_3394160418.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingFrameBox\624642324_1303489_3766780418.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingFrameBox\624642324_1704852926_3818418192.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingFrameBox.mp4'

                    # # # INFO     Rendered MovingFrameBox                                                                                                                                                 scene.py:247
                             # # # Played 5 animations
# # # [12/19/24 23:44:27] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingFrameBox.mp4'                                                                              file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingFrameBox
# # # Manim Community v0.18.1

# # # [12/19/24 23:45:00] INFO     Animation 0 : Using cached data (hash : 1185818338_2138901128_223132457)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_271042858_833714077)                                                                                          cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_1704852926_3394160418)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 3 : Using cached data (hash : 624642324_1303489_3766780418)                                                                                           cairo_renderer.py:88
                    # # # INFO     Animation 4 : Using cached data (hash : 624642324_1704852926_3818418192)                                                                                        cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingFrameBox.mp4'

                    # # # INFO     Rendered MovingFrameBox                                                                                                                                                 scene.py:247
                             # # # Played 5 animations
# # # [12/19/24 23:45:01] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingFrameBox.mp4'                                                                              file_ops.py:231
		
from manim import *

class RotationUpdater(Scene):
    def construct(self):
        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
        line_reference = Line(ORIGIN, LEFT).set_color(WHITE)
        line_moving = Line(ORIGIN, LEFT).set_color(YELLOW)
        line_moving.add_updater(updater_forth)
        self.add(line_reference, line_moving)
        self.wait(2)
        line_moving.remove_updater(updater_forth)
        line_moving.add_updater(updater_back)
        self.wait(2)
        line_moving.remove_updater(updater_back)
        self.wait(0.5)		
		
		
		
		
		
		
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py RotationUpdater
# # # Manim Community v0.18.1

# # # [12/20/24 00:11:53] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\RotationUpdater\1185818338_804019694_4063736301.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\RotationUpdater\624642324_1190504341_1155822862.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\RotationUpdater\624642324_1959358871_4175985776.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\RotationUpdater.mp4'

                    # # # INFO     Rendered RotationUpdater                                                                                                                                                scene.py:247
                             # # # Played 3 animations
# # # [12/20/24 00:11:54] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\RotationUpdater.mp4'             		


from manim import *

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PointWithTrace
# # # Manim Community v0.18.1

# # # [12/20/24 00:15:17] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointWithTrace\1185818338_368319200_2869406106.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointWithTrace\624642324_1704852926_3054328761.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointWithTrace\624642324_3715520414_2726630345.mp4'
# # # [12/20/24 00:15:18] INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointWithTrace\624642324_3830559194_2520779180.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PointWithTrace\624642324_1704852926_1025181051.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\PointWithTrace.mp4'

                    # # # INFO     Rendered PointWithTrace                                                                                                                                                 scene.py:247
                             # # # Played 5 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\PointWithTrace.mp4'      


from manim import *

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)
        self.add(plot, labels)


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py SinAndCosFunctionPlot
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # [12/20/24 00:51:53] INFO     Writing - to media\Tex\ba96de15f98acfc8.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:51:54] INFO     Writing 1 to media\Tex\6ecf9f51170c1a70.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:51:55] INFO     Writing 0 to media\Tex\66e1bc57a83e0f07.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:51:56] INFO     Writing 8 to media\Tex\b47c9feb1c667bc8.tex                                                                                                                  tex_file_writing.py:109
                    # # # INFO     Writing 6 to media\Tex\b330e3953bf029d7.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:51:57] INFO     Writing 4 to media\Tex\31d3165490bf3404.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:51:58] INFO     Writing 2 to media\Tex\2b7ffb3c38a5a6e0.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:51:59] INFO     Writing x to media\Tex\d3c1af651a272204.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:52:00] INFO     Writing y to media\Tex\3ecdda5b14fcaacb.tex                                                                                                                  tex_file_writing.py:109
                    # # # INFO     Writing \sin(x) to media\Tex\f9c15c78681bd50d.tex                                                                                                            tex_file_writing.py:109
# # # [12/20/24 00:52:01] INFO     Writing \cos(x) to media\Tex\d5728df2ff96f913.tex                                                                                                            tex_file_writing.py:109
# # # [12/20/24 00:52:02] INFO     Writing x=2\pi to media\Tex\6654d53bc4ac00b2.tex                                                                                                             tex_file_writing.py:109
# # # [12/20/24 00:52:03] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\SinAndCosFunctionPlot_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered SinAndCosFunctionPlot                                                                                                                                          scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\SinAndCosFunctionPlot_ManimCE_v0.18.1.png'                                                              file_ops.py:231


from manim import *

class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)

        def func(x):
            return 2 * (x - 5) ** 2
        graph = ax.plot(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        self.add(ax, labels, graph, dot)
        self.play(t.animate.set_value(x_space[minimum_index]))
        self.wait()
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ArgMinExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # [12/20/24 00:53:05] INFO     Writing f(x) to media\Tex\70b3a8630e8c4922.tex                                                                                                               tex_file_writing.py:109
# # # [12/20/24 00:53:06] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ArgMinExample\1185818338_822966917_3999337152.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ArgMinExample\624642324_1704852926_2071562607.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ArgMinExample.mp4'

                    # # # INFO     Rendered ArgMinExample                                                                                                                                                  scene.py:247
                             # # # Played 2 animations
# # # [12/20/24 00:53:07] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ArgMinExample.mp4'                                                                               file_ops.py:231



from manim import *

class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()

        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=GREEN_B,
        )

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[0.3, 0.6], dx=0.03, color=BLUE, fill_opacity=0.5)
        area = ax.get_area(curve_2, [2, 3], bounded_graph=curve_1, color=GREY, opacity=0.5)

        self.add(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GraphAreaPlot
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # [12/20/24 00:54:12] INFO     Writing 3 to media\Tex\8de07035cb22c903.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:54:13] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\GraphAreaPlot_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GraphAreaPlot                                                                                                                                                  scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\GraphAreaPlot_ManimCE_v0.18.1.png'      







from manim import *

class PolygonOnAxes(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]

    def construct(self):
        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )

        t = ValueTracker(5)
        k = 25

        graph = ax.plot(
            lambda x: k / x,
            color=YELLOW_D,
            x_range=[k / 10, 10.0, 0.01],
            use_smoothing=False,
        )

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (t.get_value(), k / t.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon

        polygon = always_redraw(get_rectangle)

        dot = Dot()
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k / t.get_value())))
        dot.set_z_index(10)

        self.add(ax, graph, dot)
        self.play(Create(polygon))
        self.play(t.animate.set_value(10))
        self.play(t.animate.set_value(k / 10))
        self.play(t.animate.set_value(5))         

























# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PolygonOnAxes
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # [12/20/24 00:55:17] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PolygonOnAxes\1185818338_1590570684_372290050.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PolygonOnAxes\624642324_2615300367_3494051416.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PolygonOnAxes\624642324_1262632519_3611539396.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PolygonOnAxes\624642324_472101433_956845220.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\PolygonOnAxes.mp4'

                    # # # INFO     Rendered PolygonOnAxes                                                                                                                                                  scene.py:247
                             # # # Played 4 animations
# # # [12/20/24 00:55:18] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\PolygonOnAxes.mp4'             


from manim import *

class HeatDiagramPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 40, 5],
            y_range=[-8, 32, 5],
            x_length=9,
            y_length=6,
            x_axis_config={"numbers_to_include": np.arange(0, 40, 5)},
            y_axis_config={"numbers_to_include": np.arange(-5, 34, 5)},
            tips=False,
        )
        labels = ax.get_axis_labels(
            x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
        )

        x_vals = [0, 8, 38, 39]
        y_vals = [20, 0, 0, -5]
        graph = ax.plot_line_graph(x_values=x_vals, y_values=y_vals)

        self.add(ax, labels, graph)


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py HeatDiagramPlot
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 00:56:17] INFO     Writing 5 to media\Tex\5683d89f396abe50.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 00:56:18] INFO     Writing $\Delta Q$ to media\Tex\19c459b85696cd8f.tex                                                                                                         tex_file_writing.py:109
# # # [12/20/24 00:56:19] INFO     Writing T[$^\circ C$] to media\Tex\8df39c438e730538.tex                                                                                                      tex_file_writing.py:109
# # # [12/20/24 00:56:20] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\HeatDiagramPlot_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered HeatDiagramPlot                                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\HeatDiagramPlot_ManimCE_v0.18.1.png'      


from manim import *

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))

		
		
		
		
		
		
		
		
		
		
		
		

		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>

# # # D:\SANJOY_NATH_MANIMS>

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py FollowingGraphCamera
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 00:57:30] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\FollowingGraphCamera\1179099625_1073004596_2093056016.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\FollowingGraphCamera\3363072936_418360974_3129556555.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\FollowingGraphCamera\1247091081_2144201532_3350206483.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\FollowingGraphCamera.mp4'

                    # # # INFO     Rendered FollowingGraphCamera                                                                                                                                           scene.py:247
                             # # # Played 3 animations
# # # [12/20/24 00:57:31] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\FollowingGraphCamera.mp4'         		
		
		
		
from manim import *

class MovingZoomedSceneAround(ZoomedScene):
# contributed by TheoremofBeethoven, www.youtube.com/c/TheoremofBeethoven
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )

    def construct(self):
        dot = Dot().shift(UL * 2)
        image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                       [255, 0, 5, 33]]))
        image.height = 7
        frame_text = Text("Frame", color=PURPLE, font_size=67)
        zoomed_camera_text = Text("Zoomed camera", color=RED, font_size=67)

        self.add(image, dot)
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)
        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)

        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        frame_text.next_to(frame, DOWN)

        self.play(Create(frame), FadeIn(frame_text, shift=UP))
        self.activate_zooming()

        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)
        self.play(FadeIn(zoomed_camera_text, shift=UP))
        # Scale in        x   y  z
        scale_factor = [0.5, 1.5, 0]
        self.play(
            frame.animate.scale(scale_factor),
            zoomed_display.animate.scale(scale_factor),
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )
        self.wait()
        self.play(ScaleInPlace(zoomed_display, 2))
        self.wait()
        self.play(frame.animate.shift(2.5 * DOWN))
        self.wait()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera, rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.wait()		
		
		


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingZoomedSceneAround
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 00:58:43] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\3862130965_1283878679_371250055.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\1886244289_1334828345_3457388186.mp4'
# # # [12/20/24 00:58:44] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\1894242548_529482283_1917304548.mp4'
# # # [12/20/24 00:58:45] INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\3736932431_359962617_4283426766.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\2984542182_4042641242_2806247581.mp4'
# # # [12/20/24 00:58:46] INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\1040210665_1958720302_515394493.mp4'
                    # # # INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\1201542766_4042641242_865618602.mp4'
# # # [12/20/24 00:58:47] INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\1969150455_823890987_2129643846.mp4'
# # # [12/20/24 00:58:48] INFO     Animation 8 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\3940008975_4042641242_1244810050.mp4'
                    # # # INFO     Animation 9 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\1554274759_2327810266_341678262.mp4'
# # # [12/20/24 00:58:49] INFO     Animation 10 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\3175504768_1204232059_2494989537.mp4'
                    # # # INFO     Animation 11 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MovingZoomedSceneAround\3738148135_4042641242_4189397632.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingZoomedSceneAround.mp4'

                    # # # INFO     Rendered MovingZoomedSceneAround                                                                                                                                        scene.py:247
                             # # # Played 12 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingZoomedSceneAround.mp4'            


from manim import *

class FixedInFrameMObjectTest(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)
        self.add(axes)
        self.wait()					



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py FixedInFrameMObjectTest
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
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
  # # # File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  # # # File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  # # # File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  # # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # # File "D:\SANJOY_NATH_MANIMS\scene.py", line 1906
    # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MovingZoomedSceneAround
       # # # ^
# # # SyntaxError: unexpected character after line continuation character	


# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 01:00:42] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\FixedInFrameMObjectTest\3697696148_3467822883_3824565214.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\FixedInFrameMObjectTest.mp4'

                    # # # INFO     Rendered FixedInFrameMObjectTest                                                                                                                                        scene.py:247
                             # # # Played 1 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\FixedInFrameMObjectTest.mp4'                                                                     file_ops.py:231

					
					
					
					
					
					





from manim import *

class ThreeDLightSourcePosition(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
        )
        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, sphere)
		








# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ThreeDLightSourcePosition
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 01:01:38] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\ThreeDLightSourcePosition_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered ThreeDLightSourcePosition                                                                                                                                      scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\ThreeDLightSourcePosition_ManimCE_v0.18.1.png'         		
					
					







					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
from manim import *

class ThreeDCameraRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(circle,axes)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait()




# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ThreeDCameraRotation
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 01:02:37] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ThreeDCameraRotation\3799671348_755080803_2396505566.mp4'
# # # [12/20/24 01:02:38] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ThreeDCameraRotation\3812658805_513504441_3013264961.mp4'
# # # [12/20/24 01:02:39] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ThreeDCameraRotation\426877436_2304249630_2984847441.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ThreeDCameraRotation.mp4'

                    # # # INFO     Rendered ThreeDCameraRotation                                                                                                                                           scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ThreeDCameraRotation.mp4'       





from manim import *

class ThreeDCameraIllusionRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(circle,axes)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(PI/2)
        self.stop_3dillusion_camera_rotation()


		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ThreeDCameraRotation
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 01:02:37] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ThreeDCameraRotation\3799671348_755080803_2396505566.mp4'
# # # [12/20/24 01:02:38] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ThreeDCameraRotation\3812658805_513504441_3013264961.mp4'
# # # [12/20/24 01:02:39] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ThreeDCameraRotation\426877436_2304249630_2984847441.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ThreeDCameraRotation.mp4'

                    # # # INFO     Rendered ThreeDCameraRotation                                                                                                                                           scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ThreeDCameraRotation.mp4'                                                                        file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ThreeDCameraIllusionRotation
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 02:40:12] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ThreeDCameraIllusionRotation\2234236009_669445557_1539511393.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ThreeDCameraIllusionRotation.mp4'

                    # # # INFO     Rendered ThreeDCameraIllusionRotation                                                                                                                                   scene.py:247
                             # # # Played 1 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ThreeDCameraIllusionRotation.mp4'      


from manim import *

class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        resolution_fa = 24
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_gauss(u, v):
            x = u
            y = v
            sigma, mu = 0.4, [0.0, 0.0]
            d = np.linalg.norm(np.array([x - mu[0], y - mu[1]]))
            z = np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2, +2],
            u_range=[-2, +2]
        )

        gauss_plane.scale(2, about_point=ORIGIN)
        gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.5)
        axes = ThreeDAxes()
        self.add(axes,gauss_plane)


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ThreeDSurfacePlot
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 02:41:32] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\ThreeDSurfacePlot_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered ThreeDSurfacePlot                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\ThreeDSurfacePlot_ManimCE_v0.18.1.png'     


from manim import *

class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid", font_size=72)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py OpeningManim
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # [12/20/24 02:42:23] INFO     Writing This is some \LaTeX to media\Tex\95419684cd0167a8.tex                                                                                                tex_file_writing.py:109
# # # [12/20/24 02:42:24] INFO     Writing \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} to media\Tex\cd65b3ac6150d282.tex                                                                  tex_file_writing.py:109
# # # [12/20/24 02:42:26] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\1185818338_3916731119_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_1704852926_4151465905.mp4'
                    # # # INFO     Writing That was a transform to media\Tex\f626e74428a94ef7.tex                                                                                               tex_file_writing.py:109
# # # [12/20/24 02:42:27] INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_3408740689_1084955206.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_1704852926_2514186295.mp4'
                    # # # INFO     Writing This is a grid to media\Tex\107977417fa9b467.tex                                                                                                     tex_file_writing.py:109
# # # [12/20/24 02:42:28] INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_776230473_3457279939.mp4'
                    # # # INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_1704852926_3910109388.mp4'
                    # # # INFO     Writing That was a non-linear function \\ applied to the grid to media\Tex\ddc99778a23bf415.tex                                                              tex_file_writing.py:109
# # # [12/20/24 02:42:30] INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_3462897005_3248348804.mp4'
                    # # # INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_1704852926_3711024970.mp4'
# # # [12/20/24 02:42:31] INFO     Animation 8 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_2170401995_3290485850.mp4'
                    # # # INFO     Animation 9 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\OpeningManim\624642324_1704852926_1128911722.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\OpeningManim.mp4'

                    # # # INFO     Rendered OpeningManim                                                                                                                                                   scene.py:247
                             # # # Played 10 animations
# # # [12/20/24 02:42:32] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\OpeningManim.mp4'        


from manim import *

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)             	





# # # D:\SANJOY_NATH_MANIMS>

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py SineCurveUnitCircle
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 02:56:21] INFO     Writing \pi to media\Tex\19b6551b9477ad6b.tex                                                                                                                tex_file_writing.py:109
# # # [12/20/24 02:56:22] INFO     Writing 2 \pi to media\Tex\d11b20434ee26bda.tex                                                                                                              tex_file_writing.py:109
# # # [12/20/24 02:56:23] INFO     Writing 3 \pi to media\Tex\f9bafda453c77730.tex                                                                                                              tex_file_writing.py:109
# # # [12/20/24 02:56:24] INFO     Writing 4 \pi to media\Tex\92d3e436cd1d05ab.tex                                                                                                              tex_file_writing.py:109
# # # [12/20/24 02:56:26] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SineCurveUnitCircle\1185818338_3794438852_3922367318.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SineCurveUnitCircle\624642324_1704852926_3809110881.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SineCurveUnitCircle.mp4'

                    # # # INFO     Rendered SineCurveUnitCircle                                                                                                                                            scene.py:247
                             # # # Played 2 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SineCurveUnitCircle.mp4'   


from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)			


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py Shapes
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 02:58:58] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\Shapes\1185818338_2268332985_1734745091.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\Shapes.mp4'

                    # # # INFO     Rendered Shapes                                                                                                                                                         scene.py:247
                             # # # Played 1 animations
# # # [12/20/24 02:58:59] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\Shapes.mp4'                                  


from manim import *

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, LEFT)
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MobjectPlacement
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 02:59:49] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MobjectPlacement\1185818338_2268332985_4103941492.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MobjectPlacement.mp4'

                    # # # INFO     Rendered MobjectPlacement                                                                                                                                               scene.py:247
                             # # # Played 1 animations
# # # [12/20/24 02:59:50] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MobjectPlacement.mp4'                                                                            file_ops.py:231





from manim import *

class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MobjectStyling
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:00:39] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MobjectStyling\1185818338_2268332985_2664187078.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MobjectStyling.mp4'

                    # # # INFO     Rendered MobjectStyling                                                                                                                                                 scene.py:247
                             # # # Played 1 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MobjectStyling.mp4'       


from manim import *

class MobjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(triangle, square, circle)
        self.wait(1)		





# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MobjectZOrder
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:01:23] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\MobjectZOrder\1185818338_2268332985_38369994.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
# # # [12/20/24 03:01:24] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MobjectZOrder.mp4'

                    # # # INFO     Rendered MobjectZOrder                                                                                                                                                  scene.py:247
                             # # # Played 1 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MobjectZOrder.mp4'   























from manim import *

class SomeAnimations(Scene):
    def construct(self):
        square = Square()

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py SomeAnimations
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:02:17] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SomeAnimations\1185818338_3650454768_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SomeAnimations\624642324_180748073_3256495558.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SomeAnimations\624642324_1216032425_3256495558.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\SomeAnimations\624642324_3890345977_631829896.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SomeAnimations.mp4'

                    # # # INFO     Rendered SomeAnimations                                                                                                                                                 scene.py:247
                             # # # Played 4 animations
# # # [12/20/24 03:02:18] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\SomeAnimations.mp4'      


from manim import *

class AnimateExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        # animate the change of position and the rotation at the same time
        self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)     


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py AnimateExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:03:07] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\AnimateExample\1185818338_1332077962_4173930198.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\AnimateExample\624642324_3890345977_3120531477.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\AnimateExample\624642324_1624981740_1962880573.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\AnimateExample\624642324_3890345977_3222475621.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\AnimateExample.mp4'

                    # # # INFO     Rendered AnimateExample                                                                                                                                                 scene.py:247
                             # # # Played 4 animations
# # # [12/20/24 03:03:08] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\AnimateExample.mp4'                          








from manim import *

class RunTime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(square.animate.shift(UP), run_time=3)
        self.wait(1)		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py RunTime
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:03:53] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\RunTime\1185818338_2616298956_3256495558.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\RunTime\624642324_3890345977_1567936491.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
# # # [12/20/24 03:03:54] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\RunTime.mp4'

                    # # # INFO     Rendered RunTime                                                                                                                                                        scene.py:247
                             # # # Played 2 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\RunTime.mp4'               		
					
					
					
					
					
					
					
from manim import *

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)
		
		
		
		
		
		
		
		
		
		
		


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()




# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py Count
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:04:53] ERROR                                                                                                                                                                        module_ops.py:92
                                # # # Count is not in the script

# # # 1: AMSLaTeX
# # # 2: AnimateExample
# # # 3: AnimatedSquareToCircle
# # # 4: ArgMinExample
# # # 5: BooleanOperations
# # # 6: BraceAnnotation
# # # 7: ChangingCameraWidthAndRestore
# # # 8: CountingScene
# # # 9: CreateCircle
# # # 10: CreatingMobjects
# # # 11: DifferentRotations
# # # 12: DisableLigature
# # # 13: FixedInFrameMObjectTest
# # # 14: FollowingGraphCamera
# # # 15: GradientImageFromArray
# # # 16: GraphAreaPlot
# # # 17: HeatDiagramPlot
# # # 18: HelloLaTeX
# # # 19: IterateColor
# # # 20: LineSpacing
# # # 21: ManimCELogo
# # # 22: MarkupTest
# # # 23: MathTeXDemo
# # # 24: MobjectPlacement
# # # 25: MobjectStyling
# # # 26: MobjectZOrder
# # # 27: MovingAndZoomingCamera
# # # 28: MovingAngle
# # # 29: MovingAround
# # # 30: MovingCameraCenter
# # # 31: MovingCameraOnGraph
# # # 32: MovingDots
# # # 33: MovingFrameBox
# # # 34: MovingGroupToDestination
# # # 35: MovingZoomedSceneAround
# # # 36: OpeningManim
# # # 37: PointMovingOnShapes
# # # 38: PointWithTrace
# # # 39: PolygonOnAxes
# # # 40: RotationUpdater
# # # 41: RunTime
# # # 42: Shapes
# # # 43: SinAndCosFunctionPlot
# # # 44: SineCurveUnitCircle
# # # 45: SomeAnimations
# # # 46: SquareAndCircle
# # # 47: SquareToCircle
# # # 48: TEXTGEOMETRIFYINGTRIGONOMETRYQHENOMENOLOGY
# # # 49: ThreeDCameraIllusionRotation
# # # 50: ThreeDCameraRotation
# # # 51: ThreeDLightSourcePosition
# # # 52: ThreeDSurfacePlot
# # # 53: TransformCycle
# # # 54: TwoTransforms
# # # 55: VectorArrow
# # # 56: t2gExample

# # # Choose number corresponding to desired scene/arguments.
# # # (Use comma separated list for multiple entries)
# # # Choice(s):  30
# # # [12/20/24 03:05:06] INFO     Animation 0 : Using cached data (hash : 3383164744_354233455_631829896)                                                                                         cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 3593883998_295094927_4177661008)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 894920910_3156131044_2447821607)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 3 : Using cached data (hash : 3073931319_3548988089_1599536104)                                                                                       cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingCameraCenter.mp4'

                    # # # INFO     Rendered MovingCameraCenter                                                                                                                                             scene.py:247
                             # # # Played 4 animations
# # # [12/20/24 03:05:07] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\MovingCameraCenter.mp4'           		










# # # # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py CountingScene
# # # # # # Manim Community v0.18.1

# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # MathTex("\pi"), MathTex("2 \pi"),
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # MathTex("\pi"), MathTex("2 \pi"),
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # # # # [12/20/24 03:05:51] INFO     Writing . to media\Tex\ec2b01090b1fbb55.tex                                                                                                                  tex_file_writing.py:109
# # # # # # [12/20/24 03:05:52] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\CountingScene\1185818338_123554531_680583801.mp4'
# # # # # # Animation 1: Count(DecimalNumber):   0%|                                                                                                                                                 | 0/60 [00:00<?, ?it/s]
                   # # # # # # INFO     Writing 7 to media\Tex\810c550cdbbf29da.tex                                                                                                                  tex_file_writing.py:109
# # # # # # Animation 1: Count(DecimalNumber):  72%|#################################################################################################4                                      | 43/60 [00:01<00:00, 58.62it/s][12/20/24 03:05:53] INFO     Writing 9 to media\Tex\d994363fa45e89a1.tex                                                                                                                  tex_file_writing.py:109
# # # # # # [12/20/24 03:05:54] INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\CountingScene\624642324_1807919569_1377256185.mp4'
                    # # # # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\CountingScene\624642324_1704852926_1191042800.mp4'
                    # # # # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\CountingScene.mp4'

                    # # # # # # INFO     Rendered CountingScene                                                                                                                                                  scene.py:247
                             # # # # # # Played 3 animations
# # # # # # [12/20/24 03:05:55] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\CountingScene.mp4'          


from manim import *

class MobjectExample(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        a  = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        point_start  = a.get_start()
        point_end    = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MobjectExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:07:15] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\MobjectExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered MobjectExample                                                                                                                                                 scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\MobjectExample_ManimCE_v0.18.1.png'                   		
					
					
					
					
from manim import *

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        self.play(Transform(m1,m2))

		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ExampleTransform
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:07:57] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ExampleTransform\931832650_4166108062_3256495558.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ExampleTransform.mp4'

                    # # # INFO     Rendered ExampleTransform                                                                                                                                               scene.py:247
                             # # # Played 1 animations
# # # [12/20/24 03:07:58] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ExampleTransform.mp4'     





from manim import *

class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)
		
		
		
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ExampleRotation
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:08:54] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\ExampleRotation\931832650_63209373_2969017746.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ExampleRotation.mp4'

                    # # # INFO     Rendered ExampleRotation                                                                                                                                                scene.py:247
                             # # # Played 1 animations
# # # [12/20/24 03:08:55] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\ExampleRotation.mp4'       



















from manim import *

class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py AddPackageLatex
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:10:13] INFO     Writing $\mathscr{H} \rightarrow \mathbb{H}$ to media\Tex\b7a1c4e701f94203.tex                                                                               tex_file_writing.py:109
# # # This is METAFONT, Version 2.71828182 (MiKTeX 24.1)

# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\rsfs10.mf
# # # (C:\Program Files\MiKTeX\fonts/source/public/cm\cmbase.mf)
# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\script.mf
# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\scriptu.mf [65] [66] [67]
# # # [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78] [79] [80] [81] [82]
# # # [83] [84] [85] [86] [87] [88] [89] [90] [127]) ) )
# # # Font metrics written on rsfs10.tfm.
# # # Output written on rsfs10.600gf (27 characters, 9120 bytes).
# # # Transcript written on rsfs10.log.
# # # This is METAFONT, Version 2.71828182 (MiKTeX 24.1)

# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\rsfs7.mf
# # # (C:\Program Files\MiKTeX\fonts/source/public/cm\cmbase.mf)
# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\script.mf
# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\scriptu.mf [65] [66] [67]
# # # [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78] [79] [80] [81] [82]
# # # [83] [84] [85] [86] [87] [88] [89] [90] [127]) ) )
# # # Font metrics written on rsfs7.tfm.
# # # Output written on rsfs7.600gf (27 characters, 6624 bytes).
# # # Transcript written on rsfs7.log.
# # # This is METAFONT, Version 2.71828182 (MiKTeX 24.1)

# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\rsfs5.mf
# # # (C:\Program Files\MiKTeX\fonts/source/public/cm\cmbase.mf)
# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\script.mf
# # # (C:\Program Files\MiKTeX\fonts/source/public/rsfs\scriptu.mf [65] [66] [67]
# # # [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78] [79] [80] [81] [82]
# # # [83] [84] [85] [86] [87] [88] [89] [90] [127]) ) )
# # # Font metrics written on rsfs5.tfm.
# # # Output written on rsfs5.600gf (27 characters, 4704 bytes).
# # # Transcript written on rsfs5.log.
# # # [12/20/24 03:10:28] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\AddPackageLatex_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered AddPackageLatex                                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\AddPackageLatex_ManimCE_v0.18.1.png'              		
					
					
					
					
					
					
from manim import *

class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)







		
		
		
		
		
		
		
		
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LaTeXSubstrings
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:13:27] INFO     Writing Hello$\bigstar$\LaTeX to media\Tex\86870160675ebc3e.tex                                                                                              tex_file_writing.py:109
# # # [12/20/24 03:13:28] INFO     Writing Hello to media\Tex\6b0c4e5f9d59e001.tex                                                                                                              tex_file_writing.py:109
                    # # # INFO     Writing $\bigstar$ to media\Tex\39db739e1017c623.tex                                                                                                         tex_file_writing.py:109
# # # [12/20/24 03:13:29] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LaTeXSubstrings_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LaTeXSubstrings                                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LaTeXSubstrings_ManimCE_v0.18.1.png'         


					

from manim import *

class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)					
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py IncorrectLaTeXSubstringColoring
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:14:50] INFO     Writing e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots to media\Tex\f37a545300dcb560.tex                           tex_file_writing.py:109
# # # [12/20/24 03:14:51] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\IncorrectLaTeXSubstringColoring_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered IncorrectLaTeXSubstringColoring                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\IncorrectLaTeXSubstringColoring_ManimCE_v0.18.1.png'  
					
					
					
					
					
					
					
from manim import *

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)
		


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py CorrectLaTeXSubstringColoring
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:16:03] INFO     Writing e^ x  =  x ^0 +  x ^1 + \frac{1}{2}  x ^2 + \frac{1}{6}  x ^3 + \cdots + \frac{1}{n!}  x ^n + \cdots to media\Tex\03eca29655b82e8c.tex               tex_file_writing.py:109
# # # [12/20/24 03:16:04] INFO     Writing e^{\quad} to media\Tex\26492b37e43d0cc1.tex                                                                                                          tex_file_writing.py:109
# # # [12/20/24 03:16:05] INFO     Writing = to media\Tex\383d1fb9b7d92e82.tex                                                                                                                  tex_file_writing.py:109
# # # [12/20/24 03:16:06] INFO     Writing ^0 + to media\Tex\5e11032bc7eed7f3.tex                                                                                                               tex_file_writing.py:109
# # # [12/20/24 03:16:07] INFO     Writing ^1 + \frac{1}{2} to media\Tex\1fb6bd60323e1d7d.tex                                                                                                   tex_file_writing.py:109
# # # [12/20/24 03:16:08] INFO     Writing ^2 + \frac{1}{6} to media\Tex\ace87e377f098ba2.tex                                                                                                   tex_file_writing.py:109
# # # [12/20/24 03:16:09] INFO     Writing ^3 + \cdots + \frac{1}{n!} to media\Tex\fd8562405d515996.tex                                                                                         tex_file_writing.py:109
                    # # # INFO     Writing ^n + \cdots to media\Tex\7b1ce3e32e4f325f.tex                                                                                                        tex_file_writing.py:109
# # # [12/20/24 03:16:10] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\CorrectLaTeXSubstringColoring_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered CorrectLaTeXSubstringColoring                                                                                                                                  scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\CorrectLaTeXSubstringColoring_ManimCE_v0.18.1.png'   			





from manim import *

class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)

        # index the first (and only) term of the MathTex mob
        self.add(index_labels(text[0]))

        text[0][1:3].set_color(YELLOW)
        text[0][3:6].set_color(RED)
        self.add(text)


# # # D:\SANJOY_NATH_MANIMS>

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py IndexLabelsMathTex
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:17:14] INFO     Writing \binom{2n}{n+2} to media\Tex\2f23396fad89bdac.tex                                                                                                    tex_file_writing.py:109
# # # [12/20/24 03:17:15] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\IndexLabelsMathTex_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered IndexLabelsMathTex                                                                                                                                             scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\IndexLabelsMathTex_ManimCE_v0.18.1.png'               		
					
					
from manim import *

class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(
            r"$x^2 + y^2 = z^2$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=144,
        )
        self.add(tex)			



		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		



# # # SPECIALLY INSTALLS LATEX FONTS

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LaTeXMathFonts
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:18:27] INFO     Writing $x^2 + y^2 = z^2$ to media\Tex\4de401574564c095.tex                                                                                                  tex_file_writing.py:109
# # # [12/20/24 03:18:50] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LaTeXMathFonts_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LaTeXMathFonts                                                                                                                                                 scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LaTeXMathFonts_ManimCE_v0.18.1.png'   	


from manim import *

class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello ?? \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)					
		
		
		
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LaTeXTemplateLibrary
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("\pi"), MathTex("2 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # [12/20/24 03:19:41] INFO     Writing Hello ?? \LaTeX to media\Tex\6cf56319ab0943f6.tex                                                                                                    tex_file_writing.py:109

# # # Sorry, but miktex-makemf did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # hbf2gf (CJK ver. 4.8.4)


# # # Sorry, but miktex-maketfm did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # Sorry, but miktex-makemf did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # hbf2gf (CJK ver. 4.8.4)


# # # Sorry, but miktex-maketfm did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # Sorry, but miktex-makemf did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # hbf2gf (CJK ver. 4.8.4)


# # # Sorry, but miktex-maketfm did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # Sorry, but miktex-makemf did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # hbf2gf (CJK ver. 4.8.4)


# # # Sorry, but miktex-maketfm did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # Sorry, but miktex-makemf did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # hbf2gf (CJK ver. 4.8.4)


# # # Sorry, but miktex-maketfm did not succeed.

# # # The log file hopefully contains the information to get MiKTeX going again:

  # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log
# # # [12/20/24 03:21:42] ERROR    LaTeX compilation error: Package fontspec Error: The font "SimHei" cannot be found.                                                                          tex_file_writing.py:314

# # # ?------------------------------- Traceback (most recent call last) --------------------------------?
# # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\cli\render\commands.py:120 in render   ¦
# # # ¦                                                                                                  ¦
# # # ¦   117 ¦   ¦   ¦   try:                                                                           ¦
# # # ¦   118 ¦   ¦   ¦   ¦   with tempconfig({}):                                                       ¦
# # # ¦   119 ¦   ¦   ¦   ¦   ¦   scene = SceneClass()                                                   ¦
# # # ¦ ? 120 ¦   ¦   ¦   ¦   ¦   scene.render()                                                         ¦
# # # ¦   121 ¦   ¦   ¦   except Exception:                                                              ¦
# # # ¦   122 ¦   ¦   ¦   ¦   error_console.print_exception()                                            ¦
# # # ¦   123 ¦   ¦   ¦   ¦   sys.exit(1)                                                                ¦
# # # ¦                                                                                                  ¦
# # # ¦ C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\scene\scene.py:229 in  ¦
# # # ¦ render                                                                                           ¦
# # # ¦                                                                                                  ¦
# # # ¦    226 ¦   ¦   """                                                                               ¦
# # # ¦    227 ¦   ¦   self.setup()                                                                      ¦
# # # ¦    228 ¦   ¦   try:                                                                              ¦
# # # ¦ ?  229 ¦   ¦   ¦   self.construct()                                                              ¦
# # # ¦    230 ¦   ¦   except EndSceneEarlyException:                                                    ¦
# # # ¦    231 ¦   ¦   ¦   pass                                                                          ¦
# # # ¦    232 ¦   ¦   except RerunSceneException as e:                                                  ¦
# # # ¦                                                                                                  ¦
# # # ¦ D:\SANJOY_NATH_MANIMS\scene.py:3532 in construct                                                 ¦
# # # ¦                                                                                                  ¦
# # # ¦   3529                                                                                           ¦
# # # ¦   3530 class LaTeXTemplateLibrary(Scene):                                                        ¦
# # # ¦   3531 ¦   def construct(self):                                                                  ¦
# # # ¦ ? 3532 ¦   ¦   tex = Tex('Hello ?? \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=14  ¦
# # # ¦   3533 ¦   ¦   self.add(tex)                                                                     ¦
# # # ¦   3534                                                                                           ¦
# # # ¦                                                                                                  ¦
# # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:443 in     ¦
# # # ¦ __init__                                                                                         ¦
# # # ¦                                                                                                  ¦
# # # ¦   440 ¦   def __init__(                                                                          ¦
# # # ¦   441 ¦   ¦   self, *tex_strings, arg_separator="", tex_environment="center", **kwargs           ¦
# # # ¦   442 ¦   ):                                                                                     ¦
# # # ¦ ? 443 ¦   ¦   super().__init__(                                                                  ¦
# # # ¦   444 ¦   ¦   ¦   *tex_strings,                                                                  ¦
# # # ¦   445 ¦   ¦   ¦   arg_separator=arg_separator,                                                   ¦
# # # ¦   446 ¦   ¦   ¦   tex_environment=tex_environment,                                               ¦
# # # ¦                                                                                                  ¦
# # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:293 in     ¦
# # # ¦ __init__                                                                                         ¦
# # # ¦                                                                                                  ¦
# # # ¦   290 ¦   ¦   ¦   ¦   ¦   ¦   """,                                                               ¦
# # # ¦   291 ¦   ¦   ¦   ¦   ¦   ),                                                                     ¦
# # # ¦   292 ¦   ¦   ¦   ¦   )                                                                          ¦
# # # ¦ ? 293 ¦   ¦   ¦   raise compilation_error                                                        ¦
# # # ¦   294 ¦   ¦   self.set_color_by_tex_to_color_map(self.tex_to_color_map)                          ¦
# # # ¦   295 ¦   ¦                                                                                      ¦
# # # ¦   296 ¦   ¦   if self.organize_left_to_right:                                                    ¦
# # # ¦                                                                                                  ¦
# # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:272 in     ¦
# # # ¦ __init__                                                                                         ¦
# # # ¦                                                                                                  ¦
# # # ¦   269 ¦   ¦   self.brace_notation_split_occurred = False                                         ¦
# # # ¦   270 ¦   ¦   self.tex_strings = self._break_up_tex_strings(tex_strings)                         ¦
# # # ¦   271 ¦   ¦   try:                                                                               ¦
# # # ¦ ? 272 ¦   ¦   ¦   super().__init__(                                                              ¦
# # # ¦   273 ¦   ¦   ¦   ¦   self.arg_separator.join(self.tex_strings),                                 ¦
# # # ¦   274 ¦   ¦   ¦   ¦   tex_environment=self.tex_environment,                                      ¦
# # # ¦   275 ¦   ¦   ¦   ¦   tex_template=self.tex_template,                                            ¦
# # # ¦                                                                                                  ¦
# # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:81 in      ¦
# # # ¦ __init__                                                                                         ¦
# # # ¦                                                                                                  ¦
# # # ¦    78 ¦   ¦                                                                                      ¦
# # # ¦    79 ¦   ¦   assert isinstance(tex_string, str)                                                 ¦
# # # ¦    80 ¦   ¦   self.tex_string = tex_string                                                       ¦
# # # ¦ ?  81 ¦   ¦   file_name = tex_to_svg_file(                                                       ¦
# # # ¦    82 ¦   ¦   ¦   self._get_modified_expression(tex_string),                                     ¦
# # # ¦    83 ¦   ¦   ¦   environment=self.tex_environment,                                              ¦
# # # ¦    84 ¦   ¦   ¦   tex_template=self.tex_template,                                                ¦
# # # ¦                                                                                                  ¦
# # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\tex_file_writing.py:63 in        ¦
# # # ¦ tex_to_svg_file                                                                                  ¦
# # # ¦                                                                                                  ¦
# # # ¦    60 ¦   if svg_file.exists():                                                                  ¦
# # # ¦    61 ¦   ¦   return svg_file                                                                    ¦
# # # ¦    62 ¦                                                                                          ¦
# # # ¦ ?  63 ¦   dvi_file = compile_tex(                                                                ¦
# # # ¦    64 ¦   ¦   tex_file,                                                                          ¦
# # # ¦    65 ¦   ¦   tex_template.tex_compiler,                                                         ¦
# # # ¦    66 ¦   ¦   tex_template.output_format,                                                        ¦
# # # ¦                                                                                                  ¦
# # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\tex_file_writing.py:213 in       ¦
# # # ¦ compile_tex                                                                                      ¦
# # # ¦                                                                                                  ¦
# # # ¦   210 ¦   ¦   if exit_code != 0:                                                                 ¦
# # # ¦   211 ¦   ¦   ¦   log_file = tex_file.with_suffix(".log")                                        ¦
# # # ¦   212 ¦   ¦   ¦   print_all_tex_errors(log_file, tex_compiler, tex_file)                         ¦
# # # ¦ ? 213 ¦   ¦   ¦   raise ValueError(                                                              ¦
# # # ¦   214 ¦   ¦   ¦   ¦   f"{tex_compiler} error converting to"                                      ¦
# # # ¦   215 ¦   ¦   ¦   ¦   f" {output_format[1:]}. See log output above or"                           ¦
# # # ¦   216 ¦   ¦   ¦   ¦   f" the log file: {log_file}",                                              ¦
# # # ?--------------------------------------------------------------------------------------------------?
# # # ValueError: xelatex error converting to xdv. See log output above or the log file: media\Tex\6cf56319ab0943f6.log		











# # # # # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LaTeXTemplateLibrary
# # # # # # # Manim Community v0.18.1

# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # # cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
  # # # # # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
  # # # # # # # x_label=Tex("$\Delta Q$"), y_label=Tex("T[$^\circ C$]")
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # # MathTex("\pi"), MathTex("2 \pi"),
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # # MathTex("\pi"), MathTex("2 \pi"),
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
  # # # # # # # MathTex("3 \pi"), MathTex("4 \pi"),
# # # # # # # [12/20/24 03:19:41] INFO     Writing Hello ?? \LaTeX to media\Tex\6cf56319ab0943f6.tex                                                                                                    tex_file_writing.py:109

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log
# # # # # # # [12/20/24 03:21:42] ERROR    LaTeX compilation error: Package fontspec Error: The font "SimHei" cannot be found.                                                                          tex_file_writing.py:314

# # # # # # # ?------------------------------- Traceback (most recent call last) --------------------------------?
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\cli\render\commands.py:120 in render   ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   117 ¦   ¦   ¦   try:                                                                           ¦
# # # # # # # ¦   118 ¦   ¦   ¦   ¦   with tempconfig({}):                                                       ¦
# # # # # # # ¦   119 ¦   ¦   ¦   ¦   ¦   scene = SceneClass()                                                   ¦
# # # # # # # ¦ ? 120 ¦   ¦   ¦   ¦   ¦   scene.render()                                                         ¦
# # # # # # # ¦   121 ¦   ¦   ¦   except Exception:                                                              ¦
# # # # # # # ¦   122 ¦   ¦   ¦   ¦   error_console.print_exception()                                            ¦
# # # # # # # ¦   123 ¦   ¦   ¦   ¦   sys.exit(1)                                                                ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\scene\scene.py:229 in  ¦
# # # # # # # ¦ render                                                                                           ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦    226 ¦   ¦   """                                                                               ¦
# # # # # # # ¦    227 ¦   ¦   self.setup()                                                                      ¦
# # # # # # # ¦    228 ¦   ¦   try:                                                                              ¦
# # # # # # # ¦ ?  229 ¦   ¦   ¦   self.construct()                                                              ¦
# # # # # # # ¦    230 ¦   ¦   except EndSceneEarlyException:                                                    ¦
# # # # # # # ¦    231 ¦   ¦   ¦   pass                                                                          ¦
# # # # # # # ¦    232 ¦   ¦   except RerunSceneException as e:                                                  ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ D:\SANJOY_NATH_MANIMS\scene.py:3532 in construct                                                 ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   3529                                                                                           ¦
# # # # # # # ¦   3530 class LaTeXTemplateLibrary(Scene):                                                        ¦
# # # # # # # ¦   3531 ¦   def construct(self):                                                                  ¦
# # # # # # # ¦ ? 3532 ¦   ¦   tex = Tex('Hello ?? \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=14  ¦
# # # # # # # ¦   3533 ¦   ¦   self.add(tex)                                                                     ¦
# # # # # # # ¦   3534                                                                                           ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:443 in     ¦
# # # # # # # ¦ __init__                                                                                         ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   440 ¦   def __init__(                                                                          ¦
# # # # # # # ¦   441 ¦   ¦   self, *tex_strings, arg_separator="", tex_environment="center", **kwargs           ¦
# # # # # # # ¦   442 ¦   ):                                                                                     ¦
# # # # # # # ¦ ? 443 ¦   ¦   super().__init__(                                                                  ¦
# # # # # # # ¦   444 ¦   ¦   ¦   *tex_strings,                                                                  ¦
# # # # # # # ¦   445 ¦   ¦   ¦   arg_separator=arg_separator,                                                   ¦
# # # # # # # ¦   446 ¦   ¦   ¦   tex_environment=tex_environment,                                               ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:293 in     ¦
# # # # # # # ¦ __init__                                                                                         ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   290 ¦   ¦   ¦   ¦   ¦   ¦   """,                                                               ¦
# # # # # # # ¦   291 ¦   ¦   ¦   ¦   ¦   ),                                                                     ¦
# # # # # # # ¦   292 ¦   ¦   ¦   ¦   )                                                                          ¦
# # # # # # # ¦ ? 293 ¦   ¦   ¦   raise compilation_error                                                        ¦
# # # # # # # ¦   294 ¦   ¦   self.set_color_by_tex_to_color_map(self.tex_to_color_map)                          ¦
# # # # # # # ¦   295 ¦   ¦                                                                                      ¦
# # # # # # # ¦   296 ¦   ¦   if self.organize_left_to_right:                                                    ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:272 in     ¦
# # # # # # # ¦ __init__                                                                                         ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   269 ¦   ¦   self.brace_notation_split_occurred = False                                         ¦
# # # # # # # ¦   270 ¦   ¦   self.tex_strings = self._break_up_tex_strings(tex_strings)                         ¦
# # # # # # # ¦   271 ¦   ¦   try:                                                                               ¦
# # # # # # # ¦ ? 272 ¦   ¦   ¦   super().__init__(                                                              ¦
# # # # # # # ¦   273 ¦   ¦   ¦   ¦   self.arg_separator.join(self.tex_strings),                                 ¦
# # # # # # # ¦   274 ¦   ¦   ¦   ¦   tex_environment=self.tex_environment,                                      ¦
# # # # # # # ¦   275 ¦   ¦   ¦   ¦   tex_template=self.tex_template,                                            ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:81 in      ¦
# # # # # # # ¦ __init__                                                                                         ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦    78 ¦   ¦                                                                                      ¦
# # # # # # # ¦    79 ¦   ¦   assert isinstance(tex_string, str)                                                 ¦
# # # # # # # ¦    80 ¦   ¦   self.tex_string = tex_string                                                       ¦
# # # # # # # ¦ ?  81 ¦   ¦   file_name = tex_to_svg_file(                                                       ¦
# # # # # # # ¦    82 ¦   ¦   ¦   self._get_modified_expression(tex_string),                                     ¦
# # # # # # # ¦    83 ¦   ¦   ¦   environment=self.tex_environment,                                              ¦
# # # # # # # ¦    84 ¦   ¦   ¦   tex_template=self.tex_template,                                                ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\tex_file_writing.py:63 in        ¦
# # # # # # # ¦ tex_to_svg_file                                                                                  ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦    60 ¦   if svg_file.exists():                                                                  ¦
# # # # # # # ¦    61 ¦   ¦   return svg_file                                                                    ¦
# # # # # # # ¦    62 ¦                                                                                          ¦
# # # # # # # ¦ ?  63 ¦   dvi_file = compile_tex(                                                                ¦
# # # # # # # ¦    64 ¦   ¦   tex_file,                                                                          ¦
# # # # # # # ¦    65 ¦   ¦   tex_template.tex_compiler,                                                         ¦
# # # # # # # ¦    66 ¦   ¦   tex_template.output_format,                                                        ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\tex_file_writing.py:213 in       ¦
# # # # # # # ¦ compile_tex                                                                                      ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   210 ¦   ¦   if exit_code != 0:                                                                 ¦
# # # # # # # ¦   211 ¦   ¦   ¦   log_file = tex_file.with_suffix(".log")                                        ¦
# # # # # # # ¦   212 ¦   ¦   ¦   print_all_tex_errors(log_file, tex_compiler, tex_file)                         ¦
# # # # # # # ¦ ? 213 ¦   ¦   ¦   raise ValueError(                                                              ¦
# # # # # # # ¦   214 ¦   ¦   ¦   ¦   f"{tex_compiler} error converting to"                                      ¦
# # # # # # # ¦   215 ¦   ¦   ¦   ¦   f" {output_format[1:]}. See log output above or"                           ¦
# # # # # # # ¦   216 ¦   ¦   ¦   ¦   f" the log file: {log_file}",                                              ¦
# # # # # # # ?--------------------------------------------------------------------------------------------------?
# # # # # # # ValueError: xelatex error converting to xdv. See log output above or the log file: media\Tex\6cf56319ab0943f6.log

# # # # # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LaTeXTemplateLibrary
# # # # # # # Manim Community v0.18.1

# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # # # # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log

# # # # # # # Sorry, but miktex-makemf did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-makemf.log
# # # # # # # Couldn't open `OT:script=hani;language=dfl.cfg'

# # # # # # # hbf2gf (CJK ver. 4.8.4)


# # # # # # # Sorry, but miktex-maketfm did not succeed.

# # # # # # # The log file hopefully contains the information to get MiKTeX going again:

  # # # # # # # C:\Users\Sanjoy Nath\AppData\Local\MiKTeX\miktex\log\miktex-maketfm.log
# # # # # # # [12/20/24 03:22:35] ERROR    LaTeX compilation error: Package fontspec Error: The font "SimHei" cannot be found.                                                                          tex_file_writing.py:314

# # # # # # # ?------------------------------- Traceback (most recent call last) --------------------------------?
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\cli\render\commands.py:120 in render   ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   117 ¦   ¦   ¦   try:                                                                           ¦
# # # # # # # ¦   118 ¦   ¦   ¦   ¦   with tempconfig({}):                                                       ¦
# # # # # # # ¦   119 ¦   ¦   ¦   ¦   ¦   scene = SceneClass()                                                   ¦
# # # # # # # ¦ ? 120 ¦   ¦   ¦   ¦   ¦   scene.render()                                                         ¦
# # # # # # # ¦   121 ¦   ¦   ¦   except Exception:                                                              ¦
# # # # # # # ¦   122 ¦   ¦   ¦   ¦   error_console.print_exception()                                            ¦
# # # # # # # ¦   123 ¦   ¦   ¦   ¦   sys.exit(1)                                                                ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\scene\scene.py:229 in  ¦
# # # # # # # ¦ render                                                                                           ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦    226 ¦   ¦   """                                                                               ¦
# # # # # # # ¦    227 ¦   ¦   self.setup()                                                                      ¦
# # # # # # # ¦    228 ¦   ¦   try:                                                                              ¦
# # # # # # # ¦ ?  229 ¦   ¦   ¦   self.construct()                                                              ¦
# # # # # # # ¦    230 ¦   ¦   except EndSceneEarlyException:                                                    ¦
# # # # # # # ¦    231 ¦   ¦   ¦   pass                                                                          ¦
# # # # # # # ¦    232 ¦   ¦   except RerunSceneException as e:                                                  ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ D:\SANJOY_NATH_MANIMS\scene.py:3532 in construct                                                 ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:443 in     ¦
# # # # # # # ¦ __init__                                                                                         ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   440 ¦   def __init__(                                                                          ¦
# # # # # # # ¦   441 ¦   ¦   self, *tex_strings, arg_separator="", tex_environment="center", **kwargs           ¦
# # # # # # # ¦   442 ¦   ):                                                                                     ¦
# # # # # # # ¦ ? 443 ¦   ¦   super().__init__(                                                                  ¦
# # # # # # # ¦   444 ¦   ¦   ¦   *tex_strings,                                                                  ¦
# # # # # # # ¦   445 ¦   ¦   ¦   arg_separator=arg_separator,                                                   ¦
# # # # # # # ¦   446 ¦   ¦   ¦   tex_environment=tex_environment,                                               ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:293 in     ¦
# # # # # # # ¦ __init__                                                                                         ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   290 ¦   ¦   ¦   ¦   ¦   ¦   """,                                                               ¦
# # # # # # # ¦   291 ¦   ¦   ¦   ¦   ¦   ),                                                                     ¦
# # # # # # # ¦   292 ¦   ¦   ¦   ¦   )                                                                          ¦
# # # # # # # ¦ ? 293 ¦   ¦   ¦   raise compilation_error                                                        ¦
# # # # # # # ¦   294 ¦   ¦   self.set_color_by_tex_to_color_map(self.tex_to_color_map)                          ¦
# # # # # # # ¦   295 ¦   ¦                                                                                      ¦
# # # # # # # ¦   296 ¦   ¦   if self.organize_left_to_right:                                                    ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:272 in     ¦
# # # # # # # ¦ __init__                                                                                         ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   269 ¦   ¦   self.brace_notation_split_occurred = False                                         ¦
# # # # # # # ¦   270 ¦   ¦   self.tex_strings = self._break_up_tex_strings(tex_strings)                         ¦
# # # # # # # ¦   271 ¦   ¦   try:                                                                               ¦
# # # # # # # ¦ ? 272 ¦   ¦   ¦   super().__init__(                                                              ¦
# # # # # # # ¦   273 ¦   ¦   ¦   ¦   self.arg_separator.join(self.tex_strings),                                 ¦
# # # # # # # ¦   274 ¦   ¦   ¦   ¦   tex_environment=self.tex_environment,                                      ¦
# # # # # # # ¦   275 ¦   ¦   ¦   ¦   tex_template=self.tex_template,                                            ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\mobject\text\tex_mobject.py:81 in      ¦
# # # # # # # ¦ __init__                                                                                         ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦    78 ¦   ¦                                                                                      ¦
# # # # # # # ¦    79 ¦   ¦   assert isinstance(tex_string, str)                                                 ¦
# # # # # # # ¦    80 ¦   ¦   self.tex_string = tex_string                                                       ¦
# # # # # # # ¦ ?  81 ¦   ¦   file_name = tex_to_svg_file(                                                       ¦
# # # # # # # ¦    82 ¦   ¦   ¦   self._get_modified_expression(tex_string),                                     ¦
# # # # # # # ¦    83 ¦   ¦   ¦   environment=self.tex_environment,                                              ¦
# # # # # # # ¦    84 ¦   ¦   ¦   tex_template=self.tex_template,                                                ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\tex_file_writing.py:63 in        ¦
# # # # # # # ¦ tex_to_svg_file                                                                                  ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦    60 ¦   if svg_file.exists():                                                                  ¦
# # # # # # # ¦    61 ¦   ¦   return svg_file                                                                    ¦
# # # # # # # ¦    62 ¦                                                                                          ¦
# # # # # # # ¦ ?  63 ¦   dvi_file = compile_tex(                                                                ¦
# # # # # # # ¦    64 ¦   ¦   tex_file,                                                                          ¦
# # # # # # # ¦    65 ¦   ¦   tex_template.tex_compiler,                                                         ¦
# # # # # # # ¦    66 ¦   ¦   tex_template.output_format,                                                        ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦ C:\Users\Sanjoy                                                                                  ¦
# # # # # # # ¦ Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\tex_file_writing.py:213 in       ¦
# # # # # # # ¦ compile_tex                                                                                      ¦
# # # # # # # ¦                                                                                                  ¦
# # # # # # # ¦   210 ¦   ¦   if exit_code != 0:                                                                 ¦
# # # # # # # ¦   211 ¦   ¦   ¦   log_file = tex_file.with_suffix(".log")                                        ¦
# # # # # # # ¦   212 ¦   ¦   ¦   print_all_tex_errors(log_file, tex_compiler, tex_file)                         ¦
# # # # # # # ¦ ? 213 ¦   ¦   ¦   raise ValueError(                                                              ¦
# # # # # # # ¦   214 ¦   ¦   ¦   ¦   f"{tex_compiler} error converting to"                                      ¦
# # # # # # # ¦   215 ¦   ¦   ¦   ¦   f" {output_format[1:]}. See log output above or"                           ¦
# # # # # # # ¦   216 ¦   ¦   ¦   ¦   f" the log file: {log_file}",                                              ¦
# # # # # # # ?--------------------------------------------------------------------------------------------------?
# # # # # # # ValueError: xelatex error converting to xdv. See log output above or the log file: media\Tex\6cf56319ab0943f6.log



from manim import *

class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)
		
		
	




# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py LaTeXAlignEnvironment
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:25:00] INFO     Writing f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6 to media\Tex\bfc3f3c312a7934f.tex                                                                               tex_file_writing.py:109
# # # [12/20/24 03:25:01] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LaTeXAlignEnvironment_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LaTeXAlignEnvironment                                                                                                                                          scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LaTeXAlignEnvironment_ManimCE_v0.18.1.png'    

# # # class LaTeXTemplateLibrary(Scene):
    # # # def construct(self):
        # # # tex = Tex('Hello ?? \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        # # # self.add(tex)



# # # # don't remove below command for run button to work
# # # %manim -qm -v WARNING LaTeXTemplateLibrary				






# # # D:\SANJOY_NATH_MANIMS>manim -qm -v WARNING LaTeXTemplateLibrary
# # # Manim Community v0.18.1

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
  # # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\module_ops.py", line 57, in get_module
    # # # raise FileNotFoundError(f"{file_name} not found")
# # # FileNotFoundError: D:\SANJOY_NATH_MANIMS\LaTeXTemplateLibrary not found

from manim import *

class Example1Text(Scene):
    def construct(self):
        text = Text('Hello world').scale(3)
        self.add(text)	
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py Example1Text
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:32:20] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\Example1Text_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered Example1Text                                                                                                                                                   scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\Example1Text_ManimCE_v0.18.1.png'     


from manim import *

class TextColorExample(Scene):
    def construct(self):
        text1 = Text('Hello world', color=BLUE).scale(3)
        text2 = Text('Hello world', gradient=(BLUE, GREEN)).scale(3).next_to(text1, DOWN)
        self.add(text1, text2)		












# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TextColorExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:33:02] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextColorExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered TextColorExample                                                                                                                                               scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextColorExample_ManimCE_v0.18.1.png'                              

from manim import *

class TextItalicAndBoldExample(Scene):
    def construct(self):
        text1 = Text("Hello world", slant=ITALIC)
        text2 = Text("Hello world", t2s={'world':ITALIC})
        text3 = Text("Hello world", weight=BOLD)
        text4 = Text("Hello world", t2w={'world':BOLD})
        text5 = Text("Hello world", t2c={'o':YELLOW}, disable_ligatures=True)
        text6 = Text(
            "Visit us at docs.manim.community",
            t2c={"docs.manim.community": YELLOW},
            disable_ligatures=True,
       )
        text6.scale(1.3).shift(DOWN)
        self.add(text1, text2, text3, text4, text5 , text6)
        Group(*self.mobjects).arrange(DOWN, buff=.8).set(height=config.frame_height-LARGE_BUFF)			





# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TextItalicAndBoldExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:33:48] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextItalicAndBoldExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered TextItalicAndBoldExample                                                                                                                                       scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextItalicAndBoldExample_ManimCE_v0.18.1.png'                

from manim import *

class TextMoreCustomization(Scene):
    def construct(self):
        text1 = Text(
            'Google',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                 '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                 '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
        self.add(text1)	




# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TextMoreCustomization
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:34:32] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextMoreCustomization_ManimCE_v0.18.1.png'

# # # [12/20/24 03:34:33] INFO     Rendered TextMoreCustomization                                                                                                                                          scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextMoreCustomization_ManimCE_v0.18.1.png'     		
					
					
					
					
					
					
					
					
					
from manim import *

class MultipleFonts(Scene):
    def construct(self):
        morning = Text("???????", font="sans-serif")
        japanese = Text(
            "???????", t2c={"??": BLUE}
        )  # works same as ``Text``.
        mess = Text("Multi-Language", weight=BOLD)
        russ = Text("???????????? ?? ?? ? ", font="sans-serif")
        hin = Text("??????", font="sans-serif")
        arb = Text(
            "???? ????? \n ????? ????????", font="sans-serif"
        )  # don't mix RTL and LTR languages nothing shows up then ;-)
        chinese = Text("??????????", font="sans-serif")
        self.add(morning, japanese, mess, russ, hin, arb, chinese)
        for i,mobj in enumerate(self.mobjects):
            mobj.shift(DOWN*(i-3))		


			# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TextItalicAndBoldExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:33:48] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextItalicAndBoldExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered TextItalicAndBoldExample                                                                                                                                       scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextItalicAndBoldExample_ManimCE_v0.18.1.png'                                                           file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py TextMoreCustomization
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:34:32] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextMoreCustomization_ManimCE_v0.18.1.png'

# # # [12/20/24 03:34:33] INFO     Rendered TextMoreCustomization                                                                                                                                          scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\TextMoreCustomization_ManimCE_v0.18.1.png'                                                              file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MultipleFonts
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:35:16] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\MultipleFonts_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered MultipleFonts                                                                                                                                                  scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\MultipleFonts_ManimCE_v0.18.1.png'  
					
					
from manim import *

class PangoRender(Scene):
    def construct(self):
        morning = Text("???????", font="sans-serif")
        self.play(Write(morning))
        self.wait(2)		

class MultipleFonts(Scene):
    def construct(self):
        morning = Text("???????", font="sans-serif")
        japanese = Text(
            "???????", t2c={"??": BLUE}
        )  # works same as ``Text``.
        mess = Text("Multi-Language", weight=BOLD)
        russ = Text("???????????? ?? ?? ? ", font="sans-serif")
        hin = Text("??????", font="sans-serif")
        arb = Text(
            "???? ????? \n ????? ????????", font="sans-serif"
        )  # don't mix RTL and LTR languages nothing shows up then ;-)
        chinese = Text("??????????", font="sans-serif")
        self.add(morning, japanese, mess, russ, hin, arb, chinese)
        for i,mobj in enumerate(self.mobjects):
            mobj.shift(DOWN*(i-3))



# # # # don't remove below command for run button to work
# # # %manim -qm -v WARNING MultipleFonts





# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py MultipleFonts
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
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
  # # # File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  # # # File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  # # # File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  # # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # # File "D:\SANJOY_NATH_MANIMS\scene.py", line 4476
    # # # %manim -qm -v WARNING MultipleFonts
    # # # ^
# # # SyntaxError: invalid syntax
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PangoRender
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1486: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1732: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2389: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:2390: SyntaxWarning: invalid escape sequence '\p'
# # # [12/20/24 03:37:18] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PangoRender\1185818338_1060609740_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\partial_movie_files\PangoRender\624642324_1141282389_2311469246.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\PangoRender.mp4'

                    # # # INFO     Rendered PangoRender                                                                                                                                                    scene.py:247
                             # # # Played 2 animations
# # # [12/20/24 03:37:19] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\scene\480p15\PangoRender.mp4' 








                  		