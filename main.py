import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

import json
import os
import keyboard
import mouse
import time

from ui_main import Ui_MainWindow

class GameActions:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.delay = 0.01

    def mouse_left(self):
        mouse.click("left")

    def mouse_right(self):
        mouse.click("right")

    def start_left_click(self):
        for _ in range(50):
            self.mouse_left()
            time.sleep(self.delay)

    def drop_all(self):
        s_x, s_y = mouse.get_position()
        keyboard.press_and_release("i")
        time.sleep(0.2)
        for x, y in self.coordinates:
            keyboard.press("ctrl")
            mouse.move(x, y)
            self.mouse_left()
            keyboard.release("ctrl")
            time.sleep(0.02)
        keyboard.press_and_release("i")
        mouse.move(s_x, s_y, absolute=True)

    def sell_all(self):
        s_x, s_y = mouse.get_position()
        time.sleep(0.2)
        for x, y in self.coordinates:
            mouse.move(x, y)
            self.mouse_right()
            time.sleep(0.02)
        mouse.move(s_x, s_y, absolute=True)


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.inventory_coords = [
            (1292, 760), (1348, 760), (1407, 760),
            (1458, 763), (1517, 761), (1568, 762),
            (1624, 762), (1686, 762), (1733, 762),
            (1788, 759), (1843, 757), (1295, 841),
            (1352, 838), (1405, 841), (1464, 839),
            (1508, 840), (1576, 841), (1627, 839),
            (1680, 841), (1733, 842), (1793, 838),
            (1842, 836), (1289, 920), (1349, 917),
            (1401, 919), (1459, 917), (1514, 919),
            (1569, 918), (1625, 922), (1680, 919),
            (1735, 920), (1787, 921), (1842, 918)
        ]

        self.game_actions = GameActions(self.inventory_coords)

        self.btn_actv.setCheckable(True)
        self.btn_actv.clicked.connect(self.btn_activate)

        self.binding = self.load_config()
        self.script_set_text()
        self.init_scripts()
        self.register_hotkeys(activate=False)

    def load_config(self):
        default = {
            "sell all": "F1",
            "drop all": "F2",
            "more click": "w"
        }
        try:
            if os.path.exists('keyboard.json'):
                with open('keyboard.json', 'r') as f:
                    user_bindings = json.load(f)
                    return {**default, **user_bindings}

            with open('keyboard.json', 'w') as f:
                json.dump(default, f, indent=4)
                return default
        except Exception:
            return default

    def script_set_text(self):
        for i, (action, key) in enumerate(self.binding.items(), 1):
            if hasattr(self, f'script_{i}'):
                getattr(self, f'script_{i}').setText(f"{key} - {action}")

    def init_scripts(self):
        self.scripts = {
            "sell all": self.game_actions.sell_all,
            "drop all": self.game_actions.drop_all,
            "more click": self.game_actions.start_left_click
        }

    def register_hotkeys(self, activate=False):
        keyboard.unhook_all()
        for action, key in self.binding.items():
            def handler(action=action):
                if self.btn_actv.isChecked() and action in self.scripts:
                    self.scripts[action]()

            keyboard.add_hotkey(key, handler, suppress=activate)

    def btn_activate(self):
        if self.btn_actv.isChecked():
            self.btn_actv.setText('Deactivated')
            self.setWindowIcon(QIcon(":/ui/logo_active.svg"))
            self.register_hotkeys(activate=True)
        else:
            self.btn_actv.setText('Activated')
            self.setWindowIcon(QIcon(":/ui/logo.svg"))
            self.register_hotkeys(activate=False)

    def closeEvent(self, event):
        keyboard.unhook_all()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())