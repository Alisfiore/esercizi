# 17/12/24
# Esercizi su metodi e funzioni delle stringhe

# S A B R I N A
# 0 1 2 3 4 5 6

nome = input("Come ti chiami? ")
pippo = input("scrivi qualcosa ")

#caratteresi escape -\
print("le doppie virgolette che delimitano le stringhe hanno una funzione sintattica")
print('le doppie virgolette possono essere sostituite dai singoli apici')
print("l'albero fa le mele")
#metodo furbo
print("Manzoni ha scritto i 'Promessi Sposi'")
#metodo serio
print("Manzoni ha scritto i \"promessi sposi\" sotto l'albero di mele")

#stampa numero di caratteri
print(len(nome))
#prima occorrenza di una substring
print(nome.find("a"))
#quando non è presente la stampa -1
print(nome.find("ar"))
#prima occorrenza di un singolo carattere
print(nome.find("n"))
#ultima occorrenza di un singolo carattere
print(nome.rfind("a"))
#ultima occorrenza di una substring
print(nome.rfind("na"))
#trasforma in MAIUSCOLO
print(nome.upper())
print(pippo.upper())
#trasforma in minuscolo
print(nome.lower())
print(pippo.lower())
#trasforma l'iniziale in maiuscolo
print(nome.capitalize())
print(nome.capitalize() + " " + pippo.capitalize())
#controlla che sono solo caratteri alfabetici (mi aspetto un True o False)
print(nome.isalpha())
#controlla se sono tutti numeri
print(pippo.isdigit())
#controlla se la stringa inizia con un carattere o una serie di caratteri
print(nome.startswith("S"))
#controlla se la stringa finisce con .....
print(nome.endswith("na"))
#conta il n di occorrenze di una substring
print(nome.count("a"))
#conta il numero di spazi nella stringa
print(pippo.count(" "))
#sostituisce una substring con un'altra
print(nome.replace("a", "o"))
print(pippo.replace(" ", ""))
print(pippo.replace('"', "'"))
print(pippo.replace("\"", "'"))
#toglie gli spazi all'inizio e dalla fine
print(nome)
print(nome.strip())
#rimuovouna substring dall'inizio e dalla fine della stringa
print(nome)
print(nome.strip("a"))

#manuale delle istruzioni che spunta direttamente su terminale
print(help(str))
