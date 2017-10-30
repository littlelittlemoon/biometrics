#-*- coding: UTF-8 -*- 
import os
import numpy as np
from scipy import signal
from PIL import Image
from PIL import ImageEnhance
os.chdir('./picture')

def imageEnhanceProcess(image):
    original_image_array = np.asarray(image)
    print('original image array', original_image_array)
    image.show()
    enhance_type = ['Contrast', 'Brightness', 'Sharpness', 'Color']
    process_type = 'Contrast'
    accuracy = 1.0
    enhancer = ImageEnhance.Contrast(image)
    while (True):
        process_type = str(raw_input("Please input the enhance type you want to do on the image.Choose one of them: Contrast, Brightness, Sharpness, Color: "))
        print('process_type = ', process_type)
        if (process_type in enhance_type):
            break
    while (True):
        accuracy = float(raw_input("Please input accuracy. such as :1.0 or 2.0 "))
        print('accuracy = ', accuracy)
        if(not(accuracy == 0.0)):
            break
    if (process_type == 'Contrast'):
        enhancer = ImageEnhance.Contrast(image)
    elif (process_type == 'Brightness'):
        enhancer = ImageEnhance.Brightness(image)
    elif (process_type == 'Sharpness'):
        enhancer = ImageEnhance.Sharpness(image)
    else:
        enhancer = ImageEnhance.Color(image)
    enhanced_image = enhancer.enhance(accuracy)
    enhanced_image_array = np.asarray(enhanced_image)
    print('enhanced image array', enhanced_image_array)
    enhanced_image.show()
    enhanced_image.save('out.jpg')

img = Image.open('lena.png')
print(img.format, img.size , img.mode)
imageEnhanceProcess(img)

    
