formal_summer = ["shorts", "polo t-shirt", "lacoste sko"]
party_summer = ["t-shirt", "jeans", "sneaker", "shirt"]
joanna_winter = ["lange bukser", "sweatshirt", "jakke"]

def summer_hverdag_outfit():
    tast = input("Er det outfit til hverdag eller fest?: ").lower()
    if tast == "hverdag":
        print(f"Her er et outfit til hverdag: {formal_summer[1]}, {party_summer[1]}, {party_summer[2]}")
    else:
        print("Ikke en gyldig mulighed for sommer.")

def winter_hverdag_outfit():
    tast = input("Er det outfit til hverdag eller fest?: ").lower()
    if tast == "hverdag":
        print(f"Her er et outfit til hverdag vinter: {joanna_winter[1]}, {joanna_winter[0]}, {joanna_winter[2]} og {party_summer[2]}")
    else:
        print("Ikke en gyldig mulighed for vinter.")

def main():
    while True:
        tast = input("Hvordan er vejret i dag? (summer/winter): ").lower()
        if tast == "summer":
            summer_hverdag_outfit()
            break
        elif tast == "winter":
            winter_hverdag_outfit()
            break
        else:
            print("Det er ikke en af mulighederne. Jeg beklager!")
    

main()