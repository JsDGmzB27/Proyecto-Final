from PyQt6.QtWidgets import *

class LoginUi(QWidget):
    def __init__(self):
        super().__init__()

        self.loginTitle = QLabel("Login")
        self.loginButton = QPushButton("Login")
        self.usernameLabel = QLabel("Username")
        self.passwordLabel = QLabel("Password")
        self.usernameInput = QLineEdit()
        self.passwordInput = QLineEdit()

        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        
        usernameLayout = QHBoxLayout()
        usernameLayout.addWidget(self.usernameLabel)
        usernameLayout.addWidget(self.usernameInput)

        passwordLayout = QHBoxLayout()
        passwordLayout.addWidget(self.passwordLabel)
        passwordLayout.addWidget(self.passwordInput)

        loginLayout = QVBoxLayout()
        loginLayout.addWidget(self.loginTitle)
        loginLayout.addLayout(usernameLayout)
        loginLayout.addLayout(passwordLayout)
        loginLayout.addWidget(self.loginButton)

        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        hLayout.addStretch()
        hLayout.addLayout(loginLayout)
        hLayout.addStretch()

        vLayout.addStretch()
        vLayout.addLayout(hLayout)
        vLayout.addStretch()

        self.setLayout(vLayout)
