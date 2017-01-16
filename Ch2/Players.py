import random
import sys

class RandomPlayer(object):

    def __init__(self):
        pass

    def play(self, bandit, t):
        total_payout = 0.0
        for i in xrange(0, t):
            total_payout += bandit.play(self.choose(bandit))

        return total_payout



    def choose(self, bandit):
        return random.randint(0, bandit.n - 1)


class AverageGreedyEpsilonPlayer(object):

    def __init__(self, epsilon):

        self.epsilon=epsilon

    def play(self, bandit, t):

        total_payout = 0.0
        payouts = [(0.0, 0) for _ in xrange(bandit.n)]

        for i in xrange(0, t):
            if random.random() <= self.epsilon:
                # EXPLORE
                arm = random.randint(0, bandit.n - 1)
            else:
                # EXPLOIT
                arm = max([i for i in xrange(bandit.n)], key=lambda x : payouts[x][0] / (payouts[x][1]) if payouts[x][1] > 0 else sys.float_info.min)

            payout = bandit.play(arm)
            payouts[arm] = (payouts[arm][0] + payout, payouts[arm][1] + 1)

            total_payout += payout
        return total_payout

    def choose(self, bandit):



        return random.randint(0, bandit.n - 1)