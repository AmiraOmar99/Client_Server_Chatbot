# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
# class Ui_MainWindow(QtWidgets.QMainWindow):
    # def __init__(self):
    #     QtGui.QMainWindow.__init__(self)
    #     self.ui=Ui_MainWindow()
    #     self.ui.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DocBot")
        title='DocBot'
        MainWindow.setWindowTitle(title)
        mW = QtGui.QIcon("Mw.png")
        MainWindow.setWindowIcon(mW)
        MainWindow.resize(931, 787)
        MainWindow.setStyleSheet("/*Copyright (c) DevSec Studio. All rights reserved.\n"
"\n"
"MIT License\n"
"\n"
"Permission is hereby granted, free of charge, to any person obtaining a copy\n"
"of this software and associated documentation files (the \"Software\"), to deal\n"
"in the Software without restriction, including without limitation the rights\n"
"to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
"copies of the Software, and to permit persons to whom the Software is\n"
"furnished to do so, subject to the following conditions:\n"
"\n"
"The above copyright notice and this permission notice shall be included in all\n"
"copies or substantial portions of the Software.\n"
"\n"
"THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
"IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
"FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
"AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
"LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
"OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"*/\n"
"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #292f45;\n"
"    color: #000000;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: #292f45;\n"
"    color: #b9b9bb;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #f0742f;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 17px;\n"
"    border-color: #f0742f;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #fc7c11;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #ff6b35;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"    background-color: #292f45;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: #fc7c11;\n"
"    color: #000000;\n"
"    padding: 2px;\n"
"    border-radius: 15px;\n"
"    border-color: #fc7c11;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: #fc7c11;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit{\n"
"    background-color: #292f45;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #00111d;\n"
"    border: 1px solid #f0742f;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\"); /*To replace*/\n"
"    background-color: #1f2b2b;\n"
"    border: 1px solid #f0742f;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #f0742f;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(180, 10, 561, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet("color: rgb(245, 121, 0);")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.first_msg = QtWidgets.QLabel(self.centralwidget)
        self.first_msg.setGeometry(QtCore.QRect(20, 80, 831, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.first_msg.setFont(font)
        self.first_msg.setObjectName("first_msg")
        self.fst_name = QtWidgets.QLabel(self.centralwidget)
        self.fst_name.setGeometry(QtCore.QRect(30, 170, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fst_name.setFont(font)
        self.fst_name.setObjectName("fst_name")
        self.fst_name_box = QtWidgets.QLineEdit(self.centralwidget)
        self.fst_name_box.setGeometry(QtCore.QRect(20, 220, 321, 41))
        self.fst_name_box.setObjectName("fst_name_box")

        self.gender = QtWidgets.QLabel(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(470, 170,  311, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.gender.setText('Gender')
        self.gender_combo = QtWidgets.QComboBox(self.centralwidget)
        self.gender_combo.setGeometry(QtCore.QRect(470, 220, 321, 41))
        self.gender_combo.setObjectName("gender_box")
        self.gender_combo.addItem('Female')
        self.gender_combo.addItem('Male')



        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(420, 700, 121, 41))
        self.add.setObjectName("add")
        self.lst_name_box = QtWidgets.QLineEdit(self.centralwidget)
        self.lst_name_box.setGeometry(QtCore.QRect(20, 340, 321, 41))
        self.lst_name_box.setObjectName("lst_name_box")
        self.lst_name = QtWidgets.QLabel(self.centralwidget)
        self.lst_name.setGeometry(QtCore.QRect(30, 290, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lst_name.setFont(font)
        self.lst_name.setObjectName("lst_name")
        self.ssn = QtWidgets.QLabel(self.centralwidget)
        self.ssn.setGeometry(QtCore.QRect(30, 410, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ssn.setFont(font)
        self.ssn.setObjectName("ssn")
        self.ssn_box = QtWidgets.QLineEdit(self.centralwidget)
        self.ssn_box.setGeometry(QtCore.QRect(20, 460, 321, 41))
        self.ssn_box.setObjectName("ssn_box")
        self.age = QtWidgets.QLabel(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(30, 530, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.age_box = QtWidgets.QLineEdit(self.centralwidget)
        self.age_box.setGeometry(QtCore.QRect(20, 580, 321, 41))
        self.age_box.setObjectName("age_box")
        self.chronic_box = QtWidgets.QLineEdit(self.centralwidget)
        self.chronic_box.setGeometry(QtCore.QRect(20, 700, 321, 41))
        self.chronic_box.setObjectName("chronic_box")
        self.chronic = QtWidgets.QLabel(self.centralwidget)
        self.chronic.setGeometry(QtCore.QRect(30, 650, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chronic.setFont(font)
        self.chronic.setObjectName("chronic")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 170, 861, 521))
        self.widget.setObjectName("widget")
        self.widget.hide()
        self.cough = QtWidgets.QCheckBox(self.widget)
        self.cough.setGeometry(QtCore.QRect(30, 80, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cough.setFont(font)
        self.cough.setObjectName("cough")
        self.fatigue = QtWidgets.QCheckBox(self.widget)
        self.fatigue.setGeometry(QtCore.QRect(30, 140, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fatigue.setFont(font)
        self.fatigue.setObjectName("fatigue")
        self.headache = QtWidgets.QCheckBox(self.widget)
        self.headache.setGeometry(QtCore.QRect(30, 200, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.headache.setFont(font)
        self.headache.setObjectName("headache")
        self.fever = QtWidgets.QCheckBox(self.widget)
        self.fever.setGeometry(QtCore.QRect(30, 330, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fever.setFont(font)
        self.fever.setObjectName("fever")
        self.diarrhea = QtWidgets.QCheckBox(self.widget)
        self.diarrhea.setGeometry(QtCore.QRect(30, 390, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.diarrhea.setFont(font)
        self.diarrhea.setObjectName("diarrhea")
        self.throat = QtWidgets.QCheckBox(self.widget)
        self.throat.setGeometry(QtCore.QRect(30, 450, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.throat.setFont(font)
        self.throat.setObjectName("throat")
        self.chest = QtWidgets.QCheckBox(self.widget)
        self.chest.setGeometry(QtCore.QRect(470, 80, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.chest.setFont(font)
        self.chest.setObjectName("chest")
        self.common = QtWidgets.QLabel(self.widget)
        self.common.setGeometry(QtCore.QRect(30, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.common.setFont(font)
        self.common.setObjectName("common")
        self.less = QtWidgets.QLabel(self.widget)
        self.less.setGeometry(QtCore.QRect(30, 270, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.less.setFont(font)
        self.less.setObjectName("less")
        self.severe = QtWidgets.QLabel(self.widget)
        self.severe.setGeometry(QtCore.QRect(470, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.severe.setFont(font)
        self.severe.setObjectName("severe")
        self.taste = QtWidgets.QCheckBox(self.widget)
        self.taste.setGeometry(QtCore.QRect(470, 140, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.taste.setFont(font)
        self.taste.setObjectName("taste")
        self.rash = QtWidgets.QCheckBox(self.widget)
        self.rash.setGeometry(QtCore.QRect(470, 200, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rash.setFont(font)
        self.rash.setObjectName("rash")
        self.analysis = QtWidgets.QLineEdit(self.widget)
        self.analysis.setGeometry(QtCore.QRect(280, 350, 581, 71))
        self.analysis.setObjectName("analysis")
        self.consult = QtWidgets.QPushButton(self.widget)
        self.consult.setGeometry(QtCore.QRect(670, 270, 131, 41))
        self.consult.setObjectName("consult")
        self.consult.hide()

        self.new = QtWidgets.QPushButton(self.widget)
        self.new.setGeometry(QtCore.QRect(670, 430, 131, 41))
        self.new.setObjectName("new")
        self.new.setText('New Test')
        self.new.hide()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.data=[self.fst_name, self.fst_name_box, self.lst_name, self.lst_name_box, self.ssn, self.ssn_box, self.age, self.age_box, self.chronic, self.chronic_box, self.gender, self.gender_combo]
        self.comm=[self.cough, self.fatigue, self.headache]
        self.less_list=[self.fever, self.diarrhea, self.throat]
        self.sev=[self.chest, self.taste, self.rash]

        # self.timer = QtCore.QTimer()

        # # # # * adding action to timer
        # # self.timer.timeout.connect(self.check_timeout(x=recieve()))

        # # * update the timer every tenth second
        # self.timer.start(100)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "Hi ! This is your DOCBOT!"))
        self.first_msg.setText(_translate("MainWindow", "In order to have your data in our database, kindly fill these informations correctly and carefully"))
        self.fst_name.setText(_translate("MainWindow", "Please, Enter your first name:"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.lst_name.setText(_translate("MainWindow", "Last name:"))
        self.ssn.setText(_translate("MainWindow", "SSN"))
        self.age.setText(_translate("MainWindow", "Age"))
        self.chronic.setText(_translate("MainWindow", "Any Chronic Diseases?"))
        self.cough.setText(_translate("MainWindow", "Cough"))
        self.fatigue.setText(_translate("MainWindow", "Fatigue"))
        self.headache.setText(_translate("MainWindow", "Headache"))
        self.fever.setText(_translate("MainWindow", "Fever"))
        self.diarrhea.setText(_translate("MainWindow", "Diarrhea"))
        self.throat.setText(_translate("MainWindow", "Sore Throat"))
        self.chest.setText(_translate("MainWindow", "Chest Pain"))
        self.common.setText(_translate("MainWindow", "Common symptoms"))
        self.less.setText(_translate("MainWindow", "Less Common symptoms"))
        self.severe.setText(_translate("MainWindow", "Severe symptoms"))
        self.taste.setText(_translate("MainWindow", "Loss of taste or smell"))
        self.rash.setText(_translate("MainWindow", "Rash"))
        self.consult.setText(_translate("MainWindow", "Consult"))
