import sys
from PySide2.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide2.QtCore import Qt

class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.label = QLabel("Drag a file here", self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.label.setText(file_path)

app = QApplication(sys.argv)
window = DragDropWidget()
window.show()
sys.exit(app.exec_())
