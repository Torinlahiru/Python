import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First PyQt5")
        self.setGeometry(700,300,500,500)
        
        # Get the directory of the current .py file
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Join the image filename to the script's directory
        icon_path = os.path.join(script_dir, "windows.png")
       
        print(icon_path) 
        

        self.setWindowIcon(QIcon(icon_path))
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()

    
print("Icon exists:", os.path.exists("windows.png"))