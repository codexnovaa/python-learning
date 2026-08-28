#Consist of: PyQt5 GUI intro | PyQt5 labels |  PyQt5 images | PyQt5 layout managers | PyQt5 buttons | PyQt5 Checkboxes | PyQt5 RadioButtons | LineWIdgets/Textbox | setStyleSheet

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("My first GUI")
        #self.setGeometry(700, 300, 500, 500)
        #self.setWindowIcon(QIcon("sample.jpg"))
        #self.button = QPushButton("Click here!", self)
        #self.checkbox = QCheckBox("Do you like pizza?", self)
        #self.label = QLabel("Hello World", self)
        #self.radio1 = QRadioButton("Visa", self)
        #self.radio2 = QRadioButton("MasterCard", self)
        #self.radio3 = QRadioButton("GiftCard", self)
        #self.radio4 = QRadioButton("In-Store", self)
        #self.radio5 = QRadioButton("Online", self)
        #self.buttonGroup1 = QButtonGroup(self)
        #self.buttonGroup2 = QButtonGroup(self)
        #self.textbox = QLineEdit(self)
        #self.button = QPushButton("Submit", self)
        
        #label1 = QLabel("Hello World", self)
        #label1.setGeometry(0, 0, 500, 100)
        #label1.setFont(QFont("Arial", 25))
        #label1.setStyleSheet("color: blue; font-family: Verdana; font-size: 35px; font-weight: 500; font-style: italic; background-color: black;")
        #label1.setAlignment(Qt.AlignCenter)
        
        #pixmap = QPixmap("simple avatar.jpg")
        
        #label2 = QLabel(self)
        #label2.setGeometry(0, 0, 250, 250)
        #label2.setPixmap(pixmap)
        #label2.setScaledContents(True)
        #label2.setGeometry((self.width() - label2.width()) // 2, 
        #                    (self.height() - label2.height() // 2), 
        #                    label2.width(), 
        #                    label2.height())
        #label1.setAlignment(Qt.AlignTop) #Vertically to the Top
        #label1.setAlignment(Qt.AlignBottom) #Vertically to the Bottom
        #label1.setAlignment(Qt.AlignVCenter) #Vertically to the Center
        
        #label1.setAlignment(Qt.AlignRight) #Horizontally Right
        #label1.setAlignment(Qt.AlignHCenter) #Horizontally Center
        #label1.setAlignment(Qt.AlignLeft) #Horizontally Left
        
        #label1.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Center & Top
        #label1.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Center & Bottom
        #label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Center & Center
        #label1.setAlignment(Qt.AlignCenter) # Shorcut to Center & Center
        
        self.button1 = QPushButton("Button1")
        self.button2 = QPushButton("Button2")
        self.button3 = QPushButton("Button3")
        self.initUI()
        
        
    #def initUI(self):
    #    centralWidget = QWidget()
    #    self.setCentralWidget(centralWidget)
    #    
    #    label1 = QLabel("#1")
    #    label2 = QLabel("#2")
    #    label3 = QLabel("#3")
    #    label4 = QLabel("#4")
    #    label5 = QLabel("#5")
    #    
    #    label1.setStyleSheet("background-color: red;")
    #    label2.setStyleSheet("background-color: blue;")
    #    label3.setStyleSheet("background-color: yellow;")
    #    label4.setStyleSheet("background-color: brown;")
    #    label5.setStyleSheet("background-color: lime;")
    #    
    #    grid = QGridLayout()
    #    grid.addWidget(label1, 0, 0)
    #    grid.addWidget(label2, 0, 1)
    #    grid.addWidget(label3, 1, 0)
    #    grid.addWidget(label4, 1, 1)
    #    grid.addWidget(label5, 2, 0)
    #    
    #    centralWidget.setLayout(grid)
    
    def initUI(self):
        #self.button.setGeometry(150, 200, 200, 100)
        #self.button.setStyleSheet("font-size: 15px")
        #self.button.clicked.connect(self.onClick)
        #
        #self.label.setGeometry(100, 300, 300, 100)
        #self.label.setStyleSheet("font-size: 25px; background-color: black; color: white;")
        #self.label.setAlignment(Qt.AlignCenter)
        #
        #self.checkbox.setGeometry(10, 0, 200, 100)
        #self.checkbox.setStyleSheet("font-size: 20px;")
        ##self.checkbox.setChecked(True)
        #self.checkbox.stateChanged.connect(self.onChecked)
        #
        #self.radio1.setGeometry(300, 0, 300, 50)
        #self.radio2.setGeometry(300, 50, 300, 50)
        #self.radio3.setGeometry(300, 100, 300, 50)
        #self.radio4.setGeometry(300, 150, 300, 50)
        #self.radio5.setGeometry(300, 200, 300, 50)
        #
        #self.setStyleSheet("QRadioButton{font-size: 20px; font-family: Arial; }")
        #
        #self.buttonGroup1.addButton(self.radio1)
        #self.buttonGroup1.addButton(self.radio2)
        #self.buttonGroup1.addButton(self.radio3)
        #self.buttonGroup2.addButton(self.radio4)
        #self.buttonGroup2.addButton(self.radio5)
        #
        #self.radio1.toggled.connect(self.radioButtonToggle)
        #self.radio2.toggled.connect(self.radioButtonToggle)
        #self.radio3.toggled.connect(self.radioButtonToggle)
        #self.radio4.toggled.connect(self.radioButtonToggle)
        #self.radio5.toggled.connect(self.radioButtonToggle)
        
        #self.textbox.setGeometry(20, 20, 170, 40)
        #self.textbox.setStyleSheet("font-size: 17px; font-family: Arial;")
        #self.textbox.setPlaceholderText("Enter your name")
        #self.button.setGeometry(190, 20, 100, 40)
        #self.button.setStyleSheet("font-size: 25px; font-family: Arial; background-color: blue; color: white; border-radius: 5px; border: none")
        #self.button.clicked.connect(self.submit)
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addWidget(self.button1)
        horizontalLayout.addWidget(self.button2)
        horizontalLayout.addWidget(self.button3)
        
        centralWidget.setLayout(horizontalLayout)
        
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        self.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                font-family: Arial;
                padding: 10px 25px;
                margin: 20px;
                border: 3px solid;
                border-radius: 5px
            }
            
            QPushButton#button1{
                background-color: hsl(59, 79%, 69%);
            }
            
            QPushButton#button2{
                background-color: hsl(115, 79%, 69%);
            }
            
            QPushButton#button3{
                background-color: hsl(197, 79%, 69%);
            }
            
            QPushButton#button1:hover{
                background-color: hsl(62, 99%, 59%);
            }
            QPushButton#button2:hover{
                background-color: hsl(125, 93%, 36%);
            }
             QPushButton#button3:hover{
                background-color: hsl(242, 71%, 54%);
            }
                           """)
        
    #def onClick(self):
    #    print("Button Clicked!")
    #    self.button.setText("Button is Clicked!")
    #    self.button.setDisabled(True)
    #    self.label.setText("Hello world from python!")
        
    #def onChecked(self, state):
    #    if state == Qt.Checked:
    #        print("You like pizza!")
    #    else:
    #        print("You dont like pizza.")
            
    #def radioButtonToggle(self):
    #    radioButton = self.sender()
    #    if radioButton.isChecked():
    #        print(f"{radioButton.text()} is selected")
            
    #def submit(self):
    #    text = self.textbox.text()
    #    print(f"Hello {text}")
        
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
            