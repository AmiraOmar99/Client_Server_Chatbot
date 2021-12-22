## IMPORTING ALL THE REQUIERED MODULES ##
import sys
import socket
import mysql.connector as mysql 
import threading
from PyQt5 import QtWidgets, QtGui, QtCore
from mainwindow import Ui_MainWindow 
from PyQt5.QtWidgets import QMessageBox

import cryptography
from cryptography import fernet
from cryptography.fernet import Fernet
import schedule
import time

key = b'h_31cC-cjISYrMX7FABt_GEXpKRAXerreSXay8LesC0='
fernet =Fernet(key)


mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="mysql"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

y = True
for x in mycursor:
    print(x)
    if x == ('myserver',):
        y = False

if y:
    mycursor.execute("CREATE DATABASE myserver")


## INITIALIZING THE CONNECTION PARAMETERS ##
HEADER = 256
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

## Sendinig messages function from client to server
def send(msg):
    message= fernet.encrypt(msg.encode())
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    if message == 'check':
        pass
    else:
        print("Message",message)
    

## Recieve messages function for client ##
def recieve():
    x=client.recv(HEADER).decode(FORMAT) #Recieve the header of the message
    print(x) #print the message (for teminal)
    return x #return the message



class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        self.setWindowTitle("DocBot")

        ## CONNECTING BUTTONS SOGNALS AND SLOTS ##
        self.ui.add.clicked.connect(lambda:self.get_data())
        self.ui.consult.clicked.connect(lambda:self.symptoms())
        self.ui.new.clicked.connect(lambda:self.new_pat())



    ## FUNCTIONS THAT READS THE DATA ENTERED BY THE PATIENT 
    ## FROM THE TEXT BOXES , SENDS THESE DATA TO THE SERVER
    ## AND INSERT THEM TO THE DATABASE ##
    def get_data(self):
        first_name = self.ui.fst_name_box.text()
        send(first_name)
        self.check_timeout(x=recieve())
        last_name = self.ui.lst_name_box.text()
        send(last_name)
        self.check_timeout(x=recieve())
        ssn = self.ui.ssn_box.text()
        send(ssn)
        self.check_timeout(x=recieve())
        age = self.ui.age_box.text()
        send(age)
        self.check_timeout(x=recieve())
        chronic = self.ui.chronic_box.text()
        send(chronic)
        self.check_timeout(x=recieve())
        gender = self.ui.gender_combo.currentText()
        send(gender)
        self.check_timeout(x=recieve())
        sql = "INSERT INTO patients (PatientFirstName,PatientLastName,PatientSSN,PatientAge,ChronicDisease,PatientGender) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (first_name, last_name,ssn, age, chronic,gender)
        mycursor.execute(sql,val)
        mydb.commit()
        
        for item in self.ui.data:
            item.hide()
        self.ui.add.hide()
        self.ui.widget.show()
        self.ui.consult.show()
        if gender =='Female':
            label= 'Ms.'
        else:
            label= 'Mr.'
        self.ui.first_msg.setText('Now {} {}, Please check all the symptoms you feel'.format(label, first_name))
        for i in range(int(len(self.ui.data)/2)):
            self.ui.data[2*i+1].clear()  


    ## FUNCTIONS THAT READS THE SYMPTOMS CHECKED BY THE PATIENT 
    ## , SENDS THESE DATA TO THE SERVER AND INSERT THEM TO THE DATABASE ##
    def symptoms(self):
        common_symp=0
        less_symp=0
        sever_symp=0
        self.ui.consult.hide()

        # checks the number of checked data from the common symptoms part
        for i in range(len(self.ui.comm)):
            if (self.ui.comm[i].isChecked()) :
                common_symp+=1
            
        # checks the number of checked data from the less common symptoms part            
        for i in range(len(self.ui.less_list)):
            if (self.ui.less_list[i].isChecked()) :
                less_symp+=1
             

        # checks the number of checked data from the severe symptoms part
        for i in range(len(self.ui.sev)):
            if (self.ui.sev[i].isChecked()):
                sever_symp+=1

        #checks the number of the symptoms in each section and sends 
        # the decision to the server to recieve the appropiate analysis
        if (sever_symp>0):
            send("pain is sever")
            x= recieve() #recieve the message and save it in x
            self.check_timeout(x) #checks that connection is still going
            self.ui.analysis.setText(x) #write the analysis recieved from the server
                        
            
        elif (less_symp>common_symp):
            send("pain is less")
            x=recieve() #recieve the message and save it in x
            self.check_timeout(x) #checks that connection is still going
            self.ui.analysis.setText(x) #write the analysis recieved from the server

        else:
            send("pain is comm")
            x=recieve() #recieve the message and save it in x
            self.check_timeout(x) #checks that connection is still going
            self.ui.analysis.setText(x) #write the analysis recieved from the server
      

    #Function to check the time of connection
    def check_timeout(self,x):
        if x=="Timeout": #if the message is
            msg=QMessageBox(self) # create an instance of it
            msg.setIcon(QMessageBox.Information) # set icon
            msg.setText("TimeOUT") # set text
            msg.setWindowTitle("Warning") # set title
            return_value =msg.exec_() # get the return value
            sys.exit()

    # A FUNCTION TO CLOSE THE CONNECTION AT CLOSING THE GUI
    def closeEvent(self, event):
        global client
        #asks the user if he sure wants to close the gui window
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtWidgets.QMessageBox.question(self, 'Message', quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        #if yes, close both the ui and the connection
        if reply == QtWidgets.QMessageBox.Yes:
            print("[EXITING] ... ")
            send("!DISCONNECT")
            client.close()
            event.accept()
        #if no, ignore the closing event
        else:
            event.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
