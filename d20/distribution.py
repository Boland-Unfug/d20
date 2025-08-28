from collections import Counter
from itertools import product

class ProbabilityDistribution:
    def __init__(self, pmf):
        """
        pmf: dict[value, probability]
        """
        total_prob = sum(pmf.values())
        # normalize to be safe
        self.pmf = {k: v / total_prob for k, v in pmf.items()}

    def pdf(self):
        return self.pmf

    def mean(self):
        return sum(val * prob for val, prob in self.pmf.items())

    def variance(self):
        mu = self.mean()
        return sum(prob * (val - mu) ** 2 for val, prob in self.pmf.items())

    def cdf(self, x):
        return sum(prob for val, prob in self.pmf.items() if val <= x)

    def __add__(self, other):
        """Convolve two distributions (sum of outcomes)."""
        new_pmf = Counter()
        for v1, p1 in self.pmf.items():
            for v2, p2 in other.pmf.items():
                new_pmf[v1 + v2] += p1 * p2
        return ProbabilityDistribution(dict(new_pmf))

    def __mul__(self, n: int):
        """Convolve with itself n times (e.g. Nd6)."""
        if n < 1:
            raise ValueError("n must be >= 1")
        result = self
        for _ in range(n - 1):
            result = result + self
        return result
