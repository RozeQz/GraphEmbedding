# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_student_profile_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentProfilePage(object):
    def setupUi(self, StudentProfilePage):
        StudentProfilePage.setObjectName("StudentProfilePage")
        StudentProfilePage.resize(931, 714)
        self.verticalLayout = QtWidgets.QVBoxLayout(StudentProfilePage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 30, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lbl_fixed = QtWidgets.QLabel(StudentProfilePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_fixed.sizePolicy().hasHeightForWidth())
        self.lbl_fixed.setSizePolicy(sizePolicy)
        self.lbl_fixed.setObjectName("lbl_fixed")
        self.horizontalLayout_2.addWidget(self.lbl_fixed)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_logout = QtWidgets.QPushButton(StudentProfilePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_logout.setMaximumSize(QtCore.QSize(16777215, 30))
        self.btn_logout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_logout.setObjectName("btn_logout")
        self.horizontalLayout_2.addWidget(self.btn_logout)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, 60)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setContentsMargins(-1, -1, -1, 30)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(StudentProfilePage)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(StudentProfilePage)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(StudentProfilePage)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(StudentProfilePage)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(StudentProfilePage)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lbl_surname = QtWidgets.QLabel(StudentProfilePage)
        self.lbl_surname.setObjectName("lbl_surname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl_surname)
        self.lbl_midname = QtWidgets.QLabel(StudentProfilePage)
        self.lbl_midname.setObjectName("lbl_midname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbl_midname)
        self.lbl_name = QtWidgets.QLabel(StudentProfilePage)
        self.lbl_name.setObjectName("lbl_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_name)
        self.lbl_group = QtWidgets.QLabel(StudentProfilePage)
        self.lbl_group.setObjectName("lbl_group")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lbl_group)
        self.lbl_teacher = QtWidgets.QLabel(StudentProfilePage)
        self.lbl_teacher.setObjectName("lbl_teacher")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lbl_teacher)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.lbl_fixed_2 = QtWidgets.QLabel(StudentProfilePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_fixed_2.sizePolicy().hasHeightForWidth())
        self.lbl_fixed_2.setSizePolicy(sizePolicy)
        self.lbl_fixed_2.setObjectName("lbl_fixed_2")
        self.verticalLayout_2.addWidget(self.lbl_fixed_2)
        self.listWidget = QtWidgets.QListWidget(StudentProfilePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(530, 50))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, 50)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_fixed_3 = QtWidgets.QLabel(StudentProfilePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_fixed_3.sizePolicy().hasHeightForWidth())
        self.lbl_fixed_3.setSizePolicy(sizePolicy)
        self.lbl_fixed_3.setObjectName("lbl_fixed_3")
        self.verticalLayout_3.addWidget(self.lbl_fixed_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setHorizontalSpacing(20)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(StudentProfilePage)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(StudentProfilePage)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(StudentProfilePage)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lbl_num_tests = QtWidgets.QLabel(StudentProfilePage)
        self.lbl_num_tests.setObjectName("lbl_num_tests")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl_num_tests)
        self.lbl_avg_percent = QtWidgets.QLabel(StudentProfilePage)
        self.lbl_avg_percent.setObjectName("lbl_avg_percent")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_avg_percent)
        self.lbl_unique_tasks = QtWidgets.QLabel(StudentProfilePage)
        self.lbl_unique_tasks.setObjectName("lbl_unique_tasks")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lbl_unique_tasks)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(StudentProfilePage)
        QtCore.QMetaObject.connectSlotsByName(StudentProfilePage)

    def retranslateUi(self, StudentProfilePage):
        _translate = QtCore.QCoreApplication.translate
        StudentProfilePage.setWindowTitle(_translate("StudentProfilePage", "Form"))
        self.lbl_fixed.setText(_translate("StudentProfilePage", "Профиль студента"))
        self.btn_logout.setText(_translate("StudentProfilePage", "Выйти из профиля"))
        self.label.setText(_translate("StudentProfilePage", "Фамилия:"))
        self.label_2.setText(_translate("StudentProfilePage", "Имя:"))
        self.label_3.setText(_translate("StudentProfilePage", "Отчество:"))
        self.label_4.setText(_translate("StudentProfilePage", "Группа:"))
        self.label_5.setText(_translate("StudentProfilePage", "Преподаватель:"))
        self.lbl_surname.setText(_translate("StudentProfilePage", "TextLabel"))
        self.lbl_midname.setText(_translate("StudentProfilePage", "TextLabel"))
        self.lbl_name.setText(_translate("StudentProfilePage", "TextLabel"))
        self.lbl_group.setText(_translate("StudentProfilePage", "TextLabel"))
        self.lbl_teacher.setText(_translate("StudentProfilePage", "TextLabel"))
        self.lbl_fixed_2.setText(_translate("StudentProfilePage", "История тестов"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("StudentProfilePage", "1. Тест №1 12.04.2024 12:31 Результат: 7/8"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.lbl_fixed_3.setText(_translate("StudentProfilePage", "Статистика"))
        self.label_6.setText(_translate("StudentProfilePage", "Прорешено тестов:"))
        self.label_7.setText(_translate("StudentProfilePage", "Средний % правильных ответов в тесте:"))
        self.label_8.setText(_translate("StudentProfilePage", "Прорешено уникальных заданий:"))
        self.lbl_num_tests.setText(_translate("StudentProfilePage", "TextLabel"))
        self.lbl_avg_percent.setText(_translate("StudentProfilePage", "TextLabel"))
        self.lbl_unique_tasks.setText(_translate("StudentProfilePage", "TextLabel"))
