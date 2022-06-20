file = open('templates/questions_safety.txt', 'r', encoding='utf-8')

list1 = []
for line in file:
    list1.append(line.split(':'))

print(list1)

self.labelQ1.setText(questions_ready[0][0])
self.boxQ11.setText(questions_ready[0][1])
self.boxQ12.setText(questions_ready[0][2])
self.boxQ13.setText(questions_ready[0][3])
self.boxQ14.setText(questions_ready[0][4])

self.labelQ2.setText(questions_ready[1][0])
self.boxQ21.setText(questions_ready[1][1])
self.boxQ22.setText(questions_ready[1][2])
self.boxQ23.setText(questions_ready[1][3])
self.boxQ24.setText(questions_ready[1][4])

self.labelQ3.setText(questions_ready[2][0])
self.boxQ31.setText(questions_ready[2][1])
self.boxQ32.setText(questions_ready[2][2])
self.boxQ33.setText(questions_ready[2][3])
self.boxQ34.setText(questions_ready[2][4])

self.labelQ4.setText(questions_ready[3][0])
self.boxQ41.setText(questions_ready[3][1])
self.boxQ42.setText(questions_ready[3][2])
self.boxQ43.setText(questions_ready[3][3])
self.boxQ44.setText(questions_ready[3][4])
