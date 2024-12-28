	
		
		
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
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py DecimalTableExample___BOQ
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 06:59:00] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\DecimalTableExample___BOQ_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered DecimalTableExample___BOQ                                                                                                                                      scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\DecimalTableExample___BOQ_ManimCE_v0.18.1.png'                                                         file_ops.py:231

# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py MathTableExample___Tooimportant_Grouptheory
# # # Manim Community v0.18.1

# # # [12/28/24 06:59:21] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\MathTableExample___Tooimportant_Grouptheory_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered MathTableExample___Tooimportant_Grouptheory                                                                                                                    scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\MathTableExample___Tooimportant_Grouptheory_ManimCE_v0.18.1.png'                                 		
		
		
		
from manim import *

class MobjectTableExample___tiktaktoes(Scene):
    def construct(self):
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT),
        )
        a = Circle().set_color(RED).scale(0.5)
        b = cross.set_color(BLUE).scale(0.5)
        t0 = MobjectTable(
            [[a.copy(),b.copy(),a.copy()],
            [b.copy(),a.copy(),a.copy()],
            [a.copy(),b.copy(),b.copy()]]
        )
        line = Line(
            t0.get_corner(DL), t0.get_corner(UR)
        ).set_color(RED)
        self.add(t0, line)		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py MobjectTableExample___tiktaktoes
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:00:27] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\MobjectTableExample___tiktaktoes_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered MobjectTableExample___tiktaktoes                                                                                                                               scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\MobjectTableExample___tiktaktoes_ManimCE_v0.18.1.png'      		
					
					
					
					
					
					
from manim import *

class TableExamples___severalkindsoftables(Scene):
    def construct(self):
        t0 = Table(
            [["This", "is a"],
            ["simple", "Table in \n Manim."]])
        t1 = Table(
            [["This", "is a"],
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        t1.add_highlighted_cell((2,2), color=YELLOW)
        t2 = Table(
            [["This", "is a"],
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": RIGHT})
        t2.add(t2.get_cell((2,2), color=RED))
        t3 = Table(
            [["This", "is a"],
            ["simple", "Table."]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Star().scale(0.3),
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": YELLOW})
        t3.remove(*t3.get_vertical_lines())
        g = Group(
            t0,t1,t2,t3
        ).scale(0.7).arrange_in_grid(buff=1)
        self.add(g)					
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py TableExamples___severalkindsoftables
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:01:38] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\TableExamples___severalkindsoftables_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered TableExamples___severalkindsoftables                                                                                                                           scene.py:247
                             # # # Played 0 animations
# # # [12/28/24 07:01:39] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\TableExamples___severalkindsoftables_ManimCE_v0.18.1.png'          		







from manim import *

class BackgroundRectanglesExample___coloured_styles_backgrnds(Scene):
    def construct(self):
        background = Rectangle(height=6.5, width=13)
        background.set_fill(opacity=.5)
        background.set_color([TEAL, RED, YELLOW])
        self.add(background)
        t0 = Table(
            [["This", "is a"],
            ["simple", "Table."]],
            add_background_rectangles_to_entries=True)
        t1 = Table(
            [["This", "is a"],
            ["simple", "Table."]],
            include_background_rectangle=True)
        g = Group(t0, t1).scale(0.7).arrange(buff=0.5)
        self.add(g)
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py BackgroundRectanglesExample___coloured_styles_backgrnds
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:02:36] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\BackgroundRectanglesExample___coloured_styles_backgrnds_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered BackgroundRectanglesExample___coloured_styles_backgrnds                                                                                                        scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\BackgroundRectanglesExample___coloured_styles_backgrnds_ManimCE_v0.18.1.png'    		
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					


























					
from manim import *

class AddHighlightedCellExample___Highlightedcells(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.add_highlighted_cell((2,2), color=GREEN)
        self.add(table)					
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py AddHighlightedCellExample___Highlightedcells
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:03:37] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\AddHighlightedCellExample___Highlightedcells_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered AddHighlightedCellExample___Highlightedcells                                                                                                                   scene.py:247
                             # # # Played 0 animations
# # # [12/28/24 07:03:38] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\AddHighlightedCellExample___Highlightedcells_ManimCE_v0.18.1.png'               		





from manim import *

class CreateTableExample___Animated_table_cell_data_filling___BOQ_filling(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            include_outer_lines=True)
        self.play(table.create())
        self.wait()
		
		
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py CreateTableExample___Animated_table_cell_data_filling___BOQ_filling
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:04:36] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\CreateTableExample___Animated_table_cell_data_filling___BOQ_filling\1185818338_343392
                             # # # 0347_2358810818.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\CreateTableExample___Animated_table_cell_data_filling___BOQ_filling\624642324_1704852
                             # # # 926_3790722832.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\CreateTableExample___Animated_table_cell_data_filling___BOQ_filling.mp4'

                    # # # INFO     Rendered CreateTableExample___Animated_table_cell_data_filling___BOQ_filling                                                                                            scene.py:247
                             # # # Played 2 animations
# # # [12/28/24 07:04:37] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\CreateTableExample___Animated_table_cell_data_filling___BOQ_filling.mp4'                        file_ops.py:231		







from manim import *

class GetCellExample___particularcellsbordershighlight(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        cell = table.get_cell((2,2), color=RED)
        self.add(table, cell)
		
		
		
		











		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py GetCellExample___particularcellsbordershighlight
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:05:32] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\GetCellExample___particularcellsbordershighlight_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetCellExample___particularcellsbordershighlight                                                                                                               scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\GetCellExample___particularcellsbordershighlight_ManimCE_v0.18.1.png'          		
					
					
					
					
					
		






























from manim import *

class GetColLabelsExample___highlightingcells(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        lab = table.get_col_labels()
        for item in lab:
            item.set_color(random_bright_color())
        self.add(table)		
		
		
		



# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py GetColLabelsExample___highlightingcells
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:06:44] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\GetColLabelsExample___highlightingcells_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetColLabelsExample___highlightingcells                                                                                                                        scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\GetColLabelsExample___highlightingcells_ManimCE_v0.18.1.png'     		
					
					
					
from manim import *

class GetColumnsExample__to_draw_special_bordering_for_columns_operations_highlights(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.add(SurroundingRectangle(table.get_columns()[1]))
        self.add(table)					
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py GetColumnsExample__to_draw_special_bordering_for_columns_operations_highlights
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:07:58] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at
                             # # # 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\GetColumnsExample__to_draw_special_bordering_for_columns_operations_highlights_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetColumnsExample__to_draw_special_bordering_for_columns_operations_highlights                                                                                 scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\GetColumnsExample__to_draw_special_bordering_for_columns_operations_highlights_ManimCE_v0.18.1.png'    file_ops.py:231	
		
		
		
		
		
from manim import *

class GetEntriesExample__tables_cells_texts_images_swappng(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        ent = table.get_entries()
        for item in ent:
            item.set_color(random_bright_color())
        table.get_entries((2,2)).rotate(PI)
        self.add(table)		
		
		
		
		
		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py GetEntriesExample__tables_cells_texts_images_swappng
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:09:16] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\GetEntriesExample__tables_cells_texts_images_swappng_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered GetEntriesExample__tables_cells_texts_images_swappng                                                                                                           scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\GetEntriesExample__tables_cells_texts_images_swappng_ManimCE_v0.18.1.png'                              file_ops.py:231		
					
					
					
					
from manim import *

class GetEntriesWithoutLabelsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        ent = table.get_entries_without_labels()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            ent[k].set_color(colors[k])
        table.get_entries_without_labels((2,2)).rotate(PI)
        self.add(table)
					
					
					
					
					
					
from manim import *

class GetHighlightedCellExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        highlight = table.get_highlighted_cell((2,2), color=GREEN)
        table.add_to_back(highlight)
        self.add(table)					
					
					
					
					
					
					
					
					
					
					
					
					
					


















from manim import *

class GetHorizontalLinesExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.get_horizontal_lines().set_color(RED)
        self.add(table)					
		
		
		
		
		
		
from manim import *

class GetLabelsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        lab = table.get_labels()
        colors = [BLUE, GREEN, YELLOW, RED]
        for k in range(len(colors)):
            lab[k].set_color(colors[k])
        self.add(table)		
		
		
		
		
		
		
		
		
		
		
from manim import *

class GetRowLabelsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        lab = table.get_row_labels()
        for item in lab:
            item.set_color(random_bright_color())
        self.add(table)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class GetRowsExample___rowsoperations_highlighting(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.add(SurroundingRectangle(table.get_rows()[1]))
        self.add(table)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class GetVerticalLinesExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")])
        table.get_vertical_lines()[0].set_color(RED)
        self.add(table)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class MobjectScaleExample(Scene):
    def construct(self):
        f1 = Text("F")
        f2 = Text("F").scale(2)
        f3 = Text("F").scale(0.5)
        f4 = Text("F").scale(-1)

        vgroup = VGroup(f1, f2, f3, f4).arrange(6 * RIGHT)
        self.add(vgroup)		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class SetColumnColorsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")]
        ).set_column_colors([RED,BLUE], GREEN)
        self.add(table)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class SetRowColorsExample(Scene):
    def construct(self):
        table = Table(
            [["First", "Second"],
            ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")]
        ).set_row_colors([RED,BLUE], GREEN)
        self.add(table)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class CodeFromString___tooimportanttotrainprogramming(Scene):
    def construct(self):
        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.add(rendered_code)		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		









		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py CodeFromString___tooimportanttotrainprogramming
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:15:59] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\CodeFromString___tooimportanttotrainprogramming_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered CodeFromString___tooimportanttotrainprogramming                                                                                                                scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\CodeFromString___tooimportanttotrainprogramming_ManimCE_v0.18.1.png'      		
					
					
					
					
					
					
					
					
					



from manim import *

class MovingSquareWithUpdaters__Toohelpfulforphysicsbuoncyexamples(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
            unit=r"     ext{M-Units}",
            unit_buff_per_font_unit=0.003
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.animate.to_edge(DOWN),
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()					
		
		
		
		

# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py MovingSquareWithUpdaters
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:17:07] INFO     Writing \dots to media\Tex\af51b130ee8d0a92.tex                                                                                                              tex_file_writing.py:109
# # # [12/28/24 07:17:08] INFO     Writing ext{M-Units} to media\Tex\bc816beff404271b.tex                                                                                                       tex_file_writing.py:109
# # # [12/28/24 07:17:11] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\MovingSquareWithUpdaters\1185818338_1190331940_1387507159.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\MovingSquareWithUpdaters\624642324_1704852926_1595739352.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\MovingSquareWithUpdaters.mp4'

                    # # # INFO     Rendered MovingSquareWithUpdaters                                                                                                                                       scene.py:247
                             # # # Played 2 animations
# # # [12/28/24 07:17:12] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\MovingSquareWithUpdaters.mp4'                                       		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class IntegerExample(Scene):
    def construct(self):
        self.add(Integer(number=2.5).set_color(ORANGE).scale(2.5).set_x(-0.5).set_y(0.8))
        self.add(Integer(number=3.14159, show_ellipsis=True).set_x(3).set_y(3.3).scale(3.14159))
        self.add(Integer(number=42).set_x(2.5).set_y(-2.3).set_color_by_gradient(BLUE, TEAL).scale(1.7))
        self.add(Integer(number=6.28).set_x(-1.5).set_y(-2).set_color(YELLOW).scale(1.4))		
		
		
		
		
from manim import *

class VariablesWithValueTracker______tooimportantforsimulationsvalueupdations(Scene):
    def construct(self):
        var = 0.5
        on_screen_var = Variable(var, Text("var"), num_decimal_places=3)

        # You can also change the colours for the label and value
        on_screen_var.label.set_color(RED)
        on_screen_var.value.set_color(GREEN)

        self.play(Write(on_screen_var))
        # The above line will just display the variable with
        # its initial value on the screen. If you also wish to
        # update it, you can do so by accessing the `tracker` attribute
        self.wait()
        var_tracker = on_screen_var.tracker
        var = 10.5
        self.play(var_tracker.animate.set_value(var))
        self.wait()

        int_var = 0
        on_screen_int_var = Variable(
            int_var, Text("int_var"), var_type=Integer
        ).next_to(on_screen_var, DOWN)
        on_screen_int_var.label.set_color(RED)
        on_screen_int_var.value.set_color(GREEN)

        self.play(Write(on_screen_int_var))
        self.wait()
        var_tracker = on_screen_int_var.tracker
        var = 10.5
        self.play(var_tracker.animate.set_value(var))
        self.wait()

        # If you wish to have a somewhat more complicated label for your
        # variable with subscripts, superscripts, etc. the default class
        # for the label is MathTex
        subscript_label_var = 10
        on_screen_subscript_var = Variable(subscript_label_var, "{a}_{i}").next_to(
            on_screen_int_var, DOWN
        )
        self.play(Write(on_screen_subscript_var))
        self.wait()		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py VariablesWithValueTracker______tooimportantforsimulationsvalueupdations
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:19:55] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\1185818338_12
                             # # # 04485817_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_170
                             # # # 4852926_2945389657.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_690
                             # # # 284878_1355858601.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_170
                             # # # 4852926_2971580867.mp4'
# # # [12/28/24 07:19:56] INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_411
                             # # # 8168068_3323199143.mp4'
                    # # # INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_170
                             # # # 4852926_730675800.mp4'
                    # # # INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_338
                             # # # 8671798_187495387.mp4'
                    # # # INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_170
                             # # # 4852926_598948214.mp4'
                    # # # INFO     Writing {a}_{i} to media\Tex\88a481301d71c497.tex                                                                                                            tex_file_writing.py:109
# # # [12/28/24 07:19:58] INFO     Animation 8 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_127
                             # # # 1190984_3579423265.mp4'
                    # # # INFO     Animation 9 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations\624642324_170
                             # # # 4852926_2556308943.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations.mp4'

                    # # # INFO     Rendered VariablesWithValueTracker______tooimportantforsimulationsvalueupdations                                                                                        scene.py:247
                             # # # Played 10 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\VariablesWithValueTracker______tooimportantforsimulationsvalueupdations.mp4'                    file_ops.py:231
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class VariableExample___tooimportanttodemonstratehowthevaluesofsimulationschanging(Scene):
    def construct(self):
        start = 2.0

        x_var = Variable(start, 'x', num_decimal_places=3)
        sqr_var = Variable(start**2, 'x^2', num_decimal_places=3)
        Group(x_var, sqr_var).arrange(DOWN)

        sqr_var.add_updater(lambda v: v.tracker.set_value(x_var.tracker.get_value()**2))

        self.add(x_var, sqr_var)
        self.play(x_var.tracker.animate.set_value(5), run_time=2, rate_func=linear)
        self.wait(0.1)		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py VariableExample___tooimportanttodemonstratehowthevaluesofsimulationschanging
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:21:18] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariableExample___tooimportanttodemonstratehowthevaluesofsimulationschanging\11858183
                             # # # 38_3253942488_3228943131.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\VariableExample___tooimportanttodemonstratehowthevaluesofsimulationschanging\62464232
                             # # # 4_2862073587_3027610176.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\VariableExample___tooimportanttodemonstratehowthevaluesofsimulationschanging.mp4'

                    # # # INFO     Rendered VariableExample___tooimportanttodemonstratehowthevaluesofsimulationschanging                                                                                   scene.py:247
                             # # # Played 2 animations
# # # [12/28/24 07:21:19] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\VariableExample___tooimportanttodemonstratehowthevaluesofsimulationschanging.mp4'               file_ops.py:231
		
		
		
		
from manim import *

class BulletedListExample___tex(Scene):
    def construct(self):
        blist = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
        blist.set_color_by_tex("Item 1", RED)
        blist.set_color_by_tex("Item 2", GREEN)
        blist.set_color_by_tex("Item 3", BLUE)
        self.add(blist)		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class Formula___withlatex_integrals(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        self.add(t)		
		
		
		
		
		
		
		
from manim import *

import manim

class TitleExample___Goodstylesforpresentations(Scene):
    def construct(self):
        banner = ManimBanner()
        title = Title(f"Manim version {manim.__version__}")
        self.add(banner, title)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class MarkupExample___colouredtexts(Scene):
    def construct(self):
        text = MarkupText('<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"')
        self.add(text)		
		
		
		
from manim import *

class MarkupElaborateExample___arabs___notrendering(Scene):
    def construct(self):
        text = MarkupText(
            '<span foreground="purple">ا</span><span foreground="red">َ</span>'
            'ل<span foreground="blue">ْ</span>ع<span foreground="red">َ</span>ر'
            '<span foreground="red">َ</span>ب<span foreground="red">ِ</span>ي'
            '<span foreground="green">ّ</span><span foreground="red">َ</span>ة'
            '<span foreground="blue">ُ</span>'
        )
        self.add(text)		
		
		
		
		
		
		
		
from manim import *

class BasicMarkupExample___yessssss_we_can_use_thisstyles(Scene):
    def construct(self):
        text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
        text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text4 = MarkupText("type <tt>help</tt> for help")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)		
		
		
from manim import *

class ColorExample___englishtextssizescolors(Scene):
    def construct(self):
        text1 = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        text2 = MarkupText("nice gradient", gradient=(BLUE, GREEN))
        text3 = MarkupText(
            'nice <gradient from="RED" to="YELLOW">intermediate</gradient> gradient',
            gradient=(BLUE, GREEN),
        )
        text4 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW">causing trouble</gradient> here'
        )
        text5 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">defeated</gradient> with offset'
        )
        text6 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">floating</gradient> inside'
        )
        text7 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1,1">floating</gradient> inside'
        )
        group = VGroup(text1, text2, text3, text4, text5, text6, text7).arrange(DOWN)
        self.add(group)		
		
		
		
		
		
		
		
		
		
from manim import *

class UnderlineExample___yesssssswecanusethis(Scene):
    def construct(self):
        text1 = MarkupText(
            '<span underline="double" underline_color="green">bla</span>'
        )
        text2 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text3 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-1">aabb</gradient>y'
        )
        text4 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text5 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-2">aabb</gradient>y'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)		
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py UnderlineExample
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:27:27] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\UnderlineExample_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered UnderlineExample                                                                                                                                               scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\UnderlineExample_ManimCE_v0.18.1.png'                   		
		
		
		
		
from manim import *

class FontExample___yessssssworking(Scene):
    def construct(self):
        text1 = MarkupText(
            'all in sans <span font_family="serif">except this</span>', font="sans"
        )
        text2 = MarkupText(
            '<span font_family="serif">mixing</span> <span font_family="sans">fonts</span> <span font_family="monospace">is ugly</span>'
        )
        text3 = MarkupText("special char > or &gt;")
        text4 = MarkupText("special char &lt; and &amp;")
        group = VGroup(text1, text2, text3, text4).arrange(DOWN)
        self.add(group)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class NewlineExample(Scene):
    def construct(self):
        text = MarkupText('foooo<span foreground="red">oo\nbaa</span>aar')
        self.add(text)		
		
		
		
		
		
		
		
from manim import *

class NoLigaturesExample___yessssworking(Scene):
    def construct(self):
        text1 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing')
        text2 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing', disable_ligatures=True)
        group = VGroup(text1, text2).arrange(DOWN)
        self.add(group)		
		
		
		
		
		
		
		
		
		
from manim import *

class yessssworking___MultiLanguage(Scene):
    def construct(self):
        morning = MarkupText("வணக்கம்", font="sans-serif")###thisisnotcomingtheres
        japanese = MarkupText(
            '<span fgcolor="blue">日本</span>へようこそ'
        )  # works as in ``Text``.
        mess = MarkupText("Multi-Language", weight=BOLD)
        russ = MarkupText("Здравствуйте मस नम म ", font="sans-serif")
        hin = MarkupText("नमस्ते", font="sans-serif")
        chinese = MarkupText("臂猿「黛比」帶著孩子", font="sans-serif")
        group = VGroup(morning, japanese, mess, russ, hin, chinese).arrange(DOWN)
        self.add(group)		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py yessssworking___MultiLanguage
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:31:10] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\yessssworking___MultiLanguage_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered yessssworking___MultiLanguage                                                                                                                                  scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\yessssworking___MultiLanguage_ManimCE_v0.18.1.png'           		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class JustifyText____toooooimportanttomakethebookreadingvideos(Scene):
    def construct(self):
        ipsum_text = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            "Praesent feugiat metus sit amet iaculis pulvinar. Nulla posuere "
            "quam a ex aliquam, eleifend consectetur tellus viverra. Aliquam "
            "fermentum interdum justo, nec rutrum elit pretium ac. Nam quis "
            "leo pulvinar, dignissim est at, venenatis nisi."
        )
        justified_text = MarkupText(ipsum_text, justify=True).scale(0.4)
        not_justified_text = MarkupText(ipsum_text, justify=False).scale(0.4)
        just_title = Title("Justified")
        njust_title = Title("Not Justified")
        self.add(njust_title, not_justified_text)
        self.play(
            FadeOut(not_justified_text),
            FadeIn(justified_text),
            FadeOut(njust_title),
            FadeIn(just_title),
        )
        self.wait(1)		
		
		
		
		
from manim import *

class Example1Text(Scene):
    def construct(self):
        text = Text('Hello world').scale(3)
        self.add(text)


from manim import *

class TextColorExample(Scene):
    def construct(self):
        text1 = Text('Hello world', color=BLUE).scale(3)
        text2 = Text('Hello world', gradient=(BLUE, GREEN)).scale(3).next_to(text1, DOWN)
        self.add(text1, text2)


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
		
		
		
from manim import *

class TextMoreCustomization___COLORED___GOOGLES(Scene):
    def construct(self):
        text1 = Text(
            'Google',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                 '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                 '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
        self.add(text1)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class MultipleFonts(Scene):
    def construct(self):
        morning = Text("வணக்கம்", font="sans-serif")###notcoming
        japanese = Text(
            "日本へようこそ", t2c={"日本": BLUE}
        )  # works same as ``Text``.
        mess = Text("Multi-Language", weight=BOLD)
        russ = Text("Здравствуйте मस नम म ", font="sans-serif")
        hin = Text("नमस्ते", font="sans-serif")
        arb = Text(
            "صباح الخير \n تشرفت بمقابلتك", font="sans-serif"
        )  # don't mix RTL and LTR languages nothing shows up then ;-)
        chinese = Text("臂猿「黛比」帶著孩子", font="sans-serif")
        self.add(morning, japanese, mess, russ, hin, arb, chinese)
        for i,mobj in enumerate(self.mobjects):
            mobj.shift(DOWN*(i-3))		
			
			
			
			
			
			
			
			
			
			
			
from manim import *

class PangoRender(Scene):
    def construct(self):
        morning = Text("வணக்கம்", font="sans-serif")###font is not coming
        self.play(Write(morning))          ###i will use it for book reading
        self.wait(2)			
		
		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py PangoRender
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
# # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
# # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
# # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
# # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
# # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
# # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
# # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
# # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:35:30] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
						 # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\PangoRender\1185818338_135637734_223132457.mp4'
				# # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
						 # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\PangoRender\624642324_1141282389_3977241982.mp4'
				# # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
				# # # INFO                                                                                                                                                                 scene_file_writer.py:737
						 # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\PangoRender.mp4'

				# # # INFO     Rendered PangoRender                                                                                                                                                    scene.py:247
						 # # # Played 2 animations
# # # [12/28/24 07:35:31] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\PangoRender.mp4'                        	
		
		
from manim import *

class PangoRender_____________saansbookreadingstagewisecharacters(Scene):
    def construct(self):
        morning = Text("this is to read from the books", font="sans-serif")###font is not coming
        self.play(Write(morning))          ###i will use it for book reading
        self.wait(2)			
			
			
			

# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py PangoRender_____________saansbookreadingstagewisecharacters
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:36:56] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\PangoRender_____________saansbookreadingstagewisecharacters\1185818338_75050690_22313
                             # # # 2457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\partial_movie_files\PangoRender_____________saansbookreadingstagewisecharacters\624642324_1141282389_2595
                             # # # 148962.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\PangoRender_____________saansbookreadingstagewisecharacters.mp4'

                    # # # INFO     Rendered PangoRender_____________saansbookreadingstagewisecharacters                                                                                                    scene.py:247
                             # # # Played 2 animations
# # # [12/28/24 07:36:57] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\rrrrrr\480p15\PangoRender_____________saansbookreadingstagewisecharacters.mp4'     			
			
			
			
			
			
			
			
			
			
			
			
from manim import *

class DodecahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Dodecahedron()
        self.add(obj)			
			
			
			
			
from manim import *

class IcosahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Icosahedron()
        self.add(obj)			
			
			












from manim import *

class OctahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Octahedron()
        self.add(obj)


from manim import *

class SquarePyramidScene___customized_userdefined_polyhedrons(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list)
        self.add(pyramid)		
			
			
			
			
from manim import *

class saanwillusethisforstaadsmodelings___customized_userdefined_polyhedrons(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        vertex_coords = [
            [1, 1, 6],
            [1, -11, 3],
            [-1, -1, 33],
            [-22, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list)
        self.add(pyramid)		
		
# # # D:\SANJOY_NATH_MANIMS>manim -pql rrrrrr.py saanwillusethisforstaadsmodelings___customized_userdefined_polyhedrons
# # # Manim Community v0.18.1

# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:28: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{0}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:29: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{1}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:30: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{2}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:31: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{3}}{2}"),
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:32: SyntaxWarning: invalid escape sequence '\s'
  # # # MathTex("\\frac{\sqrt{4}}{2}")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\s'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:33: SyntaxWarning: invalid escape sequence '\c'
  # # # row_labels=[MathTex("\sin"), MathTex("\cos")],
# # # D:\SANJOY_NATH_MANIMS\rrrrrr.py:35: SyntaxWarning: invalid escape sequence '\c'
  # # # element_to_mobject_config={"unit": "^{\circ}"})
# # # [12/28/24 07:41:00] INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\saanwillusethisforstaadsmodelings___customized_userdefined_polyhedrons_ManimCE_v0.18.1.png'

                    # # # INFO     Rendered saanwillusethisforstaadsmodelings___customized_userdefined_polyhedrons                                                                                         scene.py:247
                             # # # Played 0 animations
                    # # # INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\images\rrrrrr\saanwillusethisforstaadsmodelings___customized_userdefined_polyhedrons_ManimCE_v0.18.1.png'            file_ops.py:231		
						
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
from manim import *
import numpy as np

class saanwillusethisforstaadsmodelings_fittoscreens___customized_userdefined_polyhedrons(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        vertex_coords = [
            [1, 1, 6],
            [1, -11, 3],
            [-1, -1, 33],
            [-22, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]
        pyramid = Polyhedron(vertex_coords, faces_list)
        
        # Scale the polyhedron to fit the screen
        pyramid.scale_to_fit_height(config.frame_height - 2)
        pyramid.scale_to_fit_width(config.frame_width - 2)
        
        self.add(pyramid)

# Create an instance of the scene to trigger the construct method
scene = saanwillusethisforstaadsmodelings___customized_userdefined_polyhedrons()
scene.render()

print("Polyhedron has been scaled to fit the screen.")			
			
			
			
			
			
			
			
			
			
from manim import *

class gggPolyhedronSubMobjects(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        octahedron = Octahedron(edge_length = 3)
        octahedron.graph[0].set_color(RED)
        octahedron.faces[2].set_color(YELLOW)
        self.add(octahedron)			
			
			
			







from manim import *

class TetrahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        obj = Tetrahedron()
        self.add(obj)			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
from manim import *

class ExampleArrow3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 2, 2]),
            resolution=8
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, arrow)			
		
from manim import *

class ExampleCone(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cone = Cone(direction=X_AXIS+Y_AXIS+2*Z_AXIS, resolution=8)
        self.set_camera_orientation(phi=5*PI/11, theta=PI/9)
        self.add(axes, cone)		
		
		
from manim import *

class CubeExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
        self.add(cube)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ExampleCylinder(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = Cylinder(radius=2, height=3)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, cylinder)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class Dot3DExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        dot_1 = Dot3D(point=axes.coords_to_point(0, 0, 1), color=RED)
        dot_2 = Dot3D(point=axes.coords_to_point(2, 0, 0), radius=0.1, color=BLUE)
        dot_3 = Dot3D(point=[0, 0, 0], radius=0.1, color=ORANGE)
        self.add(axes, dot_1, dot_2,dot_3)		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ExampleLine3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, line)		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ExamplePrism(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)
        prismSmall = Prism(dimensions=[1, 2, 3]).rotate(PI / 2)
        prismLarge = Prism(dimensions=[1.5, 3, 4.5]).move_to([2, 0, 0])
        self.add(prismSmall, prismLarge)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ExampleSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
        sphere1 = Sphere(
            center=(3, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        sphere1.set_color(RED)
        self.add(sphere1)
        sphere2 = Sphere(center=(-1, -3, 0), radius=2, resolution=(18, 18))
        sphere2.set_color(GREEN)
        self.add(sphere2)
        sphere3 = Sphere(center=(-1, 2, 0), radius=2, resolution=(16, 16))
        sphere3.set_color(BLUE)
        self.add(sphere3)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ParaSurface(ThreeDScene):
    def func(self, u, v):
        return np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])

    def construct(self):
        axes = ThreeDAxes(x_range=[-4,4], x_length=8)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU],
            resolution=8,
        )
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.add(axes, surface)		
		
		
		
		
		
		
from manim import *

class FillByValueExample(ThreeDScene):
    def construct(self):
        resolution_fa = 8
        self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(x) * np.cos(y)
            return z
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 5],
            u_range=[0, 5],
            )
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.add(axes, surface_plane)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ExampleTorus(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        torus = Torus()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, torus)		
		
		
		
from manim import *

class theImageFromArray(Scene):
    def construct(self):
        image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                       [255, 0, 5, 33]]))
        image.height = 7
        self.add(image)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ImageInterpolationEx(Scene):
    def construct(self):
        img = ImageMobject(np.uint8([[63, 0, 0, 0],
                                        [0, 127, 0, 0],
                                        [0, 0, 191, 0],
                                        [0, 0, 0, 255]
                                        ]))

        img.height = 2
        img1 = img.copy()
        img2 = img.copy()
        img3 = img.copy()
        img4 = img.copy()
        img5 = img.copy()

        img1.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        img2.set_resampling_algorithm(RESAMPLING_ALGORITHMS["lanczos"])
        img3.set_resampling_algorithm(RESAMPLING_ALGORITHMS["linear"])
        img4.set_resampling_algorithm(RESAMPLING_ALGORITHMS["cubic"])
        img5.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        img1.add(Text("nearest").scale(0.5).next_to(img1,UP))
        img2.add(Text("lanczos").scale(0.5).next_to(img2,UP))
        img3.add(Text("linear").scale(0.5).next_to(img3,UP))
        img4.add(Text("cubic").scale(0.5).next_to(img4,UP))
        img5.add(Text("box").scale(0.5).next_to(img5,UP))

        x= Group(img1,img2,img3,img4,img5)
        x.arrange()
        self.add(x)		
		
		
		
		
		
		
from manim import *

class PgroupExample___pointclouds(Scene):
    def construct(self):

        p1 = PointCloudDot(radius=1, density=20, color=BLUE)
        p1.move_to(4.5 * LEFT)
        p2 = PointCloudDot()
        p3 = PointCloudDot(radius=1.5, stroke_width=2.5, color=PINK)
        p3.move_to(4.5 * RIGHT)
        pList = PGroup(p1, p2, p3)

        self.add(pList)		
		
		
		












		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class PMobjectExampletoooooooooimportantpointcloudsshapes(Scene):
    def construct(self):

        pG = PGroup()  # This is just a collection of PMobject's

        # As the scale factor increases, the number of points
        # removed increases.
        for sf in range(1, 9 + 1):
            p = PointCloudDot(density=20, radius=1).thin_out(sf)
            # PointCloudDot is a type of PMobject
            # and can therefore be added to a PGroup
            pG.add(p)

        # This organizes all the shapes in a grid.
        pG.arrange_in_grid()

        self.add(pG)		
		
from manim import *

class ExamplePoint___customsartgenerations_with_forloops(Scene):
    def construct(self):
        colorList = [RED, GREEN, BLUE, YELLOW]
        for i in range(200):
            point = Point(location=[0.63 * np.random.randint(-4, 4), 0.37 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
            self.add(point)
        for i in range(200):
            point = Point(location=[0.37 * np.random.randint(-4, 4), 0.63 * np.random.randint(-4, 4), 0], color=np.random.choice(colorList))
            self.add(point)
        self.add(point)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class PointCloudDotExample(Scene):
    def construct(self):
        cloud_1 = PointCloudDot(color=RED)
        cloud_2 = PointCloudDot(stroke_width=4, radius=1)
        cloud_3 = PointCloudDot(density=15)

        group = Group(cloud_1, cloud_2, cloud_3).arrange()
        self.add(group)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class PointCloudDotExample2___tooimportantanimationstogeneratethroughpointclouds(Scene):
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
		
		
		
		
		
		
		
		
		
		
from manim import *
################################################not playing
class PointCloudDotExample2tocheck___py_yessssssss(Scene):
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

class DashedVMobjectExample(Scene):
    def construct(self):
        r = 0.5

        top_row = VGroup()  # Increasing num_dashes
        for dashes in range(1, 12):
            circ = DashedVMobject(Circle(radius=r, color=WHITE), num_dashes=dashes)
            top_row.add(circ)

        middle_row = VGroup()  # Increasing dashed_ratio
        for ratio in np.arange(1 / 11, 1, 1 / 11):
            circ = DashedVMobject(
                Circle(radius=r, color=WHITE), dashed_ratio=ratio
            )
            middle_row.add(circ)

        func1 = FunctionGraph(lambda t: t**5,[-1,1],color=WHITE)
        func_even = DashedVMobject(func1,num_dashes=6,equal_lengths=True)
        func_stretched = DashedVMobject(func1, num_dashes=6, equal_lengths=False)
        bottom_row = VGroup(func_even,func_stretched)

        top_row.arrange(buff=0.3)
        middle_row.arrange()
        bottom_row.arrange(buff=1)
        everything = VGroup(top_row, middle_row, bottom_row).arrange(DOWN, buff=1)
        self.add(everything)		
		
		
		
		
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








# # # D:\SANJOY_NATH_MANIMS>manim -pql tocheck.py ShapesWithVDict
# # # Manim Community v0.18.1

# # # [12/28/24 08:22:37] INFO     Animation 0 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\1185818338_2759395944_223132457.mp4'
                    # # # INFO     Animation 1 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_151333135.mp4'
                    # # # INFO     Animation 2 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_760794106.mp4'
                    # # # INFO     Animation 3 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_3821531530_2014154177.mp4'
                    # # # INFO     Animation 4 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_3923832781.mp4'
                    # # # INFO     Animation 5 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_2810894713.mp4'
                    # # # INFO     Animation 6 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_3605235151.mp4'
                    # # # INFO     Animation 7 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_2996143138_4067543713.mp4'
# # # [12/28/24 08:22:38] INFO     Animation 8 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_853990248.mp4'
                    # # # INFO     Animation 9 : Partial movie file written in                                                                                                                 scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_2889909005_367433180.mp4'
                    # # # INFO     Animation 10 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_2284358977.mp4'
                    # # # INFO     Animation 11 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_692431636_2809894269.mp4'
                    # # # INFO     Animation 12 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_3864704535.mp4'
                    # # # INFO     Animation 13 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_2327288063_691662086.mp4'
                    # # # INFO     Animation 14 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_2052034747_1085555599.mp4'
                    # # # INFO     Animation 15 : Partial movie file written in                                                                                                                scene_file_writer.py:527
                             # # # 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\partial_movie_files\ShapesWithVDict\624642324_1704852926_2557559699.mp4'
                    # # # INFO     Combining to Movie file.                                                                                                                                    scene_file_writer.py:617
                    # # # INFO                                                                                                                                                                 scene_file_writer.py:737
                             # # # File ready at 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\ShapesWithVDict.mp4'

                    # # # INFO     Rendered ShapesWithVDict                                                                                                                                                scene.py:247
                             # # # Played 16 animations
# # # [12/28/24 08:22:39] INFO     Previewed File at: 'D:\SANJOY_NATH_MANIMS\media\videos\tocheck\480p15\ShapesWithVDict.mp4'   		
		
		
		
		
		
		
		
from manim import *

class ArcShapeIris(Scene):
    def construct(self):
        colors = [DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
        radius = [1 + rad * 0.1 for rad in range(len(colors))]

        circles_group = VGroup()

        # zip(radius, color) makes the iterator [(radius[i], color[i]) for i in range(radius)]
        circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)
                            for rad, col in zip(radius, colors)])
        self.add(circles_group)		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class AddToVGroup(Scene):
    def construct(self):
        circle_red = Circle(color=RED)
        circle_green = Circle(color=GREEN)
        circle_blue = Circle(color=BLUE)
        circle_red.shift(LEFT)
        circle_blue.shift(RIGHT)
        gr = VGroup(circle_red, circle_green)
        gr2 = VGroup(circle_blue) # Constructor uses add directly
        self.add(gr,gr2)
        self.wait()
        gr += gr2 # Add group to another
        self.play(
            gr.animate.shift(DOWN),
        )
        gr -= gr2 # Remove group
        self.play( # Animate groups separately
            gr.animate.shift(LEFT),
            gr2.animate.shift(UP),
        )
        self.play( #Animate groups without modification
            (gr+gr2).animate.shift(RIGHT)
        )
        self.play( # Animate group without component
            (gr-circle_red).animate.shift(RIGHT)
        )		
		
		
		
		
		
		
		
		
from manim import *

class PointFromProportion(Scene):
    def construct(self):
        line = Line(2*DL, 2*UR)
        self.add(line)
        colors = (RED, BLUE, YELLOW)
        proportions = (1/4, 1/2, 3/4)
        for color, proportion in zip(colors, proportions):
            self.add(Dot(color=color).move_to(
                    line.point_from_proportion(proportion)
            ))		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class ChangeOfDirection(Scene):
    def construct(self):
        ccw = RegularPolygon(5)
        ccw.shift(LEFT)
        cw = RegularPolygon(5)
        cw.shift(RIGHT).reverse_direction()

        self.play(Create(ccw), Create(cw),
        run_time=4)		
		
		
		
		
		
		
		
		
from manim import *

class CapStyleExample(Scene):
    def construct(self):
        line = Line(LEFT, RIGHT, color=YELLOW, stroke_width=20)
        line.set_cap_style(CapStyleType.ROUND)
        self.add(line)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class SetFill(Scene):
    def construct(self):
        square = Square().scale(2).set_fill(WHITE,1)
        circle1 = Circle().set_fill(GREEN,0.8)
        circle2 = Circle().set_fill(YELLOW) # No fill_opacity
        circle3 = Circle().set_fill(color = '#FF2135', opacity = 0.2)
        group = Group(circle1,circle2,circle3).arrange()
        self.add(square)
        self.add(group)		
		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class PointsAsCornersExample(Scene):
    def construct(self):
        corners = (
            # create square
            UR, UL,
            DL, DR,
            UR,
            # create crosses
            DL, UL,
            DR
        )
        vmob = VMobject(stroke_color=RED)
        vmob.set_points_as_corners(corners).scale(2)
        self.add(vmob)		
		
		
		
		
		
		
		
		
		
		
		
from manim import *

class SetSheen(Scene):
    def construct(self):
        circle = Circle(fill_opacity=1).set_sheen(-0.3, DR)
        self.add(circle)		
		
		
		
		
		
		
		
		
		
from manim import *

class vectorizedpointsHeightExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()		
		
		
		
from manim import *

class vectorizedpointsWidthExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()		