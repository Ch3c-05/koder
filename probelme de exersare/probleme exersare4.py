def functie():
    while True:
        number = input("Enter your number please: ")

        if number.isdigit() and int(number) > 0:
            break
        else:
            ("Error, please try agaian!")
    
    suma_maxima = 0
    pereche = ()

    for i in range(len(number) - 1):
        digit1 = int(number[i])
        digit2 = int(number[i + 1])
        sum = digit1 + digit2
    
        if sum > suma_maxima:
            suma_maxima = sum
            pereche = (digit1, digit2)

    print(f"Perechea de cifre consecutive cu suma maxima este: {pereche[0]}, {pereche[1]}")
    print(f"Suma lor: {suma_maxima}")


functie()