from manim import *

class Co(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        t1 = Text("Centro Universitario UAEM Zumpango", font_size=35, color=BLACK)
        t2 = Text("Graficación computacional", font_size=30, color=BLACK)
        t3 = Text("Por: Guerrero Estrada David Israel", font_size=25, color=BLACK)
        t4 = Text("Ingeniería en computación", font_size=20, color=BLACK)

        t1.shift(UP * 2.5)
        t2.next_to(t1, DOWN, buff=0.5)
        t3.next_to(t2, DOWN, buff=0.5)
        t4.next_to(t3, DOWN, buff=0.5)
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4))
        self.wait(2)

        self.camera.background_color = BLACK

        # TransformationText1V1
        texto1 = Text("First text")
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.remove(texto1, texto2)
        self.camera.background_color = BLUE
        # TransformationText1V2
        texto1 = Text("First text")
        texto1.to_edge(UP)
        texto2 = Text("Second text")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.remove(texto1, texto2)
        self.camera.background_color = PINK
        # TransformationText2
        text1 = Text("Function")
        text2 = Text("Derivative")
        text3 = Text("Integral")
        text4 = Text("Transformation")
        self.play(Write(text1))
        self.wait()
        self.play(ReplacementTransform(text1, text2))
        self.wait()
        self.play(ReplacementTransform(text2, text3))
        self.wait()
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        self.remove(text1, text2, text3, text4)
        self.camera.background_color = BLUE_B
        # CopyTextV1
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        )
        formula.scale(2)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9])
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10])
        )
        self.wait()
        self.remove(formula)
        self.camera.background_color = RED
        # CopyTextV2
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        )
        formula.scale(2)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()
        self.remove(formula)
        self.camera.background_color = GREEN
        # CopyTextV3
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        )
        formula.scale(2)
        formula[8].set_color(RED)
        formula[11].set_color(BLUE)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()
        self.remove(formula)
        self.camera.background_color = YELLOW_B
        # CopyTextV4
        formula = MathTex(
            "\\frac{d}{dx}", "(", "u", "+", "v", ")", "=", 
            "\\frac{d}{dx}", "u", "+", "\\frac{d}{dx}", "v"
        )
        formula.scale(2)
        for letter, color in [("u", RED), ("v", BLUE)]:
            formula.set_color_by_tex(letter, color)
        self.play(Write(formula[:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
            run_time=3
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
            run_time=3
        )
        self.wait()
        self.remove(formula)

        # CopyTwoFormulas1
        formula1 = MathTex("\\neg", "\\forall", "x", ":", "P(x)")
        formula2 = MathTex("\\exists", "x", ":", "\\neg", "P(x)")
        for size, pos, formula in [(2, 2 * UP, formula1), (2, 2 * DOWN, formula2)]:
            formula.scale(size)
            formula.move_to(pos)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [(0, 1, 2, 3, 4), (3, 0, 1, 2, 4)],
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i].copy(), formula2[j])
                for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()
        self.remove(formula1, formula2)

        # CopyTwoFormulas2
        formula1 = MathTex("\\neg", "\\forall", "x", ":", "P(x)")
        formula2 = MathTex("\\exists", "x", ":", "\\neg", "P(x)")
        for size, pos, formula in [(2, 2 * UP, formula1), (2, 2 * DOWN, formula2)]:
            formula.scale(size)
            formula.move_to(pos)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [(2, 3, 4), (1, 2, 4)],
            [(0,), (3,)],
            [(1,), (0,)]
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i].copy(), formula2[j])
                for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()
        self.remove(formula1, formula2)

        # CopyTwoFormulas2Color
        formula1 = MathTex("\\neg", "\\forall", "x", ":", "P(x)")
        formula2 = MathTex("\\exists", "x", ":", "\\neg", "P(x)")
        parametters = [(2, 2 * UP, formula1, GREEN, "\\forall"),
                       (2, 2 * DOWN, formula2, ORANGE, "\\exists")]
        for size, pos, formula, col, sim in parametters:
            formula.scale(size)
            formula.move_to(pos)
            formula.set_color_by_tex(sim, col)
            formula.set_color_by_tex("\\neg", PINK)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [(2, 3, 4), (1, 2, 4)],
            [(0,), (3,)],
            [(1,), (0,)]
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i].copy(), formula2[j])
                for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()
        self.remove(formula1, formula2)

        # CopyTwoFormulas3
        formula1 = MathTex("\\neg", "\\forall", "x", ":", "P(x)")
        formula2 = MathTex("\\exists", "x", ":", "\\neg", "P(x)")
        parametters = [(2, 2 * UP, formula1, GREEN, "\\forall"),
                       (2, 2 * DOWN, formula2, ORANGE, "\\exists")]
        for size, pos, formula, col, sim in parametters:
            formula.scale(size)
            formula.move_to(pos)
            formula.set_color_by_tex(sim, col)
            formula.set_color_by_tex("\\neg", PINK)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [(2, 3, 4), (1, 2, 4)],
            [(0,), (3,)],
            [(1,), (0,)]
        ]
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(formula1[i], formula2[j])
                for i, j in zip(pre_ind, post_ind)
            ], run_time=2)
            self.wait()
        self.remove(formula1, formula2)
