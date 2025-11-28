import requests
from bs4 import BeautifulSoup
import re
import random

# Funktion til at hente ord fra URL
def få_ord(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    tekst = soup.get_text()
    ord_liste = re.findall(r"[A-Za-zÆØÅæøå]+", tekst)
    ord_liste = [w.lower() for w in ord_liste if len(w) > 3]
    return ord_liste

# Stadier i Galgeleg
stadier = [
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# Funktion til selve spillet
def spil(ord_liste):
    valgt_ord = random.choice(ord_liste)
    skjul = ["_"] * len(valgt_ord)
    gættede_bogstaver = set()
    liv = 6
    spil_igang = True

    print("\n------------- Velkommen til Hangman -------------\n")
    print("Gæt ordet: ", ' '.join(skjul))
    print(f"Liv: {liv}")
    print(valgt_ord)

    while spil_igang:
        gæt = input("Gæt et bogstav: ").lower()

        if gæt in gættede_bogstaver:
            print(f"Du har allerede gættet '{gæt}'. Prøv et andet bogstav.")
            continue

        gættede_bogstaver.add(gæt)

        if gæt not in valgt_ord:
            liv -= 1

        for index, bogstav in enumerate(valgt_ord):
            if bogstav == gæt:
                skjul[index] = gæt

        print(' '.join(skjul))
        print(f"Liv: {liv}")
        print(stadier[6 - liv])

        if "_" not in skjul:
            print("Tillykke! Du vandt!")
            spil_igang = False
        elif liv == 0:
            print("Desværre, du tabte!")
            print(f"Ordet var: {valgt_ord}")
            spil_igang = False

# Main loop
while True:
    svar = input("Vil du spille Hangman? (ja/nej): ").lower()
    if svar in ('ja', 'j'):
        url_spg = input("Vil du bruge dit eget link? (ja/nej): ").lower()
        if url_spg in ('ja', 'j'):
            while True:  # Bliv ved med at spørge, indtil linket er gyldigt
                bruger_url = input("Indtast dit link her: ")
                try:
                    ord_liste = få_ord(bruger_url)
                    break  # Gyldigt link, bryd loopet
                except Exception:
                    print("Ugyldigt link eller fejl ved hentning. Prøv igen.")
            spil(ord_liste)
        elif url_spg in ('nej', 'n'):
            ord_liste = få_ord("https://www.bt.dk/politik/live-foelg-kommunalvalget-i-2025-her?directpost=10565857")
            spil(ord_liste)
        else:
            print("Ugyldigt input. Skriv 'ja' eller 'nej'.")
    elif svar in ('nej', 'n'):
        print("Program afsluttet.")
        break
    else:
        print("Ugyldigt input. Skriv 'ja' eller 'nej'.")
