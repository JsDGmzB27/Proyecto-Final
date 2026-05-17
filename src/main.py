from PyQt6.QtWidgets import *
from ui.windows.login import LoginUi
from ui.windows.lobby import LobbyUi
from controllers.loginController import LoginController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.stack = QStackedWidget()
        self.login_ui = LoginUi()
        self.lobby_ui = LobbyUi()

        self.stack.addWidget(self.login_ui)
        self.stack.addWidget(self.lobby_ui)

        self.login_controller = LoginController(self.login_ui)
        self.login_controller.loginSignal.connect(lambda: self.stack.setCurrentWidget(self.lobby_ui))
    
        
        self.setCentralWidget(self.stack)
        

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