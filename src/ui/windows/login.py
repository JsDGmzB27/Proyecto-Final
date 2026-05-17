from PyQt6.QtWidgets import *

class LoginUi(QWidget):
    def __init__(self):
        super().__init__()

        self.login_title = QLabel("Login")
        self.login_button = QPushButton("Login")
        self.username_label = QLabel("Username")
        self.password_label = QLabel("Password")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()

        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        username_layout = QHBoxLayout()
        username_layout.addWidget(self.username_label)
        username_layout.addWidget(self.username_input)

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)

        login_layout = QVBoxLayout()
        login_layout.addWidget(self.login_title)
        login_layout.addLayout(username_layout)
        login_layout.addLayout(password_layout)
        login_layout.addWidget(self.login_button)

        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        hLayout.addStretch()
        hLayout.addLayout(login_layout)
        hLayout.addStretch()

        vLayout.addStretch()
        vLayout.addLayout(hLayout)
        vLayout.addStretch()

        self.setLayout(vLayout)
