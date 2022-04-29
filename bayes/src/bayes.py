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

    specificities = [0.99, 0.999, 0.9999, 0.99999]
    colours = ['b', 'g', 'r', 'c']
    for i in range(4):
        plt.plot(prevalence, bayes(0.99, specificities[i], prevalence), color=colours[i])

    plt.xlabel('prevalence')
    plt.ylabel('p(true positive | positive test)')
    plt.title('Probability of true positive given a positive test')
    plt.legend(specificities, title='Specificity')

    plt.show()
