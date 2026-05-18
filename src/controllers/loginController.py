from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *
from config.database import validar_usuario


class LoginController(QObject):
    
    loginSignal = pyqtSignal()
    changeRegisterSignal = pyqtSignal()

    def __init__(self, view):
        super().__init__()
        self.view = view

        self.view.login_button.clicked.connect(self.login)
        self.view.register_button.clicked.connect(self.changeRegisterSignal.emit)


    def login(self):
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        try:
            usuario = validar_usuario(username, password)
            if usuario:
                self.loginSignal.emit()
                with open("cache/current_user.txt", "w") as f:
                    f.write(f"{usuario["usuario"]}")
        except ValueError as e:
            QMessageBox.critical(self.view, "Error", str(e))