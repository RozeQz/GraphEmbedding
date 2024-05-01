import os
import seaborn as sns
from typing import List, Optional

from PyQt5.QtWidgets import (
    QWidget,
    QListWidgetItem,
    QFileDialog,
    QSizePolicy)

from gui.ui_teacher_profile_page import Ui_TeacherProfilePage
from gui.mplcanvas import MplCanvas

from src.api.results_controller import (
    get_results_by_user,
    calc_average_percent)
from src.api.tests_controller import get_test_tasks
from src.api.tasks_controller import (
    get_all_tasks,
    get_user_tasks)
from src.api.groups_controller import get_group_users
from src.api.users_controller import get_user_by_id, get_user_data_by_id
from src.api.topics_controller import get_user_topics, get_all_topics
from src.education.group import Group
from src.education.user import User

from utils.gui import highlight_label
from utils.formatter import format_number, format_date
from utils.print_reports import print_results


class TeacherProfilePage(QWidget):
    def __init__(self, parent=None):
        super(TeacherProfilePage, self).__init__(parent)
        self.ui = Ui_TeacherProfilePage()
        self.ui.setupUi(self)

        self.parent = parent

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Привязка стилей
        with open(path + "styles/button/button-red.qss", 'r',
                  encoding="utf-8") as file:
            button_style = file.read()
            self.ui.btn_logout.setStyleSheet(button_style)

        with open(path + "styles/label/label-main.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.label.setStyleSheet(label_style)
            self.ui.label_2.setStyleSheet(label_style)
            self.ui.label_3.setStyleSheet(label_style)
            self.ui.label_4.setStyleSheet(label_style)
            self.ui.label_6.setStyleSheet(label_style)
            self.ui.label_7.setStyleSheet(label_style)
            self.ui.label_8.setStyleSheet(label_style)
            self.ui.label_9.setStyleSheet(label_style)
            self.ui.lbl_surname.setStyleSheet(label_style)
            self.ui.lbl_name.setStyleSheet(label_style)
            self.ui.lbl_midname.setStyleSheet(label_style)
            self.ui.lbl_group.setStyleSheet(label_style)
            self.ui.lbl_num_tests.setStyleSheet(label_style)
            self.ui.lbl_avg_percent.setStyleSheet(label_style)
            self.ui.lbl_unique_tasks.setStyleSheet(label_style)
            self.ui.lbl_topics_read.setStyleSheet(label_style)

        with open(path + "styles/label/label-h1.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_fixed.setStyleSheet(label_style)

        with open(path + "styles/label/label-h2.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.ui.lbl_fixed_2.setStyleSheet(label_style)
            self.ui.lbl_fixed_3.setStyleSheet(label_style)

        with open(path + "styles/list-widget/listwidget.qss", 'r',
                  encoding="utf-8") as file:
            listw_style = file.read()
            self.ui.listWidget.setStyleSheet(listw_style)

        # Добавление холста для рисования пай чарта
        self.canvas = MplCanvas(self)
        self.ui.verticalLayout_3.addWidget(self.canvas)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.ui.lbl_avg_percent.setWordWrap(True)

        # Инициализация данных пользователя
        self.ui.lbl_surname.setText(self.parent.current_user.lastname)
        self.ui.lbl_name.setText(self.parent.current_user.firstname)
        self.ui.lbl_midname.setText(self.parent.current_user.midname)
        self.groups = self.parent.current_user.groups
        groups_str = ", ".join([group.name for group in sorted(self.groups)])
        self.ui.lbl_group.setText(groups_str)

        self.refresh_statistics()

        # Обработка событий
        self.ui.btn_logout.clicked.connect(self.logout)
        self.ui.listWidget.itemDoubleClicked.connect(self.msg_print_results)
        self.ui.cbx_group.activated.connect(self.refresh)
        self.ui.cbx_student.activated.connect(self.refresh_statistics)

    def init_combobox(self):
        self.ui.cbx_group.clear()
        self.ui.cbx_group.addItem("Все группы")

        self.ui.cbx_student.clear()
        self.ui.cbx_student.addItem("Все студенты")

        for group in self.groups:
            self.ui.cbx_group.addItem(group.name, userData=group)

    def refresh(self, index: int = None) -> None:
        '''
        Вызывается при обновлении страницы.
        Обновляет содержимое профиля.
        '''
        current_group = self.ui.cbx_group.currentData()

        # Удаляем студентов из комбобокса
        for i in range(self.ui.cbx_student.count()-1, 0, -1):
            self.ui.cbx_student.removeItem(i)

        # Добавляем студентов данной группы
        if current_group is not None:
            students = self.find_group_students(current_group.id)
            for student in students:
                text = f'{student.lastname} {student.firstname}'
                self.ui.cbx_student.addItem(text, userData=student)

        if index is not None:
            self.refresh_statistics()

    def refresh_statistics(self):
        if self.ui.cbx_group.currentData() is None:
            # Если все группы и все студенты =>
            # Выводится статистика по всем группам
            self.show_group_statistics(self.groups)
        elif self.ui.cbx_student.currentData() is None:
            # Если не все группы, но все студенты конкретной группы =>
            # Выводится статистика по конкретной группе
            self.show_group_statistics([self.ui.cbx_group.currentData()])
        else:
            # Если не все группы и не все студенты =>
            # Выводится статистика по конкретному студенту
            self.show_student_statistics(self.ui.cbx_student.currentData().id)

    def show_group_statistics(self, groups: List[Group]) -> None:
        '''
        Выводит статистику по всем студентам определенных групп.

        Args:
            groups (List[Group]): Список групп.
        '''
        all_num_tests = 0
        all_percent = 0
        num_students = 0
        num_students_with_tests = 0
        all_students = []
        for group in groups:
            students = self.find_group_students(group.id)

            for student in students:
                num_students += 1

                num_tests = len(get_results_by_user(student.id))
                all_num_tests += num_tests

                if num_tests > 0:
                    num_students_with_tests += 1
                    average_percent = calc_average_percent(student.id,
                                                           obj="user")
                    all_percent += average_percent

                    # Формируем список студентов с решенными тестами
                    # для последующей инициализации истории тестов
                    all_students.append(student)

        self.ui.lbl_num_tests.setText(f"{all_num_tests}")

        if all_num_tests > 0:
            self.ui.lbl_avg_percent.setText(f"{(all_percent/num_students_with_tests):.2f}%")

            self.show_pie_chart(all_students)
            self.canvas.show()
        else:
            text = "Студенты должны решить хотя бы 1 тест, " +\
                   "чтобы получить статистику"
            self.ui.lbl_avg_percent.setText(text)

            self.canvas.hide()

        self.init_test_story(all_students)

        # Когда статистика по группам, скрываем ненужное
        self.ui.lbl_topics_read.hide()
        self.ui.lbl_unique_tasks.hide()
        self.ui.label_8.hide()
        self.ui.label_9.hide()

    def show_student_statistics(self, student_id: int) -> None:
        '''
        Выводит статистику определенного студента.

        Args:
            student_id (int): ID студента.
        '''
        user = get_user_by_id(student_id)
        user_data = get_user_data_by_id(user["user_data_id"])
        student = User(user["id"], user["role"], user_data["firstname"],
                       user_data["lastname"], user_data["midname"])

        num_tests = len(get_results_by_user(student_id))
        self.ui.lbl_num_tests.setText(f"{num_tests}")
        if num_tests > 0:
            average_percent = calc_average_percent(student_id,
                                                   obj="user")
            self.ui.lbl_avg_percent.setText(f"{average_percent:.2f}%")

            self.show_pie_chart([student])
            self.canvas.show()
        else:
            text = "Нужно решить хотя бы 1 тест, чтобы получить статистику"
            self.ui.lbl_avg_percent.setText(text)

            self.canvas.hide()

        self.init_test_story([student])

        all_topics = len(get_all_topics())
        user_topics = len(get_user_topics(student_id))
        self.ui.lbl_topics_read.setText(f"{user_topics}/{all_topics}")

        all_unique_tasks = len(get_all_tasks())
        user_tasks = len(get_user_tasks(student_id))
        self.ui.lbl_unique_tasks.setText(f"{user_tasks}/{all_unique_tasks}")

        # Когда статистика по студенту, показываем нужное
        self.ui.lbl_topics_read.show()
        self.ui.lbl_unique_tasks.show()
        self.ui.label_8.show()
        self.ui.label_9.show()

    def find_group_students(self, group_id: int) -> List[Optional[User]]:
        '''
        Находит студентов конкретной группы.

        Args:
            group_id (int): ID группы.

        Returns:
            List[Optional[User]]: Список студентов конкретной группы.
        '''
        group_students = []

        users = get_group_users(group_id)
        if users is not None:
            for user in users:
                user_info = get_user_by_id(user["user_id"])
                if user_info["role"] == "student":
                    user_data = get_user_data_by_id(user_info["user_data_id"])
                    user = User(user_info["id"], user_info["role"],
                                user_data["firstname"],
                                user_data["lastname"],
                                user_data["midname"])
                    group_students.append(user)

        return group_students

    def init_test_story(self, students: List[User]) -> None:
        '''
        Инициализирует историю тестов.

        Args:
            students (List[User]): Список студентов для которых будет
            формироваться история тестов.
        '''
        self.ui.listWidget.clear()

        for i, student in enumerate(students):
            for j, result in enumerate(get_results_by_user(student.id)):
                result_id = result['id']
                num_tasks = len(get_test_tasks(result['test_id']))
                time = format_date(result['created_at'])
                points = format_number(result["points"])
                text = f"{i+j+1}.\t №{result_id}\t" +\
                       f"{student.lastname} {student.firstname[0]}.\t" +\
                       f"Результат: {points}/{num_tasks}\t{time}"
                item = QListWidgetItem(text)
                self.ui.listWidget.insertItem(0, item)

    def msg_print_results(self, item):
        options = QFileDialog.Options()
        file_name, check = QFileDialog.getSaveFileName(self, "Сохранить файл",
                                                       "planared_results",
                                                       filter=".pdf",
                                                       options=options)
        if check:
            print_results(file_name, item)

    def show_pie_chart(self, students: List[User]) -> None:
        '''
        Показывает статистику в виде круговой диаграммы.

        Args:
            students (List[User]): Список студентов для которых будет
            построена диаграмма.
        '''
        # Чистим холст
        self.canvas.axes.clear()

        # Инициализация возможных результатов
        points = {}
        for i in range(0, 8 + 1):
            points[i] = 0
        for student in students:
            for result in get_results_by_user(student.id):
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
        self.init_combobox()
        self.refresh()

    def logout(self):
        print("Logout")
