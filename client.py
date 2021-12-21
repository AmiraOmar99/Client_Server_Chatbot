import socket
import mysql.connector as mysql 
import threading
from PyQt5 import QtWidgets, QtGui, QtCore
from mainwindow import Ui_MainWindow 



connected=True


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

mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="mysql",
  database="myserver"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
y = True
for x in mycursor:
    if x == ('patients',):
        y = False
if y:
    mycursor.execute("CREATE TABLE patients (PatientFirstName VARCHAR(50),PatientLastName VARCHAR(50),PatientSSN VARCHAR(50),PatientAge VARCHAR(50),ChronicDisease VARCHAR(50),PatientGender VARCHAR(50))")


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        self.setWindowTitle("DocBot")

        self.HEADER = 256
        self.PORT = 5050
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self. connected=True


        self.SERVER = socket.gethostbyname(socket.gethostname())

        self.ADDR = (self.SERVER, self.PORT)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

        self.idle_status= False




        self.ui.add.clicked.connect(lambda:self.get_data())
        self.ui.consult.clicked.connect(lambda:self.symptoms())
        self.ui.new.clicked.connect(lambda:self.new_pat())

        self.timer = QtCore.QTimer(self)

        # * adding action to timer
        self.timer.timeout.connect(self.check_timeout)

        # * update the timer every tenth second
        self.timer.start(100)

        # # * execute client handling in a new thread
        # self.thread = threading.Thread(target=self.idle_connection)
        # self.thread.start()


    def send(self,msg):

        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(self.FORMAT))



    def get_data(self):

        first_name = self.ui.fst_name_box.text()
        self.send(first_name)
        last_name = self.ui.lst_name_box.text()
        self.send(last_name)
        ssn = self.ui.ssn_box.text()
        self.send(ssn)
        age = self.ui.age_box.text()
        self.send(age)
        chronic = self.ui.chronic_box.text()
        self.send(chronic)
        gender = self.ui.gender_combo.currentText()
        self.send(gender)
        sql = "INSERT INTO patients (PatientFirstName,PatientLastName,PatientSSN,PatientAge,ChronicDisease,PatientGender) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (first_name, last_name,ssn, age, chronic,gender)
        mycursor.execute(sql,val)
        mydb.commit()
        print(first_name, last_name,ssn, age, chronic,gender)
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

    def symptoms(self):
        common_symp=0
        less_symp=0
        sever_symp=0
        self.ui.consult.hide()

        for i in range(len(self.ui.comm)):
            if (self.ui.comm[i].isChecked()) :
                common_symp+=1
            
        for i in range(len(self.ui.less_list)):
            if (self.ui.less_list[i].isChecked()) :
                less_symp+=1
             


        for i in range(len(self.ui.sev)):
            if (self.ui.sev[i].isChecked()):
                sever_symp+=1

        if (sever_symp>0):
            self.ui.analysis.setText("SEE A DOCTOR IMMEDIATELY !!!! ")
        elif (less_symp>common_symp):
            self.ui.analysis.setText("Isolate at Home")
        else:
            self.ui.analysis.setText("Rest at Home")

        self.ui.new.show()


    def new_pat(self):

        for symp in self.ui.comm:
            symp.setChecked(False)
            
        for symp in self.ui.less_list:
            symp.setChecked(False)

        for symp in self.ui.sev:
            symp.setChecked(False)

        self.ui.new.hide()
        self.ui.widget.hide()
        
        for item in self.ui.data:
            item.hide()

        self.ui.first_msg.setText('In order to have your data in our database, Kindly fill these informations correctly and carefully')
        for item in self.ui.data:
            item.show()
        self.ui.add.show()
        # self.ui.widget.show()
        self.ui.consult.show()
        self.ui.new.hide()

    def idle_connection(self):
        global connected
        while connected:
            try:
                try:
                    self.status_length = int(self.client.recv(self.HEADER).decode(self.FORMAT)) # * recieve of the length (header) of the status message
                except ValueError:
                    print(
                        "[FINISHED] Connection ended due to achieving required result ...")
                    # connected = False 
                    self.idle_status = True       
                # * recieve the status message itself from the server
                self.status = self.client.recv(self.status_length).decode(self.FORMAT)
                print(self.status)
                # ? If the status message is self.DISCONNECT_MESSAGE, disconnect the client as IDLE
                if self.status == self.DISCONNECT_MESSAGE:
                    self.idle_status = True
                    connected = False
                
            # ? If the server was forcedly closed
            except ConnectionAbortedError:
                print("[EXITING] The GUI was closed ... ")
        self.client.close()
        print("[EXITING] Exiting recieving thread .. ")
        sys.exit()


    def check_timeout(self):
        """
            check_timeout: keeps checking if the server is idle or not
        """
        # monitor = IdleMonitor.get_monitor()
        # timee=monitor.get_idle_time()
        # if timee>20.0:
        #     idle_status = True

        if self.idle_status or (connected == False):
            QtWidgets.QMessageBox.warning(
                self, "Connection Lost", "[IDLE] Connection was closed please open the UI again")
            sys.exit()  

    def closeEvent(self, event):

        quit_msg = "Are you sure you want to exit the program?"
        reply = QtWidgets.QMessageBox.question(self, 'Message', quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            if self.client :
                self.client.close()
            event.accept()
        else:
            event.ignore()
            global connected
            print("[EXITING] ... ")
            connected = False
            if connected:
                finished_message = f"{len(self.DISCONNECT_MESSAGE):<{self.HEADER}}" + \
                    self.DISCONNECT_MESSAGE
                self.client.send(finished_message.encode(self.FORMAT))
            self.client.close()
            time.sleep(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())
