from PyQt5.QtWidgets import QTextEdit, QHBoxLayout, QLabel, QVBoxLayout, QComboBox


class Textarea(QTextEdit):
    pass


class TextLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        # text widget
        self.textareaSrc = Textarea()
        self.textareaDest = Textarea()
        # label
        self.textareaSrcLabel = QLabel('English')
        self.textareaDestLabel = QLabel('Myanmar')
        # combo Box
        self.comboSrc = QComboBox()
        self.comboDest = QComboBox()
        # src
        self.textareaDest.setReadOnly(True)

        # combo && label layout
        textareaBarSrc = QHBoxLayout()
        textareaBarDest = QHBoxLayout()
        # add combo && label Src
        textareaBarSrc.addWidget(self.comboSrc)
        textareaBarSrc.addWidget(self.textareaSrcLabel)
        # add combo && label Dest
        textareaBarDest.addWidget(self.comboDest)
        textareaBarDest.addWidget(self.textareaDestLabel)

        # layout
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()

        # add (combo && label) layout
        layout1.addLayout(textareaBarSrc)
        layout1.addWidget(self.textareaSrc)
        # add (combo && label Dest) Layout
        layout2.addLayout(textareaBarDest)
        layout2.addWidget(self.textareaDest)

        self.addLayout(layout1)
        self.addLayout(layout2)
