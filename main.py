import sys
import time

from HashTable import *

from mainWindow import *
from addRecordWindow import *
from changeRecordWindow import *
from deleteByKeyWindow import *
from deleteByValueWindow import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QLineEdit, QTableWidget
from PyQt5.QtCore import pyqtSignal


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)

    import traceback
    text += ''.join(traceback.format_tb(tb))

    print('Error: ', text)
    QMessageBox.critical(None, 'Error', text)
    quit()


class AddRecordWin(QWidget, Ui_AddDialog):
    adding_data = pyqtSignal(str, str, str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ChangeRecordWin(QWidget, Ui_ChangeDialog):
    changing_data = pyqtSignal(str, str, str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class DeleteByKeyWin(QWidget, Ui_DeleteKeyDialog):
    deleting_key_data = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class DeleteByValueWin(QWidget, Ui_DeleteByValueDialog):
    deleting_value_data = pyqtSignal(bool, bool, bool, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWin(QMainWindow, Ui_MainWindow):
    start_add_time, end_add_time = None, None
    start_delete_key_time, end_delete_key_time = None, None
    start_delete_value_time, end_delete_value_time = None, None
    start_search_key_time, end_search_key_time = None, None
    start_search_value_time, end_search_value_time = None, None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hash_table = None

        self.initialize_windows()
        self.work_with_menu()

    def handle_input_add(self, key, val1, val2, val3):
        if self.hash_table:
            self.start_add_time = time.time()
            self.hash_table.add(key, val1, val2, val3)
            self.end_add_time = time.time()

    def handle_input_change(self, key, val1, val2, val3):
        if self.hash_table:
            self.hash_table.change(key, val1, val2, val3)

    def handle_input_delete_key(self, key):
        if self.hash_table:
            self.start_delete_key_time = time.time()
            self.hash_table.delitem(key)
            self.end_delete_key_time = time.time()

    def handle_input_delete_value(self, tf1, tf2, tf3, val):
        if self.hash_table:
            if tf1 and not tf2 and not tf3:
                self.start_delete_value_time = time.time()
                self.hash_table.delitem_value(val, None, None)
                self.end_delete_value_time = time.time()
            elif not tf1 and tf2 and not tf3:
                self.start_delete_value_time = time.time()
                self.hash_table.delitem_value(None, val, None)
                self.end_delete_value_time = time.time()
            elif not tf1 and not tf2 and tf3:
                self.start_delete_value_time = time.time()
                self.hash_table.delitem_value(None, None, val)
                self.end_delete_value_time = time.time()
            else:
                pass

    def handle_input_search(self):
        if self.hash_table:
            if self.idEdit.text() and self.serialNameEdit.text() == '' and self.numSeriesEdit.text() == ''\
                    and self.isWatchedEdit.text() == '':
                self.start_search_key_time = time.time()
                self.hash_table.getitem(self.idEdit.text())
                self.end_search_key_time = time.time()
            else:
                if self.serialNameEdit.text() and self.numSeriesEdit.text() == '' and self.isWatchedEdit.text() == '':
                    self.start_search_value_time = time.time()
                    self.hash_table.getitem_value(self.serialNameEdit.text(), None, None)
                    self.end_search_value_time = time.time()
                elif self.serialNameEdit.text() == '' and self.numSeriesEdit.text() and self.isWatchedEdit.text() == '':
                    self.start_search_value_time = time.time()
                    self.hash_table.getitem_value(None, self.numSeriesEdit.text(), None)
                    self.end_search_value_time = time.time()
                elif self.serialNameEdit.text() == '' and self.numSeriesEdit.text() == '' and self.isWatchedEdit.text():
                    self.start_search_value_time = time.time()
                    self.hash_table.getitem_value(None, None, self.isWatchedEdit.text())
                    self.end_search_value_time = time.time()
                else:
                    pass

    def initialize_windows(self):
        self.add_w = AddRecordWin()
        self.add_w.adding_data.connect(self.handle_input_add)
        self.add_w.okButton.clicked.connect(self.send_data_add_w)
        self.add_w.cancelButton.clicked.connect(self.close)

        self.change_w = ChangeRecordWin()
        self.change_w.changing_data.connect(self.handle_input_change)
        self.change_w.okButton.clicked.connect(self.send_data_change_w)
        self.change_w.cancelButton.clicked.connect(self.close)

        self.delete_k_w = DeleteByKeyWin()
        self.delete_k_w.deleting_key_data.connect(self.handle_input_delete_key)
        self.delete_k_w.okButton.clicked.connect(self.send_data_delete_k_w)
        self.delete_k_w.cancelButton.clicked.connect(self.close)

        self.delete_v_w = DeleteByValueWin()
        self.delete_v_w.deleting_value_data.connect(self.handle_input_delete_value)
        self.delete_v_w.okButton.clicked.connect(self.send_data_delete_v_w)
        self.delete_v_w.cancelButton.clicked.connect(self.close)

        self.searchButton.clicked.connect(self.search_data)

        self.tableWidget.setHorizontalHeaderLabels(['id', 'serial_name', 'number_of_series', 'is_watched'])
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setFixedSize(545, 271)

        self.showButton.clicked.connect(self.show_hash_table)

    def work_with_menu(self):
        self.actionNew.triggered.connect(self.create_new_hash_table)
        self.actionOpen.triggered.connect(self.open_hash_table)
        self.actionSave.triggered.connect(self.save_hash_table)
        self.actionClean.triggered.connect(self.clean_hash_table)
        self.actionDelete.triggered.connect(self.delete_hash_table)
        self.actionAddRecord.triggered.connect(self.show_AddRecordWin)
        self.actionChangeRecord.triggered.connect(self.show_ChangeRecordWin)
        self.actionDelete_by_key.triggered.connect(self.show_DeleteByKeyWin)
        self.actionDelete_by_value.triggered.connect(self.show_DeleteByValueWin)

    def create_new_hash_table(self):
        self.hash_table = HashTable()

    def open_hash_table(self):
        self.create_new_hash_table()
        filename = QFileDialog.getOpenFileName(self, 'Open file', '/data', "Image files (*.txt)")[0]
        self.hash_table.open_data_base(filename)
        #self.hash_table.str()

    def save_hash_table(self):
        if self.hash_table:
            if self.hash_table.current_size:
                #self.hash_table.str()
                filename = QFileDialog.getSaveFileName(self, 'Open file', '/data', "Image files (*.txt)")[0]
                self.hash_table.save_data_base(filename)

    def clean_hash_table(self):
        if self.hash_table:
            self.hash_table.clean()

    def delete_hash_table(self):
        del self.hash_table

    def show_AddRecordWin(self):
        self.add_w.show()

    def show_ChangeRecordWin(self):
        self.change_w.show()

    def show_DeleteByKeyWin(self):
        self.delete_k_w.show()

    def show_DeleteByValueWin(self):
        self.delete_v_w.show()

    def show_hash_table(self):
        try:
            if self.hash_table:
                if self.tableWidget:
                    self.tableWidget.clear()
                    self.tableWidget.setHorizontalHeaderLabels(['id', 'serial_name', 'number_of_series', 'is_watched'])
                    self.tableWidget.setRowCount(0)
                records_list = self.hash_table.repr()
                for record in records_list:
                    row_position = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_position)
                    for i in range(4):
                        self.tableWidget.setItem(row_position, i, QtWidgets.QTableWidgetItem(str(record[i])))
        except AttributeError:
            pass

    def send_data_add_w(self):
        self.add_w.adding_data.emit(
            self.add_w.idEdit.text(),
            self.add_w.serialNameEdit.text(),
            self.add_w.numSeriesEdit.text(),
            self.add_w.isWatchedEdit.text())
        '''print("def send_data(self): ",
              self.add_w.idEdit.text(),
              self.add_w.serialNameEdit.text(),
              self.add_w.numSeriesEdit.text(),
              self.add_w.isWatchedEdit.text())  # Пытаюсь посмотреть что лежит в собранных данных, временная мера'''
        self.add_w.hide()

    def send_data_change_w(self):
        self.change_w.changing_data.emit(
            self.change_w.idEdit.text(),
            self.change_w.serialNameEdit.text(),
            self.change_w.numSeriesEdit.text(),
            self.change_w.isWatchedEdit.text())
        self.change_w.hide()

    def send_data_delete_k_w(self):
        self.delete_k_w.deleting_key_data.emit(self.delete_k_w.idEdit.text())
        self.delete_k_w.hide()

    def send_data_delete_v_w(self):
        self.delete_v_w.deleting_value_data.emit(self.delete_v_w.serialNameBox.isChecked(),
                                                 self.delete_v_w.numSeriesBox.isChecked(),
                                                 self.delete_v_w.isWatchedBox.isChecked(),
                                                 self.delete_v_w.valueEdit.text())
        self.delete_v_w.hide()

    def search_data(self):
        try:
            if self.hash_table:
                if self.tableWidget:
                    self.tableWidget.clear()
                    self.tableWidget.setHorizontalHeaderLabels(['id', 'serial_name', 'number_of_series', 'is_watched'])
                    self.tableWidget.setRowCount(0)
                self.handle_input_search()
                records_list = self.hash_table.repr(path='service_files/result_search.txt')
                for record in records_list:
                    row_position = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_position)
                    for i in range(4):
                        self.tableWidget.setItem(row_position, i, QtWidgets.QTableWidgetItem(str(record[i])))
        except AttributeError:
            pass

    def time_statistic(self):
        print('Adding new record: ', self.end_add_time-self.start_add_time)
        print('Deleting by key: ', self.end_delete_key_time-self.start_delete_key_time)
        print('Deleting by one value: ', self.end_delete_value_time-self.start_delete_value_time)
        print('Searching by key: ', self.end_search_key_time-self.start_search_key_time)
        print('Searching by value: ', self.end_search_value_time-self.start_search_value_time)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.time_statistic()
            event.accept()
        else:
            event.ignore()


sys.excepthook = log_uncaught_exceptions


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()
    sys.exit(app.exec_())
