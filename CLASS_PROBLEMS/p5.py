import cv2
import numpy as np

# Load the image
image = cv2.imread('CLASS_PROBLEMS/Images/Flower.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Split the image into R, G, and B components
B, G, R = cv2.split(image)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Red Component', R)
cv2.imshow('Green Component', G)
cv2.imshow('Blue Component', B)
cv2.waitKey(0)
cv2.destroyAllWindows()
