import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt

class DragDropWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setAcceptDrops(True)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setWindowTitle('Drag and Drop File')
        self.setGeometry(300, 300, 600, 400)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            self.textEdit.append(f)

def main():
    app = QApplication(sys.argv)
    ex = DragDropWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
