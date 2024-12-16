# Question: Demonstrate enchancing and segmenting low contast 2d images

# Using CLAHE
import cv2
import numpy as np

# Load the image
image = cv2.imread('LAB_3\low_contrast_image.png', cv2.IMREAD_GRAYSCALE)

# Enhance the image using CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_image = clahe.apply(image)

# Segment the image using Otsu's thresholding
_, segmented_image = cv2.threshold(enhanced_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
