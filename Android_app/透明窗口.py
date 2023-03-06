import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QLineEdit,QVBoxLayout,QRadioButton,QGroupBox,QScrollArea
from PyQt5.QtCore import pyqtSignal,Qt
#from PyQt5 import Qt


app = QApplication(sys.argv)
w = QWidget()

w.setWindowFlag(Qt.WindowType.FramelessWindowHint) #窗口无边框
w.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) #窗口背景透明
w.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)  # 设置 "AlwaysOnTop" 标志
w.setGeometry(50,1200,3000,400)

lab = QLabel('I would say to the House, as I said to those who have joined this Government: ‘I have nothing to offer but blood, toil, tears and sweat’.\n\
We have before us an ordeal of the most grievous kind. We have before us many, many long months of struggle and of suffering. You ask, what is our policy? I will say: It is to wage war, by sea, land and air, with all our might and with all the strength that God can give us; to wage war against a monstrous tyranny, never surpassed in the dark and lamentable catalogue of human crime. That is our policy\n\
You ask, what is our aim? I can answer in one word: it is victory, victory at all costs, victory in spite of all terror, victory, however long and hard the road may be; for without victory, there is no survival. Let that be realized; no survival for the British Empire, no survival for all that the British Empire has stood for, no survival for the urge and impulse of the ages, that mankind will move forward towards its goal. \n\
But I take up my task with buoyancy and hope. I feel sure that our cause will not be suffered to fail among men. At this time I feel entitled to claim the aid of all, and I say, ‘Come then, let us go forward together with our united strength',w)
lab.setGeometry(0,0,2300,400)
lab.setWordWrap(True)
lab.setStyleSheet("color:#BCBCBE;")

w.show()
app.exec_()