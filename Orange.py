from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QListWidget,QLabel,QListWidgetItem
from PySide6.QtCore import Qt,QTimer
from PySide6.QtGui import QIcon
import PySide6.QtBluetooth as dan
import sys

class MainWindow(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        #Icon Window

        icon = QIcon("orangeRDC.ico")
        
        self.setWindowIcon(icon)
                
        #Button
        
        def activate() :
            
            self.button_1.setStyleSheet("border-radius : 10px;background-color : #333333;border : 4px solid #d95b43;font-weight : bold ; color : #d95b43")
                        
            devices = self.blue.discoveredDevices()
            
            for device in devices :
                
                info = dan.QBluetoothDeviceInfo(device)
                
                name = info.name()
                
                if name:
                    
                    item = QListWidgetItem(name)
                    
                    self.list_widget.addItem(item)
                            
        self.blue =  dan.QBluetoothDeviceDiscoveryAgent()
        
        self.blue.finished.connect(slot=activate)
        
        self.blue.start()
                        
        button_icon = QIcon("orange.ico")
        
        self.button =  QPushButton(parent=self)
        
        self.button.resize(100,50)
        
        self.button.move(650,600)
        
        self.button.setText("Orange")
        
        self.button.setStyleSheet("background-color : black ; color : #d95b43 ; border-radius : 10px ; font-family : Arial")
        
        self.button.setCursor(Qt.CursorShape(value=13))
        
        self.button.setIcon(button_icon)
        
        self.button.pressed.connect(slot=activate)
        
        self.button.show()
        
        # button
        
        self.button_1 = QPushButton(parent=self)
        
        self.button_1.setText("◉")
        
        self.button_1.setFont("Arial")
        
        self.button_1.move(1200,10)
        
        self.button_1.resize(20,20)
        
        self.button_1.setStyleSheet("border-radius : 10px;background-color : #333333;border : 4px solid gray;font-weight : bold ; color : gray")

        self.button_1.setCursor(Qt.CursorShape(value=13))
                
        self.button_1.show()
        
        # list
        
        self.list_widget = QListWidget(parent=self)
        
        self.list_widget.move(1050,50)
        
        self.list_widget.resize(300,300)
                
        self.list_widget.setStyleSheet("""QListWidget::item {
                                                    border: 1px dashed grey;
                                                    padding: 5px;
                                                }
                                            QListWidget {
                                                    color : whitesmoke ;paddding : 10px;background-color : #333333;font-weight : bold;margin : 1px;font-family : Terminal
                                            }

                                     
                                    """)
        
        self.list_widget.setCursor(Qt.CursorShape(value=13))
        
        self.list_widget.show()
        
        #Label
        
        self.label = QLabel(parent=self)
        
        self.label.setText("")
        
        self.label.resize(200,100)
        
        self.label.setCursor(Qt.CursorShape(value=3))
        
        self.label.move(550,50)
        
        self.label.setFrameStyle(1)
        
        self.label.setStyleSheet("font-size : 30px;font-weight : bold;font-family : Arial;border : 10px solid #333333;background-color : #d95b43")
        
        self.label.show()
        
        #Label 2
        
        self.label_1 = QLabel(parent=self)
        
        self.label_1.setText("ORANGE_RDC")
        
        self.label_1.setCursor(Qt.CursorShape(value=3))
        
        self.label_1.move(580,160)
        
        self.label_1.setStyleSheet("font-size : 20px ; font-weight : bold ; font-family : Arial ; color : #d95b43 ;")
        
        self.label_1.show()
        
if __name__ == "__main__" :
    
    app = QApplication(sys.argv)
    
    window = MainWindow()
    
    opacity = 1.0
    
    window.setWindowOpacity(opacity)
    
    window.setWindowTitle("Wifi ")
    
    window.setStyleSheet("background-color : #333333")
    
    window.showMaximized()
        
    sys.exit(app.exec())