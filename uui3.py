import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class JsonUrlCounter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JSON URL Counter")
        self.setGeometry(100, 100, 600, 400)

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["JSON File", "String Count"])

        self.populate_table()

    def count_strings_in_array(self, array):
        return sum(len(item) for item in array)

    def populate_table(self):
        json_files = [file for file in os.listdir('.') if file.endswith('.json')]
        
        row_count = len(json_files)
        self.table_widget.setRowCount(row_count)

        min_string_count = float('inf')

        for i, json_file in enumerate(json_files):
            with open(json_file) as f:
                data = json.load(f)
                string_count = sum(self.count_strings_in_array(data[key]) for key in data)
                min_string_count = min(min_string_count, string_count)
                
            self.table_widget.setItem(i, 0, QTableWidgetItem(json_file))
            self.table_widget.setItem(i, 1, QTableWidgetItem(str(string_count)))

            self.table_widget.item(i, 0).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_widget.item(i, 1).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

        for i in range(row_count):
            if int(self.table_widget.item(i, 1).text()) == min_string_count:
                self.table_widget.item(i, 1).setBackground(Qt.red)

if __name__ == '__main__':
    app = QApplication([])
    window = JsonUrlCounter()
    window.show()
    app.exec_()
