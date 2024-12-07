from manim import *

class cu(ThreeDScene):
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

        fondo_negro = Rectangle(width=120, height=120, color=BLACK, fill_opacity=0).set_z_index(-1)
        self.add(fondo_negro)
        self.play(fondo_negro.animate.set_fill(opacity=1), run_time=2)
        self.remove(*self.mobjects)

        self.camera.background_color = BLACK
        circle = Circle()
        self.play(Create(circle))
        self.wait()
        self.remove(*self.mobjects)

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
        self.remove(*self.mobjects)
        self.cambiar_fondo(PINK, duracion=2)
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
        self.remove(*self.mobjects)

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(Create(circle), Create(axes))
        self.wait()
        self.remove(*self.mobjects)
        self.cambiar_fondo(BLUE_D, duracion=2)

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=30 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
        self.remove(*self.mobjects)
        self.cambiar_fondo(YELLOW_B, duracion=2)

        axes = ThreeDAxes()
        self.play(Create(circle), Create(axes))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()
        self.remove(*self.mobjects)
        self.cambiar_fondo(RED_B, duracion=2)
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)
        self.wait()
        self.remove(*self.mobjects)

        curve1 = ParametricFunction(lambda u: np.array([1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]), color=RED, t_range=np.array([-TAU, TAU]))
        curve2 = ParametricFunction(lambda u: np.array([1.2 * np.cos(u), 1.2 * np.sin(u), u]), color=RED, t_range=np.array([-TAU, TAU]))

        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()
        self.remove(*self.mobjects)
        self.cambiar_fondo(PINK, duracion=2)

        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)

        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()
        self.remove(*self.mobjects)

        surfaces = [
            Surface(lambda u, v: np.array([np.cos(TAU * v), np.sin(TAU * v), 2 * (1 - u)]), resolution=(6, 32)),
            Surface(lambda u, v: np.array([np.cos(v) * u, np.sin(v) * u, u**2]), u_range=[0, 2], v_range=[0, TAU], checkerboard_colors=[PURPLE_D, PURPLE_E], resolution=(10, 32)).scale(2),
            Surface(lambda u, v: np.array([u, v, u**2 - v**2]), u_range=[-2, 2], v_range=[-2, 2], checkerboard_colors=[BLUE_D, BLUE_E], resolution=(15, 32)).scale(1),
            Surface(lambda u, v: np.array([u * np.cos(v), u * np.sin(v), u]), u_range=[0, 2], v_range=[0, TAU], checkerboard_colors=[GREEN_D, GREEN_E], resolution=(15, 32)).scale(1),
            Surface(lambda u, v: np.array([np.cosh(u) * np.cos(v), np.cosh(u) * np.sin(v), np.sinh(u)]), u_range=[-2, 2], v_range=[0, TAU], checkerboard_colors=[YELLOW_D, YELLOW_E], resolution=(15, 32)),
            Surface(lambda u, v: np.array([1 * np.cos(u) * np.cos(v), 2 * np.cos(u) * np.sin(v), 0.5 * np.sin(u)]), u_range=[-PI/2, PI/2], v_range=[0, TAU], checkerboard_colors=[TEAL_D, TEAL_E], resolution=(15, 32)).scale(2),
            Surface(lambda u, v: np.array([1.5 * np.cos(u) * np.cos(v), 1.5 * np.cos(u) * np.sin(v), 1.5 * np.sin(u)]), u_range=[-PI/2, PI/2], v_range=[0, TAU], checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)).scale(2)
        ]
        self.cambiar_fondo(BLACK, duracion=2)
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        for surface in surfaces:
            self.play(Create(surface), run_time=2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.remove(*self.mobjects)