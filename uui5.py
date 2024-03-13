import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class JsonTable(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JSON File Table")
        self.setGeometry(100, 100, 600, 400)

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        self.populate_table()

    def populate_table(self):
        files = [f for f in os.listdir('.') if f.endswith('.json')]
        self.table_widget.setRowCount(len(files))
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['File Name', 'Array Length'])

        for i, file_name in enumerate(files):
            with open(file_name) as f:
                data = json.load(f)
                array_len = len(data)
                self.table_widget.setItem(i, 0, QTableWidgetItem(file_name))
                self.table_widget.setItem(i, 1, QTableWidgetItem(str(array_len)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JsonTable()
    window.show()
    sys.exit(app.exec_())
