from PyQt5.QtGui import QFont, QFontDatabase, QIcon, QPixmap, QImageReader
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QCoreApplication

from gui.ui_main_window import Ui_MainWindow

from gui.student_task_page import StudentTaskPage
from gui.teacher_task_page import TeacherTaskPage
from gui.student_profile_page import StudentProfilePage
from gui.teacher_profile_page import TeacherProfilePage
from gui.main_page import MainPage
from gui.graph_page import GraphPage
from gui.test_page import TestPage
from gui.test_start_page import TestStartPage
from gui.theory_page import TheoryPage

from src.api.users_controller import get_user_by_id, get_user_data_by_id
from src.education.user import User

import os
from dotenv import load_dotenv


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resizeEvent = self.on_resize

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Добавление форматов изображений
        print(QImageReader.supportedImageFormats())
        load_dotenv()
        QCoreApplication.addLibraryPath(str(os.getenv("PYTHON_PATH")) + '/Lib/site-packages/PyQt5/Qt5/plugins')

        # Привязка стиля (qss)
        with open(path + "styles\\main.qss", 'r', encoding="utf-8") as file:
            main_style = file.read()
            self.setStyleSheet(main_style)

        # Отображение картинок
        icon = QIcon()
        icon.addPixmap(QPixmap(path + "img/logo_black.svg"),
                       QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.ui.lbl_logo.setPixmap(QPixmap(path + "img/logo_white.svg"))
        self.ui.lbl_arrow.setPixmap(QPixmap(path + "img/arrow.svg"))

        # Работа со шрифтом
        font_id = QFontDatabase.addApplicationFont(
            path + "fonts/OpenSans-Regular.ttf")
        if font_id < 0:
            print('Font not loaded')
        families = QFontDatabase.applicationFontFamilies(font_id)
        font = QFont(families[0])
        self.ui.lbl_profile.setFont(font)

        # Подключаем пользователя
        user = get_user_by_id(2)
        user_data = get_user_data_by_id(user["user_data_id"])

        self.current_user = User(user["id"],
                                 user["role"],
                                 user_data["firstname"],
                                 user_data["lastname"],
                                 user_data["midname"])

        # Создание страниц для отображения в stacked widget
        self.main_page = MainPage(self)
        self.student_profile_page = StudentProfilePage(self)
        self.teacher_profile_page = TeacherProfilePage(self)
        self.student_task_page = StudentTaskPage(self)
        self.teacher_task_page = TeacherTaskPage(self)
        self.graph_page = GraphPage(self)
        self.test_start_page = TestStartPage(self)
        self.test_page = TestPage(self)
        self.theory_page = TheoryPage(self)

        # Инициализация первой страницы
        self.ui.stackedWidget.addWidget(self.main_page)
        self.ui.stackedWidget.setCurrentWidget(self.main_page)

        # Добавление страниц
        self.ui.stackedWidget.addWidget(self.student_task_page)
        self.ui.stackedWidget.addWidget(self.teacher_task_page)
        self.ui.stackedWidget.addWidget(self.student_profile_page)
        self.ui.stackedWidget.addWidget(self.teacher_profile_page)
        self.ui.stackedWidget.addWidget(self.graph_page)
        self.ui.stackedWidget.addWidget(self.test_start_page)
        self.ui.stackedWidget.addWidget(self.test_page)
        self.ui.stackedWidget.addWidget(self.theory_page)

        # Обработка нажатия на кнопок
        self.ui.lbl_graph_emb.mouseReleaseEvent = self.show_graph_page
        self.ui.lbl_tasks.mouseReleaseEvent = self.show_task_page
        self.ui.lbl_exit.mouseReleaseEvent = self.close
        self.ui.lbl_logo.mouseReleaseEvent = self.show_main_page
        self.ui.lbl_profile.mouseReleaseEvent = self.show_profile_page
        self.ui.lbl_testing.mouseReleaseEvent = self.show_test_start_page
        self.ui.lbl_theory.mouseReleaseEvent = self.show_theory_page

    def show_task_page(self, event):
        event.accept()
        if self.current_user.role == "student":
            self.ui.stackedWidget.setCurrentWidget(self.student_task_page)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.teacher_task_page)

    def show_profile_page(self, event):
        event.accept()
        if self.current_user.role == "student":
            self.ui.stackedWidget.setCurrentWidget(self.student_profile_page)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.teacher_profile_page)

    def show_main_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.main_page)

    def show_graph_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.graph_page)

    def show_test_start_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.test_start_page)

    def show_theory_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.theory_page)

    def on_resize(self, event):
        event.accept()
        # print(self.main_page.size())
