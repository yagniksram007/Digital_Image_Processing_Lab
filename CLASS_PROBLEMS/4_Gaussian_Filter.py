# Gaussian Filter

import cv2
import matplotlib.pyplot as plt

# Load an HD image and resize if necessary (replace 'image.jpg' with your image path)
image = cv2.imread('CLASS_PROBLEMS/Images/Flower.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format
image_rgb = cv2.resize(image_rgb, (720, 1080))

# Convert RGB to Grayscale
grayscale_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Apply Gaussian filters with different kernel sizes
gaussian_filtered_3x3 = cv2.GaussianBlur(grayscale_image, (3, 3), 0)
gaussian_filtered_5x5 = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

# Display the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(grayscale_image, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gaussian_filtered_3x3, cmap='gray')
plt.title("Gaussian Filter (3x3)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(gaussian_filtered_5x5, cmap='gray')
plt.title("Gaussian Filter (5x5)")
plt.axis("off")

plt.show()
