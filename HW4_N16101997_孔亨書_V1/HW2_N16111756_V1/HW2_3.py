# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:43:30 2022

@author: peter
"""

import cv2
import numpy as np
import HW2_2
class Augmented_Reality():
    def __init__(self, path, messenge):
        self.messenge = messenge
        self.img = cv2.imread(path)
        self.Camera = HW2_2.Camera_Calibration(path)
        _, self.corner = self.Camera.corner()
        self.mat, self.dist, self.v_rot, self.v_trans = self.Camera.Intrinsic()
        self.axis = np.float32([[3,0,0], [0,3,0], [0,0,3]]).reshape(-1,3)
        self.x = [[7, 5],
                 [4, 5],
                 [1, 5],
                 [7, 2],
                 [4, 2],
                 [1, 2]]
    def projection(self):
        # axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)
        # axis = np.float32([[3,0,0], [0,3,0], [0,0,3]]).reshape(-1,3)
        imgpts, jac = cv2.projectPoints(self.axis, np.array(self.v_rot), np.array(self.v_trans), self.mat, self.dist)
        # cv2.imshow("imgpts",imgpts)
        # cv2.waitKey(0)
        # imgpts = np.int32(imgpts).reshape(-1,2)
        
        cv2.line(self.img, tuple(self.corner[0].astype(np.int32).ravel()), tuple(imgpts[0].astype(np.int32).ravel()),(255,0,0),2)  #BGR
        cv2.line(self.img, tuple(self.corner[0].astype(np.int32).ravel()), tuple(imgpts[1].astype(np.int32).ravel()),(0,255,0),2)
        cv2.line(self.img, tuple(self.corner[0].astype(np.int32).ravel()), tuple(imgpts[2].astype(np.int32).ravel()),(0,0,255),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(self.img, 'X', tuple(imgpts[0].astype(np.int32).ravel()), font, 0.5, (255,0,0), 2, cv2.LINE_AA)
        cv2.putText(self.img, 'Y', tuple(imgpts[1].astype(np.int32).ravel()), font, 0.5, (0,255,0), 2, cv2.LINE_AA)
        cv2.putText(self.img, 'Z', tuple(imgpts[2].astype(np.int32).ravel()), font, 0.5, (0,0,255), 2, cv2.LINE_AA)
        
    def word_on_board(self):        
        fs = cv2.FileStorage('C:/Program Files (x86)/HW2_N16111756_V1/Dataset_OpenCvDl_Hw2/Dataset_OpenCvDl_Hw2/Q3_Image/Q2_lib/alphabet_lib_onboard.txt', cv2.FILE_STORAGE_READ)
        # ch = fs.getNode("K").mat()
        # print(ch)
        img_word = self.img.copy()
        
        
        self.projection()
        
        a = self.messenge
        # ch = np.zeros((((len(a),3,2,3))))
        start = np.zeros((5,3))
        end = np.zeros((5,3))
        for i in range(len(a)):
             b = a[i]
             # ch = np.append(ch,fs.getNode(f"{b}").mat())
             c = fs.getNode(f"{b}").mat()
             for j in range(len(c)):
                 for k in range(len(c[0])):
                      c[j][k][0] += self.x[i][0]
                      c[j][k][1] += self.x[i][1]
                      start[j] = c[j][0]
                      end[j] = c[j][1]
             start_point, _ =cv2.projectPoints(start, np.array(self.v_rot), np.array(self.v_trans), self.mat, self.dist)    
             end_point, _ =cv2.projectPoints(end, np.array(self.v_rot), np.array(self.v_trans), self.mat, self.dist) 
             cv2.line(img_word, tuple(start_point[0].astype(np.int32).ravel()), tuple(end_point[0].astype(np.int32).ravel()),(0,0,255),3)
             cv2.line(img_word, tuple(start_point[1].astype(np.int32).ravel()), tuple(end_point[1].astype(np.int32).ravel()),(0,0,255),3)
             cv2.line(img_word, tuple(start_point[2].astype(np.int32).ravel()), tuple(end_point[2].astype(np.int32).ravel()),(0,0,255),3)
             cv2.line(img_word, tuple(start_point[3].astype(np.int32).ravel()), tuple(end_point[3].astype(np.int32).ravel()),(0,0,255),3)
             cv2.line(img_word, tuple(start_point[4].astype(np.int32).ravel()), tuple(end_point[4].astype(np.int32).ravel()),(0,0,255),3)
        # cv2.imshow("img_word", img_word)
        # cv2.waitKey(0)
        return img_word
     # print(c)
# print(ch)     

    def word_vertically(self):        
        fs = cv2.FileStorage('C:/Program Files (x86)/HW2_N16111756_V1/Dataset_OpenCvDl_Hw2/Dataset_OpenCvDl_Hw2/Q3_Image/Q2_lib/alphabet_lib_vertical.txt', cv2.FILE_STORAGE_READ)
        # ch = fs.getNode("K").mat()
        # print(ch)
        img_vertically = self.img.copy()
        
        
        self.projection()
        
        a = self.messenge
        # ch = np.zeros((((len(a),3,2,3))))
        start = np.zeros((5,3))
        end = np.zeros((5,3))
        for i in range(len(a)):
             b = a[i]
             # ch = np.append(ch,fs.getNode(f"{b}").mat())
             c = fs.getNode(f"{b}").mat()
             for j in range(len(c)):
                 for k in range(len(c[0])):
                      c[j][k][0] += self.x[i][0]
                      c[j][k][1] += self.x[i][1]
                      start[j] = c[j][0]
                      end[j] = c[j][1]
             start_point, _ =cv2.projectPoints(start, np.array(self.v_rot), np.array(self.v_trans), self.mat, self.dist)    
             end_point, _ =cv2.projectPoints(end, np.array(self.v_rot), np.array(self.v_trans), self.mat, self.dist) 
             cv2.line(img_vertically, tuple(start_point[0].astype(np.int32).ravel()), tuple(end_point[0].astype(np.int32).ravel()),(0,0,255),3)
             cv2.line(img_vertically, tuple(start_point[1].astype(np.int32).ravel()), tuple(end_point[1].astype(np.int32).ravel()),(0,0,255),3)
             cv2.line(img_vertically, tuple(start_point[2].astype(np.int32).ravel()), tuple(end_point[2].astype(np.int32).ravel()),(0,0,255),3)
             cv2.line(img_vertically, tuple(start_point[3].astype(np.int32).ravel()), tuple(end_point[3].astype(np.int32).ravel()),(0,0,255),3)
             cv2.line(img_vertically, tuple(start_point[4].astype(np.int32).ravel()), tuple(end_point[4].astype(np.int32).ravel()),(0,0,255),3)
             
        # cv2.imshow("img_vertically", img_vertically)
        # cv2.waitKey(0)
        return img_vertically

# # print(mat, dist, v_rot, v_trans)
# print(corner[0].ravel())
# img = cv2.imread('C:/Program Files (x86)/HW2_N16111756_V1/Dataset_OpenCvDl_Hw2/Dataset_OpenCvDl_Hw2/Q3_Image/5.bmp')
# img = cv2.resize(img, None, fx = 0.3, fy = 0.3)
# augmented_Reality = Augmented_Reality(img)
# augmented_Reality.projection()
# augmented_Reality.word_on_board()
# augmented_Reality.word_vertically()
# cv2.imshow("img", img)
# cv2.waitKey(0)