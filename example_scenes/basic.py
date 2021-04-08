#!/usr/bin/env python

from manim import *

# To watch one of these scenes, run the following:
# python --quality m manim example_scenes.py SquareToCircle -p
#
# Use the flag --quality l for a faster rendering at a lower quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have preview of the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the nth animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

#config.background_color = WHITE
config.frame_height = 32
config.frame_width = 18
config.pixel_height = 1280 # 64
config.pixel_width = 720    # 36
class tyt1(Scene):
    def construct(self):

        # numberplane = NumberPlane()
        # self.add(numberplane)


        p0_0 = [0, 10, 0]
        tt1 = Text("甲乙两人去书店买书，甲带的钱数是乙带").move_to(p0_0).scale(1.3)
        tt2 = Text("的3倍。甲买了一套180元的《百科大全》,").scale(1.3).next_to(tt1, DOWN)
        tt3 = Text("乙买了一套30元的《故事大王》后，").scale(1.3).next_to(tt2, DOWN)
        tt4 = Text("两人的钱数一样多，甲原来多少钱？").scale(1.3).next_to(tt3, DOWN)
        vg = VGroup(tt1, tt2, tt3, tt4)
        self.add(vg)
        self.play(Write(vg))

        p1_0 = [-4, 2, 0]
        p1_1_0 = [-2, 2, 0]
        p1_1 = [0, 2, 0]

        p2_0 = [-4, -2, 0]
        p2_1_0 = [-2, -2, 0]
        p2_1 = [0, -2, 0]
        p2_2 = [4, -2, 0]
        p2_3 = [8, -2, 0]

        dot1_1 = Dot(p1_0).scale(2)
        dot1_2 = Dot(p1_1).scale(2)

        dot2_0 = Dot(p2_0).scale(2)
        dot2_1 = Dot(p2_1).scale(2)
        dot2_2 = Dot(p2_2).scale(2)
        dot2_3 = Dot(p2_3).scale(2)

        line1 = Line(p1_0, p1_1, stroke_width=10).set_color(YELLOW)
        line2 = Line(p2_0, p2_1, stroke_width=10).set_color(RED)
        line3 = Line(p2_1, p2_2, stroke_width=10).set_color(RED)
        line4 = Line(p2_2, p2_3, stroke_width=10).set_color(RED)

        t1 = Text("乙: ").scale(2).next_to(line1, LEFT, buff=1)
        self.add(line1, t1, dot1_1, dot1_2)
        self.play(GrowFromCenter(line1))
        #self.wait(1)
        t2 = Text("甲: ").scale(2).next_to(line2, LEFT, buff=1)
        self.add(line2,t2, dot2_0,dot2_1)
        self.play(FadeIn(line2))
        self.add(line3, dot2_2)
        self.play(FadeIn(line3))
        self.add(line4, dot2_3)
        self.play(FadeIn(line4))

        line_sub = DashedLine(p1_1_0, p2_1_0, stroke_width=10).set_color(GRAY).scale(2)
        self.add(line_sub)
        self.play(FadeIn(line_sub))

        line1_b = Line(p1_1_0, p1_1, stroke_width=10).set_color(YELLOW)
        line2_b = Line(p2_1_0, p2_3, stroke_width=10).set_color(RED)
        line2_b2 = Line(p2_0, p2_3, stroke_width=10).set_color(RED)
        b1 = Brace(line1_b, direction=UP, buff=0.5)
        b2 = Brace(line2_b, direction=UP, buff=0.5)
        b3 = Brace(line2_b2, direction=DOWN, buff=0.5)
        b1text = b1.get_tex("30").scale(2)
        b2text = b2.get_tex("180").scale(2)

        b3t = b3.get_tex("?").scale(2)
        self.add(b1, b1text )
        self.play(FadeIn(b1text))
        self.add(b2, b2text)
        self.play(FadeIn(b2text))
        self.add(b3, b3t)
        self.play(ShowCreation(b3t))

        self.wait(3)
        pd = [0, -6, 0]
        td0 = Text("答案：").move_to(pd).scale(1.3)
        td1 = Text("(180 - 30) ÷ (3 -1) = 75(元)").scale(1.3).next_to(td0, DOWN)
        td2 = Text("75 x 3 = 225(元）").scale(1.3).next_to(td1, DOWN)

        vg2 = VGroup(td0, td1, td2)
        self.add(vg2)
        self.play(ShowCreation(vg2))
        self.wait(10)
        # self.play(GrowFromCenter(circle))
        # self.play(Transform(dot, dot2))
        # self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        # self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        # self.wait()
class tyt(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)

        text=Text("This  唐元天")

        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[4], buff = .1)
        framebox2 = SurroundingRectangle(text[5], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )

        self.wait(2)

class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFrom(grid_title, direction=DOWN),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
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


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = Tex("This is a some text 中文", tex_to_color_map={"text": YELLOW})
        example_tex = MathTex(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(config["frame_width"] - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
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


# See many more examples at https://docs.manim.community/en/latest/examples.html
