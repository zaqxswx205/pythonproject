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
        
        self.frame1 = QFrame(self)
        self.frame1.resize(100,100)
        self.frame1.setStyleSheet('background-color:red;')
        self.frame2 = QFrame(self)
        self.frame2.resize(100,100)
        self.frame2.setStyleSheet('background-color:green;')
        self.frame3 = QFrame(self)
        self.frame3.resize(100,100)
        self.frame3.setStyleSheet('background-color:red;')
        self.frame4 = QFrame(self)
        self.frame4.resize(100,100)
        self.frame4.setStyleSheet('background-color:green;')
        self.frame1.setVisible(True)
        self.frame2.setVisible(False)
        SMG1 = QAction('&寿命罐1', self)
        SMG1.triggered.connect(self.PlotSMG1)
        menu1 = self.menuBar().addMenu('寿命罐')
        menu1.addAction(SMG1)
        menu2 = self.menuBar().addMenu('载荷')

        '''     SMG2 = menu1.addAction('寿命罐2')
        SMG3 = menu1.addAction('寿命罐3')
        SMG4 = menu1.addAction('寿命罐4')
        SM = menu2.addAction('扫描')
        ZB = menu2.addAction('中波')
        DB = menu2.addAction('短波')'''
    def PlotSMG1(self):
        self.frame1.setVisible(True)
        self.frame2.setVisible(False)
 
    def on_pushButton_enter_clicked_1(self):
        self.frame1.setVisible(False)
        self.frame2.setVisible(True)
if __name__ == "__main__":
    def run_app():
        app = QtWidgets.QApplication(sys.argv)
        mainWin = Plot()
        mainWin.show()
        app.exec_()
    run_app()