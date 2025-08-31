inp = input("Gæt bogstaven: ")
while not inp == "A" or inp == "B":
    inp = input("Gæt bogstaven: ")


if inp == "A":
    print("Godt")
elif inp == "B":
    print("flot")
    
print("Du indtastede", inp)
