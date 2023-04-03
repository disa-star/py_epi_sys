# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form - untitlednHlxfq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(476, 495)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(110, 240, 232, 175))
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 230, 173))
        self.scrollAreaWidgetContents.setMouseTracking(False)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 231, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 231, 31))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 0, 75, 23))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 0, 101, 21))
        self.label.setAutoFillBackground(True)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(200, 0, 21, 23))
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 30, 231, 31))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 0, 81, 23))
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(200, 0, 21, 23))
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 60, 231, 31))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 0, 81, 23))
        self.radioButton = QRadioButton(self.frame_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(93, 4, 101, 16))
        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(200, 1, 21, 21))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(110, 70, 221, 80))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_5)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u8eab\u4efd\u7801", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4e0a\u6b21\u66f4\u65b0:xxx", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"i", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u542f\u6fc0\u8fdb\u6a21\u5f0f", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"i", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4e0a\u62a5\u6570\u636e", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u8bb0\u5f55\u5e76\u4e0a\u62a5\u65f6\u95f4", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"i", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9644\u8fd1\u7528\u6237\u6570\u91cf", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"123", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u53ef\u89c2\u6d4b\u9633\u6027\u60a3\u8005\u6570\u91cf", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"456", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u98ce\u9669\u9884\u4f30", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8f83\u9ad8", None))
    # retranslateUi


# 主函数
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()     # 创建窗体对象
    ui = Ui_Form()      # 创建PyQt5设计的窗体对象
    MainWindow.show()      # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    ui.setupUi(MainWindow)     # 显示窗体
    sys.exit(app.exec_())     # 程序关闭时退出进程