import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Company':      ['Microsoft', 'Google', 'Amazon', 'IBM',
                     'Deloitte', 'Capgemini', 'ATOS Origin', 'Amdocs'],
    'Recruitments': [4500, 5200, 6100, 3200,
                     2800, 3900, 1500, 2100],
}

df = pd.DataFrame(data)

print("=" * 40)
print("   New Recruitments Dataset")
print("=" * 40)
print(df.to_string(index=False))
print()

companies    = df['Company'].tolist()
recruitments = df['Recruitments'].tolist()
colors       = ['#3498db', '#e74c3c', '#f39c12', '#2ecc71',
                '#9b59b6', '#1abc9c', '#e67e22', '#34495e']

plt.figure(figsize=(11, 6))
bars = plt.bar(companies, recruitments, color=colors,
               edgecolor='black', linewidth=0.6, width=0.6)

# Value labels on top of each bar
for bar, val in zip(bars, recruitments):
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 80,
             str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title('New Recruitments in Top IT / Consulting Companies', fontsize=14, fontweight='bold')
plt.xlabel('Company')
plt.ylabel('Number of Recruitments')
plt.xticks(rotation=30, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('a_bar_chart_recruitments.png', dpi=150)
plt.show()
print("Plot (a) saved: a_bar_chart_recruitments.png")

plt.figure(figsize=(9, 9))
wedges, texts, autotexts = plt.pie(
    recruitments,
    labels=companies,
    autopct='%1.1f%%',
    colors=colors,
    startangle=120,
    textprops={'fontsize': 10},
)
for at in autotexts:
    at.set_fontweight('bold')

plt.title('Recruitment Share Across Companies', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('b_pie_chart_recruitments.png', dpi=150)
plt.show()
print("Plot (b) saved: b_pie_chart_recruitments.png")

explode = [0.05] * len(companies)
explode[recruitments.index(max(recruitments))] = 0.15   # highlight leader

plt.figure(figsize=(9, 9))
wedges, texts, autotexts = plt.pie(
    recruitments,
    labels=companies,
    autopct='%1.1f%%',
    explode=explode,
    colors=colors,
    shadow=True,
    startangle=140,
    textprops={'fontsize': 10},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
)
for at in autotexts:
    at.set_fontweight('bold')
    at.set_fontsize(9)

plt.title('Customised Pie Chart – Recruitments\n(Largest slice exploded)',
          fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('c_custom_pie_chart_recruitments.png', dpi=150)
plt.show()
print("Plot (c) saved: c_custom_pie_chart_recruitments.png")

fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    recruitments,
    labels=companies,
    autopct='%1.1f%%',
    colors=colors,
    startangle=140,
    pctdistance=0.80,
    textprops={'fontsize': 10},
    wedgeprops={'width': 0.55, 'edgecolor': 'white', 'linewidth': 2},  # doughnut gap
)
for at in autotexts:
    at.set_fontweight('bold')
    at.set_fontsize(9)

# Centre label
ax.text(0, 0, f"Total\n{sum(recruitments):,}", ha='center', va='center',
        fontsize=13, fontweight='bold', color='#2c3e50')

ax.set_title('Doughnut Chart – New Recruitments', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('d_doughnut_chart_recruitments.png', dpi=150)
plt.show()
print("Plot (d) saved: d_doughnut_chart_recruitments.png")

ibm_data   = df[df['Company'] == 'IBM']['Recruitments'].values[0]
amdocs_data = df[df['Company'] == 'Amdocs']['Recruitments'].values[0]

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

ax1 = axes[0]
bar_colors = ['#2ecc71', '#e74c3c']
bars = ax1.bar(['IBM', 'Amdocs'], [ibm_data, amdocs_data],
               color=bar_colors, edgecolor='black', width=0.4)
for bar, val in zip(bars, [ibm_data, amdocs_data]):
    ax1.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 50,
             str(val), ha='center', fontsize=12, fontweight='bold')
ax1.set_title('IBM vs Amdocs – Bar Chart', fontsize=13, fontweight='bold')
ax1.set_ylabel('Number of Recruitments')
ax1.set_ylim(0, max(ibm_data, amdocs_data) + 500)
ax1.grid(axis='y', linestyle='--', alpha=0.6)

ax2 = axes[1]
ax2.pie(
    [ibm_data, amdocs_data],
    labels=['IBM', 'Amdocs'],
    autopct='%1.1f%%',
    colors=bar_colors,
    explode=(0.05, 0.05),
    shadow=True,
    startangle=90,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 2},
)
ax2.set_title('IBM vs Amdocs – Pie Chart', fontsize=13, fontweight='bold')

plt.suptitle('Comparison: IBM & Amdocs New Recruitments',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('e_ibm_vs_amdocs.png', dpi=150)
plt.show()
print("Plot (e) saved: e_ibm_vs_amdocs.png")