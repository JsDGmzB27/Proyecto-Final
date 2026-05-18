from PyQt6.QtWidgets import *

class RegisterUi(QWidget):
    def __init__(self):
        super().__init__()

        self.register_title = QLabel("Register")
        self.email_label = QLabel("Email")
        self.username_label = QLabel("Username")
        self.password_label = QLabel("Password")
        self.register_button = QPushButton("Register")
        self.back_to_login_button = QPushButton("Back to Login")
        self.email_input = QLineEdit()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()

        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        email_layout = QHBoxLayout()
        email_layout.addWidget(self.email_label)
        email_layout.addWidget(self.email_input)

        username_layout = QHBoxLayout()
        username_layout.addWidget(self.username_label)
        username_layout.addWidget(self.username_input)

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)

        register_layout = QVBoxLayout()
        register_layout.addWidget(self.register_title)
        register_layout.addLayout(email_layout)
        register_layout.addLayout(username_layout)
        register_layout.addLayout(password_layout)
        register_layout.addWidget(self.register_button)
        register_layout.addWidget(self.back_to_login_button)

        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        hLayout.addStretch()
        hLayout.addLayout(register_layout)
        hLayout.addStretch()

        vLayout.addStretch()
        vLayout.addLayout(hLayout)
        vLayout.addStretch()

        self.setLayout(vLayout)