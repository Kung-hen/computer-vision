# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:20:12 2022

@author: peter
"""

import cv2
import numpy as np

class Disparity_Map():
    def __init__(self, path1, path2):
        self.path_R = path2
        self.img_L = cv2.imread(path1)
        self.img_R = cv2.imread(path2)
        # img_L = cv2.resize(img_L, (255,173))
        # img_R = cv2.resize(img_R, (255,173))
        self.img_L_gray = cv2.cvtColor(self.img_L, cv2.COLOR_BGR2GRAY)
        self.img_R_gray = cv2.cvtColor(self.img_R, cv2.COLOR_BGR2GRAY)
        self.fx = 4019.284
        self.baseline = 342.789
        self.doffs = 279.184
        
    def Stereo_Map(self):
        stereo = cv2.StereoBM_create(numDisparities=256, blockSize=25)
        
        self.disparity = stereo.compute(self.img_L_gray, self.img_R_gray)
        self.disparity = cv2.normalize(self.disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        
        return self.disparity
    def draw_circle(self):
        
        def OnMouseAction(event, x, y, flags, param):
            global x_new, y_new
            if event == cv2.EVENT_LBUTTONDOWN:
            
                img = cv2.cvtColor(np.copy(self.disparity),cv2.COLOR_GRAY2BGR)
                img_dot = cv2.cvtColor(np.copy(self.disparity) ,cv2.COLOR_GRAY2BGR)
                cv2.circle(img_dot,(x,y),10,(255,0,0),-1)
                x_new = x
                y_new = y
                depth = self.baseline * self.fx / (img[y][x][0] + self.doffs)
        
                img_dot = cv2.imread(self.path_R)
                z=img[y][x][0]
                
                if img[y][x][0] != 0:       
                    cv2.circle(img_dot,(x-z,y),25,(0,255,0),-1)
                
                
                cv2.namedWindow('img_R',cv2.WINDOW_NORMAL)
                cv2.resizeWindow("img_R", int(img_dot.shape[1]/4), int(img_dot.shape[0]/4))
                cv2.imshow('img_R', img_dot)           
                cv2.waitKey(0)
                
        img_L = self.img_L
        img_R = cv2.imread(self.path_R)
        disparity = self.disparity
        
        cv2.namedWindow('img_L',cv2.WINDOW_NORMAL)
        cv2.resizeWindow("img_L", int(img_L.shape[1]/4), int(img_L.shape[0]/4))
        cv2.setMouseCallback('img_L',OnMouseAction)
        cv2.imshow("img_L",img_L)
        cv2.namedWindow('img_R',cv2.WINDOW_NORMAL)
        cv2.resizeWindow("img_R", int(img_L.shape[1]/4), int(img_L.shape[0]/4))
        cv2.imshow("img_R",img_R)
        cv2.namedWindow('img_disparity',cv2.WINDOW_NORMAL)
        cv2.resizeWindow("img_disparity", int(img_L.shape[1]/4), int(img_L.shape[0]/4))
        cv2.imshow("img_disparity", disparity)
        cv2.waitKey(0)
# path_L = "C:/Program Files (x86)/HW2_N16111756_V1/Dataset_OpenCvDl_Hw2/Dataset_OpenCvDl_Hw2/Q4_Image/imL.png"
# path_R = "C:/Program Files (x86)/HW2_N16111756_V1/Dataset_OpenCvDl_Hw2/Dataset_OpenCvDl_Hw2/Q4_Image/imR.png"
    
# Disparity_Map = Disparity_Map(path_L, path_R)
# disparity = Disparity_Map.Stereo_Map()
# Disparity_Map.draw_circle()    
    