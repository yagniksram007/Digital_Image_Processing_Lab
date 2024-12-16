import cv2
import numpy as np

# Load the image
image = cv2.imread('CLASS_PROBLEMS/Images/Flower.jpeg')

# Convert the image to a negative image
negative_image = cv2.bitwise_not(image)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
