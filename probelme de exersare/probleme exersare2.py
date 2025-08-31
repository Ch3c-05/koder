def program ():
    while True:
        number = input("Type your number: ")

        if number.isdigit() and int(number) > 0:
            break
        else:
            print("the wrong number mate, try again!")
    
    number_digit_even = 0
    number_digit_odd = 0
    sum_digit_even = 0
    sum_digit_odd = 0
    digit_even = []
    digit_odd = []

    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            number_digit_even += 1
            sum_digit_even += digit
            digit_even.append(digit)
        else:
            number_digit_odd += 1
            sum_digit_odd += digit
            digit_odd.append(digit)


    print(f"your even numbers: {number_digit_even} ({", ".join(map(str, digit_even))})")
    print(f"your odd numbers: {number_digit_odd} ({", ".join(map(str, digit_odd))})")
    print(f"The sum of your even numbers: {sum_digit_even}")
    print(f"The sum of your odd numbers: {sum_digit_odd}")


program()