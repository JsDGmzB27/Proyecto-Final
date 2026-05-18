from PyQt6.QtWidgets import *

class ProfileUI(QWidget):
    def __init__(self):
        super().__init__()

        self.profile_title = QLabel("Profile")
        self.username_label = QLabel("Username: ")
        self.email_label = QLabel("Email: ")

        vLayout = QVBoxLayout()
        vLayout.addStretch()
        vLayout.addWidget(self.profile_title)
        vLayout.addWidget(self.username_label)
        vLayout.addWidget(self.email_label)
        vLayout.addStretch()

        self.setLayout(vLayout)