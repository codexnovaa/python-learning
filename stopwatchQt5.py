# Simple PyQt5 Stopwatch

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.timeLabel = QLabel("00:00:00.00", self)
        self.startBtn = QPushButton("Start", self)
        self.stopBtn = QPushButton("Stop", self)
        self.resetBtn = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Simple Stopwatch")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        self.setLayout(vbox)
        
        self.timeLabel.setAlignment(Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.startBtn)
        hbox.addWidget(self.stopBtn)
        hbox.addWidget(self.resetBtn)
        
        vbox.addLayout(hbox)
        
        self.startBtn.setObjectName("startBtn")
        self.stopBtn.setObjectName("stopBtn")
        self.resetBtn.setObjectName("resetBtn")
        
        self.setStyleSheet("""
                QPushButton{
                    font-size: 20px;
                    font-family: Arial;
                    font-weight: bold;
                    padding: 10px 25px;
                    border: 2px solid;
                    border-radius: 5px;
                }
                
                QPushButton#startBtn{
                    background-color: hsl(205, 77%, 55%);
                }
                
                QPushButton#stopBtn{
                    background-color: hsl(355, 65%, 50%);
                }
                
                QPushButton#resetBtn{
                    background-color: hsl(58, 60%, 49%);
                }
                
                QPushButton#startBtn:hover{
                    background-color: hsl(218, 88%, 48%);
                }
                
                QPushButton#stopBtn:hover{
                    background-color: hsl(0, 97%, 50%);
                }
                
                QPushButton#resetBtn:hover{
                    background-color: hsl(61, 100%, 50%);
                }
                
                
                QLabel{
                    font-size: 100px;
                    font-weight: bold;
                    background-color: hsl(59, 99%, 77%);
                    border-radius: 10px;
                    padding: 10px;
                }       
                           """)

        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.stop)
        self.resetBtn.clicked.connect(self.reset)
        self.timer.timeout.connect(self.updateDisplay)
        
        
        
    def start(self):
        self.timer.start(10)
        
    def stop(self):
        self.timer.stop()
        
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.timeLabel.setText("00:00:00.00")
        
    def formatTime(self, time):
        hour = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hour:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
        
    def updateDisplay(self):
        self.time = self.time.addMSecs(10)
        self.timeLabel.setText(self.formatTime(self.time))
        
def main():
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()