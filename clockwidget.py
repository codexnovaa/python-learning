#Simple Digital Clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timeLabel = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Simple Digital Clock")
        self.setGeometry(800, 500, 300, 100)
        self.setStyleSheet("background-color: black;")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        self.setLayout(vbox)
        
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("""
                    font-size: 50px;
                    font-family: Arial;
                    color: lime;
                                     """)
        
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
    
    def updateTime(self):
        currentTime = QTime.currentTime().toString("hh:mm:ss AP")
        self.timeLabel.setText(currentTime)
     
    
def main():
    application = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(application.exec_())
    
if __name__ == "__main__":
    main()