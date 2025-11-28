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
            print("Du har tabt!")
            break
        p1()

        if bricks_alt == 0:
            print("CPU har tabt!")
            break
        p2()



game_loop()