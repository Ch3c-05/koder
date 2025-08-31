while True:
    import math


    figur = input("Figur?: ").strip().lower()


    if figur == "cirkel":
        radius = float(input("Indtæst cirklens radius: "))
        areal = math.pi * radius ** 2
        print(f"Arealet med radius: {radius}, det er: {areal} ")
    elif figur == "firkant":
        længden = float(input("Indtæst længden: "))
        bredden = float(input("Indtæst bredden: "))
        areal = længden * bredden
        print(f"Arealet med: {længden} og {bredden}, det er: {areal} ")