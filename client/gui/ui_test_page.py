# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_test_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestPage(object):
    def setupUi(self, TestPage):
        TestPage.setObjectName("TestPage")
        TestPage.resize(765, 494)
        self.verticalLayout = QtWidgets.QVBoxLayout(TestPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hbox_top = QtWidgets.QHBoxLayout()
        self.hbox_top.setObjectName("hbox_top")
        self.lbl_status = QtWidgets.QLabel(TestPage)
        self.lbl_status.setObjectName("lbl_status")
        self.hbox_top.addWidget(self.lbl_status)
        self.lbl_time = QtWidgets.QLabel(TestPage)
        self.lbl_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_time.setObjectName("lbl_time")
        self.hbox_top.addWidget(self.lbl_time)
        self.lbl_clock = QtWidgets.QLabel(TestPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_clock.sizePolicy().hasHeightForWidth())
        self.lbl_clock.setSizePolicy(sizePolicy)
        self.lbl_clock.setMaximumSize(QtCore.QSize(20, 20))
        self.lbl_clock.setText("")
        self.lbl_clock.setPixmap(QtGui.QPixmap("resources/img/clock.png"))
        self.lbl_clock.setScaledContents(True)
        self.lbl_clock.setObjectName("lbl_clock")
        self.hbox_top.addWidget(self.lbl_clock)
        self.verticalLayout.addLayout(self.hbox_top)
        self.hbox_main = QtWidgets.QHBoxLayout()
        self.hbox_main.setObjectName("hbox_main")
        self.vbox_task = QtWidgets.QVBoxLayout()
        self.vbox_task.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.vbox_task.setObjectName("vbox_task")
        self.lbl_num_question = QtWidgets.QLabel(TestPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_num_question.sizePolicy().hasHeightForWidth())
        self.lbl_num_question.setSizePolicy(sizePolicy)
        self.lbl_num_question.setObjectName("lbl_num_question")
        self.vbox_task.addWidget(self.lbl_num_question)
        self.lbl_question = QtWidgets.QLabel(TestPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_question.sizePolicy().hasHeightForWidth())
        self.lbl_question.setSizePolicy(sizePolicy)
        self.lbl_question.setObjectName("lbl_question")
        self.vbox_task.addWidget(self.lbl_question)
        self.hbox_main.addLayout(self.vbox_task)
        self.vbox_movement = QtWidgets.QVBoxLayout()
        self.vbox_movement.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.vbox_movement.setObjectName("vbox_movement")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.vbox_movement.addLayout(self.gridLayout)
        self.hbox_end_test = QtWidgets.QHBoxLayout()
        self.hbox_end_test.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.hbox_end_test.setObjectName("hbox_end_test")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.hbox_end_test.addItem(spacerItem)
        self.btn_end = QtWidgets.QPushButton(TestPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_end.sizePolicy().hasHeightForWidth())
        self.btn_end.setSizePolicy(sizePolicy)
        self.btn_end.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_end.setObjectName("btn_end")
        self.hbox_end_test.addWidget(self.btn_end)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.hbox_end_test.addItem(spacerItem1)
        self.vbox_movement.addLayout(self.hbox_end_test)
        self.hbox_main.addLayout(self.vbox_movement)
        self.verticalLayout.addLayout(self.hbox_main)
        self.hbox_btn_answer = QtWidgets.QHBoxLayout()
        self.hbox_btn_answer.setObjectName("hbox_btn_answer")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_btn_answer.addItem(spacerItem2)
        self.btn_answer = QtWidgets.QPushButton(TestPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_answer.sizePolicy().hasHeightForWidth())
        self.btn_answer.setSizePolicy(sizePolicy)
        self.btn_answer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_answer.setStyleSheet("")
        self.btn_answer.setObjectName("btn_answer")
        self.hbox_btn_answer.addWidget(self.btn_answer)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hbox_btn_answer.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.hbox_btn_answer)

        self.retranslateUi(TestPage)
        QtCore.QMetaObject.connectSlotsByName(TestPage)

    def retranslateUi(self, TestPage):
        _translate = QtCore.QCoreApplication.translate
        TestPage.setWindowTitle(_translate("TestPage", "Form"))
        self.lbl_status.setText(_translate("TestPage", "Идет тестирование"))
        self.lbl_time.setText(_translate("TestPage", "До окончания тестирования:"))
        self.lbl_num_question.setText(_translate("TestPage", "Вопрос №5"))
        self.lbl_question.setText(_translate("TestPage", "Сколько внутренних граней у графа, представленного ниже?"))
        self.btn_end.setText(_translate("TestPage", "Завершить\n"
"тестирование"))
        self.btn_answer.setText(_translate("TestPage", "Ответить"))
