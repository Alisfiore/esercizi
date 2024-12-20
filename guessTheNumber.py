

#codice sbagliato correggere
#CODICE FATTO CON SABRINA AIUTO SONO STPT

import random
numero_segreto = random.randint(1,100)
tentativiRimasti = 5

#DEBUG
print(numero_segreto)

while tentativiRimasti > 0:
    print(f"Hai ancora {tentativiRimasti} tentativi")
    # validazione dell'input: gestisco inserimento "pizza"
    scommessa = ""
    while not scommessa.isdigit():
        print("Devi inserire un numero!")
        scommessa = (input("quale numero scegli? ").strip())
    else:
        scommessa = int(scommessa)

    tentativiRimasti -= 1




    if scommessa == numero_segreto:
        print("Hai vinto!")
        break

    else:
        print("Che peccato! Hai sbagliato.")
        if scommessa > numero_segreto and tentativiRimasti != 0:
            print("Prova con un numero più basso... ")
        elif scommessa < numero_segreto and tentativiRimasti != 0:
            print("Prova con un numero più alto... ")
        else:
            print("Hai perso miseramente")


else:
    print(f"il numero da indovinare era {numero_segreto}")

