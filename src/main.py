from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
import random

class PlaceHolder(QWidget):
    def __init__(self):
        super().__init__()
        colors = ["red", "green", "blue", "yellow", "purple"]
        title = QLabel("Hola buenas")
        button = QPushButton("Hola")
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(title)
        layout.addWidget(button)

        button.clicked.connect(lambda: title.setStyleSheet(f"color: {colors[random.randint(0, len(colors) - 1)]};")) 

        self.show()


#Lo dejo asi mientras miramos que hacer JASJASJAS  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.setCentralWidget(PlaceHolder())


if __name__ == "__main__":
    app = QApplication([])
    try:
        with open("style\\style.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("No se encontró el archivo de estilo.")
    window = MainWindow()
    window.show()
    app.exec()