import numpy as np
import pandas as pd
import cv2

image=cv2.imread('paris.jpg', cv2.IMREAD_GRAYSCALE)
image=image.astype(np.uint8)



cv2.imshow('test',image)
cv2.waitKey(0)

def medianfilter(image,kernel_size=3):
    height,width=image.shape
    pad_size=kernel_size//2
    
    padded_image=np.pad(image,pad_size,mode='constant',constant_values=0)
    filtered_image = np.zeros_like(image)
    
    for i in range(height):
        for j in range(width):
            window=padded_image[i:i+kernel_size,j:j+kernel_size]
            
            median_values=np.median(window)
            filtered_image[i,j]=median_values
            
    return filtered_image

new_image=medianfilter(image,3)

cv2.imshow('filterd image',new_image)
cv2.waitKey(0)

combined_image = cv2.hconcat([image, new_image])  
cv2.imshow('old vs new',combined_image)   
cv2.waitKey(0)           