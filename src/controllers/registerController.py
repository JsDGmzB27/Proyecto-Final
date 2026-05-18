from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *
from config.database import agregar_usuario, buscar_usuario

class RegisterController(QObject):
    
    changeLoginSignal = pyqtSignal()

    def __init__(self, view):
        super().__init__()
        self.view = view

        self.view.register_button.clicked.connect(self.register)
        self.view.back_to_login_button.clicked.connect(self.changeLoginSignal.emit)

    def register(self):
        email = self.view.email_input.text()
        username = self.view.username_input.text()
        password = self.view.password_input.text()
        if email != "" and username != "" and password != "":
            if "@" in email and "." in email:
                if buscar_usuario(username) == "Usuario no encontrado":
                    try:
                        agregar_usuario(username, password, email)
                        QMessageBox.information(self.view, "Éxito", "Usuario registrado exitosamente.")
                        self.changeLoginSignal.emit()
                    except ValueError as e:
                        QMessageBox.warning(self.view, "Error", str(e))
                else:
                    QMessageBox.warning(self.view, "Error", "El nombre de usuario ya existe.")
            else:
                QMessageBox.warning(self.view, "Error", "Por favor, ingrese un correo electrónico válido.")
        else:
            QMessageBox.warning(self.view, "Error", "Por favor, complete todos los campos.")