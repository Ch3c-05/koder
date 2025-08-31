
formal_summer = ["shorts","polo t-shirt", "lacoste sko"]
party_summer = ["t-shirt","jeans","sneaker","shirt"]
casual_winter = ["lange bukser","sweatshirt","jakke"]



def summer_hverdag_outfit():
    tast = input("Er det outfit til hverdag eller fast?: ")
    print(tast)
    while tast == "hverdag":
        print(f"Her er et outfit til hverdag: {formal_summer [1]}, {party_summer [1]}, {party_summer [2]} " )
        break


def winter_hverdag_outfit():
    tast = input("Er det outfit til hverdag eller fast?: ")
    print(tast)
    while tast == "hverdag":
        print(f"Her er et outfit til hverdag vinter: {joanna_winter [1]}, {joanna_winter [0]}, {joanna_winter[2]} og {party_summer[2]}")
        break

def stop():
    while not tast ==  "summer" or "winter":
        print("Det er ikke en af mulighederne. Jeg beklager!")
        break


while True:
    tast = input("")
    if tast == "summer":
        summer_hverdag_outfit()
        break
    elif tast == "winter":
        winter_hverdag_outfit()
        break
    else:
        not tast == "summer" or "winter"
        prin
        break

        




