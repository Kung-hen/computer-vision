# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:54:46 2022

@author: peter
"""

import cv2
import numpy as np
class Camera_Calibration:
    def __init__(self, path):
        self.img = cv2.imread(path)
        # self.img = cv2.resize(self.img, None, fx = 0.3, fy = 0.3)
        self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.w = 11
        self.h = 8
    def corner(self):
        img_corner = self.img.copy()
        ret, self.cp_img = cv2.findChessboardCorners(self.img, (self.w,self.h), None)
        cv2.drawChessboardCorners(img_corner, (self.w,self.h), self.cp_img, ret)
        img_corner = cv2.resize(img_corner, None, fx = 0.4, fy = 0.4)
        return img_corner, self.cp_img 
    
    def Intrinsic(self):
        cp_int = np.zeros((self.w * self.h, 3), np.float32)
        cp_int[:, :2] = np.mgrid[0:self.w, 0:self.h].T.reshape(-1, 2)
        # cp_world: corner point in world space, save the coordinate of corner points in world space.
        cp_world = cp_int 
        
        # print(ret,cp_img)
        obj_points = []  # the points in world space
        img_points = []  # the points in image space (relevant to obj_points)
        obj_points.append(cp_world)
        img_points.append(self.cp_img) 
        
        ret, self.mat_inter, self.coff_dis, self.v_rot, self.v_trans = cv2.calibrateCamera(obj_points, img_points, self.img_gray.shape[::-1], None, None)
        
        # print(v_rot.shape)
        
        # R = np.array(R)
        # print("R=",R[0])
       
        # print(R.shape)
        # print("Intrinsic:",self.mat_inter,"\n")
        # print("畸变系数=",coff_dis)
        # print("旋转向量=",v_rot)
        # print("平移向量=",v_trans)
        return self.mat_inter, self.coff_dis, self.v_rot, self.v_trans
    def Extrinsic(self):
        self.v_rot = np.array(self.v_rot)
        self.v_rot = np.reshape(self.v_rot, (1,3))
        R = cv2.Rodrigues(self.v_rot)
        R = np.array(R[0])
        extrinsic = np.zeros((3,4))
        self.v_trans = np.array(self.v_trans)
        for i in range(3):
            # print(self.v_trans[0][i])
            extrinsic[i] = np.append(R[i],self.v_trans[0][i])
        # print("Extrinsic:", extrinsic,"\n")
        return extrinsic
    
    def Distortion(self):
        # print("Distortion:", self.coff_dis, "\n")
        return self.coff_dis
        
    def Undistort(self):
        undistort_result = cv2.undistort(self.img_gray, self.mat_inter, self.coff_dis, None, self.mat_inter)
        
        return undistort_result
# path = "C:/Program Files (x86)/HW2_N16111756_V1/Dataset_OpenCvDl_Hw2/Dataset_OpenCvDl_Hw2/Q2_Image/4.bmp"


# img = cv2.resize(img, None, fx = 0.3, fy = 0.3)
# cv2.imshow("img_origin", img)
# Camera = Camera_Calibration(path) 
# img, _ = Camera.corner()
# cv2.imshow("img", img)
# mat, _, _, _ = Camera.Intrinsic()
# print(mat)
# extrinsic = Camera.Extrinsic()
# print(extrinsic)
# _ = Camera.Distortion()

# img_result = Camera.Undistort()
# cv2.imshow("img_result", img_result)
# cv2.waitKey(0)