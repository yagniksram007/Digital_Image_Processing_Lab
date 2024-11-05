# Spoil the image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an HD image 
image = cv2.imread('CLASS_PROBLEMS/Images/Sky.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format
image_rgb = cv2.resize(image_rgb, (720, 1080))

# Function to add Gaussian noise
def add_gaussian_noise(image, mean=0, stddev=25):
    # Generate Gaussian noise
    noise = np.random.normal(mean, stddev, image.shape)
    noise = noise.reshape(image.shape)
    
    # Add noise to the image and clip values to maintain valid pixel range
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)  # Keep pixel values within [0, 255]
    
    return noisy_image.astype(np.uint8)

# Spoil the image by adding Gaussian noise
spoiled_image = add_gaussian_noise(image_rgb, mean=0, stddev=30)

# Display the original and spoiled images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(spoiled_image)
plt.title("Spoiled Image with Gaussian Noise")
plt.axis("off")

plt.show()
