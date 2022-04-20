# -*- coding: utf-8 -*-
import cv2
import numpy as np
import pytesseract
import os
#Current Working Directory
cwd = os.getcwd()
#print(cwd)
#workflow_Excel_path = os.path.join(cwd, "Workflow.xlsx")

tessdata_dir_config = '--tessdata-dir'+'"'+os.path.join(cwd, "Tesseract-OCR\\tessdata")+'"';
pytesseract.pytesseract.tesseract_cmd = os.path.join(cwd, "Tesseract-OCR\\tesseract.exe")



imagePath = "C:\\Users\\manivel.muthusamy\\Desktop\\pdfs-digital\\checkForImageIntensity\\SOA 18.03.2019 - Copy_Page_1.png"

img = cv2.imread(imagePath,0)
img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

# Apply blur to smooth out the edges
#img = cv2.GaussianBlur(img, (5, 5), 0)
img3 = cv2.bilateralFilter(img,9,75,75)
       
# Apply threshold to get image with only b&w (binarization)
ret, thresh1 = cv2.threshold(img3, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)      
    
    
# Save the filtered image in the output directory
save_path = "C:\\Users\\manivel.muthusamy\\Desktop\\pdfs-digital\\checkForImageIntensity\\SOA 18.03.2019 - Copy_Page_1-res.jpg"
cv2.imwrite(save_path, thresh1)

# Recognize text with tesseract for python
result = pytesseract.image_to_string(img, lang="eng")
print(result)




