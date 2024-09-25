from PIL import Image

def mask_image(input_image_path, output_image_path, background_color=(0, 255, 0)):
    # Open the input image
    img = Image.open(input_image_path).convert("RGBA")
    width, height = img.size

    # Create a new image for the masked output
    masked_img = Image.new("RGBA", (width, height))

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            current_pixel = img.getpixel((x, y))

            # Check if the pixel matches the background color
            if current_pixel[:3] == background_color:
                # Set to transparent if it matches the background color
                masked_img.putpixel((x, y), (0, 0, 0, 0))  # Transparent
            else:
                # Keep the original pixel
                masked_img.putpixel((x, y), current_pixel)

    # Save or show the resulting masked image
    masked_img.save(output_image_path)
    masked_img.show()

# Example usage
input_image_path = 'LAB_2/peter.jpg'  # Path to the original image
output_image_path = 'LAB_2/masked_image.png'  # Path to save the masked output

mask_image(input_image_path, output_image_path)
