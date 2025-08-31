def program ():
    while True:
        number = input("Type your number: ")

        if number.isdigit() and int(number) > 0:
            break
        else:
            print("the wrong number mate, try again!")
    
    sum = 0
    product = 1

    for digit in number:
        digit = int(digit)
        sum += digit 
        product *= digit

    print(f"the sum of yout number is: {sum}")
    print(f"the product of your number: {product}")

program()