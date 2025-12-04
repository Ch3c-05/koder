bricks_emoji = "🧱"
bricks_alt = 21
bricks = 0
player = 0


def vis_brikker():
    
    print("Brikkerne tilbage:", bricks_emoji * bricks_alt)


def p2():
    
    global player2, bricks_alt
    vis_brikker()
    print("Der er nu", bricks_alt, "brikker tilbage.")
    
    while True:
        try:
            player2 = int(input("Hvor mange vil du fjerne?: "))
            if player2 < 1 or player2 > 3:
                print("Du kan kun fjerne 1, 2 eller 3 brikker.")
            elif player2 > bricks_alt:
                print("Der er ikke nok brikker tilbage.")
            else:
                print("Player2 tager", player2, "brikker.")
                bricks_alt -= player2
                break
        except ValueError:  
            print("Indtast et gyldigt tal.")

   



def p1():
        
    global player, bricks_alt
    vis_brikker()
    print("Der er nu", bricks_alt, "brikker tilbage.")
    
    while True:
        try:
            player = int(input("Hvor mange vil du fjerne?: "))
            if player < 1 or player > 3:
                print("Du kan kun fjerne 1, 2 eller 3 brikker.")
            elif player > bricks_alt:
                print("Der er ikke nok brikker tilbage.")
            else:
                print("Player1 tager", player, "brikker.")
                bricks_alt -= player
                break
        except ValueError:  
            print("Indtast et gyldigt tal.")


def game_loop():

    global bricks_alt
    
    while True:
        if bricks_alt == 0:
            print("Player1 har tabt!")
            break
        p1()

        if bricks_alt == 0:
            print("Player2 har tabt!")
            break
        p2()

    #Den stykke kode er faktisk algoritmen som man bruger for at vinder spillet.

    #print("Der er", bricks_alt, "brikker tilbage.")
    #if bricks_alt % 4 == 3:
     #   bricks = 2
    #elif bricks_alt % 4 == 2:
    #    bricks = 1
    #elif bricks_alt % 4 == 0:
    #    bricks = 3
    #else:
     #   bricks = 1 
    #print("CPU takes some", bricks)
    #bricks_alt -= bricks
    #print("Der er", bricks_alt, "brikker tilbage.")

game_loop()