import socket   

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.132", 8000))

while True:
    msgS = input("Inserisci un comando: ")
    s.sendall(msgS.encode())
    
s.close()  