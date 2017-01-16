import random


class NGuassianArmedBandit(object):

    def __init__(self, distributions):

        self.n = len(distributions)
        self.distributions = distributions

    def play(self, i):

        mean, stddev = self.distributions[i]
        payout = random.gauss(mean,stddev)
        return payout