#esercizio fatto da sabrina in modalità 1 (semplice)
import random
# voglio fare in modo che il gioco continua finché il giocatore vuole giocare
risposta = "Y"
pntUsr = 0
pntCpu = 0
while risposta == "Y":
    #cpu sceglie la mossa
    cpu = random.randint(1, 3)
    #sfrutto la tipizzazione dinamica di python
    if cpu == 1:
        cpu = "sasso"
    else:
        cpu = "carta" if cpu == 2 else "forbici"
    #DEBUG
    print(F"La cpu ha scelto {cpu}")
    #chiedo la mossa all'utente SENZA validazione
    usr = int(input("""Fai la tua mossa
    1 --> sasso
    2 --> carta
    3 --> forbice""").strip())
    if usr == 1:
        usr = "sasso"
    elif usr == 2:
        usr = "carta"
    else:
        usr = "forbice"
    print(f"L'utente ha scelto {usr}")

#il programma incomincia qui
    if cpu == usr:
        print("Pareggio!")
        pntUsr += 1
        pntCpu += 1
    else:
        #quando non c'è pareggio bisogna verificare chi ha vinto
        if cpu == "sasso":
            # l'utente ha scelto carta oppure forbici
            if usr == "forbice":
                print(f"{cpu} batte {usr}. Hai perso")
                pntCpu += 1
            else:
                print(f"{usr} batte {cpu}. Hai vinto!")
                pntUsr += 1
        elif cpu == "carta":
            # l'utente ha scelto sasso o forbice
            if usr == "sasso":
                print(f"{cpu} batte {usr}. Hai perso")
                pntCpu += 1
            else:
                print(f"{usr} batte {cpu}. Hai vinto!")
                pntUsr += 1
        else:
            # l'utente ha scelto sasso oppure carta
            if usr == "carta":
                print(f"{cpu} batte {usr}. Hai perso")
                pntCpu += 1
            else:
                print(f"{usr} batte {cpu}. Hai vinto!")
                pntUsr += 1

    risposta = input("Premi Y per giocare ancora").strip().upper()
else:
    print("Hai scelto di smettere di giocare")
    print(f" pnt cpu ={pntCpu}")
    print(f"pnt utente = {pntUsr}")
    if pntCpu > pntUsr:
        print("HAI PERSO!!!")
    elif pntCpu == pntUsr:
        print("Pareggio, rigiochiamo?")
    else:
        print("Mi hai battuto")
