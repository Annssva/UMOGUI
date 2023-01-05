# -*- coding: utf-8 -*-
import json
# import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import dbWork


# класс окна для авторизации
class Ui_Auth(object):
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("MainWindow")
        AuthWindow.resize(500, 350)
        AuthWindow.setMinimumSize(QtCore.QSize(500, 350))
        AuthWindow.setMaximumSize(QtCore.QSize(500, 350))
        AuthWindow.setStyleSheet("background-color:white;")
        self.AuthWindow = AuthWindow
        self.centralwidget = QtWidgets.QWidget(AuthWindow)

        self.centralwidget.setStyleSheet(".QPushButton {\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                         "stop:0 rgba(205, 66, 255, 255), stop:0.5 rgba(0, 218, 255, 255), "
                                         "stop:1 rgba(0, 108, 255, 255));\n"
                                         "border-radius: 12px;\n"
                                         "font: 75 10pt \"Tahoma\";\n"
                                         "color: white;\n"
                                         "}\n"
                                         ".QPushButton:hover {\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                         "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), "
                                         "stop:1 rgba(97, 164, 255, 255));\n"
                                         "}\n"
                                         "QLineEdit {\n"
                                         "border: 1px solid rgb(200, 200, 200);\n"
                                         "border-top: 0px;\n"
                                         "border-left: 0px;\n"
                                         "border-right:0px;\n"
                                         "font: 75 10pt \"Tahoma\";\n"
                                         "}\n"
                                         "QLabel {\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.539773, "
                                         "stop:0 rgba(67, 65, 255, 255), stop:0.676617 rgba(120, 226, 255, 255), "
                                         "stop:1 rgba(255, 255, 255, 255));\n"
                                         "padding-left: 5px;\n"
                                         "padding-right:5px;\n"
                                         "border-radius:12px;\n"
                                         "max-width:120px;\n"
                                         "font: 75 10pt \"Tahoma\";\n"
                                         "color:white;\n"
                                         "}\n"
                                         )
        self.centralwidget.setObjectName("centralwidget")
        # кнопка для авторизации
        self.butAuth = QtWidgets.QPushButton(self.centralwidget)
        self.butAuth.setGeometry(QtCore.QRect(150, 250, 200, 30))
        self.butAuth.setStyleSheet("")
        self.butAuth.setObjectName("butAuth")

        # строка ввода логина
        self.loginGet = QtWidgets.QLineEdit(self.centralwidget)
        self.loginGet.setGeometry(QtCore.QRect(170, 130, 260, 31))
        self.loginGet.setStyleSheet("")
        self.loginGet.setAlignment(QtCore.Qt.AlignCenter)
        self.loginGet.setObjectName("loginGet")

        # строка ввода пароля
        self.passwGet = QtWidgets.QLineEdit(self.centralwidget)
        self.passwGet.setGeometry(QtCore.QRect(170, 170, 260, 32))
        self.passwGet.setStyleSheet("")
        self.passwGet.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwGet.setAlignment(QtCore.Qt.AlignCenter)
        self.passwGet.setObjectName("passwGet")

        # текст "логин"
        self.loginText = QtWidgets.QLabel(self.centralwidget)
        self.loginText.setGeometry(QtCore.QRect(50, 130, 130, 32))
        self.loginText.setStyleSheet("")
        self.loginText.setAlignment(QtCore.Qt.AlignCenter)
        self.loginText.setObjectName("loginText")

        # текст "пароль"
        self.passwText = QtWidgets.QLabel(self.centralwidget)
        self.passwText.setGeometry(QtCore.QRect(50, 170, 130, 31))
        self.passwText.setStyleSheet("")
        self.passwText.setAlignment(QtCore.Qt.AlignCenter)
        self.passwText.setObjectName("passwText")

        # текст "авторизация"
        self.authText = QtWidgets.QLabel(self.centralwidget)
        self.authText.setGeometry(QtCore.QRect(185, 50, 130, 31))
        self.authText.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(217, 112, 255, "
            "255), stop:0.5 rgba(111, 234, 255, 255), stop:1 rgba(97, 164, 255, 255));")
        self.authText.setAlignment(QtCore.Qt.AlignCenter)
        self.authText.setObjectName("authText")
        AuthWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

        # метод для проверки нажатия кнопки авторизации
        self.checkClick()

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Авторизация"))
        self.butAuth.setText(_translate("AuthWindow", "Войти"))
        self.loginText.setText(_translate("AuthWindow", "Логин"))
        self.passwText.setText(_translate("AuthWindow", "Пароль"))
        self.authText.setText(_translate("AuthWindow", "Авторизация"))

    # метод для проверки нажатия кнопки авторизации
    # если она нажата, вызывается метод для авторизации
    def checkClick(self):
        self.butAuth.clicked.connect(lambda: self.authorization())

    # метод для авторизации
    def authorization(self):
        try:
            # если заполнены все поля, то вызывается метод из файла с запросами к бд
            if (self.loginGet.text().strip() != '') and (self.passwGet.text().strip()):
                result = dbWork.authorization(self.loginGet.text(), self.passwGet.text())
                # если возвращен не отрицательный результат, то открывается главное окно
                if result[0] != False:
                    idUser = result[0]
                    login = result[1]
                    passUser = result[2]
                    postUser = dbWork.getPostuser(idUser)

                    self.window = QtWidgets.QMainWindow()
                    ui = Ui_MainWindow()
                    ui.setupUi(self.window, idUser, login, passUser, postUser)
                    self.window.show()
                    self.AuthWindow.close()
                # если результат отрицательный, всплывает ошибка
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка!')
                    msg.setText(result[1])
                    msg.exec()
            # если заполнены не все поля, всплывает ошибка
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка!')
                msg.setText('Все поля должны быть заполнены!')
                msg.exec()
            print('okay')
        except Exception as ex:
            print(ex)


# класс главного окна для обычного пользователя
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, idUser, login, passUser, postUser):
        try:
            self.MainWindow = MainWindow

            self.idUser = idUser
            self.loginUser = login
            self.passUser = passUser
            self.postUser = postUser
        except Exception as _ex:
            print("Error! ", _ex)

        # показ окна в соответствии с ролью
        if self.postUser == 'just_user':
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(990, 613)
            MainWindow.setStyleSheet(".QMainWindow {\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "}")
            self.centralwidget = QtWidgets.QWidget(MainWindow)

            self.centralwidget.setStyleSheet("QLabel {\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, "
                                             "y2:0.539773, stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, "
                                             "255), stop:0.676617 rgba(120, 226, 255, 255));\n "
                                             "padding-left: 6px;\n"
                                             "padding-right:6px;\n"
                                             "border-radius:10px;\n"
                                             "max-width:160px;\n"
                                             "font: 75 8pt \"Tahoma\";\n"
                                             "color:white;\n"
                                             "}\n"
                                             ".QPushButton{\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, "
                                             "y2:0.5,  stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, "
                                             "255));\n "
                                             "border-radius: 10px;\n"
                                             "font: 75 8pt \"Tahoma\";\n"
                                             "color: white;\n"
                                             "}\n"
                                             ".QPushButton:hover {\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, "
                                             "y2:0.5, stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, "
                                             "255), stop:1 rgba(97, 164, 255, 255));\n "
                                             "}\n"
                                             ".QTableWidget{\n"
                                             "border-radius: 20px;\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit {\n"
                                             "border: 1px solid rgb(200, 200, 200);\n"
                                             "border-top: 0px;\n"
                                             "border-left: 0px;\n"
                                             "border-right:0px;\n"
                                             "font: 75 10pt \"Tahoma\";\n"
                                             "}")

            self.centralwidget.setObjectName("centralwidget")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            # лого УМО
            self.UmoLabel = QtWidgets.QLabel(self.centralwidget)
            self.UmoLabel.setMinimumSize(QtCore.QSize(61, 51))
            self.UmoLabel.setMaximumSize(QtCore.QSize(130, 51))
            self.UmoLabel.setStyleSheet("padding-left: 5px;\n"
                                        "padding-right:5px;\n"
                                        "border-radius:12px;\n"
                                        "max-width:120px;\n"
                                        "font: 75 12pt \"Tahoma\";\n"
                                        "color:white;")
            self.UmoLabel.setObjectName("UmoLabel")
            self.horizontalLayout_2.addWidget(self.UmoLabel)
            self.gridLayout_2 = QtWidgets.QGridLayout()
            self.gridLayout_2.setObjectName("gridLayout_2")
            # текст "тип пользователя"
            self.userPostText = QtWidgets.QLabel(self.centralwidget)
            self.userPostText.setMinimumSize(QtCore.QSize(131, 21))
            self.userPostText.setMaximumSize(QtCore.QSize(172, 21))
            self.userPostText.setObjectName("userPostText")
            self.gridLayout_2.addWidget(self.userPostText, 1, 0, 1, 1)
            # текст "пользователь"
            self.userText = QtWidgets.QLabel(self.centralwidget)
            self.userText.setMinimumSize(QtCore.QSize(101, 21))
            self.userText.setMaximumSize(QtCore.QSize(172, 21))
            self.userText.setObjectName("userText")
            self.gridLayout_2.addWidget(self.userText, 0, 0, 1, 1)
            # поле куда кладется логин пользователя
            self.userSet = QtWidgets.QLabel(self.centralwidget)
            self.userSet.setMinimumSize(QtCore.QSize(111, 21))
            self.userSet.setMaximumSize(QtCore.QSize(172, 21))
            self.userSet.setStyleSheet("color:rgb(0, 0, 0);\n"
                                       "background-color: rgb(255, 255, 255);")
            self.userSet.setObjectName("userSet")
            self.gridLayout_2.addWidget(self.userSet, 0, 1, 1, 1)
            # поле куда кладется должность\роль пользователя
            self.userPostSet = QtWidgets.QLabel(self.centralwidget)
            self.userPostSet.setMinimumSize(QtCore.QSize(131, 21))
            self.userPostSet.setMaximumSize(QtCore.QSize(172, 21))
            self.userPostSet.setStyleSheet("color:rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
            self.userPostSet.setObjectName("userPostSet")
            self.gridLayout_2.addWidget(self.userPostSet, 1, 1, 1, 1)
            # кнопка для выхода из аккаунта
            self.signOutButt = QtWidgets.QPushButton(self.centralwidget)
            self.signOutButt.setMinimumSize(QtCore.QSize(71, 21))
            self.signOutButt.setMaximumSize(QtCore.QSize(71, 21))
            self.signOutButt.setObjectName("signOutButt")
            self.gridLayout_2.addWidget(self.signOutButt, 1, 2, 1, 1)
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_4.addItem(spacerItem)
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setPointSize(8)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(9)
            self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 3, 1, 1)
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")
            spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_6.addItem(spacerItem1)
            # кнопка для ввода группы
            self.groupButt = QtWidgets.QPushButton(self.centralwidget)
            self.groupButt.setMinimumSize(QtCore.QSize(95, 21))
            self.groupButt.setMaximumSize(QtCore.QSize(95, 21))
            self.groupButt.setObjectName("groupButt")
            self.horizontalLayout_6.addWidget(self.groupButt)
            # кнопка для нахождения преподавателя
            self.findTeachButt = QtWidgets.QPushButton(self.centralwidget)
            self.findTeachButt.setMinimumSize(QtCore.QSize(160, 22))
            self.findTeachButt.setMaximumSize(QtCore.QSize(160, 22))
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setPointSize(8)
            font.setBold(False)
            font.setItalic(False)
            font.setWeight(9)
            self.findTeachButt.setFont(font)
            self.findTeachButt.setObjectName("pushButton")
            self.horizontalLayout_6.addWidget(self.findTeachButt)
            self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 3, 1, 1)
            self.horizontalLayout_2.addLayout(self.gridLayout_2)
            self.verticalLayout_2.addLayout(self.horizontalLayout_2)
            spacerItem2 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            self.verticalLayout_2.addItem(spacerItem2)
            # меню со вкладками, где отображаются таблицы
            self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setPointSize(8)
            font.setKerning(False)
            self.tabWidget.setFont(font)
            self.tabWidget.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(213, 117, 255, 255), "
                "stop:0.462687 rgba(155, 251, 255, 255), stop:1 rgba(120, 172, 255, 255));\n "
                "border-radius: 20px;")
            self.tabWidget.setObjectName("tabWidget")
            # вкладка с таблицей институтов
            self.instWidget = QtWidgets.QWidget()
            self.instWidget.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(213, 117, 255, 255), "
                "stop:0.462687 rgba(155, 251, 255, 255), stop:1 rgba(120, 172, 255, 255));\n "
                "border-radius: 20px;")
            self.instWidget.setObjectName("instWidget")
            self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.instWidget)
            self.verticalLayout_5.setObjectName("verticalLayout_5")
            # таблица институтов
            self.instTable = QtWidgets.QTableWidget(self.instWidget)
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(75)
            self.instTable.setFont(font)
            self.instTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "")
            self.instTable.setObjectName("instTable")
            self.instTable.setColumnCount(5)
            self.instTable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setStyleStrategy(QtGui.QFont.PreferDefault)
            item.setFont(font)
            self.instTable.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.instTable.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.instTable.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.instTable.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            self.instTable.setHorizontalHeaderItem(4, item)
            self.verticalLayout_5.addWidget(self.instTable)
            self.tabWidget.addTab(self.instWidget, "")
            # вкладка с таблицей кафедр
            self.departWidget = QtWidgets.QWidget()
            self.departWidget.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(213, 117, 255, 255), "
                "stop:0.462687 rgba(155, 251, 255, 255), stop:1 rgba(120, 172, 255, 255));\n "
                "border-radius: 20px;")
            self.departWidget.setObjectName("departWidget")
            self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.departWidget)
            self.verticalLayout_6.setObjectName("verticalLayout_6")
            # таблица кафедр
            self.departTable = QtWidgets.QTableWidget(self.departWidget)
            self.departTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "")
            self.departTable.setObjectName("departTable")
            self.departTable.setColumnCount(6)
            self.departTable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            self.departTable.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.departTable.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.departTable.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.departTable.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            self.departTable.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            self.departTable.setHorizontalHeaderItem(5, item)
            self.verticalLayout_6.addWidget(self.departTable)
            self.tabWidget.addTab(self.departWidget, "")
            # вкладка с таблицей направлений
            self.directWidget = QtWidgets.QWidget()
            self.directWidget.setObjectName("directWidget")
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.directWidget)
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            # таблица направлений
            self.directTable = QtWidgets.QTableWidget(self.directWidget)
            self.directTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "")
            self.directTable.setObjectName("directTable")
            self.directTable.setColumnCount(3)
            self.directTable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            self.directTable.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.directTable.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.directTable.setHorizontalHeaderItem(2, item)
            self.verticalLayout_7.addWidget(self.directTable)
            self.tabWidget.addTab(self.directWidget, "")
            # вкладка с таблицей дисциплин
            self.discipWidget = QtWidgets.QWidget()
            self.discipWidget.setObjectName("discipWidget")
            self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.discipWidget)
            self.verticalLayout_8.setObjectName("verticalLayout_8")
            # таблица дисциплин
            self.discipTable = QtWidgets.QTableWidget(self.discipWidget)
            self.discipTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "")
            self.discipTable.setObjectName("discipTable")
            self.discipTable.setColumnCount(4)
            self.discipTable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.discipTable.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.discipTable.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.discipTable.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.discipTable.setHorizontalHeaderItem(3, item)
            self.verticalLayout_8.addWidget(self.discipTable)
            self.tabWidget.addTab(self.discipWidget, "")
            # вкладка с планом дисциплин
            self.planWidget = QtWidgets.QWidget()
            self.planWidget.setObjectName("planWidget")
            self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.planWidget)
            self.verticalLayout_9.setObjectName("verticalLayout_9")
            # таблица планов дисциплин
            self.planTable = QtWidgets.QTableWidget(self.planWidget)
            self.planTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "")
            self.planTable.setObjectName("planTable")
            self.planTable.setColumnCount(2)
            self.planTable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.planTable.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.planTable.setHorizontalHeaderItem(1, item)
            self.verticalLayout_9.addWidget(self.planTable)
            self.tabWidget.addTab(self.planWidget, "")
            # вкладка с таблицей преподавателей
            self.teachWidget = QtWidgets.QWidget()
            self.teachWidget.setObjectName("teachWidget")
            self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.teachWidget)
            self.verticalLayout_10.setObjectName("verticalLayout_10")
            # таблица с преподавателями
            self.teachTable = QtWidgets.QTableWidget(self.teachWidget)
            self.teachTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "")
            self.teachTable.setObjectName("teachTable")
            self.teachTable.setColumnCount(4)
            self.teachTable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.teachTable.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.teachTable.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.teachTable.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.teachTable.setHorizontalHeaderItem(3, item)
            self.verticalLayout_10.addWidget(self.teachTable)
            self.tabWidget.addTab(self.teachWidget, "")
            # вкладка с таблицей расписания
            self.timeWidget = QtWidgets.QWidget()
            self.timeWidget.setObjectName("timeWidget")
            self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.timeWidget)
            self.verticalLayout_11.setObjectName("verticalLayout_11")
            # таблица расписания
            self.timeTable = QtWidgets.QTableWidget(self.timeWidget)
            self.timeTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "")
            self.timeTable.setTextElideMode(QtCore.Qt.ElideLeft)
            self.timeTable.setObjectName("timeTable")
            self.timeTable.setColumnCount(6)
            self.timeTable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.timeTable.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.timeTable.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.timeTable.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.timeTable.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.timeTable.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.timeTable.setHorizontalHeaderItem(5, item)
            self.verticalLayout_11.addWidget(self.timeTable)
            self.tabWidget.addTab(self.timeWidget, "")
            # вкладка с таблицей информации о группе
            self.groupWidget = QtWidgets.QWidget()
            self.groupWidget.setObjectName("groupWidget")
            self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupWidget)
            self.verticalLayout_12.setObjectName("verticalLayout_12")
            # таблица информации о группе
            self.groupTable = QtWidgets.QTableWidget(self.groupWidget)
            self.groupTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "")
            self.groupTable.setObjectName("groupTable")
            self.groupTable.setColumnCount(4)
            self.groupTable.setRowCount(0)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.groupTable.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.groupTable.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.groupTable.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(9)
            item.setFont(font)
            self.groupTable.setHorizontalHeaderItem(3, item)
            self.verticalLayout_12.addWidget(self.groupTable)
            self.tabWidget.addTab(self.groupWidget, "")
            self.verticalLayout_2.addWidget(self.tabWidget)
            self.tabWidget.raise_()
            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            self.tabWidget.setCurrentIndex(5)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

            # методы для загрузки таблиц
            self.loadInsts(self.loginUser, self.passUser)
            self.loadDeparts(self.loginUser, self.passUser)
            self.loadDirect(self.loginUser, self.passUser)

            # метод проверки нажатия кнопки "выйти"
            self.checkSignOut()
            # метод проверки нажатия кнопки "ввести группу"
            self.checkGroupButton()
            # метод проверки нажатия кнопки "найти преподавателя"
            self.checkSearchButton()

        if self.postUser == 'methodist' or self.postUser == 'admin':
            try:
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(990, 613)
                MainWindow.setStyleSheet(".QMainWindow {\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "}")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("QLabel {\n"
                                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, "
                                                 "y2:0.539773, stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, "
                                                 "255), stop:0.676617 rgba(120, 226, 255, 255));\n "
                                                 "padding-left: 6px;\n"
                                                 "padding-right:6px;\n"
                                                 "border-radius:10px;\n"
                                                 "max-width:160px;\n"
                                                 "font: 75 8pt \"Tahoma\";\n"
                                                 "color:white;\n"
                                                 "}\n"
                                                 ".QPushButton{\n"
                                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                                 "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                                 "border-radius: 10px;\n"
                                                 "font: 75 8pt \"Tahoma\";\n"
                                                 "color: white;\n"
                                                 "}\n"
                                                 ".QPushButton:hover {\n"
                                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                                 "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), "
                                                 "stop:1 rgba(97, 164, 255, 255));\n "
                                                 "}\n"
                                                 ".QTableWidget{\n"
                                                 "border-radius: 20px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit {\n"
                                                 "border: 1px solid rgb(200, 200, 200);\n"
                                                 "border-top: 0px;\n"
                                                 "border-left: 0px;\n"
                                                 "border-right:0px;\n"
                                                 "font: 75 10pt \"Tahoma\";\n"
                                                 "}")
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.UmoLabel = QtWidgets.QLabel(self.centralwidget)
                self.UmoLabel.setMinimumSize(QtCore.QSize(61, 51))
                self.UmoLabel.setMaximumSize(QtCore.QSize(130, 51))
                self.UmoLabel.setStyleSheet("padding-left: 5px;\n"
                                            "padding-right:5px;\n"
                                            "border-radius:12px;\n"
                                            "max-width:120px;\n"
                                            "font: 75 12pt \"Tahoma\";\n"
                                            "color:white;")
                self.UmoLabel.setObjectName("UmoLabel")
                self.horizontalLayout_2.addWidget(self.UmoLabel)
                self.gridLayout_2 = QtWidgets.QGridLayout()
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.userPostText = QtWidgets.QLabel(self.centralwidget)
                self.userPostText.setMinimumSize(QtCore.QSize(131, 21))
                self.userPostText.setMaximumSize(QtCore.QSize(172, 21))
                self.userPostText.setObjectName("userPostText")
                self.gridLayout_2.addWidget(self.userPostText, 1, 0, 1, 1)
                self.userText = QtWidgets.QLabel(self.centralwidget)
                self.userText.setMinimumSize(QtCore.QSize(101, 21))
                self.userText.setMaximumSize(QtCore.QSize(172, 21))
                self.userText.setObjectName("userText")
                self.gridLayout_2.addWidget(self.userText, 0, 0, 1, 1)
                self.userSet = QtWidgets.QLabel(self.centralwidget)
                self.userSet.setMinimumSize(QtCore.QSize(111, 21))
                self.userSet.setMaximumSize(QtCore.QSize(172, 21))
                self.userSet.setStyleSheet("color:rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.userSet.setObjectName("userSet")
                self.gridLayout_2.addWidget(self.userSet, 0, 1, 1, 1)
                self.userPostSet = QtWidgets.QLabel(self.centralwidget)
                self.userPostSet.setMinimumSize(QtCore.QSize(131, 21))
                self.userPostSet.setMaximumSize(QtCore.QSize(172, 21))
                self.userPostSet.setStyleSheet("color:rgb(0, 0, 0);\n"
                                               "background-color: rgb(255, 255, 255);")
                self.userPostSet.setObjectName("userPostSet")
                self.gridLayout_2.addWidget(self.userPostSet, 1, 1, 1, 1)

                self.signOutButt = QtWidgets.QPushButton(self.centralwidget)
                self.signOutButt.setMinimumSize(QtCore.QSize(71, 21))
                self.signOutButt.setMaximumSize(QtCore.QSize(71, 21))
                self.signOutButt.setObjectName("signOutButt")
                self.gridLayout_2.addWidget(self.signOutButt, 1, 2, 1, 1)
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                   QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_4.addItem(spacerItem)
                self.searchTimetable = QtWidgets.QPushButton(self.centralwidget)
                self.searchTimetable.setMinimumSize(QtCore.QSize(200, 21))
                self.searchTimetable.setMaximumSize(QtCore.QSize(200, 18))
                self.searchTimetable.setObjectName("searchTimetable")
                self.horizontalLayout_4.addWidget(self.searchTimetable)
                self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 3, 1, 1)
                self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_6.setObjectName("horizontalLayout_6")
                spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_6.addItem(spacerItem1)
                self.findCapButt = QtWidgets.QPushButton(self.centralwidget)
                self.findCapButt.setMinimumSize(QtCore.QSize(160, 22))
                self.findCapButt.setMaximumSize(QtCore.QSize(160, 22))
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.findCapButt.setFont(font)
                self.findCapButt.setObjectName("findCapButt")
                self.horizontalLayout_6.addWidget(self.findCapButt)
                self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 3, 1, 1)
                self.horizontalLayout_2.addLayout(self.gridLayout_2)
                self.verticalLayout_2.addLayout(self.horizontalLayout_2)
                spacerItem2 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                self.verticalLayout_2.addItem(spacerItem2)
                self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
                font = QtGui.QFont()
                font.setFamily("Tahoma")
                font.setPointSize(8)
                font.setKerning(False)
                self.tabWidget.setFont(font)
                self.tabWidget.setStyleSheet(
                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(213, 117, 255, 255), "
                    "stop:0.462687 rgba(155, 251, 255, 255), stop:1 rgba(120, 172, 255, 255));\n "
                    "border-radius: 20px;")
                self.tabWidget.setObjectName("tabWidget")
                self.instWidget = QtWidgets.QWidget()
                self.instWidget.setStyleSheet(
                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(213, 117, 255, 255), "
                    "stop:0.462687 rgba(155, 251, 255, 255), stop:1 rgba(120, 172, 255, 255));\n "
                    "border-radius: 20px;")
                self.instWidget.setObjectName("instWidget")
                self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.instWidget)
                self.verticalLayout_5.setObjectName("verticalLayout_5")
                self.instTable = QtWidgets.QTableWidget(self.instWidget)
                font = QtGui.QFont()
                font.setPointSize(8)
                font.setBold(True)
                font.setWeight(75)
                self.instTable.setFont(font)
                self.instTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "")
                self.instTable.setObjectName("instTable")
                self.instTable.setColumnCount(6)
                self.instTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.instTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                item.setFont(font)
                self.instTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.instTable.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.instTable.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.instTable.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.instTable.setHorizontalHeaderItem(5, item)
                self.verticalLayout_5.addWidget(self.instTable)
                self.tabWidget.addTab(self.instWidget, "")
                self.departWidget = QtWidgets.QWidget()
                self.departWidget.setStyleSheet(
                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(213, 117, 255, 255), "
                    "stop:0.462687 rgba(155, 251, 255, 255), stop:1 rgba(120, 172, 255, 255));\n "
                    "border-radius: 20px;")
                self.departWidget.setObjectName("departWidget")
                self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.departWidget)
                self.verticalLayout_6.setObjectName("verticalLayout_6")
                self.departTable = QtWidgets.QTableWidget(self.departWidget)
                self.departTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "")
                self.departTable.setObjectName("departTable")
                self.departTable.setColumnCount(7)
                self.departTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.departTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.departTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.departTable.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.departTable.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.departTable.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.departTable.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.departTable.setHorizontalHeaderItem(6, item)
                self.verticalLayout_6.addWidget(self.departTable)
                self.tabWidget.addTab(self.departWidget, "")
                self.directWidget = QtWidgets.QWidget()
                self.directWidget.setObjectName("directWidget")
                self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.directWidget)
                self.verticalLayout_7.setObjectName("verticalLayout_7")
                self.directTable = QtWidgets.QTableWidget(self.directWidget)
                self.directTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "")
                self.directTable.setObjectName("directTable")
                self.directTable.setColumnCount(3)
                self.directTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.directTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.directTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.directTable.setHorizontalHeaderItem(2, item)
                self.verticalLayout_7.addWidget(self.directTable)
                self.tabWidget.addTab(self.directWidget, "")
                self.discipWidget = QtWidgets.QWidget()
                self.discipWidget.setObjectName("discipWidget")
                self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.discipWidget)
                self.verticalLayout_8.setObjectName("verticalLayout_8")
                self.discipTable = QtWidgets.QTableWidget(self.discipWidget)
                self.discipTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "")
                self.discipTable.setObjectName("discipTable")
                self.discipTable.setColumnCount(5)
                self.discipTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.discipTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.discipTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.discipTable.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.discipTable.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.discipTable.setHorizontalHeaderItem(4, item)
                self.verticalLayout_8.addWidget(self.discipTable)
                self.tabWidget.addTab(self.discipWidget, "")
                self.planWidget = QtWidgets.QWidget()
                self.planWidget.setObjectName("planWidget")
                self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.planWidget)
                self.verticalLayout_9.setObjectName("verticalLayout_9")
                self.planTable = QtWidgets.QTableWidget(self.planWidget)
                self.planTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "")
                self.planTable.setObjectName("planTable")
                self.planTable.setColumnCount(4)
                self.planTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.planTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.planTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.planTable.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.planTable.setHorizontalHeaderItem(3, item)
                self.verticalLayout_9.addWidget(self.planTable)
                self.tabWidget.addTab(self.planWidget, "")
                self.teachWidget = QtWidgets.QWidget()
                self.teachWidget.setObjectName("teachWidget")
                self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.teachWidget)
                self.verticalLayout_10.setObjectName("verticalLayout_10")
                self.teachTable = QtWidgets.QTableWidget(self.teachWidget)
                self.teachTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "")
                self.teachTable.setObjectName("teachTable")
                self.teachTable.setColumnCount(6)
                self.teachTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.teachTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.teachTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.teachTable.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.teachTable.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.teachTable.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.teachTable.setHorizontalHeaderItem(5, item)
                self.verticalLayout_10.addWidget(self.teachTable)
                self.tabWidget.addTab(self.teachWidget, "")
                self.discTeachWidget = QtWidgets.QWidget()
                self.discTeachWidget.setObjectName("discTeachWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.discTeachWidget)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.discTeachTable = QtWidgets.QTableWidget(self.discTeachWidget)
                self.discTeachTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "")
                self.discTeachTable.setObjectName("discTeachTable")
                self.discTeachTable.setColumnCount(3)
                self.discTeachTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.discTeachTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.discTeachTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.discTeachTable.setHorizontalHeaderItem(2, item)
                self.horizontalLayout.addWidget(self.discTeachTable)
                self.tabWidget.addTab(self.discTeachWidget, "")
                self.groupsWidget = QtWidgets.QWidget()
                self.groupsWidget.setObjectName("groupsWidget")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupsWidget)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.groupTable = QtWidgets.QTableWidget(self.groupsWidget)
                self.groupTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "")
                self.groupTable.setObjectName("groupTable")
                self.groupTable.setColumnCount(4)
                self.groupTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.groupTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.groupTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.groupTable.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.groupTable.setHorizontalHeaderItem(3, item)
                self.horizontalLayout_3.addWidget(self.groupTable)
                self.tabWidget.addTab(self.groupsWidget, "")
                self.otherWidget = QtWidgets.QWidget()
                self.otherWidget.setObjectName("otherWidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.otherWidget)
                self.verticalLayout.setObjectName("verticalLayout")
                self.controlTypeText = QtWidgets.QLabel(self.otherWidget)
                self.controlTypeText.setMinimumSize(QtCore.QSize(0, 21))
                self.controlTypeText.setStyleSheet("QLabel {\n"
                                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, "
                                                   "y2:0.539773, stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, "
                                                   "255), stop:0.676617 rgba(120, 226, 255, 255));\n "
                                                   "padding-left: 6px;\n"
                                                   "padding-right:6px;\n"
                                                   "border-radius:10px;\n"
                                                   "max-width:160px;\n"
                                                   "font: 75 8pt \"Tahoma\";\n"
                                                   "color:white;\n"
                                                   "}")
                self.controlTypeText.setObjectName("controlTypeText")
                self.verticalLayout.addWidget(self.controlTypeText)
                self.controlTable = QtWidgets.QTableWidget(self.otherWidget)
                self.controlTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "")
                self.controlTable.setObjectName("controlTable")
                self.controlTable.setColumnCount(2)
                self.controlTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.controlTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.controlTable.setHorizontalHeaderItem(1, item)
                self.verticalLayout.addWidget(self.controlTable)
                self.lessonTypeText = QtWidgets.QLabel(self.otherWidget)
                self.lessonTypeText.setMinimumSize(QtCore.QSize(0, 21))
                self.lessonTypeText.setStyleSheet("QLabel {\n"
                                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, "
                                                  "y2:0.539773, stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, "
                                                  "255), stop:0.676617 rgba(120, 226, 255, 255));\n "
                                                  "padding-left: 6px;\n"
                                                  "padding-right:6px;\n"
                                                  "border-radius:10px;\n"
                                                  "max-width:160px;\n"
                                                  "font: 75 8pt \"Tahoma\";\n"
                                                  "color:white;\n"
                                                  "}")
                self.lessonTypeText.setObjectName("lessonTypeText")
                self.verticalLayout.addWidget(self.lessonTypeText)
                self.lessonTable = QtWidgets.QTableWidget(self.otherWidget)
                self.lessonTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "")
                self.lessonTable.setObjectName("lessonTable")
                self.lessonTable.setColumnCount(2)
                self.lessonTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.lessonTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.lessonTable.setHorizontalHeaderItem(1, item)
                self.verticalLayout.addWidget(self.lessonTable)
                self.tabWidget.addTab(self.otherWidget, "")

                self.tabWidget.addTab(self.otherWidget, "")
                self.timeWidget = QtWidgets.QWidget()
                self.timeWidget.setObjectName("timeWidget")
                self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.timeWidget)
                self.verticalLayout_11.setObjectName("verticalLayout_11")
                self.timeTable = QtWidgets.QTableWidget(self.timeWidget)
                self.timeTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "")
                self.timeTable.setTextElideMode(QtCore.Qt.ElideLeft)
                self.timeTable.setObjectName("timeTable")
                self.timeTable.setColumnCount(3)
                self.timeTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.timeTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(9)
                item.setFont(font)
                self.timeTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.timeTable.setHorizontalHeaderItem(2, item)
                self.verticalLayout_11.addWidget(self.timeTable)
                self.tabWidget.addTab(self.timeWidget, "")
                self.lessWidget = QtWidgets.QWidget()
                self.lessWidget.setObjectName("lessWidget")
                self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.lessWidget)
                self.horizontalLayout_5.setObjectName("horizontalLayout_5")
                self.lessTable = QtWidgets.QTableWidget(self.lessWidget)
                self.lessTable.setStyleSheet("\n"
                                             "background-color: rgb(255, 255, 255);\\n")
                self.lessTable.setObjectName("lessTable")
                self.lessTable.setColumnCount(7)
                self.lessTable.setRowCount(0)
                item = QtWidgets.QTableWidgetItem()
                self.lessTable.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.lessTable.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.lessTable.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.lessTable.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.lessTable.setHorizontalHeaderItem(4, item)
                item = QtWidgets.QTableWidgetItem()
                self.lessTable.setHorizontalHeaderItem(5, item)
                item = QtWidgets.QTableWidgetItem()
                self.lessTable.setHorizontalHeaderItem(6, item)
                self.horizontalLayout_5.addWidget(self.lessTable)
                self.tabWidget.addTab(self.lessWidget, "")
                self.funcWidget = QtWidgets.QWidget()
                self.funcWidget.setStyleSheet(".QPushButton{\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                              "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                              "border-radius: 10px;\n"
                                              "font: 75 8pt \"Tahoma\";\n"
                                              "color: white;\n"
                                              "}\n"
                                              ".QPushButton:hover {\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                              "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), "
                                              "stop:1 rgba(97, 164, 255, 255));\n "
                                              "}")
                self.funcWidget.setObjectName("funcWidget")
            except Exception as _ex:
                print("Error! ", _ex)


            if self.postUser == 'methodist':
                try:
                    self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.funcWidget)
                    self.verticalLayout_3.setObjectName("verticalLayout_3")
                    self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
                    self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                    spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_7.addItem(spacerItem3)
                    self.addPlanDiscipButt = QtWidgets.QPushButton(self.funcWidget)
                    self.addPlanDiscipButt.setMinimumSize(QtCore.QSize(200, 21))
                    self.addPlanDiscipButt.setObjectName("addPlanDiscipButt")
                    self.horizontalLayout_7.addWidget(self.addPlanDiscipButt)
                    spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_7.addItem(spacerItem4)
                    self.verticalLayout_3.addLayout(self.horizontalLayout_7)
                    self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
                    self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                    spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_8.addItem(spacerItem5)
                    self.addLessButt = QtWidgets.QPushButton(self.funcWidget)
                    self.addLessButt.setMinimumSize(QtCore.QSize(130, 21))
                    self.addLessButt.setObjectName("addLessButt")
                    self.horizontalLayout_8.addWidget(self.addLessButt)
                    spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_8.addItem(spacerItem6)
                    self.verticalLayout_3.addLayout(self.horizontalLayout_8)
                    self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
                    self.horizontalLayout_9.setObjectName("horizontalLayout_9")
                    spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_9.addItem(spacerItem7)
                    self.addTimetButt = QtWidgets.QPushButton(self.funcWidget)
                    self.addTimetButt.setMinimumSize(QtCore.QSize(220, 21))
                    self.addTimetButt.setObjectName("addTimetButt")
                    self.horizontalLayout_9.addWidget(self.addTimetButt)
                    spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_9.addItem(spacerItem8)
                    self.verticalLayout_3.addLayout(self.horizontalLayout_9)
                    self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
                    self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                    spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                        QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_10.addItem(spacerItem9)
                    self.addTeachDiscip = QtWidgets.QPushButton(self.funcWidget)
                    self.addTeachDiscip.setMinimumSize(QtCore.QSize(250, 21))
                    self.addTeachDiscip.setObjectName("addTeachDiscip")
                    self.horizontalLayout_10.addWidget(self.addTeachDiscip)

                    spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                         QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_10.addItem(spacerItem10)
                    self.verticalLayout_3.addLayout(self.horizontalLayout_10)

                    self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
                    self.horizontalLayout_11.setObjectName("horizontalLayout_11")
                    spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                         QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_11.addItem(spacerItem11)
                    self.updateButt = QtWidgets.QPushButton(self.funcWidget)
                    self.updateButt.setMinimumSize(QtCore.QSize(150, 21))
                    self.updateButt.setMaximumSize(QtCore.QSize(150, 16777215))
                    self.updateButt.setObjectName("updateButt")
                    self.horizontalLayout_11.addWidget(self.updateButt)
                    spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                         QtWidgets.QSizePolicy.Minimum)
                    self.horizontalLayout_11.addItem(spacerItem12)
                    self.verticalLayout_3.addLayout(self.horizontalLayout_11)

                except Exception as _ex:
                    print("Error! ", _ex)


            if self.postUser == 'admin':
                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.funcWidget)
                self.verticalLayout_4.setObjectName("verticalLayout_4")

                self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_7.setObjectName("horizontalLayout_7")
                spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_7.addItem(spacerItem3)
                self.addPlanDiscipButt = QtWidgets.QPushButton(self.funcWidget)
                self.addPlanDiscipButt.setMinimumSize(QtCore.QSize(200, 21))
                self.addPlanDiscipButt.setObjectName("addPlanDiscipButt")
                self.horizontalLayout_7.addWidget(self.addPlanDiscipButt)
                spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_7.addItem(spacerItem4)
                self.verticalLayout_4.addLayout(self.horizontalLayout_7)
                self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_8.setObjectName("horizontalLayout_8")
                spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_8.addItem(spacerItem5)
                self.addLessButt = QtWidgets.QPushButton(self.funcWidget)
                self.addLessButt.setMinimumSize(QtCore.QSize(130, 21))
                self.addLessButt.setObjectName("addLessButt")
                self.horizontalLayout_8.addWidget(self.addLessButt)
                spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_8.addItem(spacerItem6)
                self.verticalLayout_4.addLayout(self.horizontalLayout_8)
                self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_9.setObjectName("horizontalLayout_9")
                spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_9.addItem(spacerItem7)
                self.addTimetButt = QtWidgets.QPushButton(self.funcWidget)
                self.addTimetButt.setMinimumSize(QtCore.QSize(220, 21))
                self.addTimetButt.setObjectName("addTimetButt")
                self.horizontalLayout_9.addWidget(self.addTimetButt)
                spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_9.addItem(spacerItem8)
                self.verticalLayout_4.addLayout(self.horizontalLayout_9)
                self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                    QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_10.addItem(spacerItem9)
                self.addTeachDiscip = QtWidgets.QPushButton(self.funcWidget)
                self.addTeachDiscip.setMinimumSize(QtCore.QSize(250, 21))
                self.addTeachDiscip.setObjectName("addTeachDiscip")
                self.horizontalLayout_10.addWidget(self.addTeachDiscip)
                spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_10.addItem(spacerItem10)
                self.verticalLayout_4.addLayout(self.horizontalLayout_10)

                self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_25.setObjectName("horizontalLayout_25")
                spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_25.addItem(spacerItem21)
                self.transferStudButt = QtWidgets.QPushButton(self.funcWidget)
                self.transferStudButt.setMinimumSize(QtCore.QSize(200, 21))
                self.transferStudButt.setObjectName("transferStudButt")
                self.horizontalLayout_25.addWidget(self.transferStudButt)
                spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_25.addItem(spacerItem22)
                self.verticalLayout_4.addLayout(self.horizontalLayout_25)

                self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_31.setObjectName("horizontalLayout_31")
                spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_31.addItem(spacerItem31)
                self.addUserButt = QtWidgets.QPushButton(self.funcWidget)
                self.addUserButt.setMinimumSize(QtCore.QSize(180, 21))
                self.addUserButt.setMaximumSize(QtCore.QSize(180, 16777215))
                self.addUserButt.setObjectName("addUserButt")
                self.horizontalLayout_31.addWidget(self.addUserButt)
                spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_31.addItem(spacerItem32)
                self.verticalLayout_4.addLayout(self.horizontalLayout_31)
                self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_32.setObjectName("horizontalLayout_32")
                spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_32.addItem(spacerItem33)
                self.delUserButt = QtWidgets.QPushButton(self.funcWidget)
                self.delUserButt.setMinimumSize(QtCore.QSize(170, 21))
                self.delUserButt.setMaximumSize(QtCore.QSize(170, 16777215))
                self.delUserButt.setObjectName("delUserButt")
                self.horizontalLayout_32.addWidget(self.delUserButt)
                spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_32.addItem(spacerItem34)
                self.verticalLayout_4.addLayout(self.horizontalLayout_32)
                self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_11.setObjectName("horizontalLayout_11")
                spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_11.addItem(spacerItem35)
                self.updateButt = QtWidgets.QPushButton(self.funcWidget)
                self.updateButt.setMinimumSize(QtCore.QSize(150, 21))
                self.updateButt.setMaximumSize(QtCore.QSize(150, 16777215))
                self.updateButt.setObjectName("updateButt")
                self.horizontalLayout_11.addWidget(self.updateButt)
                spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                                     QtWidgets.QSizePolicy.Minimum)
                self.horizontalLayout_11.addItem(spacerItem36)
                self.verticalLayout_4.addLayout(self.horizontalLayout_11)

                self.checkAddUser()
                self.checkDelUser()

            try:
                self.tabWidget.addTab(self.funcWidget, "")
                self.verticalLayout_2.addWidget(self.tabWidget)
                self.tabWidget.raise_()

                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                self.tabWidget.setCurrentIndex(10)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

            except Exception as _ex:
                print("Error! ", _ex)

            # метод для выгрузки таблиц
            self.loadTables(self.loginUser, self.passUser)

            # метод проверки нажатия кнопки "найти старосту"
            self.checkFindCapButton()

            # метод для поиска расписания для группы
            self.checkFindTimeButton()

            # метод проверки нажатия кнопки "выйти"
            self.checkSignOut()

            # метод проверки нажатия кнопки "добавить план дисциплины"
            self.checkAddPlan()

            self.checkAddLess()

            self.checkAddTimeTButton()

            self.checkAddTeachDiscipButton()

            self.checkUpdate()

            if self.postUser == 'admin':
                self.checkTransferButton()

    def retranslateUi(self, MainWindow):
        if self.postUser == 'just_user':
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "УМО"))
            self.UmoLabel.setText(_translate("MainWindow", "УМО"))
            self.userPostText.setText(_translate("MainWindow", "Тип пользователя:"))
            self.userText.setText(_translate("MainWindow", "Пользователь: "))
            self.userSet.setText(_translate("MainWindow", "TextLabel"))
            self.userPostSet.setText(_translate("MainWindow", "Главный Методист"))
            self.signOutButt.setText(_translate("MainWindow", "Выйти"))
            self.groupButt.setText(_translate("MainWindow", "Ввести группу"))
            self.findTeachButt.setText(_translate("MainWindow", "Найти преподавателя"))
            item = self.instTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Название института"))
            item = self.instTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Аббревиатура "))
            item = self.instTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Декан"))
            item = self.instTable.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Номер телефона"))
            item = self.instTable.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "Электронная почта"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.instWidget), _translate("MainWindow", "Институты"))
            item = self.departTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Название кафедры"))
            item = self.departTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Аббревиатура"))
            item = self.departTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Заведующий"))
            item = self.departTable.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Номер телефона"))
            item = self.departTable.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "Электронная почта"))
            item = self.departTable.horizontalHeaderItem(5)
            item.setText(_translate("MainWindow", "Институт"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.departWidget), _translate("MainWindow", "Кафедры"))
            item = self.directTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Название"))
            item = self.directTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Шифр направления"))
            item = self.directTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Институт"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.directWidget),
                                      _translate("MainWindow", "Направления подготовки"))
            item = self.discipTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Название"))
            item = self.discipTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Кафедра"))
            item = self.discipTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Количество часов"))
            item = self.discipTable.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Вид контроля"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.discipWidget),
                                      _translate("MainWindow", "Мои дисциплины"))
            item = self.planTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Название дисциплины"))
            item = self.planTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Номер семестра"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.planWidget),
                                      _translate("MainWindow", "План дисциплин"))
            item = self.teachTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Имя "))
            item = self.teachTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Фамилия"))
            item = self.teachTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Отчество"))
            item = self.teachTable.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Электронная почта"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.teachWidget),
                                      _translate("MainWindow", "Преподаватели"))
            item = self.timeTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "Дата"))
            item = self.timeTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Номер пары"))
            item = self.timeTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Кабинет"))
            item = self.timeTable.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Тип занятия"))
            item = self.timeTable.horizontalHeaderItem(4)
            item.setText(_translate("MainWindow", "Преподаватель"))
            item = self.timeTable.horizontalHeaderItem(5)
            item.setText(_translate("MainWindow", "Дисциплина"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.timeWidget), _translate("MainWindow", "Расписание"))
            item = self.groupTable.horizontalHeaderItem(0)

            item.setText(_translate("MainWindow", "Шифр группы"))
            item = self.groupTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "Институт"))
            item = self.groupTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "Направление"))
            item = self.groupTable.horizontalHeaderItem(3)
            item.setText(_translate("MainWindow", "Количество человек"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.groupWidget), _translate("MainWindow", "Моя группа"))

            self.userSet.setText(self.loginUser)
            self.userPostSet.setText(self.postUser)

        if self.postUser == 'methodist' or self.postUser == 'admin':
            try:
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "УМО"))
                self.UmoLabel.setText(_translate("MainWindow", "УМО"))
                self.userPostText.setText(_translate("MainWindow", "Тип пользователя:"))
                self.userText.setText(_translate("MainWindow", "Пользователь: "))
                self.userSet.setText(_translate("MainWindow", "TextLabel"))
                self.signOutButt.setText(_translate("MainWindow", "Выйти"))
                self.userPostSet.setText(_translate("MainWindow", "Главный Методист"))
                self.searchTimetable.setText(_translate("MainWindow", "Поиск расписания по группе"))
                self.findCapButt.setText(_translate("MainWindow", "Найти старосту группы"))
                item = self.instTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.instTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Название института"))
                item = self.instTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Аббревиатура "))
                item = self.instTable.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Декан ID"))
                item = self.instTable.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "Номер телефона"))
                item = self.instTable.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "Электронная почта"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.instWidget),
                                          _translate("MainWindow", "Институты"))
                item = self.departTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.departTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Название кафедры"))
                item = self.departTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Аббревиатура"))
                item = self.departTable.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Заведующий ID"))
                item = self.departTable.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "Номер телефона"))
                item = self.departTable.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "Электронная почта"))
                item = self.departTable.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "Институт ID"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.departWidget),
                                          _translate("MainWindow", "Кафедры"))
                item = self.directTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Название"))
                item = self.directTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Шифр направления"))
                item = self.directTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Институт ID"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.directWidget),
                                          _translate("MainWindow", "Направления подготовки"))
                item = self.discipTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID "))
                item = self.discipTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Название"))
                item = self.discipTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Кафедра ID"))
                item = self.discipTable.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Тип контроля ID"))
                item = self.discipTable.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "Количество часов"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.discipWidget),
                                          _translate("MainWindow", "Дисциплины"))
                item = self.planTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID "))
                item = self.planTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Дисциплина ID"))
                item = self.planTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Номер семестра"))
                item = self.planTable.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Направление подготовки"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.planWidget),
                                          _translate("MainWindow", "План дисциплин"))
                item = self.teachTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.teachTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Имя "))
                item = self.teachTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Фамилия"))
                item = self.teachTable.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Отчество"))
                item = self.teachTable.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "Институт"))
                item = self.teachTable.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "Электронная почта"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.teachWidget),
                                          _translate("MainWindow", "Преподаватели"))
                item = self.discTeachTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Дисциплина ID"))
                item = self.discTeachTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Преподаватель ID"))
                item = self.discTeachTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "ID"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.discTeachWidget),
                                          _translate("MainWindow", "Преподаватель - дисциплина"))
                item = self.groupTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "Шифр группы"))
                item = self.groupTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Институт ID"))
                item = self.groupTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Направление"))
                item = self.groupTable.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Количество человек"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.groupsWidget),
                                          _translate("MainWindow", "Учебные группы"))
                self.controlTypeText.setText(_translate("MainWindow", "Тип контроля"))
                item = self.controlTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.controlTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Название"))
                self.lessonTypeText.setText(_translate("MainWindow", "Тип занятия"))
                item = self.lessonTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.lessonTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Название"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.otherWidget), _translate("MainWindow", "Другое"))

                item = self.timeTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID занятия"))
                item = self.timeTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Шифр группы"))
                item = self.timeTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "ID"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.timeWidget),
                                          _translate("MainWindow", "Расписание"))
                item = self.lessTable.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.lessTable.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Дата"))
                item = self.lessTable.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Номер пары"))
                item = self.lessTable.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Кабинет"))
                item = self.lessTable.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "ID тип занятия"))
                item = self.lessTable.horizontalHeaderItem(5)
                item.setText(_translate("MainWindow", "ID преподаватель-дисциплина"))
                item = self.lessTable.horizontalHeaderItem(6)
                item.setText(_translate("MainWindow", "Номер семестра"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.lessWidget), _translate("MainWindow", "Занятия"))
                self.addPlanDiscipButt.setText(_translate("MainWindow", "Добавить план дисциплины"))
                self.addLessButt.setText(_translate("MainWindow", "Добавить занятие"))
                self.addTimetButt.setText(_translate("MainWindow", "Добавить занятие в расписание"))
                self.addTeachDiscip.setText(_translate("MainWindow", "Назначить преподавателю дисциплину"))
            except Exception as _ex:
                print("Error! ", _ex)

            if self.postUser == 'admin':
                self.transferStudButt.setText(_translate("MainWindow", "Перевести студента в другую группу"))
                self.addUserButt.setText(_translate("MainWindow", "Добавить пользователя"))
                self.delUserButt.setText(_translate("MainWindow", "Удалить пользователя"))

            try:
                self.updateButt.setText(_translate("MainWindow", "Обновить таблицы"))

                self.tabWidget.setTabText(self.tabWidget.indexOf(self.funcWidget), _translate("MainWindow", "Функции"))

                self.userSet.setText(self.loginUser)
                self.userPostSet.setText(self.postUser)
            except Exception as _ex:
                print("Error! ", _ex)


    # метод загрузки таблицы институтов
    def loadInsts(self, login, passw):
        instList = dbWork.instsForUser(login, passw)
        rowNumb = 0
        self.instTable.setRowCount(len(instList))
        for row in instList:
            self.instTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.instTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.instTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.instTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.instTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            rowNumb += 1

    # метод загрузки таблицы кафедр
    def loadDeparts(self, login, passw):
        departsList = dbWork.departsForUser(login, passw)
        rowNumb = 0
        self.departTable.setRowCount(len(departsList))
        for row in departsList:
            self.departTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.departTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.departTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.departTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.departTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.departTable.setItem(rowNumb, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            rowNumb += 1

    # метод загрузки таблицы направлений
    def loadDirect(self, login, passw):
        directsList = dbWork.directForUser(login, passw)
        rowNumb = 0
        self.directTable.setRowCount(len(directsList))
        for row in directsList:
            self.directTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.directTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.directTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            rowNumb += 1

    # метод загрузки таблицы дисциплин
    def loadDiscip(self, login, passw, group):
        discip = dbWork.discipForUser(login, passw, group)
        rowNumb = 0
        self.discipTable.setRowCount(len(discip))
        for row in discip:
            self.discipTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.discipTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.discipTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.discipTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            rowNumb += 1

    # метод загрузки таблицы плана дисциплин
    def loadPlan(self, login, passw, group):
        plan = dbWork.acPlanForUser(login, passw, group)
        rowNumb = 0
        self.planTable.setRowCount(len(plan))
        for row in plan:
            self.planTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.planTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            rowNumb += 1

    # метод загрузки таблицы преподавателей
    def loadTeach(self, login, passw, group):
        teach = dbWork.teachForUser(login, passw, group)
        rowNumb = 0
        self.teachTable.setRowCount(len(teach))
        for row in teach:
            self.teachTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.teachTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.teachTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.teachTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            rowNumb += 1

    # метод загрузки таблицы расписания
    def loadTimeTable(self, login, passw, group):
        taimeTable = dbWork.timetableForUser(login, passw, group)
        rowNumb = 0
        self.timeTable.setRowCount(len(taimeTable))
        for row in taimeTable:
            self.timeTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.timeTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.timeTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.timeTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.timeTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.timeTable.setItem(rowNumb, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            rowNumb += 1

    # метод загрузки таблицы информации о группе
    def loadGroup(self, login, passw, group):
        groupList = dbWork.groupForUser(login, passw, group)
        rowNumb = 0
        self.groupTable.setRowCount(len(groupList))
        for row in groupList:
            self.groupTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.groupTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.groupTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.groupTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            rowNumb += 1

    # метод для проверки нажатия кнопки "ввести группу"
    # если нажата, вызывается метод для открытия диалогового окна
    def checkGroupButton(self):
        self.groupButt.clicked.connect(lambda: self.groupW())

    # метод открытия диалогового окна и вызов метода для проверки и загрузки информации в таблицы,
    # где необходимо знать группу
    def groupW(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_DialGr()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()
        self.loadingWGroup()

    # метод для проверки нажатия кнопки "найти преподавателя"
    # если нажата, вызывается метод для открытия диалогового окна
    def checkSearchButton(self):
        self.findTeachButt.clicked.connect(lambda: self.searchT())

    # метод открытия диалогового окна
    def searchT(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_searchTeachDialog()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    # метод для проверки нажатия кнопки "ввести группу"
    # если нажата, вызывается метод для открытия диалогового окна
    def checkAddPlan(self):
        self.addPlanDiscipButt.clicked.connect(lambda: self.addPlanW())

    # метод открытия диалогового окна и вызов метода для проверки и загрузки информации в таблицы,
    # где необходимо знать группу
    def addPlanW(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_addPlanDialog()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    # метод для проверки нажатия кнопки "ввести группу"
    # если нажата, вызывается метод для открытия диалогового окна
    def checkAddLess(self):
        self.addLessButt.clicked.connect(lambda: self.addLessW())

    # метод открытия диалогового окна и вызов метода для проверки и загрузки информации в таблицы,
    # где необходимо знать группу
    def addLessW(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_addLessDialog()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    # метод для выгрузки информации в таблицы, где необходимо знать группу
    def loadingWGroup(self):
        # time.sleep(5)
        try:
            file = open("var.json", encoding="utf_8")
            info = json.loads(file.read())
            # file.write(json.dumps({"string": ""}, ensure_ascii=False, indent=4))
            file.close()
            group = info["string"]

            self.loadDiscip(self.loginUser, self.passUser, group)
            self.loadPlan(self.loginUser, self.passUser, group)
            self.loadTeach(self.loginUser, self.passUser, group)
            self.loadTimeTable(self.loginUser, self.passUser, group)
            self.loadGroup(self.loginUser, self.passUser, group)
        except Exception as ex:
            print(ex)

    # методы для окна для методистов
    def loadTables(self, login, passw):
        tables = dbWork.methodistsTable(login, passw)
        inst = tables[0]
        depart = tables[1]
        direct = tables[2]
        disc = tables[3]
        plan = tables[4]
        teach = tables[5]
        discTeach = tables[6]
        group = tables[7]
        control = tables[8]
        less = tables[9]
        lesson = tables[10]
        timetable = tables[11]

        rowNumb = 0
        self.instTable.setRowCount(len(inst))
        for row in inst:
            self.instTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.instTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.instTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.instTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.instTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.instTable.setItem(rowNumb, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            rowNumb += 1

        rowNumb = 0
        self.departTable.setRowCount(len(depart))
        for row in depart:
            self.departTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.departTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.departTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.departTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.departTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.departTable.setItem(rowNumb, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.departTable.setItem(rowNumb, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            rowNumb += 1

        rowNumb = 0
        self.directTable.setRowCount(len(direct))
        for row in direct:
            self.directTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.directTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.directTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            rowNumb += 1

        rowNumb = 0
        self.discipTable.setRowCount(len(disc))
        for row in disc:
            self.discipTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.discipTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.discipTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.discipTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.discipTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            rowNumb += 1

        rowNumb = 0
        self.planTable.setRowCount(len(plan))
        for row in plan:
            self.planTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.planTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.planTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.planTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            rowNumb += 1

        rowNumb = 0
        self.teachTable.setRowCount(len(teach))
        for row in teach:
            self.teachTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.teachTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.teachTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.teachTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.teachTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.teachTable.setItem(rowNumb, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            rowNumb += 1

        rowNumb = 0
        self.discTeachTable.setRowCount(len(discTeach))
        for row in discTeach:
            self.discTeachTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.discTeachTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.discTeachTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            rowNumb += 1

        rowNumb = 0
        self.groupTable.setRowCount(len(group))
        for row in group:
            self.groupTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.groupTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.groupTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.groupTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            rowNumb += 1

        rowNumb = 0
        self.controlTable.setRowCount(len(control))
        for row in control:
            self.controlTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.controlTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            rowNumb += 1

        rowNumb = 0
        self.lessonTable.setRowCount(len(less))
        for row in less:
            self.lessonTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.lessonTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            rowNumb += 1

        rowNumb = 0
        self.timeTable.setRowCount(len(timetable))
        for row in timetable:
            self.timeTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.timeTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.timeTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            rowNumb += 1

        rowNumb = 0
        self.lessTable.setRowCount(len(lesson))
        for row in lesson:
            self.lessTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.lessTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.lessTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.lessTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.lessTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.lessTable.setItem(rowNumb, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.lessTable.setItem(rowNumb, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            rowNumb += 1

    # метод для проверки нажатия кнопки "найти старосту"
    # если нажата, вызывается метод для открытия диалогового окна
    def checkFindCapButton(self):
        self.findCapButt.clicked.connect(lambda: self.searchCap())

    # метод открытия диалогового окна
    def searchCap(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_searchCap()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    # метод для проверки нажатия кнопки "найти старосту"
    # если нажата, вызывается метод для открытия диалогового окна
    def checkFindTimeButton(self):
        self.searchTimetable.clicked.connect(lambda: self.searchTime())

    # метод открытия диалогового окна
    def searchTime(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_findGroupDialog()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    def checkAddTimeTButton(self):
        self.addTimetButt.clicked.connect(lambda: self.addTimeW())

        # метод открытия диалогового окна

    def addTimeW(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_addTimeTDialog()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    def checkAddTeachDiscipButton(self):
        self.addTeachDiscip.clicked.connect(lambda: self.addTDW())

        # метод открытия диалогового окна

    def addTDW(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_addTeachDiscipDialog()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    # метод для проверки нажатия кнопки "ввести группу"
    # если нажата, вызывается метод для открытия диалогового окна
    def checkUpdate(self):
        self.updateButt.clicked.connect(lambda: self.loadTables(self.loginUser, self.passUser))

    def checkAddUser(self):
        self.addUserButt.clicked.connect(lambda: self.addUserW())

    def addUserW(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_addUserDialog()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    def checkDelUser(self):
        self.delUserButt.clicked.connect(lambda: self.delUserW())

    def delUserW(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_delUserDialog()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    def checkTransferButton(self):
        self.transferStudButt.clicked.connect(lambda: self.transferW())

        # метод открытия диалогового окна

    def transferW(self):
        self.dialog = QtWidgets.QDialog()
        ui = Ui_trahcserStudDial()
        ui.setupUi(self.dialog, self.loginUser, self.passUser)
        self.dialog.show()

    # метод для проверки нажатия на кнопку "выйти"
    # если нажата, то вызывается метод для открытия окна авторизации и закрытия главного окна
    def checkSignOut(self):
        self.signOutButt.clicked.connect(lambda: self.signOut())

    # метод для открытия окна авторизации и закрытия главного окна
    def signOut(self):
        self.window = QtWidgets.QMainWindow()
        ui = Ui_Auth()
        ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.close()


# диалоговое окно для введения группы
class Ui_DialGr(object):
    group = ''

    def setupUi(self, Dialog, loginUser, passUser):

        self.dialog = Dialog

        self.loginUser = loginUser
        self.passUser = passUser
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 150)
        Dialog.setMinimumSize(QtCore.QSize(400, 150))
        Dialog.setMaximumSize(QtCore.QSize(400, 150))

        Dialog.setStyleSheet("QLabel {\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.539773, "
                             "stop:0 rgba(213, 117, 255, 255), "
                             "stop:0 rgba(67, 65, 255, 255), stop:0.676617 rgba(120, 226, 255, 255));\n "
                             "padding-left: 6px;\n"
                             "padding-right:6px;\n"
                             "border-radius:10px;\n"
                             "max-width:160px;\n"
                             "font: 75 8pt \"Tahoma\";\n"
                             "color:white;\n"
                             "}\n"
                             ".QPushButton{\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  stop:0 rgba("
                             "205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                             "border-radius: 10px;\n"
                             "font: 75 8pt \"Tahoma\";\n"
                             "color: white;\n"
                             "}\n"
                             ".QPushButton:hover {\n"
                             "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba("
                             "217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), stop:1 rgba(97, 164, 255, "
                             "255));\n "
                             "}\n"
                             "\n"
                             "QLineEdit {\n"
                             "border: 1px solid rgb(200, 200, 200);\n"
                             "border-top: 0px;\n"
                             "border-left: 0px;\n"
                             "border-right:0px;\n"
                             "font: 75 10pt \"Tahoma\";\n"
                             "}\n"
                             ".QDialog{\n"
                             "background-color: rgb(255, 255, 255);\n"
                             "}")

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # текст "группа"
        self.groupText = QtWidgets.QLabel(Dialog)
        self.groupText.setMinimumSize(QtCore.QSize(200, 21))
        self.groupText.setMaximumSize(QtCore.QSize(172, 21))
        self.groupText.setObjectName("groupText")
        self.horizontalLayout.addWidget(self.groupText)
        # поле для ввода группы
        self.groupGet = QtWidgets.QLineEdit(Dialog)
        self.groupGet.setAlignment(QtCore.Qt.AlignCenter)
        self.groupGet.setObjectName("groupGet")
        self.horizontalLayout.addWidget(self.groupGet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        # кнопка "готово"
        self.okButt = QtWidgets.QPushButton(Dialog)
        self.okButt.setMinimumSize(QtCore.QSize(100, 21))
        self.okButt.setMaximumSize(QtCore.QSize(16777215, 21))
        self.okButt.setObjectName("okButt")
        self.horizontalLayout_2.addWidget(self.okButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.checkOkButt()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Группа"))
        self.groupText.setText(_translate("Dialog", "Введите шифр вашей группы:"))
        self.okButt.setText(_translate("Dialog", "Готово"))

    # метод для проверки нажатия на кнопку
    # если нажата, то вызывается метод для сохранения группы
    def checkOkButt(self):
        self.okButt.clicked.connect(lambda: self.getGroup())

    # метод для сохранения группы
    def getGroup(self):
        try:
            group = self.groupGet.text()
            file = open("var.json", "w", encoding="utf_8")
            file.write(json.dumps({"string": group}, ensure_ascii=False, indent=4))
            file.close()
            self.dialog.close()
        except Exception as ex:
            print(ex)


# диалоговое окно для поиска преподавателя
class Ui_searchTeachDialog(object):
    def setupUi(self, searchTeachDialog, login, passw):
        self.login = login
        self.passw = passw
        searchTeachDialog.setObjectName("searchTeachDialog")
        searchTeachDialog.resize(500, 385)
        searchTeachDialog.setMinimumSize(QtCore.QSize(500, 385))
        searchTeachDialog.setMaximumSize(QtCore.QSize(500, 385))
        searchTeachDialog.setStyleSheet("QLabel {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, "
                                        "y2:0.539773, stop:0 rgba(213, 117, 255, 255), "
                                        "stop:0 rgba(67, 65, 255, 255), stop:0.676617 rgba(120, 226, 255, 255));\n "
                                        "padding-left: 6px;\n"
                                        "padding-right:6px;\n"
                                        "border-radius:10px;\n"
                                        "max-width:160px;\n"
                                        "font: 75 8pt \"Tahoma\";\n"
                                        "color:white;\n"
                                        "}\n"
                                        ".QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                        "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                        "border-radius: 10px;\n"
                                        "font: 75 8pt \"Tahoma\";\n"
                                        "color: white;\n"
                                        "}\n"
                                        ".QPushButton:hover {\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                        "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), "
                                        "stop:1 rgba(97, 164, 255, 255));\n "
                                        "}\n"
                                        ".QTableWidget{\n"
                                        "border-radius: 20px;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit {\n"
                                        "border: 1px solid rgb(200, 200, 200);\n"
                                        "border-top: 0px;\n"
                                        "border-left: 0px;\n"
                                        "border-right:0px;\n"
                                        "font: 75 10pt \"Tahoma\";\n"
                                        "}\n"
                                        "\n"
                                        ".QDialog {\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(searchTeachDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # текст "введите фамилию преподавателя"
        self.teachText = QtWidgets.QLabel(searchTeachDialog)
        self.teachText.setMinimumSize(QtCore.QSize(220, 21))
        self.teachText.setObjectName("teachText")
        self.horizontalLayout.addWidget(self.teachText)
        # поле ввода фамилии
        self.teachGet = QtWidgets.QLineEdit(searchTeachDialog)
        self.teachGet.setObjectName("teachGet")
        self.horizontalLayout.addWidget(self.teachGet)
        # кнопка "найти"
        self.searchButt = QtWidgets.QPushButton(searchTeachDialog)
        self.searchButt.setMinimumSize(QtCore.QSize(70, 21))
        self.searchButt.setObjectName("searchButt")
        self.horizontalLayout.addWidget(self.searchButt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        # таблица для выгрузки информации и местонахождениях преподавателя
        self.teachTable = QtWidgets.QTableWidget(searchTeachDialog)
        self.teachTable.setObjectName("teachTable")
        self.teachTable.setColumnCount(3)
        self.teachTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.teachTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.teachTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.teachTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.teachTable)

        self.retranslateUi(searchTeachDialog)
        QtCore.QMetaObject.connectSlotsByName(searchTeachDialog)
        # метод для проверки нажатия на кнопку
        self.checkSearchButton()

    def retranslateUi(self, searchTeachDialog):
        _translate = QtCore.QCoreApplication.translate
        searchTeachDialog.setWindowTitle(_translate("searchTeachDialog", "Найти преподавателя"))
        self.teachText.setText(_translate("searchTeachDialog", "Введите фамилию преподавателя:"))
        self.searchButt.setText(_translate("searchTeachDialog", "Найти"))
        item = self.teachTable.horizontalHeaderItem(0)
        item.setText(_translate("searchTeachDialog", "Дата"))
        item = self.teachTable.horizontalHeaderItem(1)
        item.setText(_translate("searchTeachDialog", "Номер пары"))
        item = self.teachTable.horizontalHeaderItem(2)
        item.setText(_translate("searchTeachDialog", "Кабинет"))

    # метод для проверки нажатия на кнопку
    # если нажата, то вызывает метод для поиска информации
    def checkSearchButton(self):
        self.searchButt.clicked.connect(lambda: self.searchingTeach(self.login, self.passw))

    # метод для поиска информации о местонахождении преподавателя
    def searchingTeach(self, login, passw):
        teachList = dbWork.searchTeach(login, passw, self.teachGet.text())
        rowNumb = 0
        self.teachTable.setRowCount(len(teachList))
        for row in teachList:
            self.teachTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.teachTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.teachTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            rowNumb += 1


class Ui_searchCap(object):
    def setupUi(self, searchCap, login, passw):
        self.login = login
        self.passw = passw

        searchCap.setObjectName("searchTeachDialog")
        searchCap.resize(500, 385)
        searchCap.setMinimumSize(QtCore.QSize(500, 385))
        searchCap.setMaximumSize(QtCore.QSize(500, 385))
        searchCap.setStyleSheet("QLabel {\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.539773, "
                                "stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, 255), stop:0.676617 rgba("
                                "120, 226, 255, 255));\n "
                                "padding-left: 6px;\n"
                                "padding-right:6px;\n"
                                "border-radius:10px;\n"
                                "max-width:160px;\n"
                                "font: 75 8pt \"Tahoma\";\n"
                                "color:white;\n"
                                "}\n"
                                ".QPushButton{\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                "border-radius: 10px;\n"
                                "font: 75 8pt \"Tahoma\";\n"
                                "color: white;\n"
                                "}\n"
                                ".QPushButton:hover {\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), stop:1 rgba(97, "
                                "164, 255, 255));\n "
                                "}\n"
                                ".QTableWidget{\n"
                                "border-radius: 20px;\n"
                                "}\n"
                                "\n"
                                "QLineEdit {\n"
                                "border: 1px solid rgb(200, 200, 200);\n"
                                "border-top: 0px;\n"
                                "border-left: 0px;\n"
                                "border-right:0px;\n"
                                "font: 75 10pt \"Tahoma\";\n"
                                "}\n"
                                "\n"
                                ".QDialog {\n"
                                "    background-color: rgb(255, 255, 255);\n"
                                "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(searchCap)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.teachText = QtWidgets.QLabel(searchCap)
        self.teachText.setMinimumSize(QtCore.QSize(200, 21))
        self.teachText.setMaximumSize(QtCore.QSize(200, 16777215))
        self.teachText.setObjectName("teachText")
        self.horizontalLayout.addWidget(self.teachText)
        self.groupGet = QtWidgets.QLineEdit(searchCap)
        self.groupGet.setObjectName("groupGet")
        self.horizontalLayout.addWidget(self.groupGet)
        self.searchButt = QtWidgets.QPushButton(searchCap)
        self.searchButt.setMinimumSize(QtCore.QSize(70, 21))
        self.searchButt.setObjectName("searchButt")
        self.horizontalLayout.addWidget(self.searchButt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.infoTable = QtWidgets.QTableWidget(searchCap)
        self.infoTable.setObjectName("teachTable")
        self.infoTable.setColumnCount(4)
        self.infoTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.infoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.infoTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.infoTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.infoTable)

        self.retranslateUi(searchCap)
        QtCore.QMetaObject.connectSlotsByName(searchCap)

        self.checkSearchButt()

    def retranslateUi(self, searchTeachDialog):
        _translate = QtCore.QCoreApplication.translate
        searchTeachDialog.setWindowTitle(_translate("searchTeachDialog", "Найти старосту группы"))
        self.teachText.setText(_translate("searchTeachDialog", "Введите нужную группу:"))
        self.searchButt.setText(_translate("searchTeachDialog", "Найти"))
        item = self.infoTable.horizontalHeaderItem(0)
        item.setText(_translate("searchTeachDialog", "Фамилия"))
        item = self.infoTable.horizontalHeaderItem(1)
        item.setText(_translate("searchTeachDialog", "Имя"))
        item = self.infoTable.horizontalHeaderItem(2)
        item.setText(_translate("searchTeachDialog", "Кабинет"))
        item = self.infoTable.horizontalHeaderItem(3)
        item.setText(_translate("searchTeachDialog", "Почта"))

    def checkSearchButt(self):
        self.searchButt.clicked.connect(lambda: self.searching())

    def searching(self):
        info = dbWork.findCaptain(self.login, self.passw, self.groupGet.text())
        rowNumb = 0
        self.infoTable.setRowCount(len(info))
        for row in info:
            self.infoTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.infoTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.infoTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.infoTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            rowNumb += 1


class Ui_addPlanDialog(object):
    def setupUi(self, addPlanDialog, loginUser, passUser):
        self.loginUser = loginUser
        self.passUser = passUser
        addPlanDialog.setObjectName("addPlanDialog")
        addPlanDialog.resize(500, 300)
        addPlanDialog.setMinimumSize(QtCore.QSize(500, 300))
        addPlanDialog.setMaximumSize(QtCore.QSize(500, 300))
        addPlanDialog.setStyleSheet("QLabel {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.539773, "
                                    "stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, 255), stop:0.676617 "
                                    "rgba(120, 226, 255, 255));\n "
                                    "padding-left: 6px;\n"
                                    "padding-right:6px;\n"
                                    "border-radius:10px;\n"
                                    "max-width:160px;\n"
                                    "font: 75 8pt \"Tahoma\";\n"
                                    "color:white;\n"
                                    "}\n"
                                    ".QPushButton{\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                    "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                    "border-radius: 10px;\n"
                                    "font: 75 8pt \"Tahoma\";\n"
                                    "color: white;\n"
                                    "}\n"
                                    ".QPushButton:hover {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                    "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), stop:1 rgba("
                                    "97, 164, 255, 255));\n "
                                    "}\n"
                                    ".QTableWidget{\n"
                                    "border-radius: 20px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit {\n"
                                    "border: 1px solid rgb(200, 200, 200);\n"
                                    "border-top: 0px;\n"
                                    "border-left: 0px;\n"
                                    "border-right:0px;\n"
                                    "font: 75 10pt \"Tahoma\";\n"
                                    "}\n"
                                    "\n"
                                    ".QDialog {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(addPlanDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IdPlanText = QtWidgets.QLabel(addPlanDialog)
        self.IdPlanText.setMinimumSize(QtCore.QSize(200, 21))
        self.IdPlanText.setMaximumSize(QtCore.QSize(172, 21))
        self.IdPlanText.setObjectName("IdPlanText")
        self.horizontalLayout.addWidget(self.IdPlanText)
        self.idPlanGet = QtWidgets.QLineEdit(addPlanDialog)
        self.idPlanGet.setObjectName("idPlanGet")
        self.horizontalLayout.addWidget(self.idPlanGet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.idDiscipText = QtWidgets.QLabel(addPlanDialog)
        self.idDiscipText.setMinimumSize(QtCore.QSize(200, 21))
        self.idDiscipText.setMaximumSize(QtCore.QSize(172, 21))
        self.idDiscipText.setObjectName("idDiscipText")
        self.horizontalLayout_2.addWidget(self.idDiscipText)
        self.idDiscipGet = QtWidgets.QLineEdit(addPlanDialog)
        self.idDiscipGet.setObjectName("idDiscipGet")
        self.horizontalLayout_2.addWidget(self.idDiscipGet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.semestrText = QtWidgets.QLabel(addPlanDialog)
        self.semestrText.setMinimumSize(QtCore.QSize(200, 21))
        self.semestrText.setMaximumSize(QtCore.QSize(172, 21))
        self.semestrText.setObjectName("semestrText")
        self.horizontalLayout_3.addWidget(self.semestrText)
        self.semestrGet = QtWidgets.QLineEdit(addPlanDialog)
        self.semestrGet.setObjectName("semestrGet")
        self.horizontalLayout_3.addWidget(self.semestrGet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.directText = QtWidgets.QLabel(addPlanDialog)
        self.directText.setMinimumSize(QtCore.QSize(200, 21))
        self.directText.setMaximumSize(QtCore.QSize(172, 21))
        self.directText.setObjectName("directText")
        self.horizontalLayout_5.addWidget(self.directText)
        self.directGet = QtWidgets.QLineEdit(addPlanDialog)
        self.directGet.setObjectName("directGet")
        self.horizontalLayout_5.addWidget(self.directGet)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okButt = QtWidgets.QPushButton(addPlanDialog)
        self.okButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okButt.setObjectName("searchButt")
        self.horizontalLayout_4.addWidget(self.okButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(addPlanDialog)
        QtCore.QMetaObject.connectSlotsByName(addPlanDialog)

        self.checkAppPlan()

    def retranslateUi(self, addPlanDialog):
        _translate = QtCore.QCoreApplication.translate
        addPlanDialog.setWindowTitle(_translate("addPlanDialog", "Добавить план дисциплины"))
        self.IdPlanText.setText(_translate("addPlanDialog", "ID плана"))
        self.idDiscipText.setText(_translate("addPlanDialog", "ID дисциплины"))
        self.semestrText.setText(_translate("addPlanDialog", "Номер семестра"))
        self.directText.setText(_translate("addPlanDialog", "Шифр направления"))
        self.okButt.setText(_translate("addPlanDialog", "Готово"))

    def checkAppPlan(self):
        self.okButt.clicked.connect(lambda: self.adding())

    def adding(self):
        dbWork.addPlan(self.loginUser, self.passUser, self.idPlanGet.text(), self.idDiscipGet.text(),
                       self.semestrGet.text(), self.directGet.text())


class Ui_addLessDialog(object):
    def setupUi(self, addLessDialog, loginUser, passUser):
        self.loginUser = loginUser
        self.passUser = passUser

        addLessDialog.setObjectName("addLessDialog")
        addLessDialog.resize(500, 300)
        addLessDialog.setMinimumSize(QtCore.QSize(500, 300))
        addLessDialog.setMaximumSize(QtCore.QSize(500, 300))
        addLessDialog.setStyleSheet("QLabel {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.539773, "
                                    "stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, 255), stop:0.676617 "
                                    "rgba(120, 226, 255, 255));\n "
                                    "padding-left: 6px;\n"
                                    "padding-right:6px;\n"
                                    "border-radius:10px;\n"
                                    "max-width:160px;\n"
                                    "font: 75 8pt \"Tahoma\";\n"
                                    "color:white;\n"
                                    "}\n"
                                    ".QPushButton{\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                    "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                    "border-radius: 10px;\n"
                                    "font: 75 8pt \"Tahoma\";\n"
                                    "color: white;\n"
                                    "}\n"
                                    ".QPushButton:hover {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                    "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), stop:1 rgba("
                                    "97, 164, 255, 255));\n "
                                    "}\n"
                                    ".QTableWidget{\n"
                                    "border-radius: 20px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit {\n"
                                    "border: 1px solid rgb(200, 200, 200);\n"
                                    "border-top: 0px;\n"
                                    "border-left: 0px;\n"
                                    "border-right:0px;\n"
                                    "font: 75 10pt \"Tahoma\";\n"
                                    "}\n"
                                    "\n"
                                    ".QDialog {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(addLessDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IdLessText = QtWidgets.QLabel(addLessDialog)
        self.IdLessText.setMinimumSize(QtCore.QSize(200, 21))
        self.IdLessText.setMaximumSize(QtCore.QSize(172, 21))
        self.IdLessText.setObjectName("IdLessText")
        self.horizontalLayout.addWidget(self.IdLessText)
        self.idLessGet = QtWidgets.QLineEdit(addLessDialog)
        self.idLessGet.setAlignment(QtCore.Qt.AlignCenter)
        self.idLessGet.setObjectName("idLessGet")
        self.horizontalLayout.addWidget(self.idLessGet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DateText = QtWidgets.QLabel(addLessDialog)
        self.DateText.setMinimumSize(QtCore.QSize(200, 21))
        self.DateText.setMaximumSize(QtCore.QSize(172, 21))
        self.DateText.setObjectName("DateText")
        self.horizontalLayout_2.addWidget(self.DateText)
        self.DateGet = QtWidgets.QLineEdit(addLessDialog)
        self.DateGet.setObjectName("DateGet")
        self.horizontalLayout_2.addWidget(self.DateGet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.coupleText = QtWidgets.QLabel(addLessDialog)
        self.coupleText.setMinimumSize(QtCore.QSize(200, 21))
        self.coupleText.setMaximumSize(QtCore.QSize(172, 21))
        self.coupleText.setObjectName("coupleText")
        self.horizontalLayout_3.addWidget(self.coupleText)
        self.coupleGet = QtWidgets.QLineEdit(addLessDialog)
        self.coupleGet.setObjectName("coupleGet")
        self.horizontalLayout_3.addWidget(self.coupleGet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cabinetText = QtWidgets.QLabel(addLessDialog)
        self.cabinetText.setMinimumSize(QtCore.QSize(200, 21))
        self.cabinetText.setMaximumSize(QtCore.QSize(172, 21))
        self.cabinetText.setObjectName("cabinetText")
        self.horizontalLayout_5.addWidget(self.cabinetText)
        self.cabinetGet = QtWidgets.QLineEdit(addLessDialog)
        self.cabinetGet.setObjectName("cabinetGet")
        self.horizontalLayout_5.addWidget(self.cabinetGet)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tepeText = QtWidgets.QLabel(addLessDialog)
        self.tepeText.setMinimumSize(QtCore.QSize(200, 21))
        self.tepeText.setMaximumSize(QtCore.QSize(172, 21))
        self.tepeText.setObjectName("tepeText")
        self.horizontalLayout_6.addWidget(self.tepeText)
        self.typeGet = QtWidgets.QLineEdit(addLessDialog)
        self.typeGet.setObjectName("typeGet")
        self.horizontalLayout_6.addWidget(self.typeGet)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.teachDiscipText = QtWidgets.QLabel(addLessDialog)
        self.teachDiscipText.setMinimumSize(QtCore.QSize(200, 21))
        self.teachDiscipText.setMaximumSize(QtCore.QSize(172, 21))
        self.teachDiscipText.setObjectName("teachDiscipText")
        self.horizontalLayout_7.addWidget(self.teachDiscipText)
        self.teachDiscipGet = QtWidgets.QLineEdit(addLessDialog)
        self.teachDiscipGet.setObjectName("teachDiscipGet")
        self.horizontalLayout_7.addWidget(self.teachDiscipGet)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.directText_4 = QtWidgets.QLabel(addLessDialog)
        self.directText_4.setMinimumSize(QtCore.QSize(200, 21))
        self.directText_4.setMaximumSize(QtCore.QSize(172, 21))
        self.directText_4.setObjectName("directText_4")
        self.horizontalLayout_8.addWidget(self.directText_4)
        self.semestrGet = QtWidgets.QLineEdit(addLessDialog)
        self.semestrGet.setObjectName("semestrGet")
        self.horizontalLayout_8.addWidget(self.semestrGet)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okButt = QtWidgets.QPushButton(addLessDialog)
        self.okButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okButt.setObjectName("okButt")
        self.horizontalLayout_4.addWidget(self.okButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(addLessDialog)
        QtCore.QMetaObject.connectSlotsByName(addLessDialog)

        self.checkAppLess()

    def retranslateUi(self, addLessDialog):
        _translate = QtCore.QCoreApplication.translate
        addLessDialog.setWindowTitle(_translate("addLessDialog", "Добавить занятия"))
        self.IdLessText.setText(_translate("addLessDialog", "ID занятия"))
        self.DateText.setText(_translate("addLessDialog", "Дата (ГГГГ-ММ-ДД)"))
        self.coupleText.setText(_translate("addLessDialog", "Номер пары"))
        self.cabinetText.setText(_translate("addLessDialog", "Кабинет"))
        self.tepeText.setText(_translate("addLessDialog", "ID типа занятия"))
        self.teachDiscipText.setText(_translate("addLessDialog", "ID преодаватель-дисциплина"))
        self.directText_4.setText(_translate("addLessDialog", "Номер семестра"))
        self.okButt.setText(_translate("addLessDialog", "Готово"))

    def checkAppLess(self):
        self.okButt.clicked.connect(lambda: self.adding())

    def adding(self):
        dbWork.addLess(self.loginUser, self.passUser, self.idLessGet.text(), self.DateGet.text(), self.coupleGet.text(),
                       self.cabinetGet.text(), self.typeGet.text(), self.teachDiscipGet.text(), self.semestrGet.text())


class Ui_addTimeTDialog(object):
    def setupUi(self, addTimeTDialog, loginUser, passUser):
        self.loginUser = loginUser
        self.passUser = passUser

        addTimeTDialog.setObjectName("addTimeTDialog")
        addTimeTDialog.resize(500, 300)
        addTimeTDialog.setMinimumSize(QtCore.QSize(500, 300))
        addTimeTDialog.setMaximumSize(QtCore.QSize(500, 300))
        addTimeTDialog.setStyleSheet("QLabel {\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.539773, stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, 255), stop:0.676617 rgba(120, 226, 255, 255));\n"
                                     "padding-left: 6px;\n"
                                     "padding-right:6px;\n"
                                     "border-radius:10px;\n"
                                     "max-width:160px;\n"
                                     "font: 75 8pt \"Tahoma\";\n"
                                     "color:white;\n"
                                     "}\n"
                                     ".QPushButton{\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                     "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                     "border-radius: 10px;\n"
                                     "font: 75 8pt \"Tahoma\";\n"
                                     "color: white;\n"
                                     "}\n"
                                     ".QPushButton:hover {\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                     "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), "
                                     "stop:1 rgba(97, 164, 255, 255));\n "
                                     "}\n"
                                     ".QTableWidget{\n"
                                     "border-radius: 20px;\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit {\n"
                                     "border: 1px solid rgb(200, 200, 200);\n"
                                     "border-top: 0px;\n"
                                     "border-left: 0px;\n"
                                     "border-right:0px;\n"
                                     "font: 75 10pt \"Tahoma\";\n"
                                     "}\n"
                                     "\n"
                                     ".QDialog {\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(addTimeTDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IdTimeTText = QtWidgets.QLabel(addTimeTDialog)
        self.IdTimeTText.setMinimumSize(QtCore.QSize(200, 21))
        self.IdTimeTText.setMaximumSize(QtCore.QSize(172, 21))
        self.IdTimeTText.setObjectName("IdTimeTText")
        self.horizontalLayout.addWidget(self.IdTimeTText)
        self.idTimeTGet = QtWidgets.QLineEdit(addTimeTDialog)
        self.idTimeTGet.setAlignment(QtCore.Qt.AlignCenter)
        self.idTimeTGet.setObjectName("idTimeTGet")
        self.horizontalLayout.addWidget(self.idTimeTGet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupText = QtWidgets.QLabel(addTimeTDialog)
        self.groupText.setMinimumSize(QtCore.QSize(200, 21))
        self.groupText.setMaximumSize(QtCore.QSize(172, 21))
        self.groupText.setObjectName("groupText")
        self.horizontalLayout_2.addWidget(self.groupText)
        self.groupGet = QtWidgets.QLineEdit(addTimeTDialog)
        self.groupGet.setAlignment(QtCore.Qt.AlignCenter)
        self.groupGet.setObjectName("groupGet")
        self.horizontalLayout_2.addWidget(self.groupGet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.coupleText = QtWidgets.QLabel(addTimeTDialog)
        self.coupleText.setMinimumSize(QtCore.QSize(200, 21))
        self.coupleText.setMaximumSize(QtCore.QSize(172, 21))
        self.coupleText.setObjectName("coupleText")
        self.horizontalLayout_3.addWidget(self.coupleText)
        self.lessonGet = QtWidgets.QLineEdit(addTimeTDialog)
        self.lessonGet.setAlignment(QtCore.Qt.AlignCenter)
        self.lessonGet.setObjectName("lessonGet")
        self.horizontalLayout_3.addWidget(self.lessonGet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okButt = QtWidgets.QPushButton(addTimeTDialog)
        self.okButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okButt.setObjectName("okButt")
        self.horizontalLayout_4.addWidget(self.okButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(addTimeTDialog)
        QtCore.QMetaObject.connectSlotsByName(addTimeTDialog)

        self.checkAddTime()

    def retranslateUi(self, addTimeTDialog):
        _translate = QtCore.QCoreApplication.translate
        addTimeTDialog.setWindowTitle(_translate("addTimeTDialog", "Добавить расписание"))
        self.IdTimeTText.setText(_translate("addTimeTDialog", "ID  расписания"))
        self.groupText.setText(_translate("addTimeTDialog", "Шифр группы"))
        self.coupleText.setText(_translate("addTimeTDialog", "ID занятия"))
        self.okButt.setText(_translate("addTimeTDialog", "Готово"))

    def checkAddTime(self):
        self.okButt.clicked.connect(lambda: self.adding())

    def adding(self):
        dbWork.addTimeT(self.loginUser, self.passUser, self.idTimeTGet.text(), self.groupGet.text(),
                        self.lessonGet.text())


class Ui_addTeachDiscipDialog(object):
    def setupUi(self, addTeachDiscipDialog, loginUser, passUser):
        self.loginUser = loginUser
        self.passUser = passUser

        addTeachDiscipDialog.setObjectName("addTimeTDialog")
        addTeachDiscipDialog.resize(500, 300)
        addTeachDiscipDialog.setMinimumSize(QtCore.QSize(500, 300))
        addTeachDiscipDialog.setMaximumSize(QtCore.QSize(500, 300))
        addTeachDiscipDialog.setStyleSheet("QLabel {\n"
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, "
                                           "y2:0.539773, stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, "
                                           "255), stop:0.676617 rgba(120, 226, 255, 255));\n "
                                           "padding-left: 6px;\n"
                                           "padding-right:6px;\n"
                                           "border-radius:10px;\n"
                                           "max-width:160px;\n"
                                           "font: 75 8pt \"Tahoma\";\n"
                                           "color:white;\n"
                                           "}\n"
                                           ".QPushButton{\n"
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                           " stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                           "border-radius: 10px;\n"
                                           "font: 75 8pt \"Tahoma\";\n"
                                           "color: white;\n"
                                           "}\n"
                                           ".QPushButton:hover {\n"
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                           "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), "
                                           "stop:1 rgba(97, 164, 255, 255));\n "
                                           "}\n"
                                           ".QTableWidget{\n"
                                           "border-radius: 20px;\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit {\n"
                                           "border: 1px solid rgb(200, 200, 200);\n"
                                           "border-top: 0px;\n"
                                           "border-left: 0px;\n"
                                           "border-right:0px;\n"
                                           "font: 75 10pt \"Tahoma\";\n"
                                           "}\n"
                                           "\n"
                                           ".QDialog {\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(addTeachDiscipDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IdDTText = QtWidgets.QLabel(addTeachDiscipDialog)
        self.IdDTText.setMinimumSize(QtCore.QSize(200, 21))
        self.IdDTText.setMaximumSize(QtCore.QSize(172, 21))
        self.IdDTText.setObjectName("IdDTText")
        self.horizontalLayout.addWidget(self.IdDTText)
        self.idDTGet = QtWidgets.QLineEdit(addTeachDiscipDialog)
        self.idDTGet.setAlignment(QtCore.Qt.AlignCenter)
        self.idDTGet.setObjectName("idDTGet")
        self.horizontalLayout.addWidget(self.idDTGet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.teachText = QtWidgets.QLabel(addTeachDiscipDialog)
        self.teachText.setMinimumSize(QtCore.QSize(200, 21))
        self.teachText.setMaximumSize(QtCore.QSize(172, 21))
        self.teachText.setObjectName("teachText")
        self.horizontalLayout_2.addWidget(self.teachText)
        self.teachGet = QtWidgets.QLineEdit(addTeachDiscipDialog)
        self.teachGet.setAlignment(QtCore.Qt.AlignCenter)
        self.teachGet.setObjectName("teachGet")
        self.horizontalLayout_2.addWidget(self.teachGet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lessonText = QtWidgets.QLabel(addTeachDiscipDialog)
        self.lessonText.setMinimumSize(QtCore.QSize(200, 21))
        self.lessonText.setMaximumSize(QtCore.QSize(172, 21))
        self.lessonText.setObjectName("lessonText")
        self.horizontalLayout_3.addWidget(self.lessonText)
        self.discipGet = QtWidgets.QLineEdit(addTeachDiscipDialog)
        self.discipGet.setAlignment(QtCore.Qt.AlignCenter)
        self.discipGet.setObjectName("discipGet")
        self.horizontalLayout_3.addWidget(self.discipGet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okButt = QtWidgets.QPushButton(addTeachDiscipDialog)
        self.okButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okButt.setObjectName("okButt")
        self.horizontalLayout_4.addWidget(self.okButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(addTeachDiscipDialog)
        QtCore.QMetaObject.connectSlotsByName(addTeachDiscipDialog)

        self.checkAddTD()

    def retranslateUi(self, addTimeTDialog):
        _translate = QtCore.QCoreApplication.translate
        addTimeTDialog.setWindowTitle(_translate("addTimeTDialog", "Добавить преподаватель-дисциплина"))
        self.IdDTText.setText(_translate("addTimeTDialog", "ID  преподаватель-дисциплина"))
        self.teachText.setText(_translate("addTimeTDialog", "ID  преподавателя"))
        self.lessonText.setText(_translate("addTimeTDialog", "ID  дисциплины"))
        self.okButt.setText(_translate("addTimeTDialog", "Готово"))

    def checkAddTD(self):
        self.okButt.clicked.connect(lambda: self.adding())

    def adding(self):
        dbWork.addTeachDiscip(self.loginUser, self.passUser, self.idDTGet.text(), self.teachGet.text(),
                              self.discipGet.text())


class Ui_addUserDialog(object):
    def setupUi(self, addUserDialog, loginUser, passUser):
        self.loginUser = loginUser
        self.passUser = passUser

        addUserDialog.setObjectName("addUserialog")
        addUserDialog.resize(500, 300)
        addUserDialog.setMinimumSize(QtCore.QSize(500, 300))
        addUserDialog.setMaximumSize(QtCore.QSize(500, 300))
        addUserDialog.setStyleSheet("QLabel {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.539773, "
                                    "stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, 255), stop:0.676617 "
                                    "rgba(120, 226, 255, 255));\n "
                                    "padding-left: 6px;\n"
                                    "padding-right:6px;\n"
                                    "border-radius:10px;\n"
                                    "max-width:160px;\n"
                                    "font: 75 8pt \"Tahoma\";\n"
                                    "color:white;\n"
                                    "}\n"
                                    ".QPushButton{\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                    "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                    "border-radius: 10px;\n"
                                    "font: 75 8pt \"Tahoma\";\n"
                                    "color: white;\n"
                                    "}\n"
                                    ".QPushButton:hover {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                    "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), stop:1 rgba("
                                    "97, 164, 255, 255));\n "
                                    "}\n"
                                    ".QTableWidget{\n"
                                    "border-radius: 20px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit {\n"
                                    "border: 1px solid rgb(200, 200, 200);\n"
                                    "border-top: 0px;\n"
                                    "border-left: 0px;\n"
                                    "border-right:0px;\n"
                                    "font: 75 10pt \"Tahoma\";\n"
                                    "}\n"
                                    "\n"
                                    ".QDialog {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(addUserDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IdText = QtWidgets.QLabel(addUserDialog)
        self.IdText.setMinimumSize(QtCore.QSize(200, 21))
        self.IdText.setMaximumSize(QtCore.QSize(172, 21))
        self.IdText.setObjectName("IdText")
        self.horizontalLayout.addWidget(self.IdText)
        self.idGet = QtWidgets.QLineEdit(addUserDialog)
        self.idGet.setAlignment(QtCore.Qt.AlignCenter)
        self.idGet.setObjectName("idGet")
        self.horizontalLayout.addWidget(self.idGet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loginText = QtWidgets.QLabel(addUserDialog)
        self.loginText.setMinimumSize(QtCore.QSize(200, 21))
        self.loginText.setMaximumSize(QtCore.QSize(172, 21))
        self.loginText.setObjectName("loginText")
        self.horizontalLayout_2.addWidget(self.loginText)
        self.loginGet = QtWidgets.QLineEdit(addUserDialog)
        self.loginGet.setAlignment(QtCore.Qt.AlignCenter)
        self.loginGet.setObjectName("loginGet")
        self.horizontalLayout_2.addWidget(self.loginGet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.passText = QtWidgets.QLabel(addUserDialog)
        self.passText.setMinimumSize(QtCore.QSize(200, 21))
        self.passText.setMaximumSize(QtCore.QSize(172, 21))
        self.passText.setObjectName("passText")
        self.horizontalLayout_3.addWidget(self.passText)
        self.passGet = QtWidgets.QLineEdit(addUserDialog)
        self.passGet.setAlignment(QtCore.Qt.AlignCenter)
        self.passGet.setObjectName("passGet")
        self.horizontalLayout_3.addWidget(self.passGet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.roleText = QtWidgets.QLabel(addUserDialog)
        self.roleText.setMinimumSize(QtCore.QSize(200, 21))
        self.roleText.setMaximumSize(QtCore.QSize(172, 21))
        self.roleText.setObjectName("roleText")
        self.horizontalLayout_5.addWidget(self.roleText)
        self.roleGet = QtWidgets.QLineEdit(addUserDialog)
        self.roleGet.setAlignment(QtCore.Qt.AlignCenter)
        self.roleGet.setObjectName("roleGet")
        self.horizontalLayout_5.addWidget(self.roleGet)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okButt = QtWidgets.QPushButton(addUserDialog)
        self.okButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okButt.setObjectName("okButt")
        self.horizontalLayout_4.addWidget(self.okButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(addUserDialog)
        QtCore.QMetaObject.connectSlotsByName(addUserDialog)

        self.checkAddUser()

    def retranslateUi(self, addUserialog):
        _translate = QtCore.QCoreApplication.translate
        addUserialog.setWindowTitle(_translate("addUserialog", "Добавить пользователя"))
        self.IdText.setText(_translate("addUserialog", "ID  пользователя"))
        self.loginText.setText(_translate("addUserialog", "Логин"))
        self.passText.setText(_translate("addUserialog", "Пароль"))
        self.roleText.setText(_translate("addUserialog", "ID  роли"))
        self.okButt.setText(_translate("addUserialog", "Готово"))

    def checkAddUser(self):
        self.okButt.clicked.connect(lambda: self.adding())

    def adding(self):
        dbWork.addUser(self.loginUser, self.passUser, self.idGet.text(), self.loginGet.text(),
                       self.passGet.text(), self.roleGet.text())


class Ui_delUserDialog(object):
    def setupUi(self, delUserDialog, loginUser, passUser):
        self.loginUser = loginUser
        self.passUser = passUser

        delUserDialog.setObjectName("addUserialog")
        delUserDialog.resize(500, 200)
        delUserDialog.setMinimumSize(QtCore.QSize(500, 200))
        delUserDialog.setMaximumSize(QtCore.QSize(500, 200))
        delUserDialog.setStyleSheet("QLabel {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, y2:0.539773, "
                                    "stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, 255), stop:0.676617 "
                                    "rgba(120, 226, 255, 255));\n "
                                    "padding-left: 6px;\n"
                                    "padding-right:6px;\n"
                                    "border-radius:10px;\n"
                                    "max-width:160px;\n"
                                    "font: 75 8pt \"Tahoma\";\n"
                                    "color:white;\n"
                                    "}\n"
                                    ".QPushButton{\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                    "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                    "border-radius: 10px;\n"
                                    "font: 75 8pt \"Tahoma\";\n"
                                    "color: white;\n"
                                    "}\n"
                                    ".QPushButton:hover {\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                    "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), stop:1 rgba("
                                    "97, 164, 255, 255));\n "
                                    "}\n"
                                    ".QTableWidget{\n"
                                    "border-radius: 20px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit {\n"
                                    "border: 1px solid rgb(200, 200, 200);\n"
                                    "border-top: 0px;\n"
                                    "border-left: 0px;\n"
                                    "border-right:0px;\n"
                                    "font: 75 10pt \"Tahoma\";\n"
                                    "}\n"
                                    "\n"
                                    ".QDialog {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(delUserDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loginText = QtWidgets.QLabel(delUserDialog)
        self.loginText.setMinimumSize(QtCore.QSize(200, 21))
        self.loginText.setMaximumSize(QtCore.QSize(172, 21))
        self.loginText.setObjectName("loginText")
        self.horizontalLayout_2.addWidget(self.loginText)
        self.loginGet = QtWidgets.QLineEdit(delUserDialog)
        self.loginGet.setAlignment(QtCore.Qt.AlignCenter)
        self.loginGet.setObjectName("loginGet")
        self.horizontalLayout_2.addWidget(self.loginGet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okButt = QtWidgets.QPushButton(delUserDialog)
        self.okButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okButt.setObjectName("okButt")
        self.horizontalLayout_4.addWidget(self.okButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(delUserDialog)
        QtCore.QMetaObject.connectSlotsByName(delUserDialog)

        self.checkAddUser()

    def retranslateUi(self, addUserialog):
        _translate = QtCore.QCoreApplication.translate
        addUserialog.setWindowTitle(_translate("addUserialog", "Удалить пользователя"))
        self.loginText.setText(_translate("addUserialog", "Логин"))
        self.okButt.setText(_translate("addUserialog", "Готово"))

    def checkAddUser(self):
        self.okButt.clicked.connect(lambda: self.adding())

    def adding(self):
        dbWork.dellUser(self.loginUser, self.passUser, self.loginGet.text())


class Ui_findGroupDialog(object):
    def setupUi(self, findGroupDialog, loginUser, passUser):
        self.loginUser = loginUser
        self.passUser = passUser

        findGroupDialog.setObjectName("findGroupDialog")
        findGroupDialog.resize(800, 600)
        findGroupDialog.setMinimumSize(QtCore.QSize(800, 600))
        findGroupDialog.setMaximumSize(QtCore.QSize(800, 600))
        findGroupDialog.setStyleSheet("QLabel {\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, "
                                      "y2:0.539773, stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, 255), "
                                      "stop:0.676617 rgba(120, 226, 255, 255));\n "
                                      "padding-left: 6px;\n"
                                      "padding-right:6px;\n"
                                      "border-radius:10px;\n"
                                      "max-width:160px;\n"
                                      "font: 75 8pt \"Tahoma\";\n"
                                      "color:white;\n"
                                      "}\n"
                                      ".QPushButton{\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                      "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                      "border-radius: 10px;\n"
                                      "font: 75 8pt \"Tahoma\";\n"
                                      "color: white;\n"
                                      "}\n"
                                      ".QPushButton:hover {\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                      "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), "
                                      "stop:1 rgba(97, 164, 255, 255));\n "
                                      "}\n"
                                      ".QTableWidget{\n"
                                      "border-radius: 20px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit {\n"
                                      "border: 1px solid rgb(200, 200, 200);\n"
                                      "border-top: 0px;\n"
                                      "border-left: 0px;\n"
                                      "border-right:0px;\n"
                                      "font: 75 10pt \"Tahoma\";\n"
                                      "}\n"
                                      "\n"
                                      ".QDialog {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(findGroupDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupText = QtWidgets.QLabel(findGroupDialog)
        self.groupText.setMinimumSize(QtCore.QSize(200, 21))
        self.groupText.setMaximumSize(QtCore.QSize(172, 21))
        self.groupText.setObjectName("groupText")
        self.horizontalLayout_2.addWidget(self.groupText)
        self.groupGet = QtWidgets.QLineEdit(findGroupDialog)
        self.groupGet.setAlignment(QtCore.Qt.AlignCenter)
        self.groupGet.setObjectName("groupGet")
        self.horizontalLayout_2.addWidget(self.groupGet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okTimeButt = QtWidgets.QPushButton(findGroupDialog)
        self.okTimeButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okTimeButt.setObjectName("okTimeButt")
        self.horizontalLayout_4.addWidget(self.okTimeButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.timeTable = QtWidgets.QTableWidget(findGroupDialog)
        self.timeTable.setObjectName("timeTable")
        self.timeTable.setColumnCount(3)
        self.timeTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.timeTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.timeTable)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lessonText = QtWidgets.QLabel(findGroupDialog)
        self.lessonText.setMinimumSize(QtCore.QSize(200, 21))
        self.lessonText.setMaximumSize(QtCore.QSize(172, 21))
        self.lessonText.setObjectName("lessonText")
        self.horizontalLayout_3.addWidget(self.lessonText)
        self.lessonGet = QtWidgets.QLineEdit(findGroupDialog)
        self.lessonGet.setAlignment(QtCore.Qt.AlignCenter)
        self.lessonGet.setObjectName("lessonGet")
        self.horizontalLayout_3.addWidget(self.lessonGet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.okLessonButt = QtWidgets.QPushButton(findGroupDialog)
        self.okLessonButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okLessonButt.setObjectName("okLessonButt")
        self.horizontalLayout_5.addWidget(self.okLessonButt)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.lessonTable = QtWidgets.QTableWidget(findGroupDialog)
        self.lessonTable.setObjectName("lessonTable")
        self.lessonTable.setColumnCount(7)
        self.lessonTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lessonTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessonTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessonTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessonTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessonTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessonTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.lessonTable.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.lessonTable)

        self.retranslateUi(findGroupDialog)
        QtCore.QMetaObject.connectSlotsByName(findGroupDialog)

        self.checksearchL()
        self.checksearchT()

    def retranslateUi(self, findGroupDialog):
        _translate = QtCore.QCoreApplication.translate
        findGroupDialog.setWindowTitle(_translate("findGroupDialog", "Поиск расписания по группе"))
        self.groupText.setText(_translate("findGroupDialog", "Введите группу"))
        self.okTimeButt.setText(_translate("findGroupDialog", "Готово"))
        item = self.timeTable.horizontalHeaderItem(0)
        item.setText(_translate("findGroupDialog", "ID"))
        item = self.timeTable.horizontalHeaderItem(1)
        item.setText(_translate("findGroupDialog", "Группа"))
        item = self.timeTable.horizontalHeaderItem(2)
        item.setText(_translate("findGroupDialog", "ID занятия"))
        self.lessonText.setText(_translate("findGroupDialog", "Введите ID занятия"))
        self.okLessonButt.setText(_translate("findGroupDialog", "Готово"))
        item = self.lessonTable.horizontalHeaderItem(0)
        item.setText(_translate("findGroupDialog", "ID"))
        item = self.lessonTable.horizontalHeaderItem(1)
        item.setText(_translate("findGroupDialog", "Дата"))
        item = self.lessonTable.horizontalHeaderItem(2)
        item.setText(_translate("findGroupDialog", "Номер пары"))
        item = self.lessonTable.horizontalHeaderItem(3)
        item.setText(_translate("findGroupDialog", "Кабинет"))
        item = self.lessonTable.horizontalHeaderItem(4)
        item.setText(_translate("findGroupDialog", "Тип занятия"))
        item = self.lessonTable.horizontalHeaderItem(5)
        item.setText(_translate("findGroupDialog", "ID преподаватель-дисциплина"))
        item = self.lessonTable.horizontalHeaderItem(6)
        item.setText(_translate("findGroupDialog", "Семестр"))

    def checksearchT(self):
        self.okTimeButt.clicked.connect(lambda: self.searchTime())

    def searchTime(self):
        timeList = dbWork.searchTimetable(self.loginUser, self.passUser, self.groupGet.text())
        rowNumb = 0
        self.timeTable.setRowCount(len(timeList))
        for row in timeList:
            self.timeTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.timeTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.timeTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            rowNumb += 1

    def checksearchL(self):
        self.okLessonButt.clicked.connect(lambda: self.searchLess())

    def searchLess(self):
        lessonList = dbWork.searchLesson(self.loginUser, self.passUser, self.lessonGet.text())
        rowNumb = 0
        self.lessonTable.setRowCount(len(lessonList))
        for row in lessonList:
            self.lessonTable.setItem(rowNumb, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.lessonTable.setItem(rowNumb, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.lessonTable.setItem(rowNumb, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.lessonTable.setItem(rowNumb, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.lessonTable.setItem(rowNumb, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.lessonTable.setItem(rowNumb, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.lessonTable.setItem(rowNumb, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            rowNumb += 1


class Ui_trahcserStudDial(object):
    def setupUi(self, trahcserStudDial, loginUser, passUser):
        self.loginUser = loginUser
        self.passUser = passUser

        trahcserStudDial.setObjectName("trahcserStudDial")
        trahcserStudDial.resize(500, 300)
        trahcserStudDial.setMinimumSize(QtCore.QSize(500, 300))
        trahcserStudDial.setMaximumSize(QtCore.QSize(500, 300))
        trahcserStudDial.setStyleSheet("QLabel {\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0.528, x2:1, "
                                       "y2:0.539773, stop:0 rgba(213, 117, 255, 255), stop:0 rgba(67, 65, 255, 255), "
                                       "stop:0.676617 rgba(120, 226, 255, 255));\n "
                                       "padding-left: 6px;\n"
                                       "padding-right:6px;\n"
                                       "border-radius:10px;\n"
                                       "max-width:160px;\n"
                                       "font: 75 8pt \"Tahoma\";\n"
                                       "color:white;\n"
                                       "}\n"
                                       ".QPushButton{\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,  "
                                       "stop:0 rgba(205, 66, 255, 255),  stop:1 rgba(0, 108, 255, 255));\n "
                                       "border-radius: 10px;\n"
                                       "font: 75 8pt \"Tahoma\";\n"
                                       "color: white;\n"
                                       "}\n"
                                       ".QPushButton:hover {\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                       "stop:0 rgba(217, 112, 255, 255), stop:0.5 rgba(111, 234, 255, 255), "
                                       "stop:1 rgba(97, 164, 255, 255));\n "
                                       "}\n"
                                       ".QTableWidget{\n"
                                       "border-radius: 20px;\n"
                                       "}\n"
                                       "\n"
                                       "QLineEdit {\n"
                                       "border: 1px solid rgb(200, 200, 200);\n"
                                       "border-top: 0px;\n"
                                       "border-left: 0px;\n"
                                       "border-right:0px;\n"
                                       "font: 75 10pt \"Tahoma\";\n"
                                       "}\n"
                                       "\n"
                                       ".QDialog {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(trahcserStudDial)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IdDTText = QtWidgets.QLabel(trahcserStudDial)
        self.IdDTText.setMinimumSize(QtCore.QSize(200, 21))
        self.IdDTText.setMaximumSize(QtCore.QSize(172, 21))
        self.IdDTText.setObjectName("IdDTText")
        self.horizontalLayout.addWidget(self.IdDTText)
        self.idStudGet = QtWidgets.QLineEdit(trahcserStudDial)
        self.idStudGet.setAlignment(QtCore.Qt.AlignCenter)
        self.idStudGet.setObjectName("idStudGet")
        self.horizontalLayout.addWidget(self.idStudGet)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.teachText = QtWidgets.QLabel(trahcserStudDial)
        self.teachText.setMinimumSize(QtCore.QSize(200, 21))
        self.teachText.setMaximumSize(QtCore.QSize(172, 21))
        self.teachText.setObjectName("teachText")
        self.horizontalLayout_2.addWidget(self.teachText)
        self.teachGet = QtWidgets.QLineEdit(trahcserStudDial)
        self.teachGet.setAlignment(QtCore.Qt.AlignCenter)
        self.teachGet.setObjectName("teachGet")
        self.horizontalLayout_2.addWidget(self.teachGet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.okButt = QtWidgets.QPushButton(trahcserStudDial)
        self.okButt.setMinimumSize(QtCore.QSize(70, 21))
        self.okButt.setObjectName("okButt")
        self.horizontalLayout_4.addWidget(self.okButt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(trahcserStudDial)
        QtCore.QMetaObject.connectSlotsByName(trahcserStudDial)

        self.checkButt()

    def retranslateUi(self, trahcserStudDial):
        _translate = QtCore.QCoreApplication.translate
        trahcserStudDial.setWindowTitle(_translate("trahcserStudDial", "Перевести студента "))
        self.IdDTText.setText(_translate("trahcserStudDial", "ID  студента"))
        self.teachText.setText(_translate("trahcserStudDial", "Шифр новой группы"))
        self.okButt.setText(_translate("trahcserStudDial", "Готово"))

    def checkButt(self):
        self.okButt.clicked.connect(lambda: self.transfer())

    def transfer(self):
        dbWork.transferStud(self.loginUser, self.passUser, self.idStudGet.text(), self.teachGet.text())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    AuthWindow = QtWidgets.QMainWindow()
    AuthWindow.setWindowIcon(QtGui.QIcon('icon.png'))
    ui = Ui_Auth()
    ui.setupUi(AuthWindow)
    AuthWindow.show()
    sys.exit(app.exec_())
