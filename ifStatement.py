#18/12/24
# Esercizio costrutto if (mutualmente esclusivo)

pippo = 8

if pippo >= 7:
    print("pippo vale almeno 7")
    print("ciao! mi hanno indentato bene")
elif pippo == 8:
    print("pippo vale 8")
else:
    print("pippo NON vale 6 e non è maggiore o uguale a 7")

print("ciao! sono la riga 14!!")

#logica booleana
if True:
    print("questo if vale sempre")

if False:
    print("questo if non vale sempre")

flag = False

if flag:
    print("questo if vale solo quando flag vale True")

if not flag:
    print("questo if vale solo quando flag vale False")



#verificare se il numero è un multiplo di 2 oppure un multiplo di 3
numero = int(input("inserisci un numero"))

if numero % 2 == 0:
    print(f"{numero} è un multiplo di 2")
if numero % 3 == 0:
    print(f"{numero} è un multiplo di 3")
if numero % 5 == 0:
    print(f"{numero} è un multiplo di 5")
if numero % 2 != 0 and numero % 3 != 0 and numero % 5 !=0:
    print(f"{numero} non è multiplo di 3 ne di 2")

#operatore modulo: il modulo fa la divisione per interi
#DRY --> dont' repeat yourself


#approccio 2: utilizzo dei booleani (if not = se è vero che è...)
print("""Approccio 2 - utilizzo una variabile booleana
""")
flag = False

if numero % 2 == 0:
    print(f"{numero} è un multiplo di 2")
    flag = True
if numero % 3 == 0:
    print(f"{numero} è un multiplo di 3")
    flag = True
if numero % 4 ==0:
    print(f"{numero} è un multiplo di 4")
    flag = True
if numero % 5 == 0:
    print(f"{numero} è un multiplo di 5")
    flag = True
if numero % 7 == 0:
    print(f"{numero} è un multiplo di 7")
    flag = True
if not flag:
    print(f"{numero} NON è un multiplo di 2,3,4 o 5 o 7")