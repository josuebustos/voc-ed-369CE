"""
Color-Magnitude Diagram (Gaia BP-RP vs. G)
Visualizes stellar evolutionary tracks by plotting color index against magnitude, colored by effective temperature.
"""

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('SEIP_data.csv')

# plt.figure(figsize=(8, 6))
# sc = plt.scatter(df['BP-RP'], df['Gmag'], c=df['Teff'], cmap='magma_r', s=25, alpha=0.8, edgecolors='none')
# plt.gca().invert_yaxis()  # Invert so brighter magnitudes are at the top
# plt.colorbar(sc, label='Effective Temperature Teff (K)')
# plt.xlabel('Color Index (BP - RP) [mag]')
# plt.ylabel('G Magnitude [mag]')
# plt.title('Gaia DR3 Color-Magnitude Diagram')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()


"""
All-Sky Galactic Coordinate Distribution
Maps target positions across the sky using a Mollweide projection of Galactic longitude ($l$) and latitude ($b$).
"""

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv("SEIP_data.csv")

# # Convert longitude to range (-180, 180) and convert degrees to radians for projection
# l_rad = np.radians(np.where(df["l"] > 180, df["l"] - 360, df["l"]))
# b_rad = np.radians(df["b"])

# plt.figure(figsize=(9, 5))
# ax = plt.subplot(111, projection="mollweide")
# sc = ax.scatter(l_rad, b_rad, c=df["Dist"], cmap="viridis", s=20, alpha=0.8)
# plt.colorbar(sc, label="Distance (pc)", orientation="horizontal", pad=0.08)
# ax.set_title("Galactic Coordinate Map (l, b)", pad=20)
# ax.grid(True, linestyle="--", alpha=0.5)
# plt.tight_layout()
# plt.show()

"""
Spitzer IRAC Photometric Flux Comparison
Compares flux density distributions across all four Spitzer IRAC infrared channels on a logarithmic scale.
"""
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('SEIP_data.csv')

# irac_cols = ['i1_f_ap2', 'i2_f_ap2', 'i3_f_ap2', 'i4_f_ap2']
# labels = ['3.6 μm (I1)', '4.5 μm (I2)', '5.8 μm (I3)', '8.0 μm (I4)']
# flux_data = [df[col].dropna() for col in irac_cols]

# plt.figure(figsize=(8, 5))
# plt.boxplot(flux_data, labels=labels, patch_artist=True, boxprops=dict(facecolor='lightskyblue', color='blue'))
# plt.yscale('log')
# plt.ylabel('Flux Density (μJy)')
# plt.title('Spitzer IRAC Aperture Flux Distribution')
# plt.grid(True, which='both', linestyle='--', alpha=0.4)
# plt.tight_layout()
# plt.show()

"""
Stellar Proper Motion Scatter Plot
Plots proper motion along Right Ascension (pmRA) versus Declination (pmDE), colored by stellar parallax.
"""

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('SEIP_data.csv')

# plt.figure(figsize=(7, 6))
# sc = plt.scatter(df['pmRA'], df['pmDE'], c=df['Plx'], cmap='plasma', s=30, alpha=0.85)
# plt.colorbar(sc, label='Parallax (mas)')
# plt.axhline(0, color='grey', linestyle='--', linewidth=0.8)
# plt.axvline(0, color='grey', linestyle='--', linewidth=0.8)
# plt.xlabel('Proper Motion RA pmRA (mas/yr)')
# plt.ylabel('Proper Motion Dec pmDE (mas/yr)')
# plt.title('Proper Motion Space')
# plt.grid(True, linestyle=':', alpha=0.6)
# plt.tight_layout()
# plt.show()

"""
Kiel Diagram ($T_{text{eff}}$ vs. log g$)
Plots effective temperature against surface gravity colored by metallicity ([Fe/H]) to inspect stellar populations.
"""

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('SEIP_data.csv')

# plt.figure(figsize=(7, 5))
# sc = plt.scatter(df['Teff'], df['logg'], c=df['[Fe/H]'], cmap='coolwarm', s=30, alpha=0.85)
# plt.gca().invert_xaxis()  # Hotter stars on the left
# plt.gca().invert_yaxis()  # Higher surface gravity towards bottom
# plt.colorbar(sc, label='Metallicity [Fe/H]')
# plt.xlabel('Effective Temperature Teff (K)')
# plt.ylabel('Surface Gravity log(g)')
# plt.title('Kiel Diagram')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()


"""
Equatorial Scatter Plot (RA vs. DEC colored by Distance)
Plots standard Right Ascension versus Declination positions, color-coded by source distance in parsecs.
"""

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('SEIP_data.csv')

# plt.figure(figsize=(8, 5))
# sc = plt.scatter(df['ra'], df['dec'], c=df['Dist'], cmap='plasma', s=30, alpha=0.85)
# plt.colorbar(sc, label='Distance (pc)')
# plt.xlabel('Right Ascension (RA) [deg]')
# plt.ylabel('Declination (DEC) [deg]')
# plt.title('Equatorial Coordinates Scatter Plot (RA vs DEC)')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()

"""
2D Hexbin Density Map
Bins celestial targets into hexagonal cells to highlight clusters and spatial density across sky coordinates.
"""

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('SEIP_data.csv')

# plt.figure(figsize=(8, 5))
# hb = plt.hexbin(df['ra'], df['dec'], gridsize=20, cmap='YlOrRd', mincnt=1)
# plt.colorbar(hb, label='Source Count')
# plt.xlabel('Right Ascension (RA) [deg]')
# plt.ylabel('Declination (DEC) [deg]')
# plt.title('2D Density Map of Targets (RA vs DEC)')
# plt.grid(True, linestyle=':', alpha=0.5)
# plt.tight_layout()
# plt.show()

"""
Separate RA and DEC Frequency Histograms
Creates side-by-side marginal distribution histograms for Right Ascension and Declination values.
"""

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("SEIP_data.csv")

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))

# ax1.hist(df["ra"], bins=20, color="skyblue", edgecolor="navy", alpha=0.7)
# ax1.set_xlabel("Right Ascension (RA) [deg]")
# ax1.set_ylabel("Count")
# ax1.set_title("Right Ascension Distribution")
# ax1.grid(True, linestyle="--", alpha=0.5)

# ax2.hist(df["dec"], bins=20, color="salmon", edgecolor="darkred", alpha=0.7)
# ax2.set_xlabel("Declination (DEC) [deg]")
# ax2.set_ylabel("Count")
# ax2.set_title("Declination Distribution")
# ax2.grid(True, linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.show()

"""
Proper Motion Vector Map (Quiver Plot on Sky Position)
Overlays proper motion vectors (pmRA, pmDE) as arrows on celestial coordinates (ra, dec), colored by apparent Gaia G magnitude.
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

df = pd.read_csv('SEIP_data.csv')

# Annotate figure explicitly to clear static type warnings
fig: Figure = plt.figure(figsize=(9, 6))

q = plt.quiver(
    df['ra'], df['dec'], 
    df['pmRA'], df['pmDE'], 
    df['Gmag'], 
    cmap='viridis', 
    scale=500, 
    width=0.003
)

plt.colorbar(q, label='G Magnitude [mag]')
plt.xlabel('Right Ascension (RA) [deg]')
plt.ylabel('Declination (DEC) [deg]')
plt.title('Proper Motion Vectors across Sky Position (RA, DEC)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()