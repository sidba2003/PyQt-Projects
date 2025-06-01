import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello, world!")
        
        self.setLayout(qtw.QVBoxLayout())
        
        myLabel = qtw.QLabel("Hello, world! What's your name?")
        myLabel.setFont(qtg.QFont('Helvetica', 18))
        
        self.layout().addWidget(myLabel)
        
        myEntry = qtw.QLineEdit()
        myEntry.setObjectName("name_field")
        myEntry.setText("<your_name>")
        
        self.layout().addWidget(myEntry)
        
        myButton = qtw.QPushButton("Press me", 
                                clicked=lambda: press_it())
        
        self.layout().addWidget(myButton)  
        
        def press_it():
            myLabel.setText(f"Hello, {myEntry.text()}!")     
            myEntry.setText("")
        
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()