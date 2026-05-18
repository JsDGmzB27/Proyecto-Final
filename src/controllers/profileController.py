from PyQt6.QtCore import *
from config.database import buscar_usuario

class ProfileController(QObject):
    def __init__(self, view):
        super().__init__()
        self.view = view

    def cargar_datos_usuario(self):
        try:
            with open("cache/current_user.txt", "r") as f:
                username = f.read().strip()
                usuario = buscar_usuario(username)
                if usuario:
                    self.view.username_label.setText(f"Username: {usuario['usuario']}")
                    self.view.email_label.setText(f"Email: {usuario['correo']}")
        except FileNotFoundError:
            self.view.username_label.setText("Username: N/A")
            self.view.email_label.setText("Email: N/A")
