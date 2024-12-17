# Titolo del Mad Libs
print("""Questo è un esempio del gioco Mad Libs fatto da Sabrina!
Creo una storia divertente.""")

# Chiedi input all'utente
nome = input("Inserisci un nome: ")
print(nome.capitalize())
cosa = input("inserisci una cosa: ")
luogo = input("Inserisci un luogo: ")
print(luogo.capitalize())
persona = input("Inserisci un nome di persona famosa: ").capitalize()
famosa = input("Inserisci un cognome persona famosa: ").capitalize()
imprecazione = input("inserisci un'imprecazione ").upper()
cibo = input("Inserisci un cibo: ")
posto = input("Inserisci un posto dove sederti: ")
verbo = input("Inserisci un verbo al passato remoto: ")
nome1 = input("Inserisci il nome di un personaggio di cartoni").capitalize()
nome2 = input ("inserisci il nome di un personaggio di serie tv").capitalize()
nome3 = input ("inserisci il nome di un cattivo dei cartoni").capitalize()

#metodo di scrittura sarebbe scrivere la storia con gli imput
#storia/storia/storia "{nome.upper()}" o {nome.lower()}

# Costruisci la storia
storia = f"""Incamminandosi verso il bar, {nome} decise di andare a comprare una {cosa}. 
Ma si perse in {luogo} dove conobbe {persona} {famosa}che si era perso.
' {imprecazione} ' urli tu, 'vieni insieme a me a mangiare un pò di {cibo}'.
Entrarono in un ristorante e si sedettero su un {posto}. Lì, mangiarono il {cibo} e {verbo}. 
Incontrarono vari personaggi famosi, tra cui {nome1}, {nome2} e {nome3} che {verbo} insieme ai proprietari di {luogo}
E vissero tutti felici e contenti.
"""
# Stampa la storia completa
print("\nEcco la tua storia:")
print(storia)