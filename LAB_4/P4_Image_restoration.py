# Question: Demonstate image restoration using spatial or frequency domain

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('LAB_4/noisy_dog.jpg', 0)

# Spatial Domain Example: Gaussian Filter
spatial_filtered = cv2.GaussianBlur(image, (5, 5), 0)

# Frequency Domain Example
# Step 1: Fourier Transform
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

# Step 2: Create a mask (low-pass filter)
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols), np.uint8)
r = 30  # Radius of the mask
cv2.circle(mask, (ccol, crow), r, 1, thickness=-1)

# Step 3: Apply the mask
fshift_filtered = fshift * mask

# Step 4: Inverse Fourier Transform
f_ishift = np.fft.ifftshift(fshift_filtered)
image_restored = np.fft.ifft2(f_ishift)
image_restored = np.abs(image_restored)

# Display the results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Noisy Image')
plt.subplot(1, 3, 2), plt.imshow(spatial_filtered, cmap='gray'), plt.title('Spatial Filtered')
plt.subplot(1, 3, 3), plt.imshow(image_restored, cmap='gray'), plt.title('Frequency Filtered')
plt.show()
