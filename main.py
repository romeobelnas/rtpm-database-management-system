import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from add_data_7 import add_data_7
from add_data_8 import add_data_8
from add_data_9 import add_data_9
from add_data_10 import add_data_10
from add_data_11 import add_data_11
from add_data_12 import add_data_12
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)
        self.pushButton.clicked.connect(self.open_home)
        self.pushButton_2.clicked.connect(self.Close)
        self.pushButton_4.clicked.connect(self.open_find_a_student)

    def open_home(self):
        widget.setCurrentIndex(widget.currentIndex() + 0)

    def Close(self):
        sys.exit(app.exec_())

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


class find_a_student(QMainWindow):
    def __init__(self):
        super(find_a_student, self).__init__()
        loadUi("find_a_student.ui", self)

        self.pushButton.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.Close)
        self.pushButton_3.clicked.connect(self.open_junior_high)
        self.pushButton_6.clicked.connect(self.open_senior_high)

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def Close(self):
        sys.exit(app.exec_())

    def open_junior_high(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def open_senior_high(self):
        widget.setCurrentIndex(widget.currentIndex()+6)


class junior_high(QMainWindow):
    def __init__(self):
        super(junior_high, self).__init__()
        loadUi("junior_high.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.Close)
        self.pushButton_3.clicked.connect(self.open_grade7)
        self.pushButton_7.clicked.connect(self.open_grade8)
        self.pushButton_6.clicked.connect(self.open_grade9)
        self.pushButton_8.clicked.connect(self.open_grade10)
        self.pushButton_4.clicked.connect(self.open_find_a_student)

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def Close(self):
        sys.exit(app.exec_())

    def open_grade7(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedSize(994, 697)

    def open_grade8(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
        widget.setFixedSize(994, 697)

    def open_grade9(self):
        widget.setCurrentIndex(widget.currentIndex()+3)
        widget.setFixedSize(994, 697)

    def open_grade10(self):
        widget.setCurrentIndex(widget.currentIndex()+4)
        widget.setFixedSize(994, 697)

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


class grade7(QMainWindow):
    def __init__(self):
        super(grade7, self).__init__()
        loadUi("grade7.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def refresh(self):
        loadUi("grade7.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def add_data(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = add_data_7()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def delete_data(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM grade7")
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                Id = data[0]
                Name = data[1]
                Birth = data[2]
                Section = data[3]
                First = data[4]
                Second = data[5]
                Third = data[6]
                Fourth = data[7]
                LRN = data[8]
                cursor.execute("""DELETE FROM grade7 WHERE Id=? AND Name=? AND Birth=? AND Section=? AND First=? AND 
                                   Second=? AND Third=? AND Fourth=? AND LRN=?""", (Id, Name, Birth, Section, First,
                                                                                    Second, Third, Fourth, LRN))
                connection.commit()
                self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        sqlquery = "SELECT * FROM grade7"
        num_of_rows = cursor.execute("SELECT Id FROM grade7")
        num_of_rows = len(num_of_rows.fetchall())

        self.tableWidget.setRowCount(num_of_rows)
        table_row = 0
        cursor = cursor.execute("SELECT * FROM grade7")
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[8])))

            table_row += 1

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.setFixedSize(640, 430)

    def Close(self):
        sys.exit(app.exec_())

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()-3)
        widget.setFixedSize(640, 430)


class grade8(QMainWindow):
    def __init__(self):
        super(grade8, self).__init__()
        loadUi("grade8.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def refresh(self):
        loadUi("grade8.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def add_data(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = add_data_8()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def delete_data(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM grade8")
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                Id = data[0]
                Name = data[1]
                Birth = data[2]
                Section = data[3]
                First = data[4]
                Second = data[5]
                Third = data[6]
                Fourth = data[7]
                LRN = data[8]
                cursor.execute("""DELETE FROM grade8 WHERE Id=? AND Name=? AND Birth=? AND Section=? AND First=? AND 
                                       Second=? AND Third=? AND Fourth=? AND LRN=?""", (Id, Name, Birth, Section, First,
                                                                                        Second, Third, Fourth, LRN))
                connection.commit()
                self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        sqlquery = "SELECT * FROM grade8"
        num_of_rows = cursor.execute("SELECT Id FROM grade8")
        num_of_rows = len(num_of_rows.fetchall())

        self.tableWidget.setRowCount(num_of_rows)
        table_row = 0
        cursor = cursor.execute("SELECT * FROM grade8")
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[8])))

            table_row += 1

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
        widget.setFixedSize(640, 430)

    def Close(self):
        sys.exit(app.exec_())

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()-3)


class grade9(QMainWindow):
    def __init__(self):
        super(grade9, self).__init__()
        loadUi("grade9.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def refresh(self):
        loadUi("grade9.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def add_data(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = add_data_9()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def delete_data(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM grade9")
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                Id = data[0]
                Name = data[1]
                Birth = data[2]
                Section = data[3]
                First = data[4]
                Second = data[5]
                Third = data[6]
                Fourth = data[7]
                LRN = data[8]
                cursor.execute("""DELETE FROM grade9 WHERE Id=? AND Name=? AND Birth=? AND Section=? AND First=? AND 
                                           Second=? AND Third=? AND Fourth=? AND LRN=?""",
                               (Id, Name, Birth, Section, First,
                                Second, Third, Fourth, LRN))
                connection.commit()
                self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        sqlquery = "SELECT * FROM grade9"
        num_of_rows = cursor.execute("SELECT Id FROM grade9")
        num_of_rows = len(num_of_rows.fetchall())

        self.tableWidget.setRowCount(num_of_rows)
        table_row = 0
        cursor = cursor.execute("SELECT * FROM grade9")
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[8])))

            table_row += 1

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-3)
        widget.setFixedSize(640, 430)

    def Close(self):
        sys.exit(app.exec_())

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()-4)


class grade10(QMainWindow):
    def __init__(self):
        super(grade10, self).__init__()
        loadUi("grade10.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def refresh(self):
        loadUi("grade10.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def add_data(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = add_data_10()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def delete_data(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM grade10")
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                Id = data[0]
                Name = data[1]
                Birth = data[2]
                Section = data[3]
                First = data[4]
                Second = data[5]
                Third = data[6]
                Fourth = data[7]
                LRN = data[8]
                cursor.execute("""DELETE FROM grade10 WHERE Id=? AND Name=? AND Birth=? AND Section=? AND First=? AND 
                                               Second=? AND Third=? AND Fourth=? AND LRN=?""",
                               (Id, Name, Birth, Section, First,
                                Second, Third, Fourth, LRN))
                connection.commit()
                self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        sqlquery = "SELECT * FROM grade10"
        num_of_rows = cursor.execute("SELECT Id FROM grade10")
        num_of_rows = len(num_of_rows.fetchall())

        self.tableWidget.setRowCount(num_of_rows)
        table_row = 0
        cursor = cursor.execute("SELECT * FROM grade10")
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[8])))

            table_row += 1

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-4)
        widget.setFixedSize(640, 430)

    def Close(self):
        sys.exit(app.exec_())

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()-5)


class senior_high(QMainWindow):
    def __init__(self):
        super(senior_high, self).__init__()
        loadUi("senior_high.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.Close)
        self.pushButton_3.clicked.connect(self.open_grade11)
        self.pushButton_7.clicked.connect(self.open_grade12)
        self.pushButton_4.clicked.connect(self.open_find_a_student)

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-6)

    def Close(self):
        sys.exit(app.exec_())

    def open_grade11(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedSize(994, 697)

    def open_grade12(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
        widget.setFixedSize(994, 697)

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()-6)


class grade11(QMainWindow):
    def __init__(self):
        super(grade11, self).__init__()
        loadUi("grade11.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def refresh(self):
        loadUi("grade11.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def add_data(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = add_data_11()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def delete_data(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM grade11")
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                Id = data[0]
                Name = data[1]
                Birth = data[2]
                Section = data[3]
                First = data[4]
                Second = data[5]
                Third = data[6]
                Fourth = data[7]
                LRN = data[8]
                cursor.execute("""DELETE FROM grade11 WHERE Id=? AND Name=? AND Birth=? AND Section=? AND First=? AND 
                                                   Second=? AND Third=? AND Fourth=? AND LRN=?""",
                               (Id, Name, Birth, Section, First,
                                Second, Third, Fourth, LRN))
                connection.commit()
                self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        sqlquery = "SELECT * FROM grade11"
        num_of_rows = cursor.execute("SELECT Id FROM grade11")
        num_of_rows = len(num_of_rows.fetchall())

        self.tableWidget.setRowCount(num_of_rows)
        table_row = 0
        cursor = cursor.execute("SELECT * FROM grade11")
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[8])))

            table_row += 1

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.setFixedSize(640, 430)

    def Close(self):
        sys.exit(app.exec_())

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()-7)


class grade12(QMainWindow):
    def __init__(self):
        super(grade12, self).__init__()
        loadUi("grade12.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def refresh(self):
        loadUi("grade12.ui", self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_5.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.delete_data)
        self.pushButton_2.clicked.connect(self.refresh)
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 56)
        self.tableWidget.setColumnWidth(4, 56)
        self.tableWidget.setColumnWidth(5, 56)
        self.tableWidget.setColumnWidth(6, 56)
        self.tableWidget.setColumnWidth(7, 185)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Last Name, First Name, Middle Name", "Date of Birth", "Section", "1st", "2nd", "3rd", "4th", "LRN"])
        self.loaddata()

    def add_data(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = add_data_12()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def delete_data(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM grade12")
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                Id = data[0]
                Name = data[1]
                Birth = data[2]
                Section = data[3]
                First = data[4]
                Second = data[5]
                Third = data[6]
                Fourth = data[7]
                LRN = data[8]
                cursor.execute("""DELETE FROM grade12 WHERE Id=? AND Name=? AND Birth=? AND Section=? AND First=? AND 
                                                       Second=? AND Third=? AND Fourth=? AND LRN=?""",
                               (Id, Name, Birth, Section, First,
                                Second, Third, Fourth, LRN))
                connection.commit()
                self.loaddata()

    def loaddata(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        sqlquery = "SELECT * FROM grade12"
        num_of_rows = cursor.execute("SELECT Id FROM grade12")
        num_of_rows = len(num_of_rows.fetchall())

        self.tableWidget.setRowCount(num_of_rows)
        table_row = 0
        cursor = cursor.execute("SELECT * FROM grade12")
        for row in cursor.execute(sqlquery):
            self.tableWidget.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[7])))
            self.tableWidget.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[8])))

            table_row += 1

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
        widget.setFixedSize(640, 430)

    def Close(self):
        sys.exit(app.exec_())

    def open_find_a_student(self):
        widget.setCurrentIndex(widget.currentIndex()-8)


app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('icon.png'))
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle("Inventory System")

mainwindow = MainWindow()
find_a_Student = find_a_student()

juniorHigh = junior_high()
Grade7 = grade7()

Grade8 = grade8()
Grade9 = grade9()
Grade10 = grade10()

seniorHigh = senior_high()
Grade11 = grade11()
Grade12 = grade12()

widget.addWidget(mainwindow)
widget.addWidget(find_a_Student)

widget.addWidget(juniorHigh)
widget.addWidget(Grade7)

widget.addWidget(Grade8)
widget.addWidget(Grade9)
widget.addWidget(Grade10)

widget.addWidget(seniorHigh)
widget.addWidget(Grade11)
widget.addWidget(Grade12)

widget.setFixedSize(640, 430)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
