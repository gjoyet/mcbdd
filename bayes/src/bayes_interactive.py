import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

matplotlib.use('TkAgg')

if __name__ == '__main__':
    # The parametrized function to be plotted
    def bayes(sensitivity, specificity, prevalence):
        result = sensitivity * prevalence / (sensitivity * prevalence + (1.0 - specificity) * (1.0 - prevalence))
        return result

    prevalence = np.linspace(0.001, 0.5, 1000)

    # Define initial parameters
    init_sensitivity = 0.99
    init_specificity = 0.99

    # Create the figure and the line that we will manipulate
    fig_interactive, ax = plt.subplots()
    line, = plt.plot(prevalence, bayes(init_sensitivity, init_specificity, prevalence), lw=2)
    ax.set_xlabel('prevalence')
    ax.set_ylabel('p(true positive | positive test)')
    ax.set_title('Probability of true positive given a positive test')

    # adjust the main plot to make room for the sliders
    plt.subplots_adjust(left=0.25, bottom=0.25)

    # Make a horizontal slider to control the sensitivity.
    axsens = plt.axes([0.25, 0.1, 0.65, 0.03])
    sens_slider = Slider(
        ax=axsens,
        label='Sensitivity',
        valmin=0.98,
        valmax=1,
        valinit=init_sensitivity,
    )

    # Make a vertically oriented slider to control the specificity
    axspec = plt.axes([0.1, 0.25, 0.0225, 0.63])
    spec_slider = Slider(
        ax=axspec,
        label='Specificity',
        valmin=0.98,
        valmax=1,
        valinit=init_specificity,
        orientation="vertical"
    )


    # The function to be called anytime a slider's value changes
    def update(val):
        line.set_ydata(bayes(sens_slider.val, spec_slider.val, prevalence))
        fig_interactive.canvas.draw_idle()


    # register the update function with each slider
    sens_slider.on_changed(update)
    spec_slider.on_changed(update)

    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', hovercolor='0.975')


    def reset(event):
        sens_slider.reset()
        spec_slider.reset()
    button.on_clicked(reset)

    plt.show()