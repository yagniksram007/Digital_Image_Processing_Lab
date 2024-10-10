import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to display original and processed images
def display_images(original, enhanced, hd_image):
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.title("Original Low-Contrast Image")
    plt.imshow(original, cmap='gray')
    
    plt.subplot(1, 3, 2)
    plt.title("Enhanced Contrast Image")
    plt.imshow(enhanced, cmap='gray')
    
    plt.subplot(1, 3, 3)
    plt.title("HD Image (Upscaled)")
    plt.imshow(hd_image, cmap='gray')
    
    plt.show()

# Step 1: Load the low-contrast 2D image
image = cv2.imread('LAB 3/low_contrast_image.png', cv2.IMREAD_GRAYSCALE)

# Step 2: Contrast Enhancement using CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_image = clahe.apply(image)

# Step 3: Noise Reduction (Optional)
denoised_image = cv2.fastNlMeansDenoising(enhanced_image, None, 30, 7, 21)

# Step 4: Upscale the image to HD resolution (using interpolation)
scale_percent = 200  # Upscale by 200%
width = int(denoised_image.shape[1] * scale_percent / 100)
height = int(denoised_image.shape[0] * scale_percent / 100)
hd_image = cv2.resize(denoised_image, (width, height), interpolation=cv2.INTER_CUBIC)

# Display the images: Original, Enhanced, and HD Image
display_images(image, enhanced_image, hd_image)
