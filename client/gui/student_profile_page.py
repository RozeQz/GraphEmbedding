import seaborn as sns
from datetime import datetime

from PyQt5.QtWidgets import (
    QWidget,
    QListWidgetItem)

from gui.ui_student_profile_page import Ui_StudentProfilePage
from gui.mplcanvas import MplCanvas

from src.api.results_controller import get_results_by_user, calc_average_percent
from src.api.tests_controller import get_test_tasks

from utils.gui import highlight_label


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
            time = datetime.fromisoformat(result['created_at']).strftime("%Y-%m-%d %H:%M:%S")
            item = QListWidgetItem(f"{i+1}.\t №{result_id}\t Результат: {points}/{num_tasks}\t{time}")
            self.ui.listWidget.insertItem(0, item)

    def print_results(self, item):
        text = item.text().split('\t')
        # Удаляем символ №
        result_id = text[1][2:]

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
