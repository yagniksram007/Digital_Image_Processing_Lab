# Quesion 5: Read an image, first apply erosion to the image and then subtract the result from the original. Demonstrate the difference in the edge image if you use dilation instead of erision

#pip install opencv-python

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('anime.jpg', cv2.IMREAD_GRAYSCALE)

# Define the kernel for erosion and dilation
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Subtract the eroded image from the original
subtracted_image = cv2.subtract(image, eroded_image)

# Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Subtract the dilated image from the original

# Display the results
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(2, 2, 2)
plt.title('Eroded Image')
plt.imshow(eroded_image, cmap='gray')

plt.subplot(2, 2, 3)
plt.title('Subtracted (Erosion)')
plt.imshow(subtracted_image, cmap='gray')

plt.subplot(2, 2, 4)
plt.title('Subtracted (Dilation)')
plt.imshow(dilated_image, cmap='gray')

plt.tight_layout()
plt.show()
