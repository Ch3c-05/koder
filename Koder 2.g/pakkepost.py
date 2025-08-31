kilo_1 = 4.3 
kilo_1_pris = 32 
kilo_1_adresse = "Taarnbyvej 2A"

xg = input("hvor mange vejer dit pakke?: ")
xg_adresse = input("hvor bor du?: ")
xg = float(xg)
xg_adresse = int(xg_adresse)

if xg == kilo_1:
    xg = True , print("Du skal betale: " + str(kilo_1_pris) + "kr.")
else: 
    print ("Fejl, det er ikke din pakke!")

if xg_adresse == "Taarnbyvej 2A":
    print("Goodie!")
else:
    print("Fejl!")