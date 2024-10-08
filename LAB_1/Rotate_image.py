# pip install Pillow

from PIL import Image

# Load the image
image_path = 'LAB_1/Miguel.jpeg' 
image = Image.open(image_path)

# Rotate the image by a specified angle (e.g., 90 degrees)
rotated_image = image.rotate(90, expand=True)

# Save the rotated image
rotated_image.save('LAB_1/rotated_image.jpg')

# Display the rotated image
rotated_image.show()
