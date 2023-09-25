from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QButtonGroup, QWidget,QHBoxLayout, QVBoxLayout,QGroupBox, QRadioButton,QPushButton, QLabel)
class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = list()
questions_list.append(Question('Азерабайджан', 'помидоры', 'фуфулшмерц', 'а она ему как раз', 'носки с сандалями'))#1
questions_list.append(Question('АА','dfff','ff','ff','fgegehbegvgbvgfsdbffsvgbgfdfvbfdfbfcv'))#2
questions_list.append(Question('sdfwewf','fefeef','efefeffe','feef','feeffe'))#3
questions_list.append(Question('было 2 верблюда, сколько?', '228','1337','112','у меня 9 детей в подвале'))#4
questions_list.append(Question('не','жный','мой','рпа','гр'))#5
questions_list.append(Question('кто там?','бульбулятор','разетка','фифтифайф','прокаст в крипа'))#6
questions_list.append(Question('ясли','тысли','мысли','высли','онисли'))#7
questions_list.append(Question('черный','красный','зеленый','синий','нет правильного варианта'))#8
questions_list.append(Question('купался мужик в реке','+2 или -2','а она ему как раз','и сгорел','а там армяне в нарды играют'))#9
questions_list.append(Question('марс','плутон','плутя','плутона','плутмы'))#10

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line3.addWidget(btn_OK)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)


AnsGroupBox = QGroupBox("Резуьтат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)
layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide()
layout_line3.addWidget(btn_OK, stretch=2)
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов', window.total, '\n-Правильных ответов:', window.score)
    cur_quetion = randint(0, len(questions_list) - 1)
    q = questions_list[cur_quetion]
    ask(q)
def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def ask(q:  Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!') 
        window.score += 1
        print('Статистика\n-Всего вопросов', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг: ', (window.score/window.total*100, '%'))
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')



answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score = 0
window.total = 0
window.cur_quetion = -1
btn_OK.clicked.connect(click_ok) # проверяем, что панель ответов показывается при нажатии на кнопку
next_question()

window.show()
app.exec()