import socket

HEADER = 256
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# ALAA's
# SERVER = "192.168.168.1"

# # GAD's
# SERVER = "192.168.1.8"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
  
def recieve():
    print(client.recv(2048).decode(FORMAT))

patient_name=input("Enter Your Name: ")
send(patient_name)
recieve()

patient_snn=input("Enter Your SSN: ")
send(patient_snn)
recieve()

consult_activate=input("Enter CONSULT to activate symptoms check: ")
send(consult_activate)
recieve()
pain=input("Your pain is:  ")
send(pain)
recieve()
# send(DISCONNECT_MESSAGE)