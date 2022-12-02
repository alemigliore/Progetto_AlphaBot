#CLIENT
import socket   

#dichiarazione e inizializzazione del socket TCP che fa da client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.132", 8000))      #connessione al server dell'Alphabot

while True:
    #invio del comando al server
    msgS = input("Inserisci un comando: ")      
    s.sendall(msgS.encode())
    
s.close()  