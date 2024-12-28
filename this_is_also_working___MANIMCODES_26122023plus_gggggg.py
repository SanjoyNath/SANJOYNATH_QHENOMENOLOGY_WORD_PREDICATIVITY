					
from manim import *
class GetHorizontalLineExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        point = ax.c2p(-4, 1.5)
        dot = Dot(point)
        line = ax.get_horizontal_line(point, line_func=Line)
        self.add(ax, line, dot)
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetHorizontalLineExample
# # # Manim Community v0.18.1
# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3970: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:4018: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:8411: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:8445: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:00:01] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered GetHorizontalLineExample                                                                                                                                       scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'              		
from manim import *
class GetLinesToPointExample(Scene):
    def construct(self):
        ax = Axes()
        circ = Circle(radius=0.5).move_to([-4, -1.5, 0])
        lines_1 = ax.get_lines_to_point(circ.get_right(), color=GREEN_B)
        lines_2 = ax.get_lines_to_point(circ.get_corner(DL), color=BLUE_B)
        self.add(ax, lines_1, lines_2, circ)
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetLinesToPointExample
# # # Manim Community v0.18.1
# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3970: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:4018: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:8411: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:8445: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:00:42] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered GetLinesToPointExample                                                                                                                                         scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
from manim import *
class GetRiemannRectanglesExample(Scene):
    def construct(self):
        ax = Axes(y_range=[-2, 10])
        quadratic = ax.plot(lambda x: 0.5 * x ** 2 - 0.5)
        # the rectangles are constructed from their top right corner.
        # passing an iterable to `color` produces a gradient
        rects_right = ax.get_riemann_rectangles(
            quadratic,
            x_range=[-4, -3],
            dx=0.25,
            color=(TEAL, BLUE_B, DARK_BLUE),
            input_sample_type="right",
        )
        # the colour of rectangles below the x-axis is inverted
        # due to show_signed_area
        rects_left = ax.get_riemann_rectangles(
            quadratic, x_range=[-1.5, 1.5], dx=0.15, color=YELLOW
        )
        bounding_line = ax.plot(
            lambda x: 1.5 * x, color=BLUE_B, x_range=[3.3, 6]
        )
        bounded_rects = ax.get_riemann_rectangles(
            bounding_line,
            bounded_graph=quadratic,
            dx=0.15,
            x_range=[4, 5],
            show_signed_area=False,
            color=(MAROON_A, RED_B, PURPLE_D),
        )
        self.add(
            ax, bounding_line, quadratic, rects_right, rects_left, bounded_rects
        )		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetRiemannRectanglesExample
# # # Manim Community v0.18.1
# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3970: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:4018: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:8411: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:8445: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:01:24] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered GetRiemannRectanglesExample                                                                                                                                    scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'               
from manim import *
class GetSecantSlopeGroupExample(Scene):
    def construct(self):
        ax = Axes(y_range=[-1, 7])
        graph = ax.plot(lambda x: 1 / 4 * x ** 2, color=BLUE)
        slopes = ax.get_secant_slope_group(
            x=2.0,
            graph=graph,
            dx=1.0,
            dx_label=Tex("dx = 1.0"),
            dy_label="dy",
            dx_line_color=GREEN_B,
            secant_line_length=4,
            secant_line_color=RED_D,
        )
        self.add(ax, graph, slopes)					
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetSecantSlopeGroupExample
# # # Manim Community v0.18.1
# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3970: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:4018: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:8411: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:8445: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:02:07] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO     Writing dx = 1.0 to media\Tex\3d7240a1b1e23b0f.tex                                                                                                           tex_file_writing.py:109
# # # [12/28/24 05:02:09] INFO     Writing dy to media\Tex\3fb38292b53d3ab3.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:02:10] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'
                    # # # INFO     Rendered GetSecantSlopeGroupExample                                                                                                                                     scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'     
					
	
























































	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

from manim import *

class GetVerticalLineExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        point = ax.coords_to_point(-3.5, 2)

        dot = Dot(point)
        line = ax.get_vertical_line(point, line_config={"dashed_ratio": 0.85})

        self.add(ax, line, dot)	
					
					
					
					
					

# # # # # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetVerticalLineExample
# # # # # # Manim Community v0.18.1

# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # # # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # # # # [12/28/24 05:03:23] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # # # # Played 0 animations
                    # # # # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # # # # Graph data has been written to graph_data.csv
                    # # # # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # # # # Played 0 animations
# # # # # # [12/28/24 05:03:24] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # # # # Played 0 animations
                    # # # # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # # # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # # # # INFO     Rendered GetVerticalLineExample                                                                                                                                         scene.py:247
                             # # # # # # Played 0 animations
                    # # # # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                      					
					
					
					
from manim import *

class GetVerticalLinesToGraph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 8.0, 1],
            y_range=[-1, 1, 0.2],
            axis_config={"font_size": 24},
        ).add_coordinates()

        curve = ax.plot(lambda x: np.sin(x) / np.e ** 2 * x)

        lines = ax.get_vertical_lines_to_graph(
            curve, x_range=[0, 4], num_lines=30, color=BLUE
        )

        self.add(ax, curve, lines)					
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetVerticalLinesToGraph
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:04:04] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
# # # [12/28/24 05:04:05] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetVerticalLinesToGraph                                                                                                                                        scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                             


					
					







from manim import *

class GetXAxisLabelExample(Scene):
    def construct(self):
        ax = Axes(x_range=(0, 8), y_range=(0, 5), x_length=8, y_length=5)
        x_label = ax.get_x_axis_label(
            Tex("$x$-values").scale(0.65), edge=DOWN, direction=DOWN, buff=0.5
        )
        self.add(ax, x_label)
















# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetXAxisLabelExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:04:46] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO     Writing $x$-values to media\Tex\4dccf760cfe9cb44.tex                                                                                                         tex_file_writing.py:109
# # # [12/28/24 05:04:47] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetXAxisLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'             


					
					
					
					
from manim import *

class GetYAxisLabelExample(Scene):
    def construct(self):
        ax = Axes(x_range=(0, 8), y_range=(0, 5), x_length=8, y_length=5)
        y_label = ax.get_y_axis_label(
            Tex("$y$-values").scale(0.65).rotate(90 * DEGREES),
            edge=LEFT,
            direction=LEFT,
            buff=0.3,
        )
        self.add(ax, y_label)					
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetYAxisLabelExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:05:26] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
# # # [12/28/24 05:05:27] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO     Writing $y$-values to media\Tex\0d2186b5ae22cde2.tex                                                                                                         tex_file_writing.py:109
# # # [12/28/24 05:05:28] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetYAxisLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                          		
					
					
from manim import *

class InputToGraphPointExample(Scene):
    def construct(self):
        ax = Axes()
        curve = ax.plot(lambda x : np.cos(x))

        # move a square to PI on the cosine curve.
        position = ax.input_to_graph_point(x=PI, graph=curve)
        sq = Square(side_length=1, color=YELLOW).move_to(position)

        self.add(ax, curve, sq)					
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py InputToGraphPointExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:06:06] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:06:07] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered InputToGraphPointExample                                                                                                                                       scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                   		
					
					










from manim import *

class PlotExample(Scene):
    def construct(self):
        # construct the axes
        ax_1 = Axes(
            x_range=[0.001, 6],
            y_range=[-8, 2],
            x_length=5,
            y_length=3,
            tips=False,
        )
        ax_2 = ax_1.copy()
        ax_3 = ax_1.copy()

        # position the axes
        ax_1.to_corner(UL)
        ax_2.to_corner(UR)
        ax_3.to_edge(DOWN)
        axes = VGroup(ax_1, ax_2, ax_3)

        # create the logarithmic curves
        def log_func(x):
            return np.log(x)

        # a curve without adjustments; poor interpolation.
        curve_1 = ax_1.plot(log_func, color=PURE_RED)

        # disabling interpolation makes the graph look choppy as not enough
        # inputs are available
        curve_2 = ax_2.plot(log_func, use_smoothing=False, color=ORANGE)

        # taking more inputs of the curve by specifying a step for the
        # x_range yields expected results, but increases rendering time.
        curve_3 = ax_3.plot(
            log_func, x_range=(0.001, 6, 0.001), color=PURE_GREEN
        )

        curves = VGroup(curve_1, curve_2, curve_3)

        self.add(axes, curves)


		
from manim import *

class AntiderivativeExample(Scene):
    def construct(self):
        ax = Axes()
        graph1 = ax.plot(
            lambda x: (x ** 2 - 2) / 3,
            color=RED,
        )
        graph2 = ax.plot_antiderivative_graph(graph1, color=BLUE)
        self.add(ax, graph1, graph2)		
		
		
# # # :\SANJOY_NATH_MANIMS>manim -pql scene.py AntiderivativeExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:08:18] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered AntiderivativeExample                                                                                                                                          scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                             


					
					
					
from manim import *

class DerivativeGraphExample(Scene):
    def construct(self):
        ax = NumberPlane(y_range=[-1, 7], background_line_style={"stroke_opacity": 0.4})

        curve_1 = ax.plot(lambda x: x ** 2, color=PURPLE_B)
        curve_2 = ax.plot_derivative_graph(curve_1)
        curves = VGroup(curve_1, curve_2)

        label_1 = ax.get_graph_label(curve_1, "x^2", x_val=-2, direction=DL)
        label_2 = ax.get_graph_label(curve_2, "2x", x_val=3, direction=RIGHT)
        labels = VGroup(label_1, label_2)

        self.add(ax, curves, labels)					
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py DerivativeGraphExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:09:00] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # [12/28/24 05:09:01] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
                    # # # INFO     Writing x^2 to media\Tex\613f18c3c7fa7c72.tex                                                                                                                tex_file_writing.py:109
# # # [12/28/24 05:09:02] INFO     Writing 2x to media\Tex\93b60df4a6db052c.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:09:03] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered DerivativeGraphExample                                                                                                                                         scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'        


	











from manim import *

class ImplicitExample(Scene):
    def construct(self):
        ax = Axes()
        a = ax.plot_implicit_curve(
            lambda x, y: y * (x - y) ** 2 - 4 * x - 8, color=BLUE
        )
        self.add(ax, a)	
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ImplicitExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:10:21] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:10:22] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered ImplicitExample                                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                   		
		

		
from manim import *

class ImplicitExample___saans(Scene):
    def construct(self):
        ax = Axes()
        a = ax.plot_implicit_curve(
            lambda x, y: y * (x - y**x) ** 2 - 4 * x - 8, color=BLUE
        )
        self.add(ax, a)	
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ImplicitExample___saans
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:12:06] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # D:\SANJOY_NATH_MANIMS\scene.py:11011: RuntimeWarning: divide by zero encountered in scalar power
# # # D:\SANJOY_NATH_MANIMS\scene.py:11011: RuntimeWarning: invalid value encountered in scalar multiply
# # # D:\SANJOY_NATH_MANIMS\scene.py:11011: RuntimeWarning: invalid value encountered in scalar power
# # # [12/28/24 05:12:07] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered ImplicitExample___saans                                                                                                                                        scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'   		
		
# # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ImplicitExample___saans
# # Manim Community v0.18.1

# # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # Traceback (most recent call last):
  # # File "<frozen runpy>", line 198, in _run_module_as_main
  # # File "<frozen runpy>", line 88, in _run_code
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\Scripts\manim.exe\__main__.py", line 7, in <module>
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1157, in __call__
    # # return self.main(*args, **kwargs)
           # # ^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1078, in main
    # # rv = self.invoke(ctx)
         # # ^^^^^^^^^^^^^^^^
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1688, in invoke
    # # return _process_result(sub_ctx.command.invoke(sub_ctx))
                           # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 1434, in invoke
    # # return ctx.invoke(self.callback, **ctx.params)
           # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\click\core.py", line 783, in invoke
    # # return __callback(*args, **kwargs)
           # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\cli\render\commands.py", line 116, in render
    # # for SceneClass in scene_classes_from_file(file):
                      # # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\module_ops.py", line 131, in scene_classes_from_file
    # # module = get_module(file_path)
             # # ^^^^^^^^^^^^^^^^^^^^^
  # # File "C:\Users\Sanjoy Nath\AppData\Roaming\Python\Python312\site-packages\manim\utils\module_ops.py", line 54, in get_module
    # # spec.loader.exec_module(module)
  # # File "<frozen importlib._bootstrap_external>", line 991, in exec_module
  # # File "<frozen importlib._bootstrap_external>", line 1129, in get_code
  # # File "<frozen importlib._bootstrap_external>", line 1059, in source_to_code
  # # File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  # # File "D:\SANJOY_NATH_MANIMS\scene.py", line 11005
    # # from manim import *
# # TabError: inconsistent use of tabs and spaces in indentation
		
		
		
		
from manim import *

class ParametricCurveExample(Scene):
    def construct(self):
        ax = Axes()
        cardioid = ax.plot_parametric_curve(
            lambda t: np.array(
                [
                    np.exp(1) * np.cos(t) * (1 - np.cos(t)),
                    np.exp(1) * np.sin(t) * (1 - np.cos(t)),
                    0,
                ]
            ),
            t_range=[0, 2 * PI],
            color="#0FF1CE",
        )
        self.add(ax, cardioid)		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ParametricCurveExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:12:54] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # [12/28/24 05:12:55] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:12:56] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered ParametricCurveExample                                                                                                                                         scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'       		
				
		
		
		
		
		
		
		
		
		
		
from manim import *

class ParametricCurveExample_saans(Scene):
    def construct(self):
        ax = Axes()
        cardioid = ax.plot_parametric_curve(
            lambda t: np.array(
                [
                    np.exp(1) * np.cos(t) * (1 - np.cos(t)*np.sin(t)),
                    np.exp(1) * np.sin(t) * (np.cos(t*t) - np.cos(t)),
                    0,
                ]
            ),
            t_range=[0, 2 * PI],
            color="#0FF1CE",
        )
        self.add(ax, cardioid)		


# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py ParametricCurveExample_saans
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:14:09] INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
# # # [12/28/24 05:14:10] INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
			# # # INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:14:13] INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered ParametricCurveExample_saans                                                                                                                                   scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'      
		
from manim import *

class PolarGraphExample(Scene):
    def construct(self):
        plane = PolarPlane()
        r = lambda theta: 2 * np.sin(theta * 5)
        graph = plane.plot_polar_graph(r, [0, 2 * PI], color=ORANGE)
        self.add(plane, graph)
		
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PolarGraphExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:15:13] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:15:17] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarGraphExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'         		
					
					
					
					
					
					
					
from manim import *
# # # import numpy as np

# # # class PolarGraphExample___saaans_animations(Scene):
    # # # def construct(self):
        # # # plane = PolarPlane()
        # # # r = lambda theta: 2 * np.sin(theta * 5)
        # # # graph = plane.plot_polar_graph(r, [0, 2 * PI], color=ORANGE)
        
        # # # # Animate the construction of the graph with a run_time of 30 seconds
        # # # for _ in range(3):
            # # # self.play(Create(graph), run_time=30)
            # # # self.remove(graph)
            # # # graph = plane.plot_polar_graph(r, [0, 2 * PI], color=ORANGE)

# # # # Create an instance of the scene to trigger the construct method
# # # scene = PolarGraphExample()
# # # scene.render()

# # # print("Polar graph animation has been rendered and repeated 3 times.")		


















# # # from manim import *
# # # import numpy as np

# # # class PolarGraphExample___saaans_animations(Scene):
    # # # def construct(self):
        # # # plane = PolarPlane()
        # # # r = lambda theta: 2 * np.sin(theta * 5)
        # # # graph = plane.plot_polar_graph(r, [0, 2 * PI], color=ORANGE)
        
        # # # # Animate the construction of the graph with a run_time of 30 seconds
        # # # for _ in range(3):
            # # # self.play(Create(graph), run_time=30)
            # # # self.remove(graph)
            # # # graph = plane.plot_polar_graph(r, [0, 2 * PI], color=ORANGE)

# # # # # # # Create an instance of the scene to trigger the construct method
# # # # # # scene = PolarGraphExample___saaans_animations()
# # # # # # scene.render()

# # # print("Polar graph animation has been rendered and repeated 3 times.")
# # # ###not playing not generating the animations



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PolarGraphExample___saaans_animations
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:18:28] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
# # # [12/28/24 05:18:29] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:18:40] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
###Polar graph animation has been rendered and repeated 3 times.
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PolarGraphExample___saaans_animations
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:16:52] INFO                                                                                                                                                                 scene_file_writer.py:737
				 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

		# # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
				 # # # Played 0 animations
		# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
		# # # INFO                                                                                                                                                                 scene_file_writer.py:737
				 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

		# # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
				 # # # Played 0 animations
		# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
		# # # INFO                                                                                                                                                                 scene_file_writer.py:737
				 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

		# # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
				 # # # Played 0 animations
		# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:16:57] INFO                                                                                                                                                                 scene_file_writer.py:737
				 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

		# # # INFO     Rendered PolarGraphExample                                                                                                                                              scene.py:247
				 # # # Played 0 animations
		# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
# # # [12/28/24 05:17:07] INFO                                                                                                                                                                 scene_file_writer.py:737
				 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

		# # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
				 # # # Played 3 animations
		# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'          
		
		
from manim import *
import numpy as np

class PolarGraphExample___saaans_animations(Scene):
    def construct(self):
        plane = PolarPlane()
        r = lambda theta: 2 * np.sin(theta * 5)
        
        # Create a ValueTracker to update the graph dynamically
        theta_tracker = ValueTracker(0)
        
        # Create the graph with always_redraw
        graph = always_redraw(lambda: plane.plot_polar_graph(
            lambda theta: r(theta + theta_tracker.get_value()), 
            [0, 2 * PI], 
            color=ORANGE
        ))
        
        self.add(plane, graph)
        
        # Animate the construction of the graph with a run_time of 30 seconds
        for _ in range(3):
            self.play(theta_tracker.animate.set_value(2 * PI), run_time=30)
            theta_tracker.set_value(0)  # Reset the tracker for the next iteration

# Create an instance of the scene to trigger the construct method
scene = PolarGraphExample___saaans_animations()
scene.render()

print("Polar graph animation has been rendered and repeated 3 times.")		

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PolarGraphExample___saaans_animations

# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:21:50] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:22:01] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
# # # [12/28/24 05:22:05] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                

from manim import *

class PlotSurfaceExample(ThreeDScene):
    def construct(self):
        resolution_fa = 16
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)
        axes = ThreeDAxes(x_range=(-3, 3, 1), y_range=(-3, 3, 1), z_range=(-5, 5, 1))
        def param_trig(u, v):
            x = u
            y = v
            z = 2 * np.sin(x) + 2 * np.cos(y)
            return z
        trig_plane = axes.plot_surface(
            param_trig,
            resolution=(resolution_fa, resolution_fa),
            u_range = (-3, 3),
            v_range = (-3, 3),
            colorscale = [BLUE, GREEN, YELLOW, ORANGE, RED],
            )
        self.add(axes, trig_plane)
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PlotSurfaceExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:23:29] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:23:41] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
# # # [12/28/24 05:23:42] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PlotSurfaceExample                                                                                                                                             scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'   







from manim import *

class PolarToPointExample(Scene):
    def construct(self):
        polarplane_pi = PolarPlane(azimuth_units="PI radians", size=6)
        polartopoint_vector = Vector(polarplane_pi.polar_to_point(3, PI/4))
        self.add(polarplane_pi)
        self.add(polartopoint_vector)

					
					
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PolarToPointExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:24:23] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
# # # [12/28/24 05:24:24] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:24:26] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarToPointExample                                                                                                                                            scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                       					
					
					


























from manim import *

class NumberPlaneExample(Scene):
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.add(number_plane)			








################################################################################


from manim import *

class NumberPlaneScaled(Scene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-4, 11, 1),
            y_range=(-3, 3, 1),
            x_length=5,
            y_length=2,
        ).move_to(LEFT*3)

        number_plane_scaled_y = NumberPlane(
            x_range=(-4, 11, 1),
            x_length=5,
            y_length=4,
        ).move_to(RIGHT*3)

        self.add(number_plane)
        self.add(number_plane_scaled_y)		
		
		
		
		
################################################################################

from manim import *

class PolarPlaneExample(Scene):
    def construct(self):
        polarplane_pi = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_label_font_size=33.6,
            radius_config={"font_size": 33.6},
        ).add_coordinates()
        self.add(polarplane_pi)
		
					
					
					
# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py PolarPlaneExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:27:23] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:27:26] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO     Writing \tfrac{\pi}{10} to media\Tex\9e1f3d78fd23a5c5.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:27] INFO     Writing \tfrac{\pi}{5} to media\Tex\28d578da1e5b5523.tex                                                                                                     tex_file_writing.py:109
# # # [12/28/24 05:27:28] INFO     Writing \tfrac{3\pi}{10} to media\Tex\b7a44b0b1812b17d.tex                                                                                                   tex_file_writing.py:109
# # # [12/28/24 05:27:29] INFO     Writing \tfrac{2\pi}{5} to media\Tex\2b99fa60a81bbb60.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:30] INFO     Writing \tfrac{\pi}{2} to media\Tex\4f5e61c3e5c4c3cb.tex                                                                                                     tex_file_writing.py:109
# # # [12/28/24 05:27:31] INFO     Writing \tfrac{3\pi}{5} to media\Tex\cf6c31d2a6e985dd.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:32] INFO     Writing \tfrac{7\pi}{10} to media\Tex\c4a483fe957d80d4.tex                                                                                                   tex_file_writing.py:109
# # # [12/28/24 05:27:33] INFO     Writing \tfrac{4\pi}{5} to media\Tex\c3c064b852083212.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:34] INFO     Writing \tfrac{9\pi}{10} to media\Tex\b2c8a39791a3008e.tex                                                                                                   tex_file_writing.py:109
# # # [12/28/24 05:27:35] INFO     Writing \tfrac{11\pi}{10} to media\Tex\c40401e03f0c5885.tex                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:27:36] INFO     Writing \tfrac{6\pi}{5} to media\Tex\6e1634426d3e3bdf.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:37] INFO     Writing \tfrac{13\pi}{10} to media\Tex\071d0f66c7075123.tex                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:27:38] INFO     Writing \tfrac{7\pi}{5} to media\Tex\b95fe29b3ed51849.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:39] INFO     Writing \tfrac{3\pi}{2} to media\Tex\c71e05dd21d7bb9e.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:40] INFO     Writing \tfrac{8\pi}{5} to media\Tex\30b8c3170555072b.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:41] INFO     Writing \tfrac{17\pi}{10} to media\Tex\2d5e630e4e0999fa.tex                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:27:42] INFO     Writing \tfrac{9\pi}{5} to media\Tex\680e87d5ae9ba019.tex                                                                                                    tex_file_writing.py:109
# # # [12/28/24 05:27:43] INFO     Writing \tfrac{19\pi}{10} to media\Tex\dc3ee43adefb9186.tex                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:27:44] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarPlaneExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'    					
					
					









from manim import *

class GetAxisLabelsExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        axes = ThreeDAxes()
        labels = axes.get_axis_labels(
            Text("x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
        )
        self.add(axes, labels)			



# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py GetAxisLabelsExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:28:51] INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
			# # # INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
			# # # INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:29:03] INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
					 # # # Played 3 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
# # # [12/28/24 05:29:04] INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

			# # # INFO     Rendered GetAxisLabelsExample                                                                                                                                           scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                          
			
			
from manim import *

class GetYAxisLabelExample(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes()
        lab = ax.get_y_axis_label(Tex("$y$-label"))
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        self.add(ax, lab)			
		
		
		
		
		
		
		
		
		
		
# # # from manim import *

# # # class GetZAxisLabelExample(ThreeDScene):
    # # # def construct(self):
        # # # ax = ThreeDAxes()
        # # # lab = ax.get_z_axis_label(Tex("$z$-label"))
        # # # self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        # # # self.add(ax, lab)		
		











from manim import *

class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        sin_func_1 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            color=BLUE,
        )

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to([0, 1, 0])

        self.add(cos_func, sin_func_1, sin_func_2)


###########################################################################################################		
		
		
		



















from manim import *

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            color=YELLOW
        )
        self.add(NumberPlane(), graph)		
		
		
##########################################################################################





# # # from manim import *

# # # class ImplicitFunctionExample(Scene):
    # # # def construct(self):
        # # # graph = ImplicitFunction(
            # # # lambda x, y: x * y ** 2 - x ** 2 * y - 2,
            # # # color=YELLOW
        # # # )
        # # # self.add(NumberPlane(), graph)		
		
		
		
		
		
		
		









from manim import *

class PlotParametricFunction(Scene):
    def func(self, t):
        return (np.sin(2 * t), np.sin(3 * t), 0)

    def construct(self):
        func = ParametricFunction(self.func, t_range = (0, TAU), fill_opacity=0).set_color(RED)
        self.add(func.scale(3))		
		
		
		
		
		
		
		
from manim import *

class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: (
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.05
            ), color=RED, t_range = (-3*TAU, 5*TAU, 0.01)
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()
		
		
		
		
		
		
		
		
from manim import *

class DiscontinuousExample(Scene):
    def construct(self):
        ax1 = NumberPlane((-3, 3), (-4, 4))
        ax2 = NumberPlane((-3, 3), (-4, 4))
        VGroup(ax1, ax2).arrange()
        discontinuous_function = lambda x: (x ** 2 - 2) / (x ** 2 - 4)
        incorrect = ax1.plot(discontinuous_function, color=RED)
        correct = ax2.plot(
            discontinuous_function,
            discontinuities=[-2, 2],  # discontinuous points
            dt=0.1,  # left and right tolerance of discontinuity
            color=GREEN,
        )
        self.add(ax1, ax2, incorrect, correct)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class NumberLineExample(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )

        l1 = NumberLine(
            x_range=[-10, 10, 2],
            unit_size=0.5,
            numbers_with_elongated_ticks=[-2, 4],
            include_numbers=True,
            font_size=24,
        )
        num6 = l1.numbers[8]
        num6.set_color(RED)

        l2 = NumberLine(
            x_range=[-2.5, 2.5 + 0.5, 0.5],
            length=12,
            decimal_number_config={"num_decimal_places": 2},
            include_numbers=True,
        )

        l3 = NumberLine(
            x_range=[-5, 5 + 1, 1],
            length=6,
            include_tip=True,
            include_numbers=True,
            rotation=10 * DEGREES,
        )

        line_group = VGroup(l0, l1, l2, l3).arrange(DOWN, buff=1)
        self.add(line_group)


		
		
		
		
		
		
		
		
from manim import *

class BarChartExample(Scene):
    def construct(self):
        chart = BarChart(
            values=[-5, 40, -10, 20, -3],
            bar_names=["one", "two", "three", "four", "five"],
            y_range=[-20, 50, 10],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
        )

        c_bar_lbls = chart.get_bar_labels(font_size=48)

        self.add(chart, c_bar_lbls)		
		
		
		
		
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql scene.py BarChartExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\scene.py:1096: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\D'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1265: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1740: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:1741: SyntaxWarning: invalid escape sequence '\p'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3852: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:3890: SyntaxWarning: invalid escape sequence '\_'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7280: SyntaxWarning: invalid escape sequence '\c'
# # # D:\SANJOY_NATH_MANIMS\scene.py:7307: SyntaxWarning: invalid escape sequence '\c'
# # # [12/28/24 05:36:24] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to graph_data.csv
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered LogScalingExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetGraphLabelExample                                                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Graph data has been written to log_scaling_example_data.csv and get_graph_label_example_data.csv
# # # [12/28/24 05:36:27] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO     Writing one to media\Tex\58646fb5be093e49.tex                                                                                                                tex_file_writing.py:109
# # # [12/28/24 05:36:28] INFO     Writing two to media\Tex\64e766168e53e8bf.tex                                                                                                                tex_file_writing.py:109
# # # [12/28/24 05:36:29] INFO     Writing three to media\Tex\8b44a97c468076a6.tex                                                                                                              tex_file_writing.py:109
# # # [12/28/24 05:36:30] INFO     Writing four to media\Tex\d25f38b574837a83.tex                                                                                                               tex_file_writing.py:109
# # # [12/28/24 05:36:31] INFO     Writing five to media\Tex\5ca2603701d898fc.tex                                                                                                               tex_file_writing.py:109
# # # [12/28/24 05:36:32] INFO     Writing -5 to media\Tex\52850b4a01fd90df.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:36:33] INFO     Writing 40 to media\Tex\5c7ace69089e792f.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:36:34] INFO     Writing -10 to media\Tex\8fb30e4bd9090a75.tex                                                                                                                tex_file_writing.py:109
# # # [12/28/24 05:36:35] INFO     Writing 20 to media\Tex\4170740d5b9b61ee.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:36:36] INFO     Writing -3 to media\Tex\185ba7bf95e9be1e.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:36:37] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered BarChartExample                                                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                                                                  file_ops.py:231


					
					
					
from manim import *

class ChangeBarValuesExample(Scene):
    def construct(self):
        values=[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

        chart = BarChart(
            values,
            y_range=[-10, 10, 2],
            y_axis_config={"font_size": 24},
        )
        self.add(chart)

        chart.change_bar_values(list(reversed(values)))
        self.add(chart.get_bar_labels(font_size=24))					
		
		
		
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO     Writing 10 to media\Tex\ad754aaa15b9b3bb.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:37:28] INFO     Writing 8 to media\Tex\34a8a33d1e13b01c.tex                                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:37:29] INFO     Writing 6 to media\Tex\ae6e376fa474c034.tex                                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:37:30] INFO     Writing 4 to media\Tex\8f968242a63406f8.tex                                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:37:31] INFO     Writing 2 to media\Tex\b540d3d7ffd58d55.tex                                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:37:32] INFO     Writing 0 to media\Tex\cce9f6551ff403b5.tex                                                                                                                  tex_file_writing.py:109
# # # [12/28/24 05:37:33] INFO     Writing -2 to media\Tex\cb90db616f409db7.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:37:34] INFO     Writing -4 to media\Tex\5331077bfcfb4e79.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:37:35] INFO     Writing -6 to media\Tex\5961e63af3b2c01d.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:37:36] INFO     Writing -8 to media\Tex\4fed7dd5f54f536f.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:37:37] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered ChangeBarValuesExample                                                                                                                                         scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\scene\LogScalingExample_ManimCE_v0.18.1.png'                       

					
					
					
					
					
					
					
					
					


















from manim import *

class GetBarLabelsExample(Scene):
    def construct(self):
        chart = BarChart(values=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], y_range=[0, 10, 1])

        c_bar_lbls = chart.get_bar_labels(
            color=WHITE, label_constructor=MathTex, font_size=36
        )

        self.add(chart, c_bar_lbls)					
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ExampleSampleSpace(Scene):
    def construct(self):
        poly1 = SampleSpace(stroke_width=15, fill_opacity=1)
        poly2 = SampleSpace(width=5, height=3, stroke_width=5, fill_opacity=0.5)
        poly3 = SampleSpace(width=2, height=2, stroke_width=5, fill_opacity=0.1)
        poly3.divide_vertically(p_list=np.array([0.37, 0.13, 0.5]), colors=[BLACK, WHITE, GRAY], vect=RIGHT)
        poly_group = VGroup(poly1, poly2, poly3).arrange()
        self.add(poly_group)




from manim import *

class DarkThemeBanner___checking(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))


from manim import *

class LightThemeBanner(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))		
		
		
		
# # # from manim import *

# # # class LightThemeBanner(Scene):
    # # # def construct(self):
        # # # self.camera.background_color = "#ece6e2"
        # # # banner = ManimBanner(dark_theme=False)
        # # # self.play(banner.create())
        # # # self.play(banner.expand())
        # # # self.wait()
        # # # self.play(Unwrite(banner))
		
		
from manim import *

class ExpandDirections(Scene):
    def construct(self):
        banners = [ManimBanner().scale(0.5).shift(UP*x) for x in [-2, 0, 2]]
        self.play(
            banners[0].expand(direction="right"),
            banners[1].expand(direction="center"),
            banners[2].expand(direction="left"),
        )		
		



# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py ExpandDirections
# # # Manim Community v0.18.1

# # # [12/28/24 05:51:56] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 05:51:58] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 05:52:00] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 05:52:02] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
# # # [12/28/24 05:52:03] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\ExpandDirections\1185818338_1170429635_1182687259.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered ExpandDirections                                                                                                                                               scene.py:247
                             # # # Played 1 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'           		
		
		
		
from manim import *

class DecimalMatrixExample(Scene):
    def construct(self):
        m0 = DecimalMatrix(
            [[3.456, 2.122], [33.2244, 12]],
            element_to_mobject_config={"num_decimal_places": 2},
            left_bracket="\{",
            right_bracket="\}")
        self.add(m0)		
		
		
from manim import *

class IntegerMatrixExample(Scene):
    def construct(self):
        m0 = IntegerMatrix(
            [[3.7, 2], [42.2, 12]],
            left_bracket="(",
            right_bracket=")")
        self.add(m0)		
		
		
		
		
		
		
		
from manim import *

class MatrixExamples(Scene):
    def construct(self):
        m0 = Matrix([[2, "\pi"], [-1, 1]])
        m1 = Matrix([[2, 0, 4], [-1, 1, 5]],
            v_buff=1.3,
            h_buff=0.8,
            bracket_h_buff=SMALL_BUFF,
            bracket_v_buff=SMALL_BUFF,
            left_bracket="\{",
            right_bracket="\}")
        m1.add(SurroundingRectangle(m1.get_columns()[1]))
        m2 = Matrix([[2, 1], [-1, 3]],
            element_alignment_corner=UL,
            left_bracket="(",
            right_bracket=")")
        m3 = Matrix([[2, 1], [-1, 3]],
            left_bracket="\\langle",
            right_bracket="\\rangle")
        m4 = Matrix([[2, 1], [-1, 3]],
        ).set_column_colors(RED, GREEN)
        m5 = Matrix([[2, 1], [-1, 3]],
        ).set_row_colors(RED, GREEN)
        g = Group(
            m0,m1,m2,m3,m4,m5
        ).arrange_in_grid(buff=2)
        self.add(g)


# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py MatrixExamples
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # [12/28/24 05:58:38] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 05:58:39] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO     Writing -1 to media\Tex\dc9f1eb78129c30d.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:58:40] INFO     Writing \left\{\begin{array}{c}\quad \\\quad \\\quad \\\end{array}\right. to media\Tex\af2813764f54f716.tex                                                  tex_file_writing.py:109
# # # [12/28/24 05:58:41] INFO     Writing \left.\begin{array}{c}\quad \\\quad \\\quad \\\end{array}\right\} to media\Tex\a5eccd6502858340.tex                                                  tex_file_writing.py:109
# # # [12/28/24 05:58:42] INFO     Writing \left\langle\begin{array}{c}\quad \\\quad \\\end{array}\right. to media\Tex\cb60023661d9187d.tex                                                     tex_file_writing.py:109
# # # [12/28/24 05:58:43] INFO     Writing \left.\begin{array}{c}\quad \\\quad \\\end{array}\right\rangle to media\Tex\91f47a97b9f88eb7.tex                                                     tex_file_writing.py:109
# # # [12/28/24 05:58:45] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

                    # # # INFO     Rendered MatrixExamples                                                                                                                                                 scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'            
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class BackgroundRectanglesExample(Scene):
    def construct(self):
        background= Rectangle().scale(3.2)
        background.set_fill(opacity=.5)
        background.set_color([TEAL, RED, YELLOW])
        self.add(background)
        m0 = Matrix([[12, -30], [-1, 15]],
            add_background_rectangles_to_entries=True)
        m1 = Matrix([[2, 0], [-1, 1]],
            include_background_rectangle=True)
        m2 = Matrix([[12, -30], [-1, 15]])
        g = Group(m0, m1, m2).arrange(buff=2)
        self.add(g)		
		
		
		
		
		
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py BackgroundRectanglesExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # [12/28/24 05:59:25] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 05:59:26] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO     Writing -30 to media\Tex\82a2df5ef5032603.tex                                                                                                                tex_file_writing.py:109
# # # [12/28/24 05:59:28] INFO     Writing 15 to media\Tex\af84e529e412689b.tex                                                                                                                 tex_file_writing.py:109
# # # [12/28/24 05:59:29] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

                    # # # INFO     Rendered BackgroundRectanglesExample                                                                                                                                    scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'                     		
					
					
from manim import *

class GetBracketsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 3], [1, 5]])
        bra = m0.get_brackets()
        colors = [BLUE, GREEN]
        for k in range(len(colors)):
            bra[k].set_color(colors[k])
        self.add(m0)					
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py GetBracketsExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # [12/28/24 06:00:06] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:00:07] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

                    # # # INFO     Rendered GetBracketsExample                                                                                                                                             scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'         		
					
					
from manim import *

class GetColumnsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_columns()[1]))
        self.add(m0)					
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py GetColumnsExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # [12/28/24 06:00:42] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
                    # # # INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:00:43] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

                    # # # INFO     Rendered GetColumnsExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'          		
					
					
from manim import *

class GetEntriesExample(Scene):
    def construct(self):
        m0 = Matrix([[2, 3], [1, 5]])
        ent = m0.get_entries()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            ent[k].set_color(colors[k])
        self.add(m0)					
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py GetEntriesExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # [12/28/24 06:01:17] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:01:18] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
# # # [12/28/24 06:01:19] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

                    # # # INFO     Rendered GetEntriesExample                                                                                                                                              scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'                                                  file_ops.py:231
		
		
		
from manim import *

class GetRowsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 3], [1, 5]])
        m0.add(SurroundingRectangle(m0.get_rows()[1]))
        self.add(m0)		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py GetRowsExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2580: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # [12/28/24 06:01:55] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:01:57] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:02:00] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:02:02] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
# # # [12/28/24 06:02:03] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

                    # # # INFO     Rendered GetRowsExample                                                                                                                                                 scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'                                                  file_ops.py:231



					
					
					
from manim import *

class SetColumnColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 1], [-1, 3]],
        ).set_column_colors([RED,BLUE], GREEN)
        self.add(m0)					
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py SetColumnColorsExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2580: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2631: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # [12/28/24 06:02:46] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:02:48] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:02:50] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:02:53] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
# # # [12/28/24 06:02:54] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

                    # # # INFO     Rendered SetColumnColorsExample                                                                                                                                         scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png' 		
					












					
					
					
					
					
					
					
					
					
					
					
					

from manim import *

class SetRowColorsExample(Scene):
    def construct(self):
        m0 = Matrix([["\pi", 1], [-1, 3]],
        ).set_row_colors([RED,BLUE], GREEN)
        self.add(m0)


# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py SetRowColorsExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2580: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2631: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2707: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # [12/28/24 06:03:36] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:03:37] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:03:40] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:03:41] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
# # # [12/28/24 06:03:42] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

                    # # # INFO     Rendered SetRowColorsExample                                                                                                                                            scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'  		
					
					
					
from manim import *

class MobjectMatrixExample(Scene):
    def construct(self):
        a = Circle().scale(0.3)
        b = Square().scale(0.3)
        c = MathTex("\pi").scale(2)
        d = Star().scale(0.3)
        m0 = MobjectMatrix([[a, b], [c, d]])
        self.add(m0)	


		
		
		
		
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py MobjectMatrixExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
# # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
# # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
# # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
# # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
# # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
# # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
# # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2580: SyntaxWarning: invalid escape sequence '\p'
# # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2631: SyntaxWarning: invalid escape sequence '\p'
# # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2707: SyntaxWarning: invalid escape sequence '\p'
# # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2761: SyntaxWarning: invalid escape sequence '\p'
# # # c = MathTex("\pi").scale(2)
# # # [12/28/24 06:10:03] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:10:05] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:10:07] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:10:09] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
			# # # INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

			# # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
					 # # # Played 3 animations
# # # [12/28/24 06:10:10] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
			# # # INFO     Writing \left[\begin{array}{c}\quad \\\quad \\\quad \\\end{array}\right. to media\Tex\7d6eba804384191e.tex                                                   tex_file_writing.py:109
# # # [12/28/24 06:10:11] INFO     Writing \left.\begin{array}{c}\quad \\\quad \\\quad \\\end{array}\right] to media\Tex\f030fc9122fc6297.tex                                                   tex_file_writing.py:109
# # # [12/28/24 06:10:12] INFO                                                                                                                                                                 scene_file_writer.py:737
					 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'

			# # # INFO     Rendered MobjectMatrixExample                                                                                                                                           scene.py:247
					 # # # Played 0 animations
			# # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4.png'
			
					
					
					
					
from manim import *

class NextToUpdater(Scene):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))					
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py NextToUpdater
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2580: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2631: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2707: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2761: SyntaxWarning: invalid escape sequence '\p'
  # # # c = MathTex("\pi").scale(2)
# # # [12/28/24 06:11:37] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:11:39] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:11:41] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:11:43] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
# # # [12/28/24 06:11:44] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\NextToUpdater\1185818338_4020547453_4120939142.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered NextToUpdater                                                                                                                                                  scene.py:247
                             # # # Played 1 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                          		
					
					
				








from manim import *

class DtUpdater(Scene):
    def construct(self):
        square = Square()

        #Let the square rotate 90° per second
        square.add_updater(lambda mobject, dt: mobject.rotate(dt*90*DEGREES))
        self.add(square)
        self.wait(2)				
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py DtUpdater
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2580: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2631: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2707: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2761: SyntaxWarning: invalid escape sequence '\p'
  # # # c = MathTex("\pi").scale(2)
# # # [12/28/24 06:12:33] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:12:35] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:12:37] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:12:39] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
# # # [12/28/24 06:12:40] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\DtUpdater\1185818338_804019694_2333982699.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered DtUpdater                                                                                                                                                      scene.py:247
                             # # # Played 1 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                  		
					
					
from manim import *

class AnimateExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT))
        self.play(s.animate.scale(2))
        self.play(s.animate.rotate(PI / 2))
        self.play(Uncreate(s))					
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py AnimateExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2580: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2631: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2707: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2761: SyntaxWarning: invalid escape sequence '\p'
  # # # c = MathTex("\pi").scale(2)
# # # [12/28/24 06:13:22] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:13:24] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:13:26] INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
# # # [12/28/24 06:13:28] INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
# # # [12/28/24 06:13:29] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\AnimateExample\1185818338_1280228252_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\AnimateExample\624642324_3152466158_3256495558.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\AnimateExample\624642324_1441566062_3256495558.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\AnimateExample\624642324_631309943_3256495558.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\AnimateExample\624642324_3138189854_3256495558.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered AnimateExample                                                                                                                                                 scene.py:247
                             # # # Played 5 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                         		
					
					
from manim import *

class AnimateChainExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))
        self.play(Uncreate(s))					
		
		
from manim import *

class AnimateWithArgsExample(Scene):
    def construct(self):
        s = Square()
        c = Circle()

        VGroup(s, c).arrange(RIGHT, buff=2)
        self.add(s, c)

        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=there_and_back).shift(RIGHT),
        )		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql gggggg.py AnimateWithArgsExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2269: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2270: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2294: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([[2, "\pi"], [-1, 1]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2300: SyntaxWarning: invalid escape sequence '\{'
  # # # left_bracket="\{",
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2301: SyntaxWarning: invalid escape sequence '\}'
  # # # right_bracket="\}")
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2437: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2486: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2580: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 3], [1, 5]])
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2631: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2707: SyntaxWarning: invalid escape sequence '\p'
  # # # m0 = Matrix([["\pi", 1], [-1, 3]],
# # # D:\SANJOY_NATH_MANIMS\gggggg.py:2761: SyntaxWarning: invalid escape sequence '\p'
  # # # c = MathTex("\pi").scale(2)
# # # [12/28/24 06:32:55] INFO     Animation 0 : Using cached data (hash : 1185818338_4036054547_3035330945)                                                                                       cairo_renderer.py:88
# # # [12/28/24 06:32:56] INFO     Animation 1 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
                    # # # INFO     Animation 2 : Using cached data (hash : 624642324_4036054547_1365402269)                                                                                        cairo_renderer.py:88
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered PolarGraphExample___saaans_animations                                                                                                                          scene.py:247
                             # # # Played 3 animations
# # # [12/28/24 06:32:57] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'                                                      file_ops.py:231
# # # Polar graph animation has been rendered and repeated 3 times.
                    # # # INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\partial_movie_files\AnimateWithArgsExample\1185818338_1570067628_547105815.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'

                    # # # INFO     Rendered AnimateWithArgsExample                                                                                                                                         scene.py:247
                             # # # Played 1 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\gggggg\480p15\PolarGraphExample___saaans_animations.mp4'    		
					
					
from manim import *

class ApplyFuncExample___important(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.exp(x*1j)
        )
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.exp(x+t.get_value()*1j)
            )).set_color(BLUE)
        )
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        self.play(t.animate.set_value(TAU), run_time=3)					
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class Example___severalsquares_alikrrgned(Scene):
    def construct(self):
        s1 = Square()
        s2 = Square()
        s3 = Square()
        s4 = Square()
        x = VGroup(s1, s2, s3, s4).set_x(0).arrange(buff=1.0)
        self.add(x)		
		
		
		
		
		
		
from manim import *

class ExampleBoxes___arrayofsquares(Scene):
    def construct(self):
        boxes=VGroup(*[Square() for s in range(0,6)])
        boxes.arrange_in_grid(rows=2, buff=0.1)
        self.add(boxes)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ArrangeInGrid___Tooimportantgrids___BOQ_representations(Scene):
    def construct(self):
        boxes = VGroup(*[
            Rectangle(WHITE, 0.5, 0.5).add(Text(str(i+1)).scale(0.5))
            for i in range(24)
        ])
        self.add(boxes)

        boxes.arrange_in_grid(
            buff=(0.25,0.5),
            col_alignments="lccccr",
            row_alignments="uccd",
            col_widths=[1, *[None]*4, 1],
            row_heights=[1, None, None, 1],
            flow_order="dr"
        )		
		
		
		
		
		



from manim import *

class ArrangeSumobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT*np.random.uniform(-1,1)+UP*np.random.uniform(-1,1)) for i in range(0,15)])
        s.shift(UP).set_color(BLUE)
        s2= s.copy().set_color(RED)
        s2.arrange_submobjects()
        s2.shift(DOWN)
        self.add(s,s2)		
		
		
		
		
		
		
from manim import *

class BecomeScene__circssquares(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        circ.become(square)
        self.wait(0.5)		
		
		
from manim import *

class FlipExample(Scene):
    def construct(self):
        s= Line(LEFT, RIGHT+UP).shift(4*LEFT)
        self.add(s)
        s2= s.copy().flip()
        self.add(s2)		
		
		
		
		
from manim import *

class AngleMidPoint(Scene):
    def construct(self):
        line1 = Line(ORIGIN, 2*RIGHT)
        line2 = Line(ORIGIN, 2*RIGHT).rotate_about_origin(80*DEGREES)

        a = Angle(line1, line2, radius=1.5, other_angle=False)
        d = Dot(a.get_midpoint()).set_color(RED)

        self.add(line1, line2, a, d)
        self.wait()		
		
		
		
		
		
		
from manim import *

class HeightExample___rect_copy_enlargings___tooimportanttoimplement(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()		
		
		
		
	



	
from manim import *

class DotInterpolation(Scene):
    def construct(self):
        dotR = Dot(color=DARK_GREY)
        dotR.shift(2 * RIGHT)
        dotL = Dot(color=WHITE)
        dotL.shift(2 * LEFT)

        dotMiddle = VMobject().interpolate(dotL, dotR, alpha=0.3)

        self.add(dotL, dotR, dotMiddle)		
		
		
		
		
		
from manim import *

class InvertSumobjectsExample___Tooimportanttrailingpaths(Scene):
    def construct(self):
        s = VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2 = s.copy()
        s2.invert()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))		
		
		
		
from manim import *

class MatchPointsScene___circ_animate_match_points_operations___square(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        self.play(circ.animate.match_points(square))
        self.wait(0.5)		
		
		
		
		
		
from manim import *

class GeometricShapes(Scene):
    def construct(self):
        d = Dot()
        c = Circle()
        s = Square()
        t = Triangle()
        d.next_to(c, RIGHT)
        s.next_to(c, LEFT)
        t.next_to(c, DOWN)
        self.add(d, c, s, t)

from manim import *

class MobjectScaleExample___Differentsizesoftexts(Scene):
    def construct(self):
        f1 = Text("F")
        f2 = Text("F").scale(2)
        f3 = Text("F").scale(0.5)
        f4 = Text("F").scale(-1)

        vgroup = VGroup(f1, f2, f3, f4).arrange(6 * RIGHT)
        self.add(vgroup)		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

config.background_color = WHITE

class ChangedDefaultTextcolor(Scene):
    def construct(self):
        Text.set_default(color=BLACK)
        self.add(Text("Changing default values is easy!"))

        # we revert the colour back to the default to prevent a bug in the docs.
        Text.set_default(color=WHITE)		
		
		
		
		
		
		
		
		
		












from manim import *

class SetZIndex(Scene):
    def construct(self):
        text = Text('z_index = 3', color = PURE_RED).shift(UP).set_z_index(3)
        square = Square(2, fill_opacity=1).set_z_index(2)
        tex = Tex(r'zIndex = 1', color = PURE_BLUE).shift(DOWN).set_z_index(1)
        circle = Circle(radius = 1.7, color = GREEN, fill_opacity = 1) # z_index = 0

        # Displaying order is now defined by z_index values
        self.add(text)
        self.add(square)
        self.add(tex)
        self.add(circle)		
		
		
		
		
		
		
		






from manim import *

class ShuffleSubmobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2= s.copy()
        s2.shuffle_submobjects()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))		
		
		
		
		
		
		
		
from manim import *

class ToCornerExample(Scene):
    def construct(self):
        c = Circle()
        c.to_corner(UR)
        t = Tex("To the corner!")
        t2 = MathTex("x^3").shift(DOWN)
        self.add(c,t,t2)
        t.to_corner(DL, buff=0)
        t2.to_corner(UL, buff=1.5)		
		
		
		
		
		
		
		
from manim import *

class ToEdgeExample(Scene):
    def construct(self):
        tex_top = Tex("I am at the top!")
        tex_top.to_edge(UP)
        tex_side = Tex("I am moving to the side!")
        c = Circle().shift(2*DOWN)
        self.add(tex_top, tex_side)
        tex_side.to_edge(LEFT)
        c.to_edge(RIGHT, buff=0)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class WidthExample___growingcopyofrects(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class svg___ArcBraceExample(Scene):
    def construct(self):
        arc_1 = Arc(radius=1.5,start_angle=0,angle=2*PI/3).set_color(RED)
        brace_1 = ArcBrace(arc_1,LEFT)
        group_1 = VGroup(arc_1,brace_1)

        arc_2 = Arc(radius=3,start_angle=0,angle=5*PI/6).set_color(YELLOW)
        brace_2 = ArcBrace(arc_2)
        group_2 = VGroup(arc_2,brace_2)

        arc_3 = Arc(radius=0.5,start_angle=-0,angle=PI).set_color(BLUE)
        brace_3 = ArcBrace(arc_3)
        group_3 = VGroup(arc_3,brace_3)

        arc_4 = Arc(radius=0.2,start_angle=0,angle=3*PI/2).set_color(GREEN)
        brace_4 = ArcBrace(arc_4)
        group_4 = VGroup(arc_4,brace_4)

        arc_group = VGroup(group_1, group_2, group_3, group_4).arrange_in_grid(buff=1.5)
        self.add(arc_group.center())		
		
		
		
		
		
		
from manim import *

class svg___BraceExample(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        for i in np.linspace(0.1,1.0,4):
            br = Brace(s, sharpness=i)
            t = Text(f"sharpness= {i}").next_to(br, RIGHT)
            self.add(t)
            self.add(br)
        VGroup(*self.mobjects).arrange(DOWN, buff=0.2)		
		
		
		
		
		
from manim import *

class svg_animated_grids_constructions___BraceBPExample(Scene):
    def construct(self):
        p1 = [0,0,0]
        p2 = [1,2,0]
        brace = BraceBetweenPoints(p1,p2)
        self.play(Create(NumberPlane()))
        self.play(Create(brace))
        self.wait(2)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class DecimalTableExample___BOQ(Scene):
    def construct(self):
        x_vals = [-2,-1,0,1,2]
        y_vals = np.exp(x_vals)
        t0 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x"), MathTex("f(x)=e^{x}")],
            h_buff=1,
            element_to_mobject_config={"num_decimal_places": 2})
        self.add(t0)		
		
		
		
		
from manim import *

class IntegerTableExample___BOQ(Scene):
    def construct(self):
        t0 = IntegerTable(
            [[0,30,45,60,90],
            [90,60,45,30,0]],
            col_labels=[
                MathTex("\\frac{\sqrt{0}}{2}"),
                MathTex("\\frac{\sqrt{1}}{2}"),
                MathTex("\\frac{\sqrt{2}}{2}"),
                MathTex("\\frac{\sqrt{3}}{2}"),
                MathTex("\\frac{\sqrt{4}}{2}")],
            row_labels=[MathTex("\sin"), MathTex("\cos")],
            h_buff=1,
            element_to_mobject_config={"unit": "^{\circ}"})
        self.add(t0)		
		
		
		
		
from manim import *

class MathTableExample___Tooimportant_Grouptheory(Scene):
    def construct(self):
        t0 = MathTable(
            [["+", 0, 5, 10],
            [0, 0, 5, 10],
            [2, 2, 7, 12],
            [4, 4, 9, 14]],
            include_outer_lines=True)
        self.add(t0)		