from PyQt5.QtWidgets import QHBoxLayout,QPushButton



class ContentBarLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.convertButton = QPushButton('Convert')

        self.addWidget(self.convertButton)



