#создай приложение для запоминания информации
    # Подключение модулей
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup  
    # Создание класса
class Question():
    def __init__(self, question, r_answer, w2, w3, w4):
        self.question = question
        self.r_answer = r_answer
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
    # Создание списка с вопросами
question_list = []
question_list.append(Question('Алгоритм, написанный на языке программирования с уникальным именем?','Функция', 'Переменная', 'Список','Программа'))
question_list.append(Question('Функция для печати данных?','print()', 'Такой фунции нет', 'input()','list()'))
question_list.append(Question('Функция для ввода данных с клавиатуры?','input()', 'print()', 'int()','Такой фунции нет'))
question_list.append(Question('Что такое if и else?','Условные операторы', 'Переменные', 'Функции','Параметры'))
question_list.append(Question('Как с английского переводится while?','Пока', 'Если', 'Иначе','Когда'))
question_list.append(Question('Переменная, хранящая число шагов цикла?', 'Счётчик', 'Нет такой переменной','Хранитель', 'Список'))
question_list.append(Question('Функция, создающая последовательность в указанном диапазоне?', 'range()', 'Нет такой функции','randint()', 'str()'))
question_list.append(Question('Какого модуля НЕТ в стандартной библиотеке Pyton?', 'PyQt5', 'random','time', 'turtle'))
question_list.append(Question('Упорядоченный набор пар вида «ключ-значение»?', 'Словарь', 'Список','Переменная', 'Класс'))
question_list.append(Question('Переменная, помещённая внутрь объекта?', 'Свойство', 'Метод','Функция', 'Класс'))

#shuffle(question_list)
    # Создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.move(900,70)
main_win.resize(400,200)
    # Создание виджитов
vopros = QLabel('Самый сложный вопрос в мире!')
button_1 = QPushButton('Ответить')
    # Создание главной вертикальной линии
v_line = QVBoxLayout()
main_win.setLayout(v_line)
    # Создание горизонтальных линий
g_line_vopros = QHBoxLayout()
g_line_to_answer = QHBoxLayout()
g_line_for_box = QHBoxLayout()
    # Рассположение вопроса
g_line_vopros.addWidget(vopros, alignment = Qt.AlignCenter)
v_line.addLayout(g_line_vopros)
    # Создание 1-ой коробки
Box1 = QGroupBox('Варианты ответов:')
g_line_for_box.addWidget(Box1, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
v_line.addLayout(g_line_for_box)
    # Растягивание 1-ой коробки
g_line_for_box.addStretch(5)
g_line_for_box.addWidget(Box1, stretch=80)
g_line_for_box.addStretch(5)
    # Создание переключателей
answer1 = QRadioButton('Вариант1')
answer2 = QRadioButton('Вариант2')
answer3 = QRadioButton('Вариант3')
answer4 = QRadioButton('Вариант4')
    # Объединение переключателей в группу
group = QButtonGroup()
group.addButton(answer1)
group.addButton(answer2)
group.addButton(answer3)
group.addButton(answer4)
    # Создание вертикальных линий внутри коробки
v_line_1 = QVBoxLayout()
v_line_2 = QVBoxLayout()
    # Создание горизонтальной линии внутри коробки
g_line_box1 = QHBoxLayout()
    # Рассположение переключателей и коробки
v_line_1.addWidget(answer1)
v_line_2.addWidget(answer2)
v_line_1.addWidget(answer3)
v_line_2.addWidget(answer4)
g_line_box1.addLayout(v_line_2)
g_line_box1.addLayout(v_line_1)
Box1.setLayout(g_line_box1)   # Горозонтальную линию применяем к коробке
v_line.addLayout(g_line_box1)

v_line_1.setSpacing(10)
v_line_2.setSpacing(10)

    # Создание 2-ой коробки
Box2 = QGroupBox('Результат теста:')
g_line_for_box.addWidget(Box2, alignment = Qt.AlignCenter)
    # Расстягивание 2-ой коробки
g_line_for_box.addStretch(5)
g_line_for_box.addWidget(Box2, stretch=80)
g_line_for_box.addStretch(5)
    # Создание надписей
T_or_F = QLabel('Правильно/Неправильно')
True_answer = QLabel('Правильный ответ')
    # Создание горизонтальных линий внутри 2-ой коробки
g_line_box2_TF = QHBoxLayout()
g_line_box2_True = QHBoxLayout()
    # Создание вертикальной линии внутри 2-ой коробки
v_line_box2 = QVBoxLayout()
    # Расположение надписей и коробки
g_line_box2_TF.addWidget(T_or_F, alignment = Qt.AlignLeft)
g_line_box2_True.addWidget(True_answer, alignment = Qt.AlignHCenter)
v_line_box2.addLayout(g_line_box2_TF)
v_line_box2.addLayout(g_line_box2_True)
Box2.setLayout(v_line_box2)
v_line.addLayout(v_line_box2)
    # Отступ во 2-ой коробке
v_line_box2.setSpacing(20)
    # Скрытие 2-ой коробки
Box2.hide()
    # Рассположение кнопки 'Ответить'
g_line_to_answer.addWidget(button_1, alignment = Qt.AlignCenter)
v_line.addLayout(g_line_to_answer)
    # Расстягивание кнопки 'Следующий вопрос'
g_line_to_answer.addStretch(1)
g_line_to_answer.addWidget(button_1, stretch=2)
g_line_to_answer.addStretch(1)
    # Отступ
v_line.setSpacing(20)
    # Создание функций обработки
def show_result():   # Функция обрабатывает нажатие на 'Ответить'
    Box1.hide()
    Box2.show()
    button_1.setText('Следующий вопрос')
    
def show_question():  # Фукция обрабатывает нажатие на 'Следующий вопрос'
    Box2.hide()
    Box1.show()
    button_1.setText('Ответить')
    # Сброс переключателей
    group.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    group.setExclusive(True)
  
def start_test():
    if button_1.text() == 'Ответить':
        show_result()
    else:
        show_question()
    # Создание списка с ответами
answers = [answer1, answer2, answer3, answer4]
def ask(q: Question):
    shuffle(answers)   # Перемешиваем переключатели
    vopros.setText(q.question)
    answers[0].setText(q.r_answer)
    answers[1].setText(q.w2)
    answers[2].setText(q.w3)
    answers[3].setText(q.w4)
    True_answer.setText(q.r_answer)
    show_question()

def show_correct(res):
    T_or_F.setText(res)   
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Правильных ответов: ',main_win.score)
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')
    else:
        print('Ошибка! Выберите вариант ответа!')  
    reting = round((main_win.score/main_win.total)*100)
    print('Рейтинг: ',reting,'%')


def next_question():   # Функция для перехода между вопросами
    main_win.total += 1
    print('СТАТИСТИКА')
    print('Всего вопросов: ',main_win.total)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
    main_win.cur_question += 1
    '''if main_win.cur_question == len(question_list):
        main_win.cur_question = 0
        shuffle(question_list)
        q = question_list[main_win.cur_question]
        ask(q)'''
        
def click_ok():     # Функция для переключения вопросов
    button_1.text()
    if button_1.text() == 'Ответить':
        check_answer()    
    else:
        next_question()

main_win.total = 0
main_win.score = 0
main_win.cur_question = -1

next_question()
button_1.clicked.connect(click_ok)   

    # Отображение окна приложения
main_win.show()
app.exec_()