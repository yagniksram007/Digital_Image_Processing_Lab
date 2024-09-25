def read_bmp(filename):
    with open(filename, 'rb') as f:
        # Read BMP header
        f.read(18)  # Skip to width and height
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        f.read(28)  # Skip the rest of the header
        pixels = []
        
        # Read pixel data
        for y in range(height):
            row = []
            for x in range(width):
                b = f.read(1)[0]   # Blue
                g = f.read(1)[0]   # Green
                r = f.read(1)[0]   # Red
                row.append((r, g, b))
            pixels.append(row)
        
        return width, height, pixels

def write_bmp(filename, width, height, pixels):
    with open(filename, 'wb') as f:
        # Write BMP header
        f.write(b'BM')
        f.write((54 + width * height * 3).to_bytes(4, 'little'))  # File size
        f.write(b'\x00\x00')  # Reserved
        f.write(b'\x00\x00')  # Reserved
        f.write(b'\x36\x00\x00\x00')  # Offset to start of pixel data
        f.write(b'\x28\x00\x00\x00')  # DIB header size
        f.write(width.to_bytes(4, 'little'))
        f.write(height.to_bytes(4, 'little'))
        f.write(b'\x01\x00')  # Number of color planes
        f.write(b'\x18\x00')  # Bits per pixel
        f.write(b'\x00\x00\x00\x00')  # Compression
        f.write((width * height * 3).to_bytes(4, 'little'))  # Size of raw bitmap data
        f.write(b'\x13\x0B\x00\x00')  # Horizontal resolution (pixels per meter)
        f.write(b'\x13\x0B\x00\x00')  # Vertical resolution (pixels per meter)
        f.write(b'\x00\x00\x00\x00')  # Colors in color table
        f.write(b'\x00\x00\x00\x00')  # Important color count
        
        # Write pixel data
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[y][x]
                f.write(bytes([b, g, r]))  # Write in BGR order

def process_image(image_path):
    # Read the BMP image
    width, height, pixels = read_bmp(image_path)

    # Reduce image size (2x2 pixels to 1x1 pixel)
    reduced_pixels = []
    for y in range(0, height, 2):
        new_row = []
        for x in range(0, width, 2):
            # Average the 2x2 block of pixels
            r = (pixels[y][x][0] + pixels[y][x + 1][0] + 
                 pixels[y + 1][x][0] + pixels[y + 1][x + 1][0]) // 4
            g = (pixels[y][x][1] + pixels[y][x + 1][1] + 
                 pixels[y + 1][x][1] + pixels[y + 1][x + 1][1]) // 4
            b = (pixels[y][x][2] + pixels[y][x + 1][2] + 
                 pixels[y + 1][x][2] + pixels[y + 1][x + 1][2]) // 4
            new_row.append((r, g, b))
        reduced_pixels.append(new_row)

    # Write the reduced image back to a file
    write_bmp('reduced_' + image_path, width // 2, height // 2, reduced_pixels)

# Example usage
process_image('LAB_2/flower.bmp')  # Ensure you use a BMP file
