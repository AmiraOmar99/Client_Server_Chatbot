import socket 
import threading

HEADER = 256
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
CONSULT_ACTIVATE= "CONSULT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # symptoms=[]
        # count_common=0
        # count_less=0
        # count_severe=0
        count=0
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            # if "Name" in msg:
            #     conn.send("Hello".encode(FORMAT))
            # if "ssn" in msg:
            #     conn.send("ok".encode(FORMAT))
            # if "ID" in msg:
            #     conn.send("ok".encode(FORMAT))
            # if "age" in msg:
            #     conn.send("ok".encode(FORMAT))
            # if "pain" in msg:
            #     conn.send("oh".encode(FORMAT))
            
            if ((count ==0)&(msg !=CONSULT_ACTIVATE)):
                conn.send("Message recieved".encode(FORMAT))
            

            if((count==0) &(msg == CONSULT_ACTIVATE )):  
                # count_common=count_common+1    
                # print(count_common)
                conn.send("Choose all that apply: [cough, fever, headache , fatigue , Diarrhoea , chest pain, loss of taste or smell , sore throat , rash]".encode(FORMAT))
            print(f"[{addr}] {msg}")
            # conn.send("Msg received".encode(FORMAT))
       
               
        
            
            
            # for symptom in symptoms:
            #     if (symptom=="cough" or symptom=="headache" or symptom=="fatigue"):
            #         count_common= count_common+1
            #     if (symptom=="fever" or symptom=="Diarrhoea" or symptom=="sore throat"):
            #         count_less= count_less+1
            #     if (symptom=="chest pain" or symptom=="loss of taste or smell" or symptom=="rash"):
            #         count_severe= count_severe+1
            # if (count_severe>0):
            #     conn.send("SEE A DOCTOR IMMEDIATELY !!!! ".encode(FORMAT))
            # elif (count_less>count_common):
            #     conn.send("Isolate at Home".encode(FORMAT))
            # else:
            #     conn.send("Rest at Home".encode(FORMAT))
            
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