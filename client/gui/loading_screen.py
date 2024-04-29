import os

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(470, 150)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        # Путь к ассетам
        path = os.getcwd() + "/client/gui/resources/"

        # Вертикальный макет для компоновки виджетов
        layout = QVBoxLayout()

        # Метка для анимации загрузки
        self.label_animation = QLabel(self)
        self.movie = QMovie(path + 'img/loading.gif')
        self.label_animation.setMovie(self.movie)
        self.label_animation.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label_animation)

        # Сообщение пользователю
        self.label_text = QLabel(self)
        text = "Процесс укладки успешно запущен.\n"
        text += "Пожалуйста, дождитесь окончания вычислений."
        self.label_text.setText(text)
        self.label_text.setWordWrap(True)
        self.label_text.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label_text)

        # Привязка стилей
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(palette)

        with open(path + "styles/label/label-small.qss", 'r',
                  encoding="utf-8") as file:
            label_style = file.read()
            self.label_text.setStyleSheet(label_style)

        # Устанавливаем созданный макет для текущего виджета
        self.setLayout(layout)

        self.startAnimation()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()
