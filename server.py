import socket 
import threading

HEADER = 256
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
CONSULT_ACTIVATE= "CONSULT"
IDLE_MESSAGE = 'IDLE'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            
            conn.settimeout(20.0)
            count=0
            msg_length = conn.recv(HEADER).decode(FORMAT)
            conn.settimeout(None)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                
                if ((count ==0)&(msg !=CONSULT_ACTIVATE)):
                    conn.send("Message recieved".encode(FORMAT))
                

                if((count==0) &(msg == CONSULT_ACTIVATE )):  
                   
                    conn.send("Choose all that apply: [cough, fever, headache , fatigue , Diarrhoea , chest pain, loss of taste or smell , sore throat , rash]".encode(FORMAT))
                print(f"[{addr}] {msg}")
        except socket.timeout as e:
            print("Timeout")
            print(f"[DISCONNECTED] {addr} has disconnected")
            # connected=False
            
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