# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_teacher_task_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TeacherTaskPage(object):
    def setupUi(self, TeacherTaskPage):
        TeacherTaskPage.setObjectName("TeacherTaskPage")
        TeacherTaskPage.resize(955, 536)
        self.verticalLayout = QtWidgets.QVBoxLayout(TeacherTaskPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(TeacherTaskPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_fixed_2 = QtWidgets.QLabel(TeacherTaskPage)
        self.lbl_fixed_2.setObjectName("lbl_fixed_2")
        self.verticalLayout_2.addWidget(self.lbl_fixed_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.edt_task = QtWidgets.QLineEdit(TeacherTaskPage)
        self.edt_task.setObjectName("edt_task")
        self.verticalLayout_2.addWidget(self.edt_task)
        self.edt_options = QtWidgets.QLineEdit(TeacherTaskPage)
        self.edt_options.setObjectName("edt_options")
        self.verticalLayout_2.addWidget(self.edt_options)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_type = QtWidgets.QLabel(TeacherTaskPage)
        self.lbl_type.setObjectName("lbl_type")
        self.horizontalLayout_4.addWidget(self.lbl_type)
        self.cbx_task_type = QtWidgets.QComboBox(TeacherTaskPage)
        self.cbx_task_type.setEditable(False)
        self.cbx_task_type.setCurrentText("")
        self.cbx_task_type.setObjectName("cbx_task_type")
        self.cbx_task_type.addItem("")
        self.cbx_task_type.addItem("")
        self.cbx_task_type.addItem("")
        self.cbx_task_type.addItem("")
        self.cbx_task_type.addItem("")
        self.horizontalLayout_4.addWidget(self.cbx_task_type)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.edt_answer = QtWidgets.QLineEdit(TeacherTaskPage)
        self.edt_answer.setObjectName("edt_answer")
        self.verticalLayout_2.addWidget(self.edt_answer)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.btn_add_task = QtWidgets.QPushButton(TeacherTaskPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_task.sizePolicy().hasHeightForWidth())
        self.btn_add_task.setSizePolicy(sizePolicy)
        self.btn_add_task.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_add_task.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_task.setObjectName("btn_add_task")
        self.horizontalLayout_5.addWidget(self.btn_add_task)
        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.lbl_fixed = QtWidgets.QLabel(TeacherTaskPage)
        self.lbl_fixed.setObjectName("lbl_fixed")
        self.horizontalLayout_6.addWidget(self.lbl_fixed)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem11 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.label_2 = QtWidgets.QLabel(TeacherTaskPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cbx_sort = QtWidgets.QComboBox(TeacherTaskPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_sort.sizePolicy().hasHeightForWidth())
        self.cbx_sort.setSizePolicy(sizePolicy)
        self.cbx_sort.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbx_sort.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbx_sort.setObjectName("cbx_sort")
        self.cbx_sort.addItem("")
        self.cbx_sort.addItem("")
        self.horizontalLayout.addWidget(self.cbx_sort)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.vbox_tasks = QtWidgets.QVBoxLayout()
        self.vbox_tasks.setObjectName("vbox_tasks")
        self.horizontalLayout_3.addLayout(self.vbox_tasks)
        spacerItem15 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(TeacherTaskPage)
        self.cbx_task_type.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(TeacherTaskPage)

    def retranslateUi(self, TeacherTaskPage):
        _translate = QtCore.QCoreApplication.translate
        TeacherTaskPage.setWindowTitle(_translate("TeacherTaskPage", "Form"))
        self.label_3.setText(_translate("TeacherTaskPage", "Задания"))
        self.lbl_fixed_2.setText(_translate("TeacherTaskPage", "Конструктор заданий"))
        self.edt_task.setPlaceholderText(_translate("TeacherTaskPage", "Задание"))
        self.edt_options.setPlaceholderText(_translate("TeacherTaskPage", "Варианты ответа (через \";\")"))
        self.lbl_type.setText(_translate("TeacherTaskPage", "Выберите тип задания:"))
        self.cbx_task_type.setPlaceholderText(_translate("TeacherTaskPage", "Тип задания"))
        self.cbx_task_type.setItemText(0, _translate("TeacherTaskPage", "1 - Один вариант ответа"))
        self.cbx_task_type.setItemText(1, _translate("TeacherTaskPage", "2 - Несколько вариантов ответа"))
        self.cbx_task_type.setItemText(2, _translate("TeacherTaskPage", "3 - Открытый вопрос"))
        self.cbx_task_type.setItemText(3, _translate("TeacherTaskPage", "4 - Расставить в правильном порядке"))
        self.cbx_task_type.setItemText(4, _translate("TeacherTaskPage", "5 - Динамический ответ"))
        self.edt_answer.setPlaceholderText(_translate("TeacherTaskPage", "Правильный ответ"))
        self.btn_add_task.setText(_translate("TeacherTaskPage", "Добавить\n"
"задание"))
        self.lbl_fixed.setText(_translate("TeacherTaskPage", "Список заданий"))
        self.label_2.setText(_translate("TeacherTaskPage", "Сортировать по:"))
        self.cbx_sort.setItemText(0, _translate("TeacherTaskPage", "Идентификатору задания"))
        self.cbx_sort.setItemText(1, _translate("TeacherTaskPage", "Типу задания"))
