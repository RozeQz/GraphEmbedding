import seaborn as sns
from fpdf import FPDF

from PyQt5.QtWidgets import (
    QWidget,
    QListWidgetItem)

from gui.ui_student_profile_page import Ui_StudentProfilePage
from gui.mplcanvas import MplCanvas

from src.api.results_controller import get_results_by_user, calc_average_percent, get_result_by_id
from src.api.tests_controller import get_test_tasks
from src.api.tasks_controller import get_task_by_id

from utils.gui import highlight_label
from utils.PDF import PDF
from utils.formatter import format_number, format_date


class StudentProfilePage(QWidget):
    def __init__(self, parent=None):
        super(StudentProfilePage, self).__init__(parent)
        self.ui = Ui_StudentProfilePage()
        self.ui.setupUi(self)

        self.parent = parent

        # Добавление холста для рисования пай чарта
        self.canvas = MplCanvas(self)
        self.ui.verticalLayout_3.addWidget(self.canvas)

        self.ui.btn_logout.clicked.connect(self.logout)
        self.ui.listWidget.itemDoubleClicked.connect(self.print_results)

    def refresh(self):
        '''
        Вызывается при обновлении страницы.
        Обновляет содержимое профиля.
        '''
        self.ui.lbl_surname.setText(self.parent.current_user.lastname)
        self.ui.lbl_name.setText(self.parent.current_user.firstname)
        self.ui.lbl_midname.setText(self.parent.current_user.midname)
        self.ui.lbl_group.setText(self.parent.current_user.groups[0].name)

        self.ui.lbl_num_tests.setText(f"{len(get_results_by_user(self.parent.current_user.id))}")
        average_percent = calc_average_percent(self.parent.current_user.id, obj="user")
        self.ui.lbl_avg_percent.setText(f"{average_percent:.2f}%")

        self.show_pie_chart()
        self.init_test_story()

    def init_test_story(self):
        self.ui.listWidget.clear()

        for i, result in enumerate(get_results_by_user(self.parent.current_user.id)):
            result_id = result['id']
            points = result['points']
            num_tasks = len(get_test_tasks(result['test_id']))
            time = format_date(result['created_at'])
            item = QListWidgetItem(f"{i+1}.\t №{result_id}\t Результат: {points}/{num_tasks}\t{time}")
            self.ui.listWidget.insertItem(0, item)

    def print_results(self, item):
        text = item.text().split('\t')
        # Удаляем символ №
        result_id = text[1][2:]

        result = get_result_by_id(result_id)

        pdf = PDF(logo_path='client/gui/resources/img/logo_black.png',
                  title="Отчет о результате тестирования")
        pdf.add_page()

        pdf.cell(40, 10, "ID Результата:", ln=0)
        pdf.tab(tab_size=5)
        pdf.cell(40, 10, f"{result_id}", ln=1)

        points = format_number(result["points"])
        pdf.cell(40, 10, "Результат:", ln=0)
        pdf.tab(tab_size=5)
        # TODO: заменить костыль /8 на реальное число вопросов в тесте
        pdf.cell(40, 10, f"{points}/8", ln=1)

        fio = self.parent.current_user.lastname + " " + \
            self.parent.current_user.firstname + " " + \
            self.parent.current_user.midname
        user_id = result["user_id"]
        pdf.cell(40, 10, "Студент:", ln=0)
        pdf.tab(tab_size=5)
        pdf.cell(40, 10, f"#{user_id} {fio}", ln=1)

        test_id = result["test_id"]
        pdf.cell(40, 10, "ID Теста:", ln=0)
        pdf.tab(tab_size=5)
        pdf.cell(40, 10, f"{test_id}", ln=1)

        created_at = format_date(result['created_at'])
        pdf.cell(40, 10, f"Время окончания тестирования: {created_at}", ln=1)

        time = result["time_spent"]
        minutes = time // 60
        seconds = time % 60
        pdf.cell(40, 10, "Затраченное время:", ln=0)
        pdf.tab(tab_size=5)
        pdf.cell(40, 10, f"{minutes:02}:{seconds:02}", ln=1)

        pdf.ln(5)
        pdf.cell(40, 10, "Вопросы и ответы:", ln=1)
        pdf.ln(5)
        answers = result["answers"]
        for i, answer in enumerate(answers):
            # Цвет ячейки
            if answer["correct"] is True:
                pdf.set_fill_color(168, 255, 196)
                pdf.set_draw_color(10, 207, 131)
            else:
                pdf.set_fill_color(255, 207, 201)
                pdf.set_draw_color(255, 92, 74)
            # Отступ
            pdf.tab()
            pdf.cell(10, 10, f"{i}", ln=0)
            task = get_task_by_id(answer["task_id"])["question"]
            answ = answer["answer"]
            if isinstance(answ, list):
                answ = "; ".join(answ)
            # Ячейка с переносом строки
            pdf.multi_cell(150, 10, f"{task}", new_x="LMARGIN")
            pdf.cell(20, 10, "Ответ:")
            pdf.multi_cell(150, 10, f"{answ}", border=1, fill=True)
            pdf.ln(5)

        pdf.output("simple_demo.pdf")

    def show_pie_chart(self):
        # Чистим холст
        self.canvas.axes.clear()

        # Инициализация возможных результатов
        points = {}
        for i in range(0, 8 + 1):
            points[i] = 0
        for result in get_results_by_user(self.parent.current_user.id):
            print(result)
            points[result["points"]] += 1

        # Удаляем нулевые значения
        # Для этого создаем копию ключей словаря
        keys_to_delete = [key for key, value in points.items() if value == 0]
        # А теперь удаляем
        for key in keys_to_delete:
            del points[key]

        labels = list(points.keys())
        sizes = list(points.values())
        explode = [0.01 for _ in range(len(sizes))]
        self.canvas.axes.pie(x=sizes,
                             labels=labels,
                             autopct='%1.1f%%',
                             startangle=90,
                             colors=sns.color_palette("tab20"),
                             # plot slices clockwise
                             counterclock=False,
                             # Add space around each slice
                             explode=explode)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        self.canvas.axes.axis('equal')
        self.canvas.axes.set_title("Диаграмма баллов за тесты")
        self.canvas.draw()

    def showEvent(self, event):
        # Вызывается при открытии страницы
        highlight_label(self.parent, self.parent.ui.lbl_profile)
        # Обновляем содержимое страницы
        self.refresh()

    def logout(self):
        print("Logout")
