from PyQt5 import uic
from PyQt5.QtWidgets import *
from templates import TestFile
import smtplib


class MainForm(QMainWindow):
    def __init__(self, name, listarg, result):
        super(MainForm, self).__init__()
        self.text = None
        uic.loadUi('templates/MainForm.ui', self)
        self.result = result
        self.window = None
        self.name = name
        self.listarg = listarg
        self.value_of_correct_tests = '0'
        # functions
        self.pushButtonTake.clicked.connect(self.show_test)
        self.pushButtonSend.clicked.connect(self.send_message)

    def show_info(self):
        self.lineEditName.setText(self.name)
        '''
        for i in range(len(self.listarg)):
            if self.listarg[i][0] == self.name:
                self.value_of_correct_tests = self.listarg[i][2]
        '''

        file = open('employees.txt', 'r', encoding='utf-8')
        for line in file:
            if line.split()[0] == self.name:
                self.value_of_correct_tests = line.split()[2]
        file.close()

        self.lineEditHowMuch.setText(f'Value of correct tests: {self.value_of_correct_tests}')

    def show_test(self):
        if int(self.value_of_correct_tests) > 0:
            message = QMessageBox()
            message.setText('Tests already done!')
            message.exec_()
        else:
            self.window = TestFile.TestForm(self.name, self.value_of_correct_tests)
            self.window.show()
            self.close()
            self.window.test_on(self.name, self.listarg)

    def unpack_message(self):
        return f'{self.lineEditName.text()} : {self.lineEditProblem.text()}'

    def send_message(self):
        self.text = self.unpack_message()
        sender = 'kidavdey71@gmail.com'
        password = 'qwerty015370'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        message = QMessageBox()
        message.setText('Message sent!')
        message.exec_()
        file = open('templates/Problems', 'a', encoding='utf-8')
        file.write(f'{self.text}\n')
        file.close()
        self.lineEditProblem.setText('')
        try:
            server.login(sender, password)
            server.sendmail(sender, sender, self.text)
            return 'Done!'
        except Exception as _ex:
            return f'{_ex}\nInvalid mail or password'




