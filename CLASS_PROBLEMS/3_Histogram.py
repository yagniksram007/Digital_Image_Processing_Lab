import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image using OpenCV
image = cv2.imread('CLASS_PROBLEMS/Images/Flower.jpeg', cv2.IMREAD_COLOR)

# Convert the image to RGB (OpenCV loads images in BGR format by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create a figure for the bar plot
plt.figure(figsize=(10, 6))

# Initialize the number of bins (256 for pixel values 0-255)
bins = 256

# Create a histogram for each color channel and plot bars
colors = ('r', 'g', 'b')  # Red, Green, Blue channels
for i, color in enumerate(colors):
    hist = cv2.calcHist([image_rgb], [i], None, [bins], [0, 256])
    hist = hist.flatten()  # Flatten the histogram array
    
    # Create bar plot for each channel
    plt.bar(np.arange(bins), hist, color=color, alpha=0.7, label=f'{color.upper()} channel')

# Add labels and title
plt.title('RGB Histogram')
plt.xlabel('Pixel Intensity Value')
plt.ylabel('Frequency')
plt.legend()

# Display the histogram
plt.show()
