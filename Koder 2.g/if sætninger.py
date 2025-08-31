secret = 12245
x = input("Gæt det hemmelige tal: ")
x = int(x)
if x == secret:
    print("Tilykke skat!")
else:
    print("Forkert! Du dør i 5 sekunder")