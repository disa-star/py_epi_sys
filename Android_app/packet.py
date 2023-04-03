from PyQt5 import uic
from PyQt5.QtWidgets import *
class Select:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("1.ui")

if __name__ == "__main__":
    app = QApplication([])
    select = Select()
    select.ui.show()
    app.exec_()