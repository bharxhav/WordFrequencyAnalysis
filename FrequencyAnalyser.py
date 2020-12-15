import matplotlib.pyplot as plt
from collections import Counter

"""
* Frequency Analyser *

This is FrequencyAnalyser class, which uses the splitted up words and characters,
to map frequencies onto a line graph.

"""


class FrequencyAnalyser:
    def __init__(self, filename):
        self.fn = filename
        self.name = filename[:-4]

        self.path = "results/" + self.name + "/"

    def analyse(self):
        # Reading Words and Characters and Marking Frequencies
        with open(self.path+'words_lower.txt', 'r') as wl, open(self.path+'alpha_raw.txt', 'r') as cl:
            self.words = dict(Counter(wl.read().split()))
            self.chars = dict(Counter(cl.read().lower()))

        print("Analysed the word frequencies.")
        print("Analysed the character frequencies.")

    def plot(self):
        def second(x): return x[1]

        self.words = list(self.words.items())
        self.chars = list(self.chars.items())

        self.words.sort(key=second, reverse=True)
        self.chars.sort(key=second, reverse=True)

        print("Plotting bar graph for word frequencies.")
        plt.bar(range(len(self.words)), list(
            map(second, self.words)), align='center')
        # plt.xticks(range(len(self.words)), list(
        #     map(lambda x: x[0], self.words)))
        plt.show()

        print("Plotting bar graph for character frequencies.")
        plt.bar(range(len(self.chars)), list(
            map(second, self.chars)), align='center')
        plt.xticks(range(len(self.chars)), list(
            map(lambda x: x[0], self.chars)))
        plt.show()

        # plt.savefig()
        # plt.xticks(range(len(self.words)), list(self.words.keys()))
        # Sort, don't put xticks, set ranges neatly save image
