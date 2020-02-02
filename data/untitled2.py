# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:56:49 2020

@author: Administrator
"""

import sys
import PyQt5.QtWidgets
import PyQt5.QtCore 
import PyQt5.QtGui 
     
class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.setWindowTitle('PLOT')
        self.showMaximized()
        self.Layout = PyQt5.QtWidgets.QHBoxLayout()
        self.centralWidget = PyQt5.QtWidgets.QWidget(self)          
        self.setCentralWidget(self.centralWidget)   
        self.stackedWidget = PyQt5.QtWidgets.QStackedWidget(self.centralWidget)
        self.Layout.addWidget(self.stackedWidget)
        self.TotalCategory = 5
        self.Category = ['&寿命罐1', '&寿命罐2', '&扫描', '&中波', '&短波']
        self.SMButton = ['制冷温度', '功率', '大端散热面', '小端散热面', '压缩机散热面']
        self.ZBDBButton = ['制冷温度', '功率', '压缩机散热面', '脉管散热面']
        self.StackConfiguration()
        self.MenuConfiguration()
        
    def MenuConfiguration (self) :
        Menu1 = self.menuBar().addMenu('寿命罐')
        self.qActionList = [PyQt5.QtWidgets.QAction(self.Category[i], self) for i in range(self.TotalCategory)]
        [Menu1.addAction(self.qActionList[i]) for i in range(self.TotalCategory)]
        [self.qActionList[i].triggered.connect(self.MenuConnectStack) for i in range(self.TotalCategory)]

    def StackConfiguration (self) :
        self.StackList = globals()
        for i in range(self.TotalCategory) :
            self.StackList['self.stack'+str(i)] = PyQt5.QtWidgets.QWidget()
            self.stackedWidget.addWidget(self.StackList['self.stack'+str(i)])
        self.Stack0UI()
        self.Stack1UI()
        self.Stack2UI()
        self.Stack3UI()
        self.Stack4UI()

    def MenuConnectStack(self) :
        SenderPosition = self.Category.index(self.sender().text())
        self.stackedWidget.setCurrentIndex(SenderPosition)

    def Stack0UI(self):
        Stack0 = PyQt5.QtWidgets.QHBoxLayout()
        Title = PyQt5.QtWidgets.QLabel(self.StackList['self.stack'+str(0)])
        Title.setText('扫描 3')
        Stack0.addWidget(Title)
        [Stack0.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.SMButton]
        self.StackList['self.stack'+str(0)].setLayout(Stack0)

    def Stack1UI(self):
        Stack1 = PyQt5.QtWidgets.QVBoxLayout()
        ButtonLayout1 = PyQt5.QtWidgets.QHBoxLayout()
        ButtonLayout2 = PyQt5.QtWidgets.QHBoxLayout()
        Title1 = PyQt5.QtWidgets.QLabel(self.StackList['self.stack'+str(1)])
        Title2 = PyQt5.QtWidgets.QLabel(self.StackList['self.stack'+str(1)])
        Title1.setText('扫描 1')
        Title2.setText('扫描 2')
        ButtonLayout1.addWidget(Title1)
        ButtonLayout2.addWidget(Title2)
        [ButtonLayout1.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.SMButton]
        [ButtonLayout2.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.SMButton]
        Stack1.addLayout(ButtonLayout1)
        Stack1.addLayout(ButtonLayout2)
        self.StackList['self.stack'+str(1)].setLayout(Stack1)

    def Stack2UI(self):
        Main = PyQt5.QtWidgets.QVBoxLayout()
        Stack2 = PyQt5.QtWidgets.QHBoxLayout()
        TitleLayout = PyQt5.QtWidgets.QHBoxLayout()
        self.TabWidget = PyQt5.QtWidgets.QTabWidget(self.StackList['self.stack'+str(2)])
        self.tab1 = PyQt5.QtWidgets.QWidget()
        self.tab2 = PyQt5.QtWidgets.QWidget()
        self.tab3 = PyQt5.QtWidgets.QWidget()
        self.TabWidget.addTab(self.tab1, "扫描 1")
        self.TabWidget.addTab(self.tab2, "扫描 2")
        self.TabWidget.addTab(self.tab3, "扫描 3")
        self.Tabcat1 = PyQt5.QtWidgets.QHBoxLayout()
        self.Tabcat2 = PyQt5.QtWidgets.QHBoxLayout()
        self.Tabcat3 = PyQt5.QtWidgets.QHBoxLayout()
        [self.Tabcat1.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.SMButton]
        [self.Tabcat2.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.SMButton]
        [self.Tabcat3.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.SMButton]
        self.tab1.setLayout(self.Tabcat1)
        self.tab2.setLayout(self.Tabcat2)
        self.tab3.setLayout(self.Tabcat3)
        Stack2.addWidget(self.TabWidget)
        Title = PyQt5.QtWidgets.QLabel(self.StackList['self.stack'+str(2)])
        Title.setText('扫描')
        Title.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        TitleLayout.addWidget(Title)
        Main.addLayout(TitleLayout)
        Main.addLayout(Stack2)
        self.StackList['self.stack'+str(2)].setLayout(Main)

    def Stack3UI(self):
        Main = PyQt5.QtWidgets.QVBoxLayout()
        Stack2 = PyQt5.QtWidgets.QHBoxLayout()
        TitleLayout = PyQt5.QtWidgets.QHBoxLayout()
        self.TabWidget = PyQt5.QtWidgets.QTabWidget(self.StackList['self.stack'+str(3)])
        self.tab1 = PyQt5.QtWidgets.QWidget()
        self.tab2 = PyQt5.QtWidgets.QWidget()
        self.tab3 = PyQt5.QtWidgets.QWidget()
        self.TabWidget.addTab(self.tab1, "中波 1")
        self.TabWidget.addTab(self.tab2, "中波 2")
        self.TabWidget.addTab(self.tab3, "中波 3")
        self.Tabcat1 = PyQt5.QtWidgets.QHBoxLayout()
        self.Tabcat2 = PyQt5.QtWidgets.QHBoxLayout()
        self.Tabcat3 = PyQt5.QtWidgets.QHBoxLayout()
        [self.Tabcat1.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.ZBDBButton]
        [self.Tabcat2.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.ZBDBButton]
        [self.Tabcat3.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.ZBDBButton]
        self.tab1.setLayout(self.Tabcat1)
        self.tab2.setLayout(self.Tabcat2)
        self.tab3.setLayout(self.Tabcat3)
        Stack2.addWidget(self.TabWidget)
        Title = PyQt5.QtWidgets.QLabel(self.StackList['self.stack'+str(2)])
        Title.setText('中波')
        Title.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        TitleLayout.addWidget(Title)
        Main.addLayout(TitleLayout)
        Main.addLayout(Stack2)
        self.StackList['self.stack'+str(3)].setLayout(Main)

    def Stack4UI(self):
        Main = PyQt5.QtWidgets.QVBoxLayout()
        Stack2 = PyQt5.QtWidgets.QHBoxLayout()
        TitleLayout = PyQt5.QtWidgets.QHBoxLayout()
        self.TabWidget = PyQt5.QtWidgets.QTabWidget(self.StackList['self.stack'+str(4)])
        self.tab1 = PyQt5.QtWidgets.QWidget()
        self.tab2 = PyQt5.QtWidgets.QWidget()
        self.tab3 = PyQt5.QtWidgets.QWidget()
        self.TabWidget.addTab(self.tab1, "短波 1")
        self.TabWidget.addTab(self.tab2, "短波 2")
        self.TabWidget.addTab(self.tab3, "短波 3")
        self.Tabcat1 = PyQt5.QtWidgets.QHBoxLayout()
        self.Tabcat2 = PyQt5.QtWidgets.QHBoxLayout()
        self.Tabcat3 = PyQt5.QtWidgets.QHBoxLayout()
        [self.Tabcat1.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.ZBDBButton]
        [self.Tabcat2.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.ZBDBButton]
        [self.Tabcat3.addWidget(PyQt5.QtWidgets.QRadioButton(i)) for i in self.ZBDBButton]
        self.tab1.setLayout(self.Tabcat1)
        self.tab2.setLayout(self.Tabcat2)
        self.tab3.setLayout(self.Tabcat3)
        Stack2.addWidget(self.TabWidget)
        Title = PyQt5.QtWidgets.QLabel(self.StackList['self.stack'+str(2)])
        Title.setText('短波')
        Title.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        TitleLayout.addWidget(Title)
        Main.addLayout(TitleLayout)
        Main.addLayout(Stack2)
        self.StackList['self.stack'+str(4)].setLayout(Main)


    
if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    the_mainwindow = MainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())