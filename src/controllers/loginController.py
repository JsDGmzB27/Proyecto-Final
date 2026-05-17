from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *


class LoginController(QObject):
    
    loginSignal = pyqtSignal()

    def __init__(self, view):
        super().__init__()
        self.view = view

        self.view.login_button.clicked.connect(self.login)


    def login(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()

        print(f"Username: {username}, Password: {password}")

        if username == "admin" and password == "admin":
            self.loginSignal.emit()
        else:
            QMessageBox.warning(self.view, "Login Failed", "Invalid username or password.")