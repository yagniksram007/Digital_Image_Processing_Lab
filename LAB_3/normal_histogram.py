import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to display images
def display_images(original, enhanced, segmented):
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(original, cmap='gray')
    
    plt.subplot(1, 3, 2)
    plt.title("Enhanced Image (Histogram Equalization)")
    plt.imshow(enhanced, cmap='gray')
    
    plt.subplot(1, 3, 3)
    plt.title("Segmented Image (Thresholding)")
    plt.imshow(segmented, cmap='gray')
    
    plt.show()

# Load the low-contrast 2D image
image = cv2.imread('LAB 3/low_contrast_image.png', cv2.IMREAD_GRAYSCALE)

# Step 1: Enhancing the image using Histogram Equalization
enhanced_image = cv2.equalizeHist(image)

# Step 2: Segmenting the enhanced image using thresholding
_, segmented_image = cv2.threshold(enhanced_image, 128, 255, cv2.THRESH_BINARY)

# Display the images: Original, Enhanced, and Segmented
display_images(image, enhanced_image, segmented_image)
