from PIL import Image

def process_image(image_path):
    # Open the image
    img = Image.open('LAB_2/flower.jpg')

    # Split into RGB layers
    r, g, b = img.split()

    # Reduce image size (2x2 pixels to 1x1 pixel) using LANCZOS filter
    r = r.resize((r.width // 2, r.height // 2), Image.LANCZOS)
    g = g.resize((g.width // 2, g.height // 2), Image.LANCZOS)
    b = b.resize((b.width // 2, b.height // 2), Image.LANCZOS)

    # Merge the layers back
    reduced_img = Image.merge("RGB", (r, g, b))

    # Print the resulting image
    reduced_img.show()

# Example usage
process_image('LAB_2/flower.jpg') 
