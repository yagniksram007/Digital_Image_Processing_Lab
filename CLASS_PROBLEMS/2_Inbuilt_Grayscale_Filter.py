# Convert RGB to grayscale with the same HD sides(1080 x 720) and apply the filter 2 x 2 and 3 x 3

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an HD image (replace 'image.jpg' with your image path)
image = cv2.imread('CLASS_PROBLEMS/Images/Sky.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format

# Resize the image to 1080x720 if necessary
image_rgb = cv2.resize(image_rgb, (720, 1080))

# Convert RGB to Grayscale using built-in OpenCV function
grayscale_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Apply 2x2 and 3x3 average filters using OpenCV's blur function
filtered_image_2x2 = cv2.blur(grayscale_image, (2, 2))
filtered_image_3x3 = cv2.blur(grayscale_image, (3, 3))

# Display the results
plt.figure(figsize=(15, 10))

plt.subplot(1, 3, 1)
plt.imshow(grayscale_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(filtered_image_2x2, cmap='gray')
plt.title("2x2 Average Filter")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(filtered_image_3x3, cmap='gray')
plt.title("3x3 Average Filter")
plt.axis("off")

plt.show()
