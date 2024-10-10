# Question: Read an image and extract and display low level features such as edges, textures using filtering techniques

#pip install opencv-python
import cv2

# Function to apply Gaussian Filter
def apply_gaussian_filter(image, kernel_size=5, sigma=1.0):
    # Apply Gaussian Blur
    gaussian_filtered = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    return gaussian_filtered

# Function to apply Median Filter
def apply_median_filter(image, kernel_size=13):
    # Apply Median Filter
    median_filtered = cv2.medianBlur(image, kernel_size)
    return median_filtered

# Main function
def main():
    # Hard-coded image path
    image_path = 'LAB_2/flower.jpg'  # Change this to your image path
    
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("ERROR! Could not read the image.")
        return

    # Resize the image to a smaller size (e.g., 40% of the original)
    new_width = int(image.shape[1] * 0.4)
    new_height = int(image.shape[0] * 0.4)
    resized_image = cv2.resize(image, (new_width, new_height))

    # Apply Gaussian Filter
    gaussian_result = apply_gaussian_filter(resized_image, kernel_size=5, sigma=1.0)

    # Apply Median Filter
    median_result = apply_median_filter(resized_image, kernel_size=5)

    # Display the results
    cv2.imshow('Original Image (Resized)', resized_image)
    cv2.imshow('Gaussian Filtered Image', gaussian_result)
    cv2.imshow('Median Filtered Image', median_result)

    # Wait until a key is pressed, then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()