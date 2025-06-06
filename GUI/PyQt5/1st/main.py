import sys 
from PyQt5.Qtwidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    

if __name__ == "__main__":
    main()