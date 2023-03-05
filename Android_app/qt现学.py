import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QLineEdit,QVBoxLayout,QRadioButton,QGroupBox,QScrollArea
from PyQt5.QtCore import pyqtSignal
#print(sys.argv,'5555')

class test(QWidget):

    sig = pyqtSignal(str) #自定义信号必须放在类属性里面定义而不能放在方法中/实例中?
    #使用 self.sig.emit("str这里可以放置一些消息")
    #接收的话使用 btn.sig.connect(abc)
    #连接槽函数的话需要def abc(self,msg:str)


    def boot(self):
        
        #self.sig.connect(self.printOnScr)  你写成递归了
        self.sig.emit(f"str这里可以放置一些消息{self.i}")
        self.i = self.i + 1
        

    def printOnScr(self,msg1:str):
        self.msg_his.append(msg1)
        self.msg.resize(440,self.msg.frameSize().height() + 15)
        self.msg.setText('\n'.join(self.msg_his))
        self.msg.repaint()

    def init2(self):
        self.i = 0
        self.sig.connect(self.printOnScr)
        self.msg = QLabel("")
        self.msg.resize(440,20)
        self.msg.setWordWrap(True) #自动换行
        #self.msg.setAlignment(Qt.alignTop) #靠上边

        scroll = QScrollArea()
        scroll.setGeometry(200,200,440,90)
        scroll.setWidget(self.msg)
        

        v_lay = QVBoxLayout()
        v_lay.addWidget(scroll) #相当于添加自动滚动条 滚动一定要配合布局器使用

        boxgrp = QGroupBox('',self) #必须需要一个容器,否则滚动区域会覆盖全屏幕
        boxgrp.setLayout(v_lay)
        boxgrp.setGeometry(200,200,440,520)
        #boxgrp.setParent(self)
        

        self.msg_his = []

    def __init__(self,*args,**kwargs):
        super().__init__()
        

        self.setWindowTitle('123123123')
        self.resize(1233,1233)

        btn1 = QPushButton('按钮1')
        btn2 = QRadioButton('按钮2')
        btn1.clicked.connect(self.boot)
        btn3 = QPushButton('按钮3')

        self.boxgrp = QGroupBox('123',self)

        self.v_lay = QVBoxLayout()
        self.v_lay.addWidget(btn1)
        self.v_lay.addWidget(btn2)
        self.v_lay.addWidget(btn3)

        self.boxgrp.setLayout(self.v_lay)

        self.init2()

    

if __name__ == '__main__':
    #print(sys.argv,'5555')
    app = QApplication(sys.argv)
    w = test()
    #w.resize(1233,1233)
    #btn = QPushButton('按钮')
    #btn.setParent(w)
    #btn.clicked.connect(test) #注册一个clicked时的回调


    #label = QLabel("账号",w)
    #label.setGeometry(20,20,30,34) #x,y,w,h

    #edt = QLineEdit(w)
    #edt.setPlaceholderText('请输入')
    #edt.setGeometry(55,20,200,20)

    # btn2 = QPushButton('按钮2',label)

    w.show()
    app.exec_()