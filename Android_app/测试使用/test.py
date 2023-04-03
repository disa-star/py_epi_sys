from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5 import QtBluetooth

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 294)
        MainWindow.setWindowTitle("双色球彩票选号器")    # 设置窗口标题
        # 设置窗口背景图片
        MainWindow.setStyleSheet("border-image: url(./image/双色球彩票选号器.png)")
        self.centralwidget=QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建第一个红球数字的标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(97, 178,31, 31))
        # 设置标签的字体
        font = QtGui.QFont()    # 创建字体对象
        font.setPointSize(16)    # 设置字体大小
        font.setBold(True)      # 设置粗体
        font.setWeight(75)    # 设置字体
        self.label.setFont(font)    # 为标签设置字体
        # 设置标签的文字颜色
        self.label.setStyleSheet("color:rgb(255,0,0);")
        self.label.setObjectName("label")

        # 第2、3、4、5、6个红球和一个蓝球标签的代码的创建及设置代码与第一个红球标签的代码一样
        # 创建第2个红球
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(128, 178, 31, 31))
        self.label_2.setGeometry(QtCore.QRect(134, 178, 31, 31))
        self.label_2.setFont(font)  # 为标签设置字体
        self.label_2.setStyleSheet("color:rgb(255,0,0);")  # 设置标签的文字颜色
        self.label_2.setObjectName("label_2")
        # 创建第3个红球
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(159, 178, 31, 31))
        self.label_3.setGeometry(QtCore.QRect(171, 178, 31, 31))
        self.label_3.setFont(font)  # 为标签设置字体
        self.label_3.setStyleSheet("color:rgb(255,0,0);")  # 设置标签的文字颜色
        self.label_3.setObjectName("label_3")
        # 创建第4个红球
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(190, 178, 31, 31))
        self.label_4.setGeometry(QtCore.QRect(205, 178, 31, 31))
        self.label_4.setFont(font)  # 为标签设置字体
        self.label_4.setStyleSheet("color:rgb(255,0,0);")  # 设置标签的文字颜色
        self.label_4.setObjectName("label_4")
        # 创建第个5红球
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(221, 178, 31, 31))
        self.label_5.setGeometry(QtCore.QRect(239, 178, 31, 31))
        self.label_5.setFont(font)  # 为标签设置字体
        self.label_5.setStyleSheet("color:rgb(255,0,0);")  # 设置标签的文字颜色
        self.label_5.setObjectName("label_5")
        # 创建第6个红球
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        # self.label_6.setGeometry(QtCore.QRect(252, 178, 31, 31))
        self.label_6.setGeometry(QtCore.QRect(273, 178, 31, 31))
        self.label_6.setFont(font)  # 为标签设置字体
        self.label_6.setStyleSheet("color:rgb(255,0,0);")  # 设置标签的文字颜色
        self.label_6.setObjectName("label_6")
        # 创建第7个红球
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(283, 178, 31, 31))
        self.label_7.setGeometry(QtCore.QRect(307, 178, 31, 31))
        self.label_7.setFont(font)  # 为标签设置字体
        self.label_7.setStyleSheet("color:rgb(0,0,255);")  # 设置标签的文字颜色
        self.label_7.setObjectName("label_7")

        # 创建“开始”按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 235, 51, 51))
        # 设置按钮的背景图片
        self.pushButton.setStyleSheet("border-image: url(./image/开始.png);")
        self.pushButton.setText("1")
        self.pushButton.setObjectName("pushButton")
        # 创建“停止”按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 235, 51, 51))
        # 设置按钮的背景图片
        self.pushButton_2.setStyleSheet("border-image: url(./image/停止.png);")
        self.pushButton_2.setText("2")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        # 初始化双色球数字的Label标签的默认文本
        self.label.setText("00")
        self.label_2.setText("00")
        self.label_3.setText("00")
        self.label_4.setText("00")
        self.label_5.setText("00")
        self.label_6.setText("00")
        self.label_7.setText("00")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 设置显示双色球数字的Label标签背景透明
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_3.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_4.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_5.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_6.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_7.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 为“开始”按钮绑定单击信号
        self.pushButton.clicked.connect(self.start)
        # 为“停止”按钮绑定单击信号
        self.pushButton_2.clicked.connect(self.stop)


        

    # 自定义槽函数，用来开始计时器
    def start(self):
        self.timer = QTimer(MainWindow)    # 创建计时器对象
        self.timer.start()     # 开始计时器
        self.timer.timeout.connect(self.num)      # 设置计时器要执行的槽函数

       


    # 定义槽函数，用来设置7个Label标签中的数字
    def num(self):
        import random
        self.label.setText("{0:02d}".format(random.randint(1, 33)))     # 随机生成第一个红球数字
        self.label_2.setText("{0:02d}".format(random.randint(1, 33)))     # 随机生成第二个红球数字
        self.label_3.setText("{0:02d}".format(random.randint(1, 33)))     # 随机生成第三个红球数字
        self.label_4.setText("{0:02d}".format(random.randint(1, 33)))     # 随机生成第四个红球数字
        self.label_5.setText("{0:02d}".format(random.randint(1, 33)))     # 随机生成第五个红球数字
        self.label_6.setText("{0:02d}".format(random.randint(1, 33)))     # 随机生成第六个红球数字
        self.label_7.setText("{0:02d}".format(random.randint(1, 16)))     # 随机生成蓝球数字

    # 定义槽函数，用来停止计时器
    def stop(self):
        self.timer.stop()
        

# 主函数
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()     # 创建窗体对象
    ui = Ui_MainWindow()      # 创建PyQt5设计的窗体对象
    MainWindow.show()      # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    ui.setupUi(MainWindow)     # 显示窗体
    sys.exit(app.exec_())     # 程序关闭时退出进程
