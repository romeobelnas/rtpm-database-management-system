import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class add_data_7(object):
    def add(self):
        try:
            name = self.name.text()
            birth = self.birth.text()
            section = self.section.text()
            first = self.first.text()
            second = self.second.text()
            third = self.third.text()
            fourth = self.fourth.text()
            lrn = self.lrn.text()

            con = sqlite3.connect("data.db")
            cursor = con.cursor()
            print("Connected to database")

            Id = cursor.execute("SELECT Id FROM grade7")
            Id = len(Id.fetchall())

            sql = f"""INSERT INTO grade7 (Id, Name, Birth, Section, First, Second, Third, Fourth, LRN)
                VALUES ('{Id+1}', '{name}', '{birth}', '{section}', '{first}', '{second}', '{third}', '{fourth}', '{lrn}');"""

            cursor.execute(sql)
            con.commit()
            print("Successful")

            msg = QMessageBox()
            msg.setWindowTitle("Successfully Added")
            msg.setText("You can now close this.")

            msg.exec_()

        except sqlite3.Error as e:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText(e)
            print(e)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 332)
        MainWindow.setStyleSheet("background-color: rgb(234, 154, 165);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 20, 637, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.main_label = QtWidgets.QLabel(self.verticalLayoutWidget)

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label.setFont(font)
        self.main_label.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label.setObjectName("main_label")

        self.verticalLayout.addWidget(self.main_label)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(405, 260, 113, 39))
        self.pushButton_3.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.add)

        self.main_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_2.setGeometry(QtCore.QRect(40, 150, 221, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_2.setFont(font)
        self.main_label_2.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_2.setObjectName("main_label_2")

        self.main_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_3.setGeometry(QtCore.QRect(270, 150, 111, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_3.setFont(font)
        self.main_label_3.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_3.setObjectName("main_label_3")

        self.main_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_4.setGeometry(QtCore.QRect(390, 150, 111, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_4.setFont(font)
        self.main_label_4.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_4.setObjectName("main_label_4")

        self.main_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_5.setGeometry(QtCore.QRect(520, 150, 51, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_5.setFont(font)
        self.main_label_5.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_5.setObjectName("main_label_5")

        self.main_label_9 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_9.setGeometry(QtCore.QRect(580, 150, 51, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_9.setFont(font)
        self.main_label_9.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_9.setObjectName("main_label_9")

        self.second = QtWidgets.QLineEdit(self.centralwidget)
        self.second.setGeometry(QtCore.QRect(580, 180, 51, 20))
        self.second.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.second.setObjectName("second")

        self.main_label_10 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_10.setGeometry(QtCore.QRect(700, 150, 51, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_10.setFont(font)
        self.main_label_10.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_10.setObjectName("main_label_10")

        self.fourth = QtWidgets.QLineEdit(self.centralwidget)
        self.fourth.setGeometry(QtCore.QRect(700, 180, 51, 20))
        self.fourth.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.fourth.setObjectName("fourth")

        self.main_label_11 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_11.setGeometry(QtCore.QRect(640, 150, 51, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_11.setFont(font)
        self.main_label_11.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_11.setObjectName("main_label_11")

        self.third = QtWidgets.QLineEdit(self.centralwidget)
        self.third.setGeometry(QtCore.QRect(640, 180, 51, 20))
        self.third.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.third.setObjectName("third")

        self.main_label_6 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_6.setGeometry(QtCore.QRect(760, 150, 151, 20))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_6.setFont(font)
        self.main_label_6.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_6.setObjectName("main_label_6")

        self.first = QtWidgets.QLineEdit(self.centralwidget)
        self.first.setGeometry(QtCore.QRect(520, 180, 51, 20))
        self.first.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.first.setObjectName("first")

        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(40, 180, 221, 20))
        self.name.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.name.setObjectName("name")

        self.section = QtWidgets.QLineEdit(self.centralwidget)
        self.section.setGeometry(QtCore.QRect(390, 180, 111, 20))
        self.section.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.section.setObjectName("section")

        self.lrn = QtWidgets.QLineEdit(self.centralwidget)
        self.lrn.setGeometry(QtCore.QRect(760, 180, 151, 20))
        self.lrn.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.lrn.setObjectName("lrn")

        self.birth = QtWidgets.QLineEdit(self.centralwidget)
        self.birth.setGeometry(QtCore.QRect(270, 180, 111, 20))
        self.birth.setStyleSheet("background-color: rgb(240,234,214)\n")
        self.birth.setObjectName("birth")

        self.main_label_7 = QtWidgets.QLabel(self.centralwidget)
        self.main_label_7.setGeometry(QtCore.QRect(520, 110, 231, 31))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.main_label_7.setFont(font)
        self.main_label_7.setStyleSheet("background-color: rgb(240,234,214);\n border: 1px solid black")
        self.main_label_7.setObjectName("main_label_7")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">RTPM-DSHS Student Database Managent System</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Add"))
        self.main_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Name</p></body></html>"))
        self.main_label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Date of Birth</p></body></html>"))
        self.main_label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Section</p></body></html>"))
        self.main_label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">1st</p></body></html>"))
        self.main_label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">2nd</p></body></html>"))
        self.main_label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">4th</p></body></html>"))
        self.main_label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">3rd</p></body></html>"))
        self.main_label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">LRN</p></body></html>"))
        self.main_label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Grades</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("Inventory System")
    ui = add_data_7()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
