from PyQt5.QtGui import QFont, QFontDatabase, QIcon, QPixmap, QImageReader
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QCoreApplication

from gui.ui_main_window import Ui_MainWindow

from gui.task_page import TaskPage
from gui.profile_page import ProfilePage
from gui.main_page import MainPage
from gui.graph_page import GraphPage
from gui.test_page import TestPage
from gui.test_start_page import TestStartPage

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
            self.setStyleSheet(file.read())
        # with open(path + "styles/profile.qss", 'r', encoding="utf-8") as file:
        #     self.profile_page.setStyleSheet(file.read())
        #     self.task_page.setStyleSheet(file.read())

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

        # Создание страниц для отображения в stacked widget
        self.main_page = MainPage(self)
        self.profile_page = ProfilePage(self)
        self.task_page = TaskPage(self)
        self.graph_page = GraphPage(self)
        self.test_start_page = TestStartPage(self)
        self.test_page = TestPage(self)

        # Инициализация первой страницы
        self.ui.stackedWidget.addWidget(self.main_page)
        self.ui.stackedWidget.setCurrentWidget(self.main_page)

        # Добавление страниц
        self.ui.stackedWidget.addWidget(self.task_page)
        self.ui.stackedWidget.addWidget(self.profile_page)
        self.ui.stackedWidget.addWidget(self.graph_page)
        self.ui.stackedWidget.addWidget(self.test_start_page)
        self.ui.stackedWidget.addWidget(self.test_page)

        # Обработка нажатия на кнопок
        self.ui.lbl_graph_emb.mouseReleaseEvent = self.show_graph_page
        self.ui.lbl_tasks.mouseReleaseEvent = self.show_task_page
        self.ui.lbl_exit.mouseReleaseEvent = self.close
        self.ui.lbl_logo.mouseReleaseEvent = self.show_main_page
        self.ui.lbl_profile.mouseReleaseEvent = self.show_profile_page
        self.ui.lbl_testing.mouseReleaseEvent = self.show_test_start_page

    def show_task_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.task_page)

    def show_profile_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.profile_page)

    def show_main_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.main_page)

    def show_graph_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.graph_page)

    def show_test_start_page(self, event):
        event.accept()
        self.ui.stackedWidget.setCurrentWidget(self.test_start_page)

    def on_resize(self, event):
        event.accept()
        # print(self.main_page.size())
