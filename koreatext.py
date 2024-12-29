import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Label 생성
        self.label = QLabel('한글을 입력해주세요')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 16))

        # Line Edit 생성
        self.lineEdit = QLineEdit()
        self.lineEdit.setFont(QFont('Arial', 16))
        self.lineEdit.textChanged.connect(self.on_text_changed)

        # Layout 생성
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)

        self.setLayout(layout)

    # Text changed 이벤트 핸들러
    def on_text_changed(self, text):
        print(text)
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
