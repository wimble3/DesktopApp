from PyQt5 import uic
from PyQt5.QtWidgets import *
from templates import MainFile


class LogForm(QMainWindow):
    def __init__(self):
        super(LogForm, self).__init__()
        self.window = None
        uic.loadUi('templates/LogForm.ui', self)
        self.show()
        # functions
        self.pushButtonLog.clicked.connect(self.login)
        self.pushButtonReg.clicked.connect(self.registration)

    def login(self):
        login_flag = False
        file = open('employees.txt', 'r', encoding='utf-8')
        list_of_pairs = []
        for line in file:
            list_of_pairs.append(line.split())

        for i in range(len(list_of_pairs)):
            if list_of_pairs[i] == [self.lineEditLog.text(), self.lineEditPas.text(), '0'] \
                    or list_of_pairs[i] == [self.lineEditLog.text(), self.lineEditPas.text(), '1'] \
                    or list_of_pairs[i] == [self.lineEditLog.text(), self.lineEditPas.text(), '2']:
                file.close()
                self.window = MainFile.MainForm(self.lineEditLog.text(), list_of_pairs, None)
                self.window.show()
                self.close()
                login_flag = True
                self.window.show_info()
        if not login_flag:
            message = QMessageBox()
            message.setText('Ivalid login')
            message.exec_()

    def registration(self):
        file = open('employees.txt', 'r', encoding='utf-8')
        mas_name = []
        for line in file:
            mas_name.append(line.split()[0])
        file.close()

        file = open('employees.txt', 'a', encoding='utf-8')
        if self.lineEditKeyReg.text() == 'secretkey' and self.lineEditLogReg.text() != '' \
                and self.lineEditPasReg.text() != '' and self.lineEditLogReg.text() not in mas_name:
            file.write(f'\n{self.lineEditLogReg.text()} {self.lineEditPasReg.text()} {0}')
            file.close()
            message = QMessageBox()
            message.setText('Registration successful')
            message.exec_()
        else:
            message = QMessageBox()
            message.setText('Ivalid key or log/par is empty or user already registered')
            message.exec_()




