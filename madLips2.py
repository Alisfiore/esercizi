'''# temp è una variabile di appoggio che uso per la fase di inserimento dei dati
temp = input("Inserisci un nome di persona: ")
print(f"temp ora vale {temp}")
temp = temp.strip()
print(f"temp ora vale {temp}")
nome = temp.capitalize()
print(f"nome ora vale {nome}")

temp = input("Inserisci il nome di una città: ")
print(f"temp ora vale {temp}")
temp = temp.strip()
print(f"temp ora vale {temp}")
luogo = temp.capitalize()
print(f"luogo ora vale {luogo}")

temp = input("Inserisci il nome di un oggetto comune: ")
print(f"temp ora vale {temp}")
temp = temp.strip()
print(f"temp ora vale {temp}")
oggetto = temp.lower()
print(f"oggetto ora vale {oggetto}")

verbo = input("inserisci un verbo all'infinito: ").strip().lower().capitalize()
print(verbo)

nome = input("Inserisci un nome di persona: ").capitalize()
luogo = input("Inserisci il nome di una città: ")
oggetto = input("Inserisci il nome di un oggetto comune: ").lower()

print("\n\nEcco la tua storia:")
print(f""" 
Un giorno {nome} andò a {luogo}.
Altra frase con {nome.lower()} scritto minuscolo
{nome} cominciò a chiamarsi da solo urlando "{nome.upper()}".
{oggetto.capitalize()}
""")'''


temp = input("Inserisci un nome di persona: ").strip() or "ciao"

print(temp)