from PyQt5 import QtBluetooth
from PyQt5.QtBluetooth import QBluetoothSocket
from PyQt5.QtCore import QIODevice, QByteArray, QTimer
#import bluetooth
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 294)
        MainWindow.setWindowTitle("双色球彩票选号器")    # 设置窗口标题
        
        self.centralwidget=QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建第一个红球数字的标签
        

        # 创建“开始”按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 235, 51, 51))
        self.pushButton.setText("开")
        self.pushButton.setObjectName("pushButton")

        # 创建“停止”按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 235, 51, 51))
        self.pushButton_2.setText("停")
        self.pushButton_2.setObjectName("pushButton_2")
        
        #本地按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 235, 51, 51))
        self.pushButton_3.setText("本地")
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        # 为“开始”按钮绑定单击信号
        self.pushButton.clicked.connect(self.start_scan)
        # 为“停止”按钮绑定单击信号
        self.pushButton_2.clicked.connect(self.stop)
        # 为“本地”按钮绑定单击信号
        self.pushButton_3.clicked.connect(self.localSetUp)

        MainWindow.setCentralWidget(self.centralwidget)
        #查找远程设备
        self.agent = QtBluetooth.QBluetoothDeviceDiscoveryAgent()
        self.agent.deviceDiscovered.connect(lambda deviceInfo: print(deviceInfo.name()))

        #获取本地设备信息
        self.localDevice = QtBluetooth.QBluetoothLocalDevice()

        #连接使用
        self.socket = QtBluetooth.QBluetoothSocket(QtBluetooth.QBluetoothServiceInfo.RfcommProtocol)
        self.socket.connected.connect(lambda:print('连接到了'))
        self.socket.disconnected.connect(lambda:print('连接么了'))
        self.socket.readyRead.connect(lambda:print('准备发信'))

    # 自定义槽函数，用来开始计时器
    def start_scan(self):
        self.timer = QTimer(MainWindow)    # 创建计时器对象
        self.timer.timeout.connect(self.agent.stop)      # 设置计时器要执行的槽函数
        self.timer.timeout.connect(self.timer.stop)      # 设置计时器要执行的槽函数
        self.timer.timeout.connect(lambda:print('计时结束'))      # 设置计时器要执行的槽函数
        self.timer.start(4000)     # 开始计时器
        self.agent.start()

        

    def localSetUp(self):
        print(self.localDevice.name())
        self.localDevice.setHostMode(2)
        #self.localDevice.powerOn() #调用打开本地的蓝牙设备
        print(self.localDevice.hostMode())
        if self.localDevice.hostMode() == QtBluetooth.QBluetoothLocalDevice.HostPoweredOff:
            print('本地蓝牙关机, 开机中')
            self.localDevice.powerOn() #调用打开本地的蓝牙设备
    

    # 定义槽函数，用来停止计时器
    def stop(self):
        #self.timer.stop()
        self.agent.stop()


    def connect(self, address):
        self.socket.connectToService(address, QtBluetooth.QBluetoothUuid.SerialPort)

    def disconnect(self):
        self.socket.disconnectFromService()

    def send_data(self, data):
        if self.socket.state() == QIODevice.ConnectedState:
            self.socket.write(QByteArray(data.encode()))


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







else:
    #address = "AA:BB:CC:DD:EE:FF"
    address = '8c:7a:3d:bb:a1:ce'
    service_uuid = QtBluetooth.QBluetoothUuid.ProtocolUuid.Rfcomm
    #print()
#service_uuid = "00001101-0000-1000-8000-00805F9B34FB"
#print(service_uuid)
    socket = QBluetoothSocket(QtBluetooth.QBluetoothServiceInfo.RfcommProtocol)
    socket.connectToService(QtBluetooth.QBluetoothAddress(address), QtBluetooth.QBluetoothUuid(service_uuid), QIODevice.ReadWrite)
#print(dir(socket))
    if socket.waitForReadyRead(100000):
        socket.write(QByteArray("Hello World!"))
        socket.flush()
        print(2)
        socket.disconnectFromService()
    else:
        print('connect failed!')
