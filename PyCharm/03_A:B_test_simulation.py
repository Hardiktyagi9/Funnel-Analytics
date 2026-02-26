import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

# ✅ Real funnel data you computed
control_users = np.array([10000, 5000, 1500, 450])

# ✅ Hypothetical improved funnel (25% less drop at each stage)
variant_users = np.array([10000, 6000, 2400, 800])

stages = ['homepage', 'product_page', 'cart', 'checkout']
conversion_stage_index = 0  # convert from homepage to checkout

# Compute conversion rates
control_conversion = control_users[-1] / control_users[0]
variant_conversion = variant_users[-1] / variant_users[0]

print("\nConversion Rates:")
print(f"Control:  {control_conversion:.3%}")
print(f"Variant:  {variant_conversion:.3%}")

# ✅ Z-test for significance
successes = np.array([control_users[-1], variant_users[-1]])
totals = np.array([control_users[0], variant_users[0]])

z_stat, p_value = proportions_ztest(successes, totals)
print(f"\nZ-Statistic: {z_stat:.4f}")
print(f"P-Value: {p_value:.6f}")

if p_value < 0.05:
    print("\n✅ Result: Variant is statistically significant improvement!")
else:
    print("\n❌ Result: No significant evidence that variant is better.")

# ✅ Bar chart comparison
x = np.arange(len(stages))
width = 0.35

plt.figure(figsize=(8,5))
plt.bar(x - width/2, control_users, width, label='Control')
plt.bar(x + width/2, variant_users, width, label='Variant')
plt.xticks(x, stages)
plt.ylabel("Unique Users")
plt.title("A/B Test Funnel Comparison")
plt.legend()
plt.tight_layout()
plt.savefig("data/ab_test_comparison.png")
plt.show()

