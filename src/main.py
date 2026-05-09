import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from app.ui.main_widget import mainWidget

if __name__=="__main__":
    class MainWindow(QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)
            self.setWindowTitle("Hello!")
            self.main=mainWidget(self)
            self.setCentralWidget(self.main)
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the app
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())

