import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the digital image
image_path = "LAB_3\low_contrast_image.png"  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image. Check the path.")
    exit()

# Convert image from BGR to RGB (for displaying with Matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert image to grayscale for processing
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Enhance the contrast using Histogram Equalization
enhanced_image = cv2.equalizeHist(gray_image)

# Segment the image using Otsu's Thresholding
_, segmented_image = cv2.threshold(enhanced_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the original, enhanced, and segmented images
plt.figure(figsize=(12, 8))

# Original grayscale image
plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

# Enhanced image
plt.subplot(1, 3, 2)
plt.imshow(enhanced_image, cmap="gray")
plt.title("Enhanced Image (Histogram Equalization)")
plt.axis("off")

# Segmented image
plt.subplot(1, 3, 3)
plt.imshow(segmented_image, cmap="gray")
plt.title("Segmented Image (Otsu's Thresholding)")
plt.axis("off")

# Show the plots
plt.tight_layout()
plt.show()
