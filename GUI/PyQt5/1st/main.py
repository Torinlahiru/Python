import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__a()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    

if __name__ == "__main__":
    main()