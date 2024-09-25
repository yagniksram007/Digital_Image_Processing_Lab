import cv2

image_path = 'LAB_1/Miguel.jpeg'
image = cv2.imread(image_path)
if image is None:
    print("Error: Unable to load image.")
    exit()

print(image.shape)
height, width, _ = image.shape

center_y, center_x = height // 2, width // 2

top_left = image[0:center_y, 0:center_x]
top_right = image[0:center_y, center_x:]
bottom_left = image[center_y:, 0:center_x]
bottom_right = image[center_y:, center_x:]

cv2.imshow('Top Left', top_left)
cv2.imshow('Top Right', top_right)
cv2.imshow('Bottom Left', bottom_left)
cv2.imshow('Bottom Right', bottom_right)
cv2.waitKey(0)
cv2.destroyAllWindows()
