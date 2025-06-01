import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello, world!")
        
        self.setLayout(qtw.QVBoxLayout())
        
        myLabel = qtw.QLabel("Pick something from the list!")
        myLabel.setFont(qtg.QFont('Helvetica', 18))
        
        self.layout().addWidget(myLabel)
        
        mySpin = qtw.QSpinBox(self,
                            value=10,
                            maximum=100,
                            minimum=0,
                            singleStep=5,
                            prefix='#',
                            suffix=' order')
        mySpin.setFont(qtg.QFont('Helvetica', 18))
        
        self.layout().addWidget(mySpin)
        
        myButton = qtw.QPushButton("Press me", 
                                clicked=lambda: press_it())
        
        self.layout().addWidget(myButton)  
        
        def press_it():
            myLabel.setText(f"You picked: {mySpin.text()}!")
        
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()