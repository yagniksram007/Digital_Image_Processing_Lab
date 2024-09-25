from PIL import Image

def crop_and_paste(crop_image_path, paste_image_path, crop_box):
    crop_img = Image.open(crop_image_path)
    paste_img = Image.open(paste_image_path)

    # Crop the specified area
    cropped_person = crop_img.crop(crop_box)

    # Calculate paste position for centering
    cropped_width = crop_box[2] - crop_box[0]  # Right - Left
    cropped_height = crop_box[3] - crop_box[1]  # Lower - Upper
    
    background_width = paste_img.width
    background_height = paste_img.height

    paste_x = (background_width - cropped_width) // 2
    paste_y = (background_height - cropped_height) // 2

    # Paste the cropped image onto the second image
    paste_img.paste(cropped_person, (paste_x, paste_y))

    # Save or show the resulting image
    paste_img.show()  # You can also use paste_img.save('output.jpg')

# Load image
crop_image_path = 'LAB_2/peter.jpg'  # Image path
paste_image_path = 'LAB_2/white.jpg'  # Background image path
crop_box = (100, 0, 1200, 600)  # Left, up, right, down

crop_and_paste(crop_image_path, paste_image_path, crop_box)
