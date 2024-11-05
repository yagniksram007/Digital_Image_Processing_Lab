import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('CLASS_PROBLEMS/Images/wolf.jpg', cv2.IMREAD_GRAYSCALE)  # Load in grayscale

# 1. Detecting Isolated Points using Laplacian Filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)
abs_laplacian = np.absolute(laplacian)
isolated_points = np.uint8(abs_laplacian)

# 2. Detecting Lines using Hough Line Transform
# Apply edge detection before line detection
edges_for_lines = cv2.Canny(image, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(edges_for_lines, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

# Create a copy of the original image to draw lines on
line_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green color for lines

# 3. Detecting Edges using Canny Edge Detection
edges = cv2.Canny(image, 100, 200)

# Display results
plt.figure(figsize=(15, 10))

# Original Image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis("off")

# Isolated Points (Laplacian Filter)
plt.subplot(2, 2, 2)
plt.imshow(isolated_points, cmap='gray')
plt.title("Isolated Points (Laplacian)")
plt.axis("off")

# Detected Lines (Hough Line Transform)
plt.subplot(2, 2, 3)
plt.imshow(line_image)
plt.title("Detected Lines (Hough Transform)")
plt.axis("off")

# Detected Edges (Canny)
plt.subplot(2, 2, 4)
plt.imshow(edges, cmap='gray')
plt.title("Detected Edges (Canny)")
plt.axis("off")

plt.show()
