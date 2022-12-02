import socket
import alphabot
import time
import sqlite3

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot = alphabot.AlphaBot()
comandi = {"w":bot.forward, "a":bot.left, "d":bot.right, "s":bot.backward, "q":bot.stop}
s.bind(("0.0.0.0", 8000))
s.listen()
print("In attesa di connessione...")
connection, address = s.accept()

#comandi = {"w":"bot.forward", "a":"bot.left", "d":"bot.right", "s":"bot.backward", "q":"bot.stop"}

ls = []
while True:
    msgR = connection.recv(4096)
    msgR = msgR.decode()
    #msgR = input("scrivi: ")

    if(len(msgR) != 1):
        ls = msgR.split(" ")
        #print(comandi[ls[0]])
        #print(float(ls[1]))
        comandi[ls[0]]()
        time.sleep(float(ls[1]))
        bot.stop()
    else:
        id = msgR
        con = sqlite3.connect("./Alphabot.db")
        cur = con.cursor()
        print(f"SELECT Movimento FROM ALPHABOT WHERE ID = {id}")
        res = cur.execute(f"SELECT Movimento FROM ALPHABOT WHERE ID = {id}" )
        
        move = res.fetchall()
        move = move[0][0]

        lista = move.split(";")
        for comando in lista:
            msg = comando.split("|")
            #print(comandi[msg[0]])
            #print(float(msg[1]))
            comandi[msg[0]]()
            time.sleep(float(msg[1]))
            bot.stop()
