import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv('SEIP_data.csv')

# 2. Apply filters
reduced_df = df[
    (df['mips_obstype'] == 0) & 
    (df['Teff'] > 3930) & 
    (df['Teff'] < 5380) & 
    (df['logg'] > 3.8)
].copy()

total_k_stars = len(reduced_df)

# 3. Create Kiel diagram (log g vs Teff) plot
fig, ax = plt.subplots(figsize=(10, 6.5))

scatter = ax.scatter(
    reduced_df['Teff'], 
    reduced_df['logg'], 
    c=reduced_df['Teff'], 
    cmap='Oranges_r', 
    s=60, 
    edgecolors='black', 
    linewidths=0.6, 
    alpha=0.85,
    zorder=3
)

# Standard astronomical convention: Hotter stars on the left
ax.invert_xaxis()

# 4. Labels and annotations
ax.set_xlabel('Effective Temperature $T_{eff}$ (K)', fontsize=12, fontweight='bold')
ax.set_ylabel('Surface Gravity $\log(g)$ ($cm/s^2$)', fontsize=12, fontweight='bold')
ax.set_title('Isolated Galactic Main-Sequence K-Dwarf Stars', fontsize=14, fontweight='bold', pad=15)

# Highlight total count in an annotation box
bbox_props = dict(boxstyle="round,pad=0.5", facecolor="#FFF8DC", edgecolor="#D2691E", lw=1.5)
ax.text(
    0.03, 0.93, 
    f'Filtered Population\nTotal Main-Sequence K-Stars: {total_k_stars}', 
    transform=ax.transAxes, 
    fontsize=11, 
    fontweight='bold', 
    verticalalignment='top', 
    bbox=bbox_props,
    zorder=4
)

# Reference boundary lines
ax.axhline(3.8, color='crimson', linestyle='--', linewidth=1.2, label='log(g) Cutoff (> 3.8)')
ax.axvline(3930, color='darkorange', linestyle=':', linewidth=1.2, label='K-Type Bounds (3930K - 5380K)')
ax.axvline(5380, color='darkorange', linestyle=':', linewidth=1.2)

# Colorbar & Grid
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Effective Temperature $T_{eff}$ (K)', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5, zorder=1)
ax.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.9)

plt.tight_layout()
plt.show()