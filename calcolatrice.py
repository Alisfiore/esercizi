"""# struttura -> quale operazione vuoi fare?
operazione = input('''Quale operazione vuoi fare?
 s: somma
 d: differenza
 p: prodotto
 r: rapporto
 ''')


#input -> primo numero
op1 = float(input("inserisci il primo numero: "))
op2 = float(input("inserisci il secondo numero: "))

if operazione == "s":
    risultato = op1 + op2
elif operazione == "s":
    risultato = op1 - op2
elif operazione == "p":
    risultato = op1 * op2
elif operazione == "r":
    if op2 == 0:
        risultato = "errore, non si può dividere per zero"
    else:
        risultato = op1 / op2

else: risultato = ("operazione non supportata").capitalize()
#risultato
print(f"ecco il tuo risultato {risultato}".capitalize())"""

#CALCOLATRICE FATTA DA SABRINA

#gestire operazione non consentita
#gestire numeri non validi
#gestire spazi e lower
#imput -> quale operazione fare

operatore = input("""
Scegli un'operazione da svolgere
1 + somma
2 - differenza
3 * moltiplicazione
4 / divisione
""").strip().lower()

#controllo la validità dell'operatore
if (operatore == "1"
        or operatore == "+"
        or operatore == "somma"
        or operatore == "addizione"):
    print("Hai scelto la somma")
    a = input("Inserisci il primo addendo").strip()
    #controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("devi inserire un numero!")
    else:
        print(f"hai inserito il numero {a}")
        a = float(a)
        b =input("Inserisci secondo addendo").strip()
        if b.isalpha():
            print("devi inserire un numero!")
        else:
            b = float(b)
        #eseguo la somma
            risultato = a + b
            print(f"il tuo risultato è {risultato}")

elif (operatore == "2"
      or operatore == "-"
      or operatore == "differenza"
      or operatore == "sottrazione"):
    print("Hai scelto la sottrazione")
    a = input("Inserisci il valore del sottraendo").strip()
# controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("devi inserire un numero!")
    else:
        print(f"hai inserito il numero {a}")
    a = float(a)
    b = input("Inserisci secondo sottraendo").strip()
    if b.isalpha():
            print("devi inserire un numero!")
    else:
        b = float(b)
        # eseguo la meno
        risultato = a - b
        print(f"il tuo risultato è {risultato}")



elif (operatore == "3"
      or operatore == "*"
      or operatore == "x"
      or operatore == "prodotto"
      or operatore == "moltiplicazione"):
    print("Hai scelto la moltiplicazione")
    a = input("Inserisci il primo moltiplicatore").strip()
    # controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("devi inserire un numero!")
    else:
        print(f"hai inserito il numero {a}")
        a = float(a)
        b = input("Inserisci secondo moltiplicatore").strip()
        if b.isalpha():
            print("devi inserire un numero!")
        else:
            b = float(b)
    # eseguo la moltiplicazione
    risultato = a * b
    print(f"il tuo risultato è {risultato}")

elif (operatore == "4"
      or operatore == "/"
      or operatore == ":"
      or operatore == "rapporto"
      or operatore == "divisione"):
    print("Hai scelto la divisione")
    a = input("Inserisci il dividendo").strip()
# controllo se il valore inserito è alfabetico
    if a.isalpha():
        print("devi inserire un numero!")
    else:
        print(f"hai inserito il numero {a}")
    a = float(a)
    b = input("Inserisci divisore").strip()
    if b.isalpha():
        print("devi inserire un numero!")
    else:
        b = float(b)
    # eseguo la diviso
    risultato = a / b
    print(f"il tuo risultato è {risultato}")

else:
    print("---operazione non valida---")

#input -> primo numero
#input -> secondo numero

#controllo l'operazione scelta