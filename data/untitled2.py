# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:56:49 2020

@author: Administrator
"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize    
     
class Plot(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(1000,1000))    
        self.setWindowTitle("Plot") 
        
        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   
 
        gridLayout = QGridLayout(self)     
        centralWidget.setLayout(gridLayout)  
 
        '''title = QLabel("Hello World from PyQt", self) 
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)'''
        
        '''menu = self.menuBar().addMenu('Action for quit')
        action = menu.addAction('Quit')
        action.triggered.connect(QtWidgets.QApplication.quit)'''
        menu1 = self.menuBar().addMenu('寿命罐')
        menu2 = self.menuBar().addMenu('载荷')
        SMG1 = menu1.addAction('寿命罐1')
        SMG2 = menu1.addAction('寿命罐2')
        SMG3 = menu1.addAction('寿命罐3')
        SMG4 = menu1.addAction('寿命罐4')
        SM = menu2.addAction('扫描')
        SM1 = menu2.addAction('扫描1')
        SM2 = menu2.addAction('扫描2')
        SM3 = menu2.addAction('扫描3')
        ZB = menu2.addAction('中波')
        ZB1 = menu2.addAction('中波1')
        ZB2 = menu2.addAction('中波2')
        ZB3 = menu2.addAction('中波3')
        DB = menu2.addAction('短波')
        DB1 = menu2.addAction('短波1')
        DB2 = menu2.addAction('短波2')
        DB3 = menu2.addAction('短波3')
if __name__ == "__main__":
    def run_app():
        app = QtWidgets.QApplication(sys.argv)
        mainWin = Plot()
        mainWin.show()
        app.exec_()
    run_app()