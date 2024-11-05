# Take a HD image where atleast of 3 layers of RGB are present. Apply avg of 2 x 2, 3 x 3 filter and display the final image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an HD image (replace 'image.jpg' with your image path)
image = cv2.imread('CLASS_PROBLEMS/Images/Flower.jpeg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Convert image to a numpy array
image_array = np.array(image_rgb)

# Function to apply average filter of size NxN
def apply_average_filter(image, filter_size):
    # Get dimensions of the image
    height, width, channels = image.shape
    # Create a blank image to store the filtered result
    filtered_image = np.zeros((height, width, channels), dtype=np.uint8)
    
    # Define padding based on filter size
    pad = filter_size // 2

    # Pad the original image to handle border pixels
    padded_image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode='constant', constant_values=0)

    # Iterate over each pixel in the original image
    for i in range(height):
        for j in range(width):
            # For each pixel, extract the NxN neighborhood
            for c in range(channels):
                # Compute the sum of the neighborhood pixels
                neighborhood = padded_image[i:i+filter_size, j:j+filter_size, c]
                avg_value = np.sum(neighborhood) / (filter_size * filter_size)
                # Assign the average value to the corresponding pixel in the output image
                filtered_image[i, j, c] = int(avg_value)

    return filtered_image

# Apply 2x2 and 3x3 average filters
filtered_image_2x2 = apply_average_filter(image_array, 2)
filtered_image_3x3 = apply_average_filter(image_array, 3)

# Plot the original and filtered images
plt.figure(figsize=(15, 10))

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(filtered_image_2x2)
plt.title("2x2 Average Filter")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(filtered_image_3x3)
plt.title("3x3 Average Filter")
plt.axis("off")

plt.show()
