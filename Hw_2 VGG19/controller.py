from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_Form
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


class Form_controller(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        # qpushbutton doc: https://doc.qt.io/qt-5/qpushbutton.html
        self.ui.pushButton_14.clicked.connect(self.open_file)
        # self.open_file()

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(
            self, "Open file", "./")                 # start path
        # print(filename, filetype)
        result = os.path.split(filename)[1]
        self.img = cv2.imread(filename, -1)
        self.display_img()

    def display_img(self):
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height,
                           bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))
