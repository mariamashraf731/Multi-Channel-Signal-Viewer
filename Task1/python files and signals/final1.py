# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'final.ui'
# Created by: PyQt5 UI code generator 5.13.0
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon
import numpy as np
import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import threading
import scipy.io
from scipy import ndimage, misc

class Ui_MainWindow(object):
    time1 = []
    value1 = []
    x1 = []
    y1 = []

    time2 = []
    value2 = [] 
    x2 = []
    y2 = []

    time3 = []
    value3 = [] 
    x3 = []
    y3 = []

    time4 = []
    value4 = [] 
    x4 = []
    y4 = []

    time5 = []
    value5 = [] 
    x5 = []
    y5 = []

    i = 0
    j = 0
    k = 0 
    l = 0
    m = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.w1 = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.w1.sizePolicy().hasHeightForWidth())
        self.w1.setSizePolicy(sizePolicy)
        self.w1.setObjectName("w1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.w1)
        self.s2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s2.sizePolicy().hasHeightForWidth())
        self.s2.setSizePolicy(sizePolicy)
        self.s2.setObjectName("s2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s2)
        self.w2 = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.w2.sizePolicy().hasHeightForWidth())
        self.w2.setSizePolicy(sizePolicy)
        self.w2.setObjectName("w2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.w2)
        self.s3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s3.sizePolicy().hasHeightForWidth())
        self.s3.setSizePolicy(sizePolicy)
        self.s3.setObjectName("s3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.s3)
        self.w3 = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.w3.sizePolicy().hasHeightForWidth())
        self.w3.setSizePolicy(sizePolicy)
        self.w3.setObjectName("w3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.w3)
        self.s4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s4.sizePolicy().hasHeightForWidth())
        self.s4.setSizePolicy(sizePolicy)
        self.s4.setObjectName("s4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s4)
        self.w4 = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.w4.sizePolicy().hasHeightForWidth())
        self.w4.setSizePolicy(sizePolicy)
        self.w4.setObjectName("w4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.w4)
        self.s5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s5.sizePolicy().hasHeightForWidth())
        self.s5.setSizePolicy(sizePolicy)
        self.s5.setObjectName("s5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s5)
        self.w5 = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.w5.sizePolicy().hasHeightForWidth())
        self.w5.setSizePolicy(sizePolicy)
        self.w5.setObjectName("w5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.w5)
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_btn.sizePolicy().hasHeightForWidth())
        self.play_btn.setSizePolicy(sizePolicy)
        self.play_btn.setStyleSheet("background-color:green;\n"
"")
        self.play_btn.setObjectName("play_btn")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.play_btn)
        self.pause_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_btn.sizePolicy().hasHeightForWidth())
        self.pause_btn.setSizePolicy(sizePolicy)
        self.pause_btn.setStyleSheet("background-color:red;")
        self.pause_btn.setObjectName("pause_btn")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.pause_btn)
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_btn.sizePolicy().hasHeightForWidth())
        self.reset_btn.setSizePolicy(sizePolicy)
        self.reset_btn.setStyleSheet("background-color:yellow;")
        self.reset_btn.setObjectName("reset_btn")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.reset_btn)
        self.zoom_in = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_in.sizePolicy().hasHeightForWidth())
        self.zoom_in.setSizePolicy(sizePolicy)
        self.zoom_in.setStyleSheet("background-color:grey;")
        self.zoom_in.setObjectName("zoom_in")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.zoom_in)
        self.s1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s1.sizePolicy().hasHeightForWidth())
        self.s1.setSizePolicy(sizePolicy)
        self.s1.setStatusTip("")
        self.s1.setStyleSheet("")
        self.s1.setObjectName("s1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1)
        self.zoom_out = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_out.sizePolicy().hasHeightForWidth())
        self.zoom_out.setSizePolicy(sizePolicy)
        self.zoom_out.setStyleSheet("background-color:grey;\n"
"")
        self.zoom_out.setObjectName("zoom_out")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.zoom_out)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuOpen = QtWidgets.QMenu(self.menufile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuclose = QtWidgets.QMenu(self.menufile)
        self.menuclose.setObjectName("menuclose")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Open_S1 = QtWidgets.QAction(MainWindow)
        self.Open_S1.setObjectName("Open_S1")
        self.Open_S2 = QtWidgets.QAction(MainWindow)
        self.Open_S2.setObjectName("Open_S2")
        self.Open_S3 = QtWidgets.QAction(MainWindow)
        self.Open_S3.setObjectName("Open_S3")
        self.Open_S4 = QtWidgets.QAction(MainWindow)
        self.Open_S4.setObjectName("Open_S4")
        self.Open_S5 = QtWidgets.QAction(MainWindow)
        self.Open_S5.setObjectName("Open_S5")
        self.Hide_S1 = QtWidgets.QAction(MainWindow)
        self.Hide_S1.setObjectName("Hide_S1")
        self.Hide_S2 = QtWidgets.QAction(MainWindow)
        self.Hide_S2.setObjectName("Hide_S2")
        self.Hide_S3 = QtWidgets.QAction(MainWindow)
        self.Hide_S3.setObjectName("Hide_S3")
        self.Hide_S4 = QtWidgets.QAction(MainWindow)
        self.Hide_S4.setObjectName("Hide_S4")
        self.Hide_S5 = QtWidgets.QAction(MainWindow)
        self.Hide_S5.setObjectName("Hide_S5")
        self.menuOpen.addAction(self.Open_S1)
        self.menuOpen.addAction(self.Open_S2)
        self.menuOpen.addAction(self.Open_S3)
        self.menuOpen.addAction(self.Open_S4)
        self.menuOpen.addAction(self.Open_S5)
        self.menuclose.addAction(self.Hide_S1)
        self.menuclose.addAction(self.Hide_S2)
        self.menuclose.addAction(self.Hide_S3)
        self.menuclose.addAction(self.Hide_S4)
        self.menuclose.addAction(self.Hide_S5)
        self.menufile.addAction(self.menuOpen.menuAction())
        self.menufile.addAction(self.menuclose.menuAction())
        self.menubar.addAction(self.menufile.menuAction())

        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()
        self.timer4 = QtCore.QTimer()
        self.timer5 = QtCore.QTimer()
        self.timer1.setInterval(50)
        self.timer2.setInterval(50)
        self.timer3.setInterval(50)
        self.timer4.setInterval(50)
        self.timer5.setInterval(50)
        self.timer1.timeout.connect(self.plotting1)
        self.timer2.timeout.connect(self.plotting2)
        self.timer3.timeout.connect(self.plotting3)
        self.timer4.timeout.connect(self.plotting4)
        self.timer5.timeout.connect(self.plotting5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.s2.setText(_translate("MainWindow", "Show Signal2"))
        self.s3.setText(_translate("MainWindow", "Show Signal3"))
        self.s4.setText(_translate("MainWindow", "Show Signal4"))
        self.s5.setText(_translate("MainWindow", "Show Signal5"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.pause_btn.setText(_translate("MainWindow", "Pause"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))
        self.zoom_in.setText(_translate("MainWindow", "+"))
        self.s1.setText(_translate("MainWindow", "Show Signal1"))
        self.zoom_out.setText(_translate("MainWindow", "-"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuclose.setTitle(_translate("MainWindow", "Close"))
        self.Open_S1.setText(_translate("MainWindow", "Open Signal1"))
        self.Open_S1.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.Open_S2.setText(_translate("MainWindow", "Open Signal2"))
        self.Open_S2.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.Open_S3.setText(_translate("MainWindow", "Open Signal3"))
        self.Open_S3.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.Open_S4.setText(_translate("MainWindow", "Open Signal4"))
        self.Open_S4.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.Open_S5.setText(_translate("MainWindow", "Open Signal5"))
        self.Open_S5.setShortcut(_translate("MainWindow", "Ctrl+5"))
        self.Hide_S1.setText(_translate("MainWindow", "Hide Signal1"))
        self.Hide_S1.setShortcut(_translate("MainWindow", "Alt+1"))
        self.Hide_S2.setText(_translate("MainWindow", "Hide Signal2"))
        self.Hide_S2.setShortcut(_translate("MainWindow", "Alt+2"))
        self.Hide_S3.setText(_translate("MainWindow", "Hide Signal3"))
        self.Hide_S3.setShortcut(_translate("MainWindow", "Alt+3"))
        self.Hide_S4.setText(_translate("MainWindow", "Hide Signal4"))
        self.Hide_S4.setShortcut(_translate("MainWindow", "Alt+4"))
        self.Hide_S5.setText(_translate("MainWindow", "Hide Signal5"))
        self.Hide_S5.setShortcut(_translate("MainWindow", "Alt+5"))
        self.Open_S1.triggered.connect(self.open_dialog_box1)
        self.Open_S2.triggered.connect(self.open_dialog_box2)
        self.Open_S3.triggered.connect(self.open_dialog_box3)
        self.Open_S4.triggered.connect(self.open_dialog_box4)
        self.Open_S5.triggered.connect(self.open_dialog_box5)
        self.Hide_S1.triggered.connect(self.close1)
        self.Hide_S2.triggered.connect(self.close2)
        self.Hide_S3.triggered.connect(self.close3)
        self.Hide_S4.triggered.connect(self.close4)
        self.Hide_S5.triggered.connect(self.close5)
        self.s1.clicked.connect(self.show1)
        self.s2.clicked.connect(self.show2)
        self.s3.clicked.connect(self.show3)
        self.s4.clicked.connect(self.show4)
        self.s5.clicked.connect(self.show5)
        self.play_btn.clicked.connect(self.Play_All)
        self.pause_btn.clicked.connect(self.Pause_All)
        self.reset_btn.clicked.connect(self.Reset_All)
        self.zoom_in.clicked.connect(self.Zoom_IN)
        self.zoom_out.clicked.connect(self.Zoom_OUT)
        self.w4.hide()
        self.w5.hide()

    def show1(self):
        self.w1.show()
    def show2(self):
        self.w2.show()
    def show3(self):
        self.w3.show()        
    def show4(self):
        self.w4.show()
    def show5(self):
        self.w5.show()
    def close1(self):
        self.w1.hide()
    def close2(self):
        self.w2.hide()
    def close3(self):
        self.w3.hide()
    def close4(self):
        self.w4.hide()
    def close5(self):
        self.w5.hide()

    def open_dialog_box1(self):          
        filename = QFileDialog.getOpenFileName(None,"open file","C:/Users/Ma/Desktop/DSP/task1-team_08/python files and signals","signals(*.csv *.mat *.txt)")
        path = filename[0]
        if path:
            if path.endswith(".mat"):     
                data = scipy.io.loadmat(path)
                data = data["val"]
                self.value1 = data[0,:]            
            else:
            	with open(path, "r") as f: 
            		data = np.genfromtxt(f, delimiter = ' ')
            		self.value1 = data [:,1]
            self.timer1.start()

    def plotting1 (self):
    	pen = pg.mkPen(color=(0,50,100))
    	self.data_line1 = self.w1.plotItem.plot(self.y1, pen=pen)
    	if self.i < len(self.value1):
            self.y1.append(self.value1[self.i])
            self.data_line1.setData(self.y1)
            self.i+=10

    def open_dialog_box2(self):          
        filename = QFileDialog.getOpenFileName(None,"open file","C:/Users/Ma/Desktop/DSP/task1-team_08/python files and signals","signals(*.csv *.mat *.txt)")
        path = filename[0]
        if path:
            if path.endswith(".mat"):     
                data = scipy.io.loadmat(path)
                data = data["val"]
                self.value2 = data[0,:]            
            else:
            	with open(path, "r") as f: 
            		data = np.genfromtxt(f, delimiter = ' ')
            		self.value2 = data [:,1]
            self.timer2.start()

    def plotting2(self):
    	pen = pg.mkPen(color=(100,110,0))
    	self.data_line2 = self.w2.plotItem.plot(self.y2, pen=pen)
    	if self.j < len(self.value2):
            self.y2.append(self.value2[self.j])
            self.data_line2.setData(self.y2)
            self.j+=10

    def open_dialog_box3(self):          
        filename = QFileDialog.getOpenFileName(None,"open file","C:/Users/Ma/Desktop/DSP/task1-team_08/python files and signals","signals(*.csv *.mat *.txt)")
        path = filename[0]
        if path:
            if path.endswith(".mat"):     
                data = scipy.io.loadmat(path)
                data = data["val"]
                self.value3 = data[0,:]            
            else:
            	with open(path, "r") as f: 
            		data = np.genfromtxt(f, delimiter = ' ')
            		self.value3 = data [:,1]
            self.timer3.start()

    def plotting3 (self):
    	pen = pg.mkPen(color=(0,0,255))
    	self.data_line3 = self.w3.plotItem.plot(self.y3, pen=pen)
    	if self.k < len(self.value3):
            self.y3.append(self.value3[self.k])
            self.data_line3.setData(self.y3)
            self.k+=10
      
    def open_dialog_box4(self):          
        filename = QFileDialog.getOpenFileName(None,"open file","C:/Users/Ma/Desktop/DSP/task1-team_08/python files and signals","signals(*.csv *.mat *.txt)")
        path = filename[0]
        if path:
            if path.endswith(".mat"):     
                data = scipy.io.loadmat(path)
                data = data["val"]
                self.value4 = data[0,:]            
            else:
            	with open(path, "r") as f: 
            		data = np.genfromtxt(f, delimiter = ' ')
            		self.value4 = data [:,1]
            self.timer4.start()

    def plotting4(self):
    	pen = pg.mkPen(color=(0,255,0))
    	self.data_line4 = self.w4.plotItem.plot(self.y4, pen=pen)
    	if self.l < len(self.value4):
            self.y4.append(self.value4[self.l])
            self.data_line4.setData(self.y4)
            self.l+=10      

    def open_dialog_box5(self):          
        filename = QFileDialog.getOpenFileName(None,"open file","C:/Users/Ma/Desktop/DSP/task1-team_08/python files and signals","signals(*.csv *.mat *.txt)")
        path = filename[0]
        if path:
            if path.endswith(".mat"):     
                data = scipy.io.loadmat(path)
                data = data["val"]
                self.value5 = data[0,:]            
            else:
            	with open(path, "r") as f: 
            		data = np.genfromtxt(f, delimiter = ' ')
            		self.value5 = data [:,1]
            self.timer5.start()
           
    def plotting5(self):
    	pen = pg.mkPen(color=(255,0,0))
    	self.data_line5 = self.w5.plotItem.plot(self.y5, pen=pen)
    	if self.m < len(self.value5):
            self.y5.append(self.value5[self.m])
            self.data_line5.setData(self.y5)
            self.m+=10        

    def Play_All(self):
        self.timer1.start()
        self.timer2.start()
        self.timer3.start()
        self.timer4.start()
        self.timer5.start()

    def Pause_All(self):
        self.timer1.stop()
        self.timer2.stop()
        self.timer3.stop()
        self.timer4.stop()
        self.timer5.stop()

    def Zoom_OUT(self):
        self.w1.getViewBox().scaleBy(s = 2)
        self.w2.getViewBox().scaleBy(s = 2)
        self.w3.getViewBox().scaleBy(s = 2)
        self.w4.getViewBox().scaleBy(s = 2)
        self.w5.getViewBox().scaleBy(s = 2)

    def Zoom_IN(self):
        self.w1.getViewBox().scaleBy(s = 0.5)
        self.w2.getViewBox().scaleBy(s = 0.5)
        self.w3.getViewBox().scaleBy(s = 0.5)
        self.w4.getViewBox().scaleBy(s = 0.5)
        self.w5.getViewBox().scaleBy(s = 0.5)

    def Reset_All(self):
    	self.w1.clear()
    	self.w2.clear()
    	self.w3.clear()
    	self.w4.clear()
    	self.w5.clear()
    	self.y1 = []
    	self.y2 = []
    	self.y3 = []
    	self.y4 = []
    	self.y5 = []
    	self.data_line1 = self.w1.plotItem.plot(self.y1,)
    	self.data_line2 = self.w2.plotItem.plot(self.y2,)
    	self.data_line3 = self.w3.plotItem.plot(self.y3,)
    	self.data_line4 = self.w4.plotItem.plot(self.y4,)
    	self.data_line5 = self.w5.plotItem.plot(self.y5,)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())