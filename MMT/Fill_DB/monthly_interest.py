from matplotlib import pyplot as plt
import numpy as np
from math import pow

class MoneyTree:
    #  Main data
    GOAL = 30000000
    PRINCIPLE = 1000000
    TIMES_PER_ANNUM = 12
    YEARS = 3
    RATE = 0
    INTEREST = 0
    TIMES = TIMES_PER_ANNUM * YEARS
    AMOUNTS = [] #  x
    PROFITS = [] #  y

    def __init__(self):
        self.calc_rate()
        self.calc_values()


    def calc_rate(self):
        gOverp = self.GOAL / self.PRINCIPLE
        root_gop = pow(gOverp, (1/self.TIMES))
        rate = (root_gop - 1) * 100
        self.RATE = rate
        self.INTEREST = (rate/100)


    def calc_values(self):
        self.AMOUNTS.append(self.PRINCIPLE)
        for i in range(0, self.TIMES):
            interest = self.AMOUNTS[i] * self.INTEREST
            self.PROFITS.append(interest)
            self.AMOUNTS.append(interest + self.AMOUNTS[i])


    def plot_values(self):
        yvalues = np.array([int(i) for i in self.PROFITS])
        y2values = np.array([int(i) for i in self.AMOUNTS])

        plt.title("Trading Interest Goals")
        plt.ylabel("Compound Interest")
        plt.xlabel("Months")
        plt.grid()

        plt.plot([i for i in range(0, len(yvalues))],yvalues)
        plt.plot([i for i in range(0, len(yvalues))],y2values[:-1])

        plt.show()




