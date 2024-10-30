import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Define a structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Subtract the eroded image from the original
erosion_difference = cv2.subtract(image, eroded_image)

# Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Subtract the dilated image from the original
dilation_difference = cv2.subtract(image, dilated_image)

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Erosion Difference')
plt.imshow(erosion_difference, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Dilation Difference')
plt.imshow(dilation_difference, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
