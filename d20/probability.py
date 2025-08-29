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


# # # Build single-die PMF: each side equally likely
#         single_die_pmf = {i: 1 / dice_expr.size for i in range(1, dice_expr.size + 1)}
#         single_die_dist = ProbabilityDistribution(single_die_pmf)

#         # Convolve for multiple dice
#         total_dist = single_die_dist * dice_expr.num

#         pdf = total_dist.pdf()

#         outcomes = sorted(pdf.keys())
#         probabilities = [pdf[o] for o in outcomes]

#         # Plot the PDF
#         plt.figure(figsize=(8, 4))
#         plt.bar(outcomes, probabilities, width=0.6, edgecolor='black')
#         plt.title(f"Probability Distribution for {dice_expr.num}d{dice_expr.size}")
#         plt.xlabel("Sum of Dice")
#         plt.ylabel("Probability")
#         plt.grid(axis='y', linestyle='--', alpha=0.7)
#         plt.show()