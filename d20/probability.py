from collections import Counter
from itertools import product

class ProbabilityDistribution:
    def __init__(self, pmf):
        """
        pmf: dict[value, probability]
        """
        total = sum(pmf.values())
        if total == 0:
            raise ValueError("Total probability mass cannot be zero")
        # normalize to ensure safety
        self.pmf = {k: v / total for k, v in pmf.items()}

    def die_distribution(size: int):
        return ProbabilityDistribution({i: 1/size for i in range(1, size+1)})

    def percentile_distribution():
        return ProbabilityDistribution({i*10: 0.1 for i in range(10)})

    def pdf(self):
        return self.pmf

    def mean(self):
        return sum(val * prob for val, prob in self.pmf.items())

    def variance(self):
        mu = self.mean()
        return sum(prob * (val - mu) ** 2 for val, prob in self.pmf.items())

    def cdf(self, x):
        return sum(prob for val, prob in self.pmf.items() if val <= x)

    @staticmethod
    def combine(a: "ProbabilityDistribution", b: "ProbabilityDistribution", op) -> "ProbabilityDistribution":
            """
            General convolution of two distributions with an arbitrary operator.
            """
            outcomes = {}
            for l_val, l_prob in a.pmf.items():
                for r_val, r_prob in b.pmf.items():
                    result = op(l_val, r_val)
                    outcomes[result] = outcomes.get(result, 0) + l_prob * r_prob
            return ProbabilityDistribution(outcomes)
    
    
    @staticmethod
    def apply(dist: "ProbabilityDistribution", op):
        """
        Apply a unary operation to a probability distribution.
        
        :param dist: ProbabilityDistribution to transform
        :param op: function taking one argument (e.g., lambda x: -x)
        :return: new ProbabilityDistribution
        """
        new_pmf = {op(val): prob for val, prob in dist.pmf.items()}
        return ProbabilityDistribution(new_pmf)

    def __mul__(self, n: int): #maybe I don't need this anymore? can't I just feed multiplication into the combine function
        """Convolve with itself n times (e.g. Nd6)."""
        print(n)
        if n < 1:
            raise ValueError("n must be >= 1")
        result = self
        for _ in range(n - 1):
            result = result + ProbabilityDistribution.combine(result, self, operator.add)
        return result