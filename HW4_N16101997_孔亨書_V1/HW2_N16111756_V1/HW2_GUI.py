# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:14:28 2022

@author: peter
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import HW2_1
import HW2_2
import HW2_3
import HW2_4



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Load_Data = QtWidgets.QGroupBox(self.centralwidget)
        self.Load_Data.setGeometry(QtCore.QRect(10, 70, 131, 371))
        self.Load_Data.setObjectName("Load Data")
        
        self.Load_Folder_button = QtWidgets.QPushButton(self.Load_Data)
        self.Load_Folder_button.setGeometry(QtCore.QRect(20, 60, 91, 23))
        self.Load_Folder_button.setObjectName("Load Folder")
        
        self.Load_Image_L_button = QtWidgets.QPushButton(self.Load_Data)
        self.Load_Image_L_button.setGeometry(QtCore.QRect(20, 160, 91, 23))
        self.Load_Image_L_button.setObjectName("Load Image_L")
        
        self.Load_Image_R_button = QtWidgets.QPushButton(self.Load_Data)
        self.Load_Image_R_button.setGeometry(QtCore.QRect(20, 260, 91, 23))
        self.Load_Image_R_button.setObjectName("Load_Image_R")
        
        self.Find_Contour = QtWidgets.QGroupBox(self.centralwidget)
        self.Find_Contour.setGeometry(QtCore.QRect(150, 70, 151, 371))
        self.Find_Contour.setObjectName("1. Find Contour")
        
        self.Draw_Contour_button = QtWidgets.QPushButton(self.Find_Contour)
        self.Draw_Contour_button.setGeometry(QtCore.QRect(10, 90, 131, 23))
        self.Draw_Contour_button.setObjectName("1.1 Draw Contour")
        
        self.Count_Rings_button = QtWidgets.QPushButton(self.Find_Contour)
        self.Count_Rings_button.setGeometry(QtCore.QRect(10, 210, 131, 23))
        self.Count_Rings_button.setObjectName("1.2 Count Rings")
        
        self.Calibration = QtWidgets.QGroupBox(self.centralwidget)
        self.Calibration.setGeometry(QtCore.QRect(310, 70, 161, 371))
        self.Calibration.setObjectName("2. Calibration")
        
        self.Find_Corners_button = QtWidgets.QPushButton(self.Calibration)
        self.Find_Corners_button.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.Find_Corners_button.setObjectName("2.1 Find Corners")
        
        self.Find_Intrinsic_button = QtWidgets.QPushButton(self.Calibration)
        self.Find_Intrinsic_button.setGeometry(QtCore.QRect(20, 90, 121, 31))
        self.Find_Intrinsic_button.setObjectName("2.2 Find Intrinsic")
        
        self.Find_Extrinsic_box = QtWidgets.QGroupBox(self.Calibration)
        self.Find_Extrinsic_box.setGeometry(QtCore.QRect(10, 140, 141, 91))
        self.Find_Extrinsic_box.setObjectName("2.3 Find Extrinstic")
        
        self.Find_Extrinsic_button = QtWidgets.QPushButton(self.Find_Extrinsic_box)
        self.Find_Extrinsic_button.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.Find_Extrinsic_button.setObjectName("2.3 Find Extrinsic")
        
        self.comboBox = QtWidgets.QComboBox(self.Find_Extrinsic_box)
        self.comboBox.setGeometry(QtCore.QRect(40, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        
        self.Find_Distortion_button = QtWidgets.QPushButton(self.Calibration)
        self.Find_Distortion_button.setGeometry(QtCore.QRect(20, 250, 121, 31))
        self.Find_Distortion_button.setObjectName("2.4 Find Distortion")
        
        self.Show_Result_button = QtWidgets.QPushButton(self.Calibration)
        self.Show_Result_button.setGeometry(QtCore.QRect(20, 310, 121, 31))
        self.Show_Result_button.setObjectName("2.5 Show Result")
        
        self.Augmented_Reality = QtWidgets.QGroupBox(self.centralwidget)
        self.Augmented_Reality.setGeometry(QtCore.QRect(480, 70, 161, 371))
        self.Augmented_Reality.setObjectName("3. Augmented Reality")
        
        self.Show_Words_On_Board_button = QtWidgets.QPushButton(self.Augmented_Reality)
        self.Show_Words_On_Board_button.setGeometry(QtCore.QRect(10, 150, 141, 31))
        self.Show_Words_On_Board_button.setObjectName("3.1 Show Words On Board")
        
        self.Show_Words_Veritically_button = QtWidgets.QPushButton(self.Augmented_Reality)
        self.Show_Words_Veritically_button.setGeometry(QtCore.QRect(10, 260, 141, 31))
        self.Show_Words_Veritically_button.setObjectName("3.2 Show Words Veritically")
        
        self.lineEdit = QtWidgets.QLineEdit(self.Augmented_Reality)
        self.lineEdit.setGeometry(QtCore.QRect(20, 59, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        self.Stereo_Disparity_Map_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Stereo_Disparity_Map_box.setGeometry(QtCore.QRect(650, 70, 151, 371))
        self.Stereo_Disparity_Map_box.setObjectName("4. Stereo Disparity Map")
        
        self.Stereo_Disparity_Map_buttom = QtWidgets.QPushButton(self.Stereo_Disparity_Map_box)
        self.Stereo_Disparity_Map_buttom.setGeometry(QtCore.QRect(10, 160, 131, 31))
        self.Stereo_Disparity_Map_buttom.setObjectName("4.1 Stereo Disparity Map")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuHW2 = QtWidgets.QMenu(self.menubar)
        self.menuHW2.setObjectName("menuHW2")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHW2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Load_Data.setTitle(_translate("MainWindow", "Load Data"))
        self.Load_Folder_button.setText(_translate("MainWindow", "Load Folder"))
        self.Load_Image_L_button.setText(_translate("MainWindow", "Load Image_L"))
        self.Load_Image_R_button.setText(_translate("MainWindow", "Load Image_R"))
        self.Find_Contour.setTitle(_translate("MainWindow", "1. Find Contour"))
        self.Draw_Contour_button.setText(_translate("MainWindow", "1.1 Draw Contour"))
        self.Count_Rings_button.setText(_translate("MainWindow", "1.2 Count Rings"))
        self.Calibration.setTitle(_translate("MainWindow", "2. Calibration"))
        self.Find_Corners_button.setText(_translate("MainWindow", "2.1 Find Corners"))
        self.Find_Intrinsic_button.setText(_translate("MainWindow", "2.2 Find Intrinsic"))
        self.Find_Extrinsic_box.setTitle(_translate("MainWindow", "2.3 Find Extrinsic"))
        self.Find_Extrinsic_button.setText(_translate("MainWindow", "2.3 Find Extrinsic"))
        self.Find_Distortion_button.setText(_translate("MainWindow", "2.4 Find Distortion"))
        self.Show_Result_button.setText(_translate("MainWindow", "2.5 Show Result"))
        self.Augmented_Reality.setTitle(_translate("MainWindow", "3. Augmented Reality"))
        self.Show_Words_On_Board_button.setText(_translate("MainWindow", "3.1 Show Words On Board"))
        self.Show_Words_Veritically_button.setText(_translate("MainWindow", "3.2 Show Words Veritically"))
        self.Stereo_Disparity_Map_box.setTitle(_translate("MainWindow", "4. Stereo Disparity Map"))
        self.Stereo_Disparity_Map_buttom.setText(_translate("MainWindow", "4.1 Stereo Disparity Map"))
        self.menuHW2.setTitle(_translate("MainWindow", "HW2"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.Load_Folder_button.clicked.connect(self.Load_Folder)
        
        self.Load_Image_L_button.clicked.connect(self.Load_Image_L)
        
        self.Load_Image_R_button.clicked.connect(self.Load_Image_R)

        self.Draw_Contour_button.clicked.connect(self.Draw_Contour)

        self.Count_Rings_button.clicked.connect(self.Count_Rings)

        self.Find_Corners_button.clicked.connect(self.Find_Corners)

        self.Find_Intrinsic_button.clicked.connect(self.Find_Intrinsic)
        
        self.Find_Extrinsic_button.clicked.connect(self.Find_Extrinsic)
        
        self.Find_Distortion_button.clicked.connect(self.Find_Distortion)
        
        self.Show_Result_button.clicked.connect(self.Show_Result)
        
        self.Show_Words_On_Board_button.clicked.connect(self.Show_Words_On_Board)
        
        self.Show_Words_Veritically_button.clicked.connect(self.Show_Words_Veritically)
        
        self.Stereo_Disparity_Map_buttom.clicked.connect(self.Stereo_Disparity_Map)
        
        choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        self.comboBox.addItems(choices)
        self.comboBox.currentIndexChanged.connect(self.Number)

    @QtCore.pyqtSlot()
    def Number(self):
        global number
        number = 0
        for i in range(15):
            a = self.comboBox.currentText()  
            if i+1 == int(a):
                number = i
    def Load_Folder(self):
        image, _filter = QtWidgets.QFileDialog.getOpenFileNames(None, 'OpenFile' ,'', "Image file(*.png *.jpg *.bmp)")
        global paths
        # path = np.array(image[0])
        paths = image
        return paths
    
    def Load_Image_L(self):
        global path_L
        image_L, _filter = QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile' ,'', "Image file(*.png *.jpg *.bmp)")
        path_L = image_L
        return path_L
        
    def Load_Image_R(self):
        global path_R
        image_R, _filter = QtWidgets.QFileDialog.getOpenFileName(None, 'OpenFile' ,'', "Image file(*.png *.jpg *.bmp)")
        path_R = image_R
        return path_R
        
    def Draw_Contour(self):
        for path in paths:
            img , _ = HW2_1.Canny(path)
            cv2.imshow("img", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
         
        
    def Count_Rings(self):
        i = 1
        for path in paths:
            _ , count = HW2_1.Canny(path)
            print(f"There are {count} rings in img{i}.jpg")
            i += 1
    
    def Find_Corners(self):
        
        for path in paths:
            Calibration = HW2_2.Camera_Calibration(path)
            img, _ = Calibration.corner()
            cv2.imshow("img", img)
            cv2.waitKey(500)
            cv2.destroyAllWindows()
            
            
    def Find_Intrinsic(self):
        Calibration = HW2_2.Camera_Calibration(paths[0])
        _, _ = Calibration.corner()
        mat, _, _, _ = Calibration.Intrinsic()
        print(mat, "\n")
        
    def Find_Extrinsic(self):
        Calibration = HW2_2.Camera_Calibration(paths[number])
        _, _ = Calibration.corner()
        _, _, _, _ = Calibration.Intrinsic()
        extrinsic = Calibration.Extrinsic()
        
        print(extrinsic, "\n")
        
    def Find_Distortion(self):
        i = 1
        for path in paths:
            Calibration = HW2_2.Camera_Calibration(path)
            _, _ = Calibration.corner()
            _, _, _, _ = Calibration.Intrinsic()
            _ = Calibration.Extrinsic() 
            Distortion = Calibration.Distortion()
            print(f"img{i} distortion:", Distortion, "\n")
            i += 1
    def Show_Result(self):
        for path in paths:
            img_origin = cv2.imread(path, 0)
            Calibration = HW2_2.Camera_Calibration(path)
            _, _ = Calibration.corner()
            _, _, _, _ = Calibration.Intrinsic()
            _ = Calibration.Extrinsic() 
            _ = Calibration.Distortion()
            img_result = Calibration.Undistort()
            imgs = np.hstack([img_origin, img_result])
            imgs = cv2.resize(imgs, None, fx = 0.4, fy = 0.4)
            cv2.imshow("img", imgs)
            cv2.waitKey(500)
            cv2.destroyAllWindows()
        
    def Show_Words_On_Board(self):
        messenge = self.lineEdit.text()
        for path in paths:
            Augmented = HW2_3.Augmented_Reality(path, messenge)
            img = Augmented.word_on_board()
            img = cv2.resize(img, None, fx = 0.4, fy = 0.4)
            cv2.imshow("img", img)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
        
    def Show_Words_Veritically(self):
        messenge = self.lineEdit.text()
        for path in paths:
            Augmented = HW2_3.Augmented_Reality(path, messenge)
            img = Augmented.word_vertically()
            img = cv2.resize(img, None, fx = 0.4, fy = 0.4)
            cv2.imshow("img", img)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
        
    def Stereo_Disparity_Map(self):
        
        # img_L = cv2.imread(path_L)
        # img_R = cv2.imread(path_R)
        Disparity_Map = HW2_4.Disparity_Map(path_L, path_R)
        disparity = Disparity_Map.Stereo_Map()
        Disparity_Map.draw_circle()
        # cv2.namedWindow('imgR_dot',cv2.WINDOW_NORMAL)
        # cv2.resizeWindow("imgR_dot", int(imgR_dot.shape[1]/4), int(imgR_dot.shape[0]/4))
        # cv2.imshow('imgR_dot', imgR_dot)           
        

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())