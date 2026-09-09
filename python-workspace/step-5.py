import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Load dataset and select target star (e.g., SSTSL2 J224656.98+602924.5)
df = pd.read_csv('SEIP_data.csv')
star = df.iloc[3]  # Teff in catalog = 3820.3 K

# Define Wavelengths (micrometers)
wavelengths_um = np.array([1.235, 1.662, 2.159, 3.6, 4.5, 5.8, 8.0, 24.0])

# Extract Flux Densities (convert microJanskys to Janskys)
fluxes_ujy = np.array([
    star['j'], star['h'], star['k'],
    star['i1_f_ap2'], star['i2_f_ap2'], star['i3_f_ap2'], star['i4_f_ap2'], star['m1_f_psf']
])
fluxes_jy = fluxes_ujy / 1e6  # 1 Jy = 10^6 uJy

# -------------------------------------------------------------
# 2. Linear Model: y = m*x + b
# -------------------------------------------------------------
def line_func(x, m, b):
    return m * x + b

popt_line, _ = curve_fit(line_func, wavelengths_um, fluxes_jy)
m_fit, b_fit = popt_line

# -------------------------------------------------------------
# 3. Parabolic Model: y = a*x^2 + b*x + c
# -------------------------------------------------------------
def poly_func(x, a, b, c):
    return a * x**2 + b * x + c

popt_poly, _ = curve_fit(poly_func, wavelengths_um, fluxes_jy)
a_fit, b_poly_fit, c_fit = popt_poly

# -------------------------------------------------------------
# 4. Blackbody Model: Planck's Law
# -------------------------------------------------------------
# Physical Constants (SI Units)
h = 6.62607015e-34  # Planck constant (J s)
c = 2.99792458e8    # Speed of light (m/s)
k = 1.380649e-23    # Boltzmann constant (J/K)

def planck_jy(wave_um, T, N):
    wave_m = wave_um * 1e-6  # Convert um to meters
    # Planck radiance B_nu in W / (m^2 Hz sr)
    b_nu = (2 * h * c / (wave_m**3)) / (np.exp((h * c) / (wave_m * k * T)) - 1.0)
    # Convert W/(m^2 Hz sr) to Janskys (1 Jy = 1e-26 W/m^2/Hz) and scale by normalization N
    return N * b_nu * 1e26

# Fit Temperature (T) and Normalization factor (N)
popt_bb, _ = curve_fit(
    planck_jy, wavelengths_um, fluxes_jy, 
    p0=[4000, 1e-18], bounds=([1000, 1e-25], [15000, 1e-5])
)
T_fit, N_fit = popt_bb

# -------------------------------------------------------------
# Plotting Results
# -------------------------------------------------------------
x_fine = np.linspace(1.0, 25.0, 500)

plt.figure(figsize=(10, 6.5))
plt.scatter(wavelengths_um, fluxes_jy, color='black', s=60, label='Photometry Data (SEIP)', zorder=5)

# Plot Linear Fit
plt.plot(x_fine, line_func(x_fine, *popt_line), '--', color='tab:blue', 
         label=f'Line: $y = {m_fit:.4f}x + {b_fit:.4f}$')

# Plot Parabolic Fit
plt.plot(x_fine, poly_func(x_fine, *popt_poly), '-.', color='tab:green', 
         label=f'Parabola: $y = {a_fit:.4f}x^2 + {b_poly_fit:.4f}x + {c_fit:.4f}$')

# Plot Blackbody Fit
plt.plot(x_fine, planck_jy(x_fine, *popt_bb), '-', color='tab:red', linewidth=2, 
         label=f'Planck Blackbody: $T = {T_fit:.1f}\\,\\mathrm{{K}}$, $N = {N_fit:.2e}$')

# Axis Formatting
plt.xlabel('Wavelength $\\lambda$ ($\\mu\\mathrm{m}$)', fontsize=12)
plt.ylabel('Flux Density $F_\\nu$ (Jy)', fontsize=12)
plt.title(f'Stellar Photometry Model Fitting ($T_{{eff, catalog}} = {star["Teff"]:.1f}\\,\\mathrm{{K}}$)', fontsize=13)
plt.legend(fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------
# Log-Log SED Plot (plt.loglog)
# -------------------------------------------------------------
plt.figure(figsize=(10, 6.5))
plt.scatter(wavelengths_um, fluxes_jy, color='black', s=60, label='Photometry Data', zorder=5)
plt.loglog(x_fine, np.maximum(line_func(x_fine, *popt_line), 1e-6), '--', color='tab:blue', label='Line Fit')
plt.loglog(x_fine, np.maximum(poly_func(x_fine, *popt_poly), 1e-6), '-.', color='tab:green', label='Parabola Fit')
plt.loglog(x_fine, planck_jy(x_fine, *popt_bb), '-', color='tab:red', linewidth=2, label=f'Blackbody Fit ($T={T_fit:.1f}\\,\\mathrm{{K}}$)')

plt.xlabel('Wavelength $\\lambda$ ($\\mu\\mathrm{m}$)', fontsize=12)
plt.ylabel('Flux Density $F_\\nu$ (Jy)', fontsize=12)
plt.title('Spectral Energy Distribution (SED) - Log-Log Scale', fontsize=13)
plt.legend(fontsize=10)
plt.grid(True, which="both", linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()