import cv2
import numpy as np

# Load the image
image = cv2.imread('CLASS_PROBLEMS/Images/Flower.jpeg', cv2.IMREAD_GRAYSCALE)

# Linear Transformation
alpha = 1.5  # Simple contrast control
beta = 50    # Simple brightness control
linear_transformed = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Gamma Transformation
gamma = 2.0
gamma_corrected = np.array(255 * (image / 255) ** gamma, dtype='uint8')

# Logarithmic Transformation
c = 255 / np.log(1 + np.max(image))
log_transformed = c * (np.log(image + 1))
log_transformed = np.array(log_transformed, dtype='uint8')

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Linear Transformed Image', linear_transformed)
cv2.imshow('Gamma Corrected Image', gamma_corrected)
cv2.imshow('Logarithmic Transformed Image', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
