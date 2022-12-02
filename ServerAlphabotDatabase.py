#SERVER ALPHABOT
import socket
import alphabot
import time
import sqlite3

#dichiarazione e inizializzazione del socket TCP che fa da server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#inizializzazione Alphabot
bot = alphabot.AlphaBot()
#dizionario utile all'associazione messaggioInviato-comandoDaEseguire
comandi = {"w":bot.forward, "a":bot.left, "d":bot.right, "s":bot.backward, "q":bot.stop}
s.bind(("0.0.0.0", 8000))
s.listen()
print("In attesa di connessione...")
connection, address = s.accept()

ls = []
while True:
    #ricezione del messaggio del client e decodifica
    msgR = connection.recv(4096)
    msgR = msgR.decode()
    #msgR = input("scrivi: ")

    #se il messaggio è di un solo carattere significa che l'operazione da eseguire va preso dal db e corrisponde ad una sequenza di comandi con i relativi tempi
    #se il messaggio ha lunghezza diversa da 1, è un'operazione "standard" e dovrà quindi eseguire un solo comando per il tempo determinato
    #(Esempio msg: "w 3")
    if(len(msgR) != 1):
        ls = msgR.split(" ")
        #print(comandi[ls[0]])
        #print(float(ls[1]))

        #esecuzione del singolo domando per il tempo passato come secondo parametro
        comandi[ls[0]]()
        time.sleep(float(ls[1]))
        bot.stop()
    else:
        id = msgR
        con = sqlite3.connect("./Alphabot.db")  #connessione al db utile all'acquisizione dei dati
        cur = con.cursor()
        #print(f"SELECT Movimento FROM ALPHABOT WHERE ID = {id}")        
        res = cur.execute(f"SELECT Movimento FROM ALPHABOT WHERE ID = {id}" )       #query utile all'acquisizione della riga del db corretta in base al messaggio inviato
        
        move = res.fetchall()
        move = move[0][0]

        #esecuzione della serie di comandi acquisiti dal db con i relativi tempi
        lista = move.split(";")
        for comando in lista:
            msg = comando.split("|")
            #print(comandi[msg[0]])
            #print(float(msg[1]))
            comandi[msg[0]]()
            time.sleep(float(msg[1]))
            bot.stop()

"""Nel database per creare la sequenza di comandi da eseguire e per assegnare i valori di tempo adatti, abbiamo dovuto compiere numerose
prove sul percorso cercando di avvicinarci nel modo più preciso possibile all'obiettivo"""
