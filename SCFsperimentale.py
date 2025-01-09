import random
# voglio fare in modo che il gioco continua finché il giocatore vuole giocare
risposta = "Y"
pntUsr = 0
pntCpu = 0
while risposta == "Y":
    #cpu sceglie la mossa
    cpu = random.randint(1, 3)
    # DEBUG
    print(F"La cpu ha scelto {cpu}")
    # chiedo la mossa all'utente SENZA validazione
    usr = int(input("""Fai la tua mossa
        1 --> sasso
        2 --> carta
        3 --> forbice""").strip())
    print(f"L'utente ha scelto {usr} ")

    #voglio fare in modo che quando cpu > usr vince la cpu e viceversa
    if cpu == usr:
        print("Pareggio!")
        pntUsr += 1
        pntCpu += 1
    else:
        # se la cpu sceglie carta l'algoritmo funziona
        #se la cpu sceglie sasso
        if cpu == 1 and usr == 3:
            usr = 0
        #se la cpu sceglie forbice e l'utente sceglie sasso...
        elif cpu == 3 and usr == 1:
            usr = 4
        else:
            print("Nessuna conversione da fare")

        if cpu > usr:
            print(f"{cpu} batte {usr}! Hai perso")
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