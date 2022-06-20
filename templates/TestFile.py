import random
from PyQt5 import uic
from PyQt5.QtWidgets import *
from templates import MainFile
import os


class TestForm(QMainWindow):
    def __init__(self, name, value):
        self.sum = 0
        super(TestForm, self).__init__()
        uic.loadUi('templates/TestForm.ui', self)
        self.name = name
        self.value = value
        self.pushButtonNext.clicked.connect(self.next_push)
        self.pushButtonFinish.clicked.connect(self.finish)

    def test_on(self, name, list_of_pairs):
        self.result = 0
        self.name = name
        self.list_of_pairs = list_of_pairs
        questions_not_ready = []
        questions_ready = []
        file = open('templates/questions_safety.txt', 'r', encoding='utf-8')
        self.get_questions_ready(file, questions_not_ready, questions_ready)

    def get_questions_ready(self, file, questions_not_ready, questions_ready):
        for line in file:
            questions_not_ready.append(line.split(':'))
        randoms = self.get_four_random_values()
        for line in randoms:
            questions_ready.append(questions_not_ready[line])
        self.unpack(questions_ready)

    def unpack(self, questions_ready):
        self.a1 = questions_ready[0][1].split()
        self.a2 = questions_ready[1][1].split()
        self.a3 = questions_ready[2][1].split()
        self.a4 = questions_ready[3][1].split()

        mas = [self.a1, self.a2, self.a3, self.a4]
        for m in mas:
            for i in range(len(m)):
                if m[i][0] == '!':
                    m.append(i)
                    m[i] = m[i][1:]

        self.labelQ1.setText(questions_ready[0][0])
        self.boxQ11.setText(mas[0][0])
        self.boxQ12.setText(mas[0][1])
        self.boxQ13.setText(mas[0][2])
        self.boxQ14.setText(mas[0][3])

        self.labelQ2.setText(questions_ready[1][0])
        self.boxQ21.setText(mas[1][0])
        self.boxQ22.setText(mas[1][1])
        self.boxQ23.setText(mas[1][2])
        self.boxQ24.setText(mas[1][3])

        self.labelQ3.setText(questions_ready[2][0])
        self.boxQ31.setText(mas[2][0])
        self.boxQ32.setText(mas[2][1])
        self.boxQ33.setText(mas[2][2])
        self.boxQ34.setText(mas[2][3])

        self.labelQ4.setText(questions_ready[3][0])
        self.boxQ41.setText(mas[3][0])
        self.boxQ42.setText(mas[3][1])
        self.boxQ43.setText(mas[3][2])
        self.boxQ44.setText(mas[3][3])

    def next_push(self):
        self.calculate()
        self.labelConst.setText('Пожарная безопасность')
        self.to_zero()
        self.pushButtonNext.setEnabled(False)
        self.pushButtonFinish.setEnabled(True)
        self.test_second_part()

    def test_second_part(self):
        questions_not_ready = []
        questions_ready = []
        file = open('templates/questions_fire.txt', 'r', encoding='utf-8')
        self.get_questions_ready(file, questions_not_ready, questions_ready)
        file.close()

    def finish(self):
        points = self.calculate()
        print('CHECK!')
        print(points)
        if points >= 6:
            self.result = '2'
        elif points >= 4:
            self.result = '1'
        else:
            self.result = '0'
        print(self.result)
        print(self.list_of_pairs)

        self.show_main()

    def show_main(self):
        with open('employees.txt', encoding='utf-8') as infile, open('output.txt', "w", encoding='utf-8') as outfile:
            for line in infile:
                if line.split()[0] != self.name:
                    outfile.write(line)
                else:
                    output_line = line.split()[0] + ' ' + line.split()[1] + ' ' + str(self.result) + '\n'
                    outfile.write(output_line)
        os.remove('employees.txt')
        os.rename('output.txt', 'employees.txt')

        self.window = MainFile.MainForm(self.name, self.list_of_pairs, self.result)
        self.window.show()
        self.close()
        self.window.show_info()

    def calculate(self):
        mas = [self.a1, self.a2, self.a3, self.a4]
        m = []
        if self.boxQ11.checkState(): m.append(0)
        if self.boxQ12.checkState(): m.append(1)
        if self.boxQ13.checkState(): m.append(2)
        if self.boxQ14.checkState(): m.append(3)

        if len(m) == 1 and m[0] == mas[0][-1]:
            self.sum += 1

        m = []
        if self.boxQ21.checkState(): m.append(0)
        if self.boxQ22.checkState(): m.append(1)
        if self.boxQ23.checkState(): m.append(2)
        if self.boxQ24.checkState(): m.append(3)

        if len(m) == 1 and m[0] == mas[1][-1]:
            self.sum += 1

        m = []
        if self.boxQ31.checkState(): m.append(0)
        if self.boxQ32.checkState(): m.append(1)
        if self.boxQ33.checkState(): m.append(2)
        if self.boxQ34.checkState(): m.append(3)

        if len(m) == 1 and m[0] == mas[2][-1]:
            self.sum += 1

        m = []
        if self.boxQ41.checkState():
            m.append(0)
        if self.boxQ42.checkState():
            m.append(1)
        if self.boxQ43.checkState():
            m.append(2)
        if self.boxQ44.checkState():
            m.append(3)

        if len(m) == 1 and m[0] == mas[3][-1]:
            self.sum += 1
        return self.sum

    def to_zero(self):
        self.boxQ11.setChecked(False)
        self.boxQ12.setChecked(False)
        self.boxQ13.setChecked(False)
        self.boxQ14.setChecked(False)

        self.boxQ21.setChecked(False)
        self.boxQ22.setChecked(False)
        self.boxQ23.setChecked(False)
        self.boxQ24.setChecked(False)

        self.boxQ31.setChecked(False)
        self.boxQ32.setChecked(False)
        self.boxQ33.setChecked(False)
        self.boxQ34.setChecked(False)

        self.boxQ41.setChecked(False)
        self.boxQ42.setChecked(False)
        self.boxQ43.setChecked(False)
        self.boxQ44.setChecked(False)

    @staticmethod
    def get_four_random_values():
        randoms = []
        while len(randoms) <= 3:
            a = random.randint(0, 7)
            if a not in randoms:
                randoms.append(a)
        return randoms
