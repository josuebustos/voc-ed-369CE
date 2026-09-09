import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import Cutout2D
from astropy.coordinates import SkyCoord
import astropy.units as u

# 1. Target star celestial coordinates from SEIP catalog
# Star ID: SSTSL2 J012412.12-741735.2
ra_deg = 21.050533
dec_deg = -74.293111

fits_filename = 'SPITZER_I1_22839808_0000_6_E8143254_maic.fits'  # Replace with your local FITS file path

# 2. Open FITS file and inspect header
with fits.open(fits_filename) as hdul:
    hdul.info()  # Print summary of HDU extensions
    
    # Extract image data and header (typically HDU 0)
    data = hdul[0].data
    header = hdul[0].header

    # Print header metadata
    print("\n--- FITS Header Metadata ---")
    print("TELESCOP:", header.get('TELESCOP', 'N/A'))
    print("INSTRUME:", header.get('INSTRUME', 'N/A'))
    print("NAXIS1 x NAXIS2:", header.get('NAXIS1'), "x", header.get('NAXIS2'))

    # 3. Create World Coordinate System (WCS) object
    wcs = WCS(header)

    # 4. Convert Target On-Sky Coordinates (RA, Dec) to Pixel Coordinates (X, Y)
    target_coord = SkyCoord(ra=ra_deg*u.deg, dec=dec_deg*u.deg, frame='icrs')
    x_pixel, y_pixel = wcs.world_to_pixel(target_coord)

    print(f"\nTarget Star Coordinates: RA={ra_deg}°, Dec={dec_deg}°")
    print(f"Mapped Pixel Coordinates: X={x_pixel:.2f}, Y={y_pixel:.2f}")

    # 5. Crop a 30x30 pixel box centered on the target star
    crop_size = (30, 30)  # (nY, nX) pixels
    cutout = Cutout2D(data, position=(x_pixel, y_pixel), size=crop_size, wcs=wcs)

# 6. Plot and Display the Cropped Star Image
plt.figure(figsize=(6, 6))

# Plot cutout data using its embedded cutout WCS for coordinate axes
ax = plt.subplot(projection=cutout.wcs)
im = ax.imshow(cutout.data, origin='lower', cmap='viridis', vmin=np.percentile(cutout.data, 5), vmax=np.percentile(cutout.data, 98))

# Annotations & Labeling
ax.scatter(cutout.input_position_cutout[0], cutout.input_position_cutout[1], 
           s=100, facecolors='none', edgecolors='red', linewidths=1.5, label='SSTSL2 J012412.12-741735.2')

ax.set_xlabel('Right Ascension (J2000)')
ax.set_ylabel('Declination (J2000)')
ax.set_title('30x30 Pixel Crop: SSTSL2 J012412.12-741735.2')
plt.colorbar(im, label='Flux Density (MJy/sr)')
plt.legend(loc='upper right')

plt.tight_layout()
plt.savefig('cropped_star_30x30.png', dpi=300)
plt.show()