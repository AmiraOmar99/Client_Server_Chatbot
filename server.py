import socket 
import threading
import time
import cryptography
from cryptography import fernet
from cryptography.fernet import Fernet

key = b'h_31cC-cjISYrMX7FABt_GEXpKRAXerreSXay8LesC0='
fernet =Fernet(key)

HEADER = 256
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
Pain="pain"
CONSULT_ACTIVATE= "CONSULT"
comm=["cough", "fatigue", "headache"]
less_list=["fever", "diarrhea", "throat"]
sev=["chest", "taste", "rash"]
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            common_symp=0
            less_symp=0
            sever_symp=0
            
            conn.settimeout(50.0)
            count=0
            var=0
            msg_length = conn.recv(HEADER).decode(FORMAT)
            conn.settimeout(None)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length)
                msg= fernet.decrypt(msg).decode()
                print("Message",msg)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                
                if ((count ==0)&(msg !=CONSULT_ACTIVATE)&((Pain not in msg))):
                    conn.send("Message recieved".encode(FORMAT))
                

                if((count==0) &(msg == CONSULT_ACTIVATE )&(msg !=Pain)):  
                   
                    conn.send("Choose all that apply: [cough, fever, headache , fatigue , Diarrhoea , chest pain, loss of taste or smell , sore throat , rash]".encode(FORMAT))
                if((count==0) &(msg != CONSULT_ACTIVATE )&(Pain in msg)):
                    
                    if ("sever" in msg):
                        conn.send("SEE A DOCTOR IMMEDIATELY !!!! ".encode(FORMAT))
                        
                    elif ("less" in msg):
                        conn.send("Isolate at Home ".encode(FORMAT))
                    elif("comm" in msg):
                        conn.send("Rest at Home ".encode(FORMAT))
                            
                
                print(f"[{addr}] {msg}")
        except socket.timeout as e:
            print("Timeout")
            print(f"[DISCONNECTED] {addr} has disconnected")
            conn.send("Timeout".encode(FORMAT))
            time.sleep(50)
            connected=False
            
    conn.close()

        
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()