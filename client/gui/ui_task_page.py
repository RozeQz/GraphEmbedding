# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_task_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaskPage(object):
    def setupUi(self, TaskPage):
        TaskPage.setObjectName("TaskPage")
        TaskPage.resize(555, 314)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TaskPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.edt_task = QtWidgets.QLineEdit(TaskPage)
        self.edt_task.setObjectName("edt_task")
        self.verticalLayout.addWidget(self.edt_task)
        self.edt_options = QtWidgets.QLineEdit(TaskPage)
        self.edt_options.setObjectName("edt_options")
        self.verticalLayout.addWidget(self.edt_options)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_type = QtWidgets.QLabel(TaskPage)
        self.lbl_type.setObjectName("lbl_type")
        self.horizontalLayout_2.addWidget(self.lbl_type)
        self.cbx_task_type = QtWidgets.QComboBox(TaskPage)
        self.cbx_task_type.setEditable(False)
        self.cbx_task_type.setCurrentText("")
        self.cbx_task_type.setObjectName("cbx_task_type")
        self.cbx_task_type.addItem("")
        self.cbx_task_type.addItem("")
        self.cbx_task_type.addItem("")
        self.cbx_task_type.addItem("")
        self.cbx_task_type.addItem("")
        self.horizontalLayout_2.addWidget(self.cbx_task_type)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.edt_answer = QtWidgets.QLineEdit(TaskPage)
        self.edt_answer.setObjectName("edt_answer")
        self.verticalLayout.addWidget(self.edt_answer)
        self.btn_add_task = QtWidgets.QPushButton(TaskPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_task.sizePolicy().hasHeightForWidth())
        self.btn_add_task.setSizePolicy(sizePolicy)
        self.btn_add_task.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_add_task.setObjectName("btn_add_task")
        self.verticalLayout.addWidget(self.btn_add_task)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.btn_get_task = QtWidgets.QPushButton(TaskPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_get_task.sizePolicy().hasHeightForWidth())
        self.btn_get_task.setSizePolicy(sizePolicy)
        self.btn_get_task.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_get_task.setObjectName("btn_get_task")
        self.verticalLayout_2.addWidget(self.btn_get_task)
        self.lbl_task = QtWidgets.QLabel(TaskPage)
        self.lbl_task.setMaximumSize(QtCore.QSize(700, 16777215))
        self.lbl_task.setWordWrap(True)
        self.lbl_task.setObjectName("lbl_task")
        self.verticalLayout_2.addWidget(self.lbl_task)
        self.btn_check = QtWidgets.QPushButton(TaskPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_check.sizePolicy().hasHeightForWidth())
        self.btn_check.setSizePolicy(sizePolicy)
        self.btn_check.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_check.setObjectName("btn_check")
        self.verticalLayout_2.addWidget(self.btn_check)
        self.lbl_result = QtWidgets.QLabel(TaskPage)
        self.lbl_result.setObjectName("lbl_result")
        self.verticalLayout_2.addWidget(self.lbl_result)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(TaskPage)
        self.cbx_task_type.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(TaskPage)

    def retranslateUi(self, TaskPage):
        _translate = QtCore.QCoreApplication.translate
        TaskPage.setWindowTitle(_translate("TaskPage", "Form"))
        self.edt_task.setPlaceholderText(_translate("TaskPage", "Задание"))
        self.edt_options.setPlaceholderText(_translate("TaskPage", "Варианты ответа (через \";\")"))
        self.lbl_type.setText(_translate("TaskPage", "Выберите тип задания:"))
        self.cbx_task_type.setPlaceholderText(_translate("TaskPage", "Тип задания"))
        self.cbx_task_type.setItemText(0, _translate("TaskPage", "1 - Один вариант ответа"))
        self.cbx_task_type.setItemText(1, _translate("TaskPage", "2 - Несколько вариантов ответа"))
        self.cbx_task_type.setItemText(2, _translate("TaskPage", "3 - Открытый вопрос"))
        self.cbx_task_type.setItemText(3, _translate("TaskPage", "4 - Расставить в правильном порядке"))
        self.cbx_task_type.setItemText(4, _translate("TaskPage", "5 - Динамический ответ"))
        self.edt_answer.setPlaceholderText(_translate("TaskPage", "Правильный ответ"))
        self.btn_add_task.setText(_translate("TaskPage", "Добавить задание"))
        self.btn_get_task.setText(_translate("TaskPage", "Получить задание"))
        self.lbl_task.setText(_translate("TaskPage", "Задание:"))
        self.btn_check.setText(_translate("TaskPage", "Ответить"))
        self.lbl_result.setText(_translate("TaskPage", "Результат:"))
