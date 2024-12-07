from manim import *

class dos(Scene):
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

        self.camera.background_color = BLUE
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+", "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(GrowFromCenter(brace1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(brace1, brace2), ReplacementTransform(t1, t2))
        self.wait()
        self.remove(text, brace1, brace2, t1, t2)

        self.camera.background_color = GREEN
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+", "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(GrowFromCenter(brace1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(brace1.copy(), brace2), ReplacementTransform(t1.copy(), t2))
        self.wait()
        self.remove(text, brace1, brace2, t1, t2)

        self.camera.background_color = RED
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+", "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()
        self.remove(text, framebox1, framebox2)

        self.camera.background_color = YELLOW
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+", "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1.copy(), framebox2, path_arc=-np.pi))
        self.wait()
        self.remove(text, framebox1, framebox2)

        self.camera.background_color = PURPLE
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+", "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        t1 = MathTex("g'f")
        t2 = MathTex("f'g")
        t1.next_to(framebox1, UP, buff=0.1)
        t2.next_to(framebox2, UP, buff=0.1)
        self.play(Create(framebox1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(framebox1.copy(), framebox2), ReplacementTransform(t1.copy(), t2))
        self.wait()
        self.remove(text, framebox1, framebox2, t1, t2)

        self.camera.background_color = ORANGE
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        arrow = Arrow(LEFT, RIGHT)
        step1.move_to(LEFT * 2)
        arrow.next_to(step1, RIGHT, buff=0.1)
        step2.next_to(arrow, RIGHT, buff=0.1)
        self.play(Write(step1))
        self.wait()
        self.play(Create(arrow))
        self.play(Write(step2))
        self.wait()
        self.remove(step1, step2, arrow)

        self.camera.background_color = TEAL
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = Arrow(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Arrow(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()
        self.remove(step1, step2, arrow1, arrow2)

        self.camera.background_color = MAROON
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = Line(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()
        self.remove(step1, step2, arrow1, arrow2)

        self.camera.background_color = PINK
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()
        self.remove(step1, step2, arrow1, arrow2)

        self.camera.background_color = LIGHT_BROWN
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        line = Line(step1.get_right(), step2.get_left(), buff=0.1)
        self.play(Write(step1), Write(step2))
        self.play(Create(line))
        self.play(step2.animate.next_to(step2, LEFT * 2))
        self.wait()
        self.remove(step1, step2, line)

        self.camera.background_color = DARK_BLUE
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step3 = step2.copy()
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        step3.next_to(step2, LEFT * 2)
        line = Line(step1.get_right(), step2.get_left(), buff=0.1)
        lineCopy = Line(step1.get_right(), step3.get_bottom(), buff=0.1)
        self.play(Write(step1), Write(step2))
        self.play(Create(line))
        self.play(ReplacementTransform(step2, step3), ReplacementTransform(line, lineCopy))
        self.wait()
        self.remove(step1, step2, step3, line, lineCopy)