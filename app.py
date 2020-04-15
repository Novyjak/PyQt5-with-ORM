from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

# pouze pro spuštění, složka MainWindow je nejdůležitější
App = QApplication(sys.argv)
window = MainWindow()
sys.exit(App.exec())