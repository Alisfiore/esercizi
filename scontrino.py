# 16/12/24

#Programma che visualizza uno scontrino relativo
# all'acquisto di un prodotto dati:
# nome del prodotto
# quantità desiderata
# prezzo

item = input("Che cosa vuoi comprare? ")
price = input("Quanto costa? ")
qnt = input("Quanti ne compri? ")

# metodo1 - calcolare il risultato e metterlo in una variabile
tot = round(int(qnt) * float(price), 2)
# print(type(tot))
# print(type(qnt))

print("Per comprare " + qnt + " di " + item + " devi pagare " + str(tot) + " €")

# metodo2 - faccio l'operazione direttamente all'interno della stringa stessa con le f-strings
print(f"Per comprare {qnt} di {item} devi pagare {round(int(qnt) * float(price), 2)}€ ")

# metodo 3-fare le conversioni direttamente alla radice
# per comodità riprendo gli imput e li modifico
item1 = input("Che cosa vuoi comprare? ")
price1 = float(input("Quanto costa? "))
qnt1 = int(input("Quanti ne compri? "))
print(f"Per comprare {qnt} di {item} devi pagare {round(qnt1 * price1, 2)}€")
