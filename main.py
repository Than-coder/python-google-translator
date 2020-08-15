from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QTextEdit, QMessageBox
from PyQt5.Qt import QIcon
import sys
# translate
from googletrans import Translator, LANGCODES

# class
from _class.TextLayout import TextLayout
from _class.ContentBarLayout import ContentBarLayout


app = QApplication(sys.argv)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Google Translator'
        self.top = 150
        self.left = 300
        self.width = 800
        self.height = 500

        self.language = []
        self.currentLanguageSrc = 'en'
        self.currentLanguageDest = 'my'

        self.initUI()
        self.setDefault()
        self.eventListener()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        # main layout
        self.mainLayout = QVBoxLayout()
        # layout class
        self.textLayout = TextLayout()
        self.contentBarLayout = ContentBarLayout()

        # layout add
        self.mainLayout.addLayout(self.contentBarLayout)
        self.mainLayout.addLayout(self.textLayout)

        # set main layout
        self.setLayout(self.mainLayout)

    def setDefault(self):
        lang = LANGCODES
        for l in lang:
            key = l
            value = lang[l]
            self.language.append((key, value))

        # combox box
        for lan in self.language:

            self.textLayout.comboSrc.addItem(lan[0])
            self.textLayout.comboDest.addItem(lan[0])

    ######Event Listener###########
    def eventListener(self):
        # convert button clicked
        self.contentBarLayout.convertButton.clicked.connect(
            self.convertClicked)
        #########
        # textlayout combo box change
        # change src
        self.textLayout.comboSrc.currentTextChanged.connect(
            self.textLayoutComboTextSrcChange)
        # change dest
        self.textLayout.comboDest.currentTextChanged.connect(
            self.textLayoutComboTextDestChange)
        ##########

    ###### event #########

    # convert button click
    def convertClicked(self):
        text = self.textLayout.textareaSrc.toPlainText()
        if text != '':
            try:
                # google translate
                trans = Translator().translate(
                    text, dest=self.currentLanguageDest, src=self.currentLanguageSrc)
                # set dest
                self.textLayout.textareaDest.setPlainText(trans.text)
            except:
                self.showErrorInternetMessage()

    # combo change src
    def textLayoutComboTextSrcChange(self, text):
        for lang in self.language:
            if lang[0] == text:
                # set
                self.textLayout.textareaSrcLabel.setText(text)
                self.currentLanguageSrc = lang[1]
    # combo change dest

    def textLayoutComboTextDestChange(self, text):
        for lang in self.language:
            if lang[0] == text:
                # set
                self.textLayout.textareaDestLabel.setText(text)
                self.currentLanguageDest = lang[1]

    ########### End Event ##########

    def showErrorInternetMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("""
        translate error
        Please Check Internet Connection!
        """)

        msg.exec()


if __name__ == "__main__":

    main = MainWindow()
    main.show()
    sys.exit(app.exec())
