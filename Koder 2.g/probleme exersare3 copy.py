def program ():
    
    while True:
        number = input("Insert yout number: ")

        if number.isdigit and int(number) > 0:
            break
        else:
            print("Please insert a valid number!")

    digits = [int(digit) for digit in number]
    max_cifra = max(digits)
    min_cifra = min(digits) 
    difference = max_cifra - min_cifra

    print(f"Your number: {number}")
    print(f"The biggest digit of your number: {max_cifra}")
    print(f"The smallest digit of your number: {min_cifra}")
    print(f"The difference between these two digits: {difference}")

program()

    

