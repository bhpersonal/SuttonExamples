from Ch2.NArmedBandit import NGuassianArmedBandit
from Ch2.Players import *
import random

def experiment1():


    n = 100
    trials = 1000000
    ds = [(random.gauss(0, 100), (random.gauss(0, 100))) for i in xrange(n)]

    bandit = NGuassianArmedBandit(ds)
    players = [RandomPlayer(),
               AverageGreedyEpsilonPlayer(0.00001),
               AverageGreedyEpsilonPlayer(0.0001),
               AverageGreedyEpsilonPlayer(0.001),
               AverageGreedyEpsilonPlayer(0.01),
               AverageGreedyEpsilonPlayer(0.05),
               AverageGreedyEpsilonPlayer(0.1),
               AverageGreedyEpsilonPlayer(0.2),
               AverageGreedyEpsilonPlayer(0.3),
               AverageGreedyEpsilonPlayer(0.5),
               AverageGreedyEpsilonPlayer(1.0)]

    for player in players:
        payout = player.play(bandit, trials)
        print type(player).__name__  + ": " + str(round(payout / float(trials), 5))







if __name__ == "__main__":
    experiment1()

