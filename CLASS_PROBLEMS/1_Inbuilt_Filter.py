# Take a HD image where atleast of 3 layers of RGB are present. Apply avg of 2 x 2, 3 x 3 filter and display the final image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an HD image with RGB layers (replace 'image.jpg' with your image path)
image = cv2.imread('CLASS_PROBLEMS/Images/Flower.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Apply 2x2 average filter
kernel_2x2 = np.ones((2, 2), np.float32) / 4
filtered_2x2 = cv2.filter2D(image_rgb, -1, kernel_2x2)

# Apply 3x3 average filter
kernel_3x3 = np.ones((3, 3), np.float32) / 9
filtered_3x3 = cv2.filter2D(image_rgb, -1, kernel_3x3)

# Plot the original and filtered images
plt.figure(figsize=(15, 10))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(filtered_2x2)
plt.title("2x2 Average Filter")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(filtered_3x3)
plt.title("3x3 Average Filter")
plt.axis("off")

plt.show()
