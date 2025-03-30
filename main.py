import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

import json
import os
import keyboard

from ui_main import Ui_MainWindow

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_actv.setCheckable(True)
        self.btn_actv.clicked.connect(self.activate)
        self.activate()
        self.keyboard = self.json_load()
        self.set_script_text()

    def activate(self):
        if self.btn_actv.isChecked():
            self.btn_actv.setText('Deactivated')
            self.setWindowIcon(QIcon(":/ui/logo_active.svg"))
        else:
            self.btn_actv.setText('Activated')
            self.setWindowIcon(QIcon(":/ui/logo.svg"))

    def json_load(self):
        default = {
            "sell all": "F1",
            "drop all": "F2",
            "more click": "w"
        }
        path = 'keyboard.json'

        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(default, f, indent=4, ensure_ascii=False)
            return default.copy()
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if all(key in data for key in default):
                    return data
                return {**default, **data}

        except (json.JSONDecodeError, IOError) as e:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(default, f, indent=4, ensure_ascii=False)
            return default.copy()

    def set_script_text(self):
        for i, (action, key) in enumerate(self.keyboard.items(), start=1):
            script_widget = getattr(self, f'script_{i}')
            script_widget.setText(f'{key} - {action}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())