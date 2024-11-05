# Convert RGB to grayscale with the same HD sides(1080 x 720) and apply the filter 2 x 2 and 3 x 3

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an HD image (replace 'image.jpg' with your image path)
image = cv2.imread('CLASS_PROBLEMS/Images/Sky.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Resize the image to 1080x720 if necessary
image_rgb = cv2.resize(image_rgb, (720, 1080))

# Convert RGB to Grayscale manually
def rgb_to_grayscale(image):
    height, width, _ = image.shape
    grayscale_image = np.zeros((height, width), dtype=np.uint8)
    
    for i in range(height):
        for j in range(width):
            r, g, b = image[i, j]
            grayscale_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            grayscale_image[i, j] = grayscale_value

    return grayscale_image

# Apply average filter of size NxN
def apply_average_filter(image, filter_size):
    height, width = image.shape
    filtered_image = np.zeros((height, width), dtype=np.uint8)
    pad = filter_size // 2
    padded_image = np.pad(image, ((pad, pad), (pad, pad)), mode='constant', constant_values=0)

    for i in range(height):
        for j in range(width):
            neighborhood = padded_image[i:i+filter_size, j:j+filter_size]
            avg_value = np.sum(neighborhood) / (filter_size * filter_size)
            filtered_image[i, j] = int(avg_value)

    return filtered_image

# Convert the image to grayscale
grayscale_image = rgb_to_grayscale(image_rgb)

# Apply 2x2 and 3x3 average filters
filtered_image_2x2 = apply_average_filter(grayscale_image, 2)
filtered_image_3x3 = apply_average_filter(grayscale_image, 3)

# Plot the original grayscale and filtered images
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
