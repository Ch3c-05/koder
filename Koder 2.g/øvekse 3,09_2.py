def billetkøb(navn, alder, klubgæst = False, studerende = False):
    result = 0

    if (alder) < 18:
        result = 0
    elif (klubgæst):
        result += 120
    elif (studerende):
        result += 125





antal_personer = input("Hvor mange personer er i?: ")

for i in range(0, antal_personer):
    navn = input(f"Hvad hedder personen {i+1}?: ")
    alder = input(f"Hvor gammel er {navn}?: ")
    klubgæst = False
    studerende = False

    if alder >= 18:
        klubgæst = input(f"Er {navn} klubgæst?: ").lower().strip() == "ja"
        if klubgæst == False :
            studerende = input(f"Er {navn} studerende?: ").lower().strip() == "ja"
    pris = billetkøb(navn, alder, klubgæst, studerende)
    print(f"Billeten til {navn} koster {pris}")
    samlet += pris