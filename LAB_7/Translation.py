import cv2
import numpy as np

# Load the image
image = cv2.imread('LAB_7/cat.jpg')

# Get the dimensions of the image
(h, w) = image.shape[:2]

# Define the center of the image
center = (w // 2, h // 2)

# Rotation
angle = 45  # Rotate by 45 degrees
scale = 1.0  # No scaling during rotation
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# Scaling
scale_x = 1.5  # Scale by 1.5 times along the x-axis
scale_y = 1.5  # Scale by 1.5 times along the y-axis
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

# Translation
tx = 100  # Translate by 100 pixels along the x-axis
ty = 50  # Translate by 50 pixels along the y-axis
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, translation_matrix, (w, h))

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
