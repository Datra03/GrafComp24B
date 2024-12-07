from manim import *

class tre(Scene):
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
        plot_graph = self.create_plot_graph()
        self.play(Create(plot_graph), run_time=2)
        self.wait()
        self.remove(plot_graph)

        self.camera.background_color = GREEN
        plot1 = self.create_plot1()
        self.play(Create(plot1), run_time=2)
        self.wait()
        self.remove(plot1)

        self.camera.background_color = RED
        plot1v2 = self.create_plot1v2()
        self.play(Create(plot1v2), run_time=2)
        self.wait()
        self.remove(plot1v2)

        self.camera.background_color = YELLOW
        plot2 = self.create_plot2()
        self.play(Create(plot2), run_time=2)
        self.wait()
        self.remove(plot2)

        self.camera.background_color = PURPLE
        plot3 = self.create_plot3()
        self.play(Create(plot3), run_time=2)
        self.wait()
        self.remove(plot3)

        self.camera.background_color = ORANGE
        plot4 = self.create_plot4()
        self.play(Create(plot4), run_time=2)
        self.wait()
        self.remove(plot4)

        self.camera.background_color = TEAL
        plot5 = self.create_plot5()
        self.play(Create(plot5), run_time=2)
        self.wait()
        self.remove(plot5)

        self.camera.background_color = MAROON
        plot6 = self.create_plot6()
        self.play(Create(plot6), run_time=2)
        self.wait()
        self.remove(plot6)

        self.camera.background_color = PINK
        plot7 = self.create_plot7()
        self.play(Create(plot7), run_time=2)
        self.wait()
        self.remove(plot7)

        self.camera.background_color = LIGHT_BROWN
        plot_sin_cos = self.create_plot_sin_cos()
        self.play(Create(plot_sin_cos), run_time=2)
        self.wait()
        self.remove(plot_sin_cos)

    def create_plot_graph(self):
        axes = Axes(
            x_range=[4, 7, 0.5],
            y_range=[20, 50, 5],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(4, 7.5, 0.5)},
            y_axis_config={"numbers_to_include": range(30, 60, 10)},
            tips=False,
            x_length=10,
            y_length=6,
        )
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[5, 7])
        
        return VGroup(axes, axes_labels, graph)

    def create_plot1(self):
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 5],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(2, 7.5, 0.5)},
            y_axis_config={"numbers_to_include": range(0, 60, 10)},
            tips=False,
            x_length=10,
            y_length=6,
        )
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])
        
        return VGroup(axes, axes_labels, graph)

    def create_plot1v2(self):
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 5],
            axis_config={"color": BLUE},
            tips=False,
            x_length=10,
            y_length=6,
        )
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])
        
        return VGroup(axes, axes_labels, graph)

    def create_plot2(self):
       axes = Axes(
           x_range=[0, 7, 1],
           y_range=[0, 50, 5],
           axis_config={"color": BLUE},
           tips=False,
           x_length=10,
           y_length=6,
       )
       
       axes_labels = axes.get_axis_labels(x_label="t", y_label="f(t)")
       graph = axes.plot(lambda x: x**2, color=GREEN)
       
       return VGroup(axes, axes_labels, graph)

    def create_plot3(self):
       axes = Axes(
           x_range=[0, 7, 1],
           y_range=[0, 50, 10],
           axis_config={"color": BLUE},
           tips=False,
           x_length=10,
           y_length=6,
       )
       
       axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
       graph = axes.plot(lambda x: x**2, color=GREEN)
       
       return VGroup(axes, axes_labels, graph)

    def create_plot4(self):
       axes = Axes(
           x_range=[0, 7, 1],
           y_range=[0, 50, 10],
           axis_config={"color": BLUE},
           tips=False,
           x_length=10,
           y_length=6,
       )
       
       axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
       graph = axes.plot(lambda x: x**2, color=GREEN)
       
       return VGroup(axes, axes_labels, graph)

    def create_plot5(self):
       axes = Axes(
           x_range=[0, 7, 0.5],
           y_range=[0, 50, 10],
           axis_config={"color": BLUE},
           tips=False,
           x_length=10,
           y_length=6,
       )
       
       axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
       graph = axes.plot(lambda x: x**2, color=GREEN)
       
       return VGroup(axes, axes_labels, graph)

    def create_plot6(self):
       axes = Axes(
           x_range=[0, 7, 0.5],
           y_range=[0, 50, 10],
           axis_config={"color": BLUE},
           tips=False,
           x_length=10,
           y_length=6,
       )
       
       axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
       graph = axes.plot(lambda x: x**2, color=GREEN)
       
       return VGroup(axes, axes_labels, graph)

    def create_plot7(self):
       axes = Axes(
           x_range=[0, 7, 0.5],
           y_range=[0, 50, 10],
           axis_config={"color": BLUE},
           tips=False,
           x_length=10,
           y_length=6,
       )
       
       axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
       graph = axes.plot(lambda x: x**2, color=GREEN)
       
       return VGroup(axes, axes_labels, graph)

    def create_plot_sin_cos(self):
        axes = Axes(
            x_range=[-3 * PI / 2, 3 * PI / 2, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE},
            tips=False,
            x_length=10,
            y_length=6,
        )
        
        plot_sin = axes.plot(lambda x: np.sin(x), color=GREEN, x_range=[-4, 4])
        plot_cos = axes.plot(lambda x: np.cos(x), color=GRAY, x_range=[-PI, 0])
        
        plot_sin.set_stroke(width=3)
        plot_cos.set_stroke(width=2)
        
        axes_labels = axes.get_axis_labels(x_label="\\theta", y_label="\\sin\\theta")
        
        return VGroup(axes, axes_labels, plot_sin, plot_cos)