import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Face_Cream':  [1500, 1800, 2100, 1700, 2300, 2500,
                    2700, 2200, 1900, 2100, 2400, 2800],
    'Face_Wash':   [1200, 1400, 1600, 1300, 1700, 1900,
                    2100, 1800, 1500, 1700, 2000, 2300],
    'Moisturizer': [1000, 1100, 1300, 1200, 1400, 1500,
                    1700, 1600, 1400, 1500, 1800, 2000],
    'Lipstick':    [ 800,  900, 1000,  950, 1100, 1200,
                    1300, 1250, 1100, 1200, 1400, 1600],
    'Eye_Liner':   [ 600,  700,  800,  750,  900, 1000,
                    1100, 1050,  900, 1000, 1200, 1400],
}

df = pd.DataFrame(data)

# Cost is 60 % of sales; profit = 40 %
products = ['Face_Cream', 'Face_Wash', 'Moisturizer', 'Lipstick', 'Eye_Liner']
df['Total_Sales']  = df[products].sum(axis=1)
df['Total_Profit'] = (df['Total_Sales'] * 0.40).round(2)

print("=" * 55)
print("       Cosmetic Company Sales Dataset")
print("=" * 55)
print(df[['Month', 'Total_Sales', 'Total_Profit']].to_string(index=False))
print()

plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Total_Profit'], marker='o',
         color='royalblue', linewidth=2.5, markersize=8,
         markerfacecolor='orange', label='Monthly Profit')
plt.fill_between(df['Month'], df['Total_Profit'], alpha=0.15, color='royalblue')
plt.title('Total Monthly Profit – Cosmetic Company', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Profit (₹)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('a_line_plot_profit.png', dpi=150)
plt.show()
print("Plot (a) saved: a_line_plot_profit.png")

colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
plt.figure(figsize=(12, 6))
for product, color in zip(products, colors):
    plt.plot(df['Month'], df[product], marker='o',
             linewidth=2, label=product.replace('_', ' '), color=color)
plt.title('All Product Sales – Monthly Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('b_multiline_plot_products.png', dpi=150)
plt.show()
print("Plot (b) saved: b_multiline_plot_products.png")

x      = np.arange(len(df['Month']))
width  = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, df['Face_Cream'], width,
               label='Face Cream', color='#e74c3c', edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, df['Face_Wash'],  width,
               label='Face Wash',  color='#3498db', edgecolor='black', linewidth=0.5)

ax.set_title('Face Cream vs Face Wash – Monthly Sales', fontsize=14, fontweight='bold')
ax.set_xlabel('Month')
ax.set_ylabel('Units Sold')
ax.set_xticks(x)
ax.set_xticklabels(df['Month'])
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)
fig.tight_layout()
plt.savefig('c_bar_chart_face_products.png', dpi=150)
plt.show()
print("Plot (c) saved: c_bar_chart_face_products.png")

annual_sales = df[products].sum()
explode      = (0.05,) * len(products)
colors_pie   = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']

plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    annual_sales,
    labels=[p.replace('_', ' ') for p in products],
    autopct='%1.1f%%',
    explode=explode,
    colors=colors_pie,
    startangle=140,
    textprops={'fontsize': 11}
)
for at in autotexts:
    at.set_fontweight('bold')

plt.title('Annual Product-wise Sales Share', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('d_pie_chart_annual_sales.png', dpi=150)
plt.show()
print("Plot (d) saved: d_pie_chart_annual_sales.png")