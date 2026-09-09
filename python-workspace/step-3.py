import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv('SEIP_data.csv')

# 2. Define function to bin Teff into Spectral Types
def get_spectral_type(teff):
    if pd.isna(teff):
        return None
    elif teff >= 30000:
        return 'O'
    elif teff >= 10000:
        return 'B'
    elif teff >= 7500:
        return 'A'
    elif teff >= 6000:
        return 'F'
    elif teff >= 5200:
        return 'G'
    elif teff >= 3700:
        return 'K'
    elif teff >= 2400:
        return 'M'
    else:
        return 'Late'

# Apply spectral classification
df['Spectral_Type'] = df['Teff'].apply(get_spectral_type)

# Filter for rows with complete data
plot_df = df.dropna(subset=['Spectral_Type', 'BP-RP', 'Gmag']).copy()

# 3. Define spectral order (Hot -> Cold) and Blue-to-Red color palette
spec_order = ['O', 'B', 'A', 'F', 'G', 'K', 'M']
color_map = {
    'O': '#0000FF',  # Blue
    'B': '#1E90FF',  # Light Blue
    'A': '#00FFFF',  # Cyan
    'F': '#00FF00',  # Green
    'G': '#FFD700',  # Yellow
    'K': '#FF8C00',  # Orange
    'M': '#FF0000'   # Red
}

# 4. Generate the plot
plt.figure(figsize=(10, 7))

for st in spec_order:
    sub = plot_df[plot_df['Spectral_Type'] == st]
    if not sub.empty:
        plt.scatter(
            sub['BP-RP'], 
            sub['Gmag'], 
            color=color_map[st], 
            label=f'Type {st} (N={len(sub)})', 
            s=35, 
            alpha=0.85,
            edgecolors='black',
            linewidths=0.5
        )

# 5. Styling and formatting
plt.gca().invert_yaxis()  # Invert y-axis (brighter stars at the top)
plt.xlabel('Color Index ($BP - RP$)', fontsize=12)
plt.ylabel('Apparent Magnitude ($G$)', fontsize=12)
plt.title('Gaia DR3 Color-Magnitude Diagram Grouped by Spectral Type ($T_{eff}$)', fontsize=13)
plt.legend(title='Spectral Type', loc='upper right', frameon=True)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()