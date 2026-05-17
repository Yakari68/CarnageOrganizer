import sys
from app.core.state import AppState
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow

if __name__=="__main__":
    app = QApplication(sys.argv)
    state=AppState()
    window = MainWindow(state=state)
    window.show()
    sys.exit(app.exec())
