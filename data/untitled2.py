# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:56:49 2020

@author: Administrator
"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QFrame,QAction
from PyQt5.QtCore import QSize   
from PyQt5.QtGui import QIcon 
     
class Plot(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(1000,1000))    
        self.setWindowTitle("Plot") 
        
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   
 
        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  
        self.framecon = [0, 1, 0, 0, 0, 0, 0]
        self.frame1 = QFrame(self)
        self.frame2 = QFrame(self)
        self.frame3 = QFrame(self)
        self.frame4 = QFrame(self)
        self.frame5 = QFrame(self)
        self.frame6 = QFrame(self)
        self.frame7 = QFrame(self)
        self.framelist = [self.frame1, self.frame2, self.frame3, self.frame4, self.frame5, self.frame6, self.frame7]
        [i.resize(1000, 1000) for i in self.framelist]
        self.framecon = [1, 0, 0, 0, 0, 0, 0]
        self.frame1.setStyleSheet('background-color:red;')
        self.frame2.setStyleSheet('background-color:blue;')
        self.frame3.setStyleSheet('background-color:black;')
        self.frame4.setStyleSheet('background-color:green;')
        self.frame5.setStyleSheet('background-color:red;')
        self.frame6.setStyleSheet('background-color:green;')
        self.frame7.setStyleSheet('background-color:blue;')
        self.Plotmain()
        self.framecon = [0, 1, 0, 0, 0, 0, 0]
        SMG1 = QAction('&寿命罐1', self)
        SMG2 = QAction('&寿命罐2', self)
        SMG3 = QAction('&寿命罐3', self)
        SMG4 = QAction('&寿命罐4', self)
        SM = QAction('&扫描', self)
        ZB = QAction('&中波', self)
        DB = QAction('&短波', self)
        self.qactionlist = [SMG1, SMG2, SMG3, SMG4, SM, ZB, DB]
        [i.triggered.connect(self.Plotmain) for i in self.qactionlist]
        menu1 = self.menuBar().addMenu('寿命罐')
        [menu1.addAction(self.qactionlist[i]) for i in range(4)]
        menu2 = self.menuBar().addMenu('载荷')
        [menu2.addAction(self.qactionlist[i]) for i in range(4,7)]

    def Plotmain(self):
        [self.framelist[i].setVisible(self.framecon[i]) for i in range(7)]
if __name__ == "__main__":
    def run_app():
        app = QtWidgets.QApplication(sys.argv)
        mainWin = Plot()
        mainWin.show()
        app.exec_()
    run_app()