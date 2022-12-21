# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:02:15 2022

@author: peter
"""
import cv2
import numpy as np
def Canny(path):
    img = cv2.imread(path)
    img = cv2.resize(img, None, fx = 0.5, fy = 0.5)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_canny = cv2.Canny(img_blurred, 100, 200)
    # cv2.imshow("img_canny", img_canny)
    contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    # print(len(contours))
    index = []
    
    for i in range(len(hierarchy[0])):
        if hierarchy[0][i][0] == -1 and hierarchy[0][i][1] == -1:
            continue
        j = 0
        index.append(i) 
        j += 1
    contours_new = [] 
    for i in range(len(index)):
        if index[i] == -1:
            break
        a = index[i]
        contours_new.append(contours[a]) 
    # print(len(contours_new))   
    for contour in contours_new:
        
        
        cv2.drawContours(img, contour, -1, (255, 255, 0), 1)
        
        
        # print(lens)
        
    count = int(len(contours_new) / 2)      
                  
    
    return img, count


# img1 = cv2.imread("C:\Program Files (x86)\HW2_N16111756_V1\Dataset_OpenCvDl_Hw2\Dataset_OpenCvDl_Hw2\Q1_Image\img1.jpg")    
# img1, count1 = Canny(img1)
# print("count1 =", count1)
# img2 = cv2.imread("C:\Program Files (x86)\HW2_N16111756_V1\Dataset_OpenCvDl_Hw2\Dataset_OpenCvDl_Hw2\Q1_Image\img2.jpg")
# img2, count2 = Canny(img2)
# print("count2 =", count2)

# cv2.imshow("img1_canny", img1)
# cv2.imshow("img2_canny", img2)
# cv2.waitKey(0)