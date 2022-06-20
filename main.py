from PyQt5 import uic
from PyQt5.QtWidgets import *
from templates import LogFile


def main():
    app = QApplication([])
    window = LogFile.LogForm()
    app.exec_()


if __name__ == '__main__':
    main()
