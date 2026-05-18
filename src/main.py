from PyQt6.QtWidgets import *
from ui.windows.login import LoginUi
from ui.windows.lobby import LobbyUi
from ui.windows.register import RegisterUi
from controllers.loginController import LoginController
from controllers.registerController import RegisterController
from controllers.settingsController import SettingsController
from controllers.profileController import ProfileController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.stack = QStackedWidget()
        self.login_ui = LoginUi()
        self.lobby_ui = LobbyUi()
        self.register_ui = RegisterUi()
        self.stack.addWidget(self.login_ui)
        self.stack.addWidget(self.lobby_ui)
        self.stack.addWidget(self.register_ui)

        self.login_controller = LoginController(self.login_ui)
        self.login_controller.loginSignal.connect(lambda: self.stack.setCurrentWidget(self.lobby_ui))
        self.login_controller.changeRegisterSignal.connect(lambda: self.stack.setCurrentWidget(self.register_ui))

        self.register_controller = RegisterController(self.register_ui)
        self.register_controller.changeLoginSignal.connect(lambda: self.stack.setCurrentWidget(self.login_ui))

        self.settings_controller = SettingsController(self.lobby_ui.settings_page)
        self.settings_controller.logoutSignal.connect(lambda: self.stack.setCurrentWidget(self.login_ui))
        self.setCentralWidget(self.stack)
        
        self.profile_controller = ProfileController(self.lobby_ui.profile_page)


if __name__ == "__main__":
    app = QApplication([])
    try:
        with open("style\\style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("No se encontró el archivo de estilo.")
    window = MainWindow()
    window.showMaximized()
    app.exec()