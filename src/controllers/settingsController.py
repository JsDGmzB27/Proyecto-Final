from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *


class SettingsController(QObject):

    logoutSignal = pyqtSignal()

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.view.logout_button.clicked.connect(self.logout)

    def logout(self):
        confirm = QMessageBox.question(self.view, "Confirmar Cierre de Sesión", "¿Estás seguro de que quieres cerrar sesión?")
        if confirm == QMessageBox.StandardButton.Yes:
            self.logoutSignal.emit()