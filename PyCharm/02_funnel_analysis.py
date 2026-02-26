import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path('data/user_data.csv')  # Original dataset

df = pd.read_csv(DATA)

# Normalize columns
df['stage'] = df['stage'].str.lower()

# Funnel ordered stages
funnel_order = ['homepage', 'product_page', 'cart', 'checkout', 'payment', 'order_complete']

# Count unique users at each stage
funnel_counts = {
    stage: df[df['stage'] == stage]['user_id'].nunique()
    for stage in funnel_order
    if stage in df['stage'].unique()
}

funnel_df = pd.DataFrame({
    'stage': list(funnel_counts.keys()),
    'users': list(funnel_counts.values())
})

# Conversion from previous & from start
funnel_df['conversion_from_prev_%'] = funnel_df['users'].pct_change().fillna(1) * 100
funnel_df['conversion_from_start_%'] = funnel_df['users'] / funnel_df['users'].iloc[0] * 100

print("\n📊 Funnel Metrics:\n")
print(funnel_df)

# ✅ Visualization using Matplotlib
plt.figure(figsize=(8,5))
plt.barh(funnel_df['stage'], funnel_df['users'])
plt.gca().invert_yaxis()
plt.xlabel("Unique Users")
plt.title("Customer Journey Funnel")
for i, v in enumerate(funnel_df['users']):
    plt.text(v + 0.5, i, str(v), va='center')
plt.tight_layout()
plt.savefig('data/funnel_chart.png')
plt.show()

print("\n✅ Funnel chart saved to: data/funnel_chart.png")

