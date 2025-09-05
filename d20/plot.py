
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