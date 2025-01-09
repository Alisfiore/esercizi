'''#parola = "testo a caso"
for pippo in parola:
    print(pippo)

for numero in reversed(range(31, 0, -7)):
    print(f"{numero} dicembre")

for n in range(11):
    if n == 5:
        print("interrompo in corrispondenza del numero", 5)
        break
        #print("istruzione non eseguibile")
    print(n)
else:
    print("il ciclo for è finito")

#Esercizio tabellina

numero = int(input("Quale tabellina vuoi vedere? ").strip())

for fattore in range (1, 11):
    print(f"{numero} x {fattore} = {numero * fattore}")'''


for primo in range(2, 10):
    print(f"stampo la tabellina del {primo}")
    for secondo in range(1, 11):
        print(f"{primo} x {secondo} = {primo * secondo}")
    else:
        print("------------")
