# Esempio brack
print("""Esempio brack
""")
contatore = 1

while contatore <= 10:
    print("contatore vale", contatore)
    contatore = contatore + 1
    #contatore += 1 (sintassi uguale alla linea 5)
    if contatore == 4:
        print("trovato!", contatore)
        break

print("istruzione dopo il while")


# Esempio continue
print("""
Esempio continue
""")
contatore = 0

while contatore <= 9:
    contatore += 1
    if contatore == 4:
        print("questa volta passo...")
        continue
    print("contatore vale ", contatore)
    #contatore += 1 questo manda in loop il ciclo

# Esempio else
print("""
Esempio else
""")
contatore = 1
x = 3

while contatore <= 10:
    if contatore == x:

        print("trovato! ", contatore)
        break
        print("istruzione dopo il break")
    contatore += 1
else:
    print(f"Non ho trovato {x}")

print("istruzione dopo il while")


# Esempio valutazione input
print("""
Esempio validazione input: l'utente inserisce la password finché non la azzecca
""")
password = ""

while password != "laMiaPassword":
    password = input("inserisci la tua password ").strip()

print("accesso consentito")

# Esempio valutazione input
print("""
Esempio validazione input: l'utente inserisce la password sbagliata al massimo 3 volte
""")
password = ""
tentativi = 0


while password != "passwordCorretta" and tentativi < 3:
    #qui parte il tentativo di inserire la pw corretta
    #passo 1 - incrementare i tentativi
    tentativi += 1

    mexTry = f"Ti sono rimasti {4 - tentativi} tentativi "
    mexLast = "Ultimo tentativo rimasto!"

    mex = mexTry if tentativi < 3 else mexLast
    print(mex)
    password = input("inserisci la password: ").strip()
    risultato = "Accesso consentito" if password == "passwordCorretta" else "Accesso non consentito"
else:
    print("il ciclo è finito")

print("il ciclo è finito anche qui")
