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

lab = QLabel('The first thing that struck me on landing in America was that if the Americans are not the most well-dressed people in the world, they are the most comfortablydressed. Men are seen there with the dreadful chimney-pothat, but there are very few hatless men; men wear theshocking swallow-tail coat, but few are to be seen with no coat at all. There is an air of comfort in the appearance of the people which is a marked contrast to that seen in this country, where, too often, people are seen in close contact with rags.\n\
             The next thing particularly noticeable is that everybody seems in a hurry to catch a train. This is a state of things which is not favourable to poetry or romance. Had Romeo or Juliet been in a constant state of anxiety about trains, or had their minds been agitated° by the question of return-tickets, Shakespeare could not have given us those lovely balcony scenes which are so full of poetry and pathos.\n\
             America is the noisiest country that ever existed. One is waked up in the morning, not by the singing of the nightingale, but by the steam whistle. It is surprising that the sound practical sense of the Americans does not reduce this intolerable noise. All Art depends upon exquisite and delicate sensibility, and such continual turmoil must ultimately be destructive of the musical faculty\n\
             There is not so much beauty to be found in American cities as in Oxford, Cambridge, Salisbury or Winchester, where are lovely relics of a beautiful age; but still there is a good deal of beauty to be seen in them now and then, but only where the American has not attempted to create it. Where the Americans have attempted to produce beauty they have signally° failed. A remarkable characteristic of the Americans is the manner in which they have applied science to modern life.',w)
lab.setGeometry(0,0,2300,400)
lab.setWordWrap(True)
lab.setStyleSheet("color:#BCBCBE;")

w.show()
app.exec_()