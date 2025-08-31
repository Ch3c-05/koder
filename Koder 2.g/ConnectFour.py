


Game = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]


NoneColor = '\033[0m'

PlayerOneColor = '\033[34m'

PlayerTwoColor = '\033[31m'



# Game = [[0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]


Width = len(Game[0])
Height = len(Game)










def PutBrik(plads, teamID):
    
    i = len(Game) - 1

    while i >= 0:

        if (Game[i][plads] == 0):
            Game[i][plads] = teamID

            break
        elif (i == 0):
            print("Column is full")


        i -= 1






def CheckBoard(teamID):
    for y in range(len(Game)):
        

        for x in range(len(Game[y])):
            

            if (Game[y][x] == teamID):
                
                # print(f'x = {x}, y = {y}')


                
                if (CheckHor(y, x, teamID) or CheckVer(y, x, teamID) or CheckDia(y, x, teamID)):
                    return True







def CheckDia(y, x, teamID):
    if ((x + 3) <= (Width - 1)) and (y + 3 <= Height - 1):
        i = 0

        while True:
            if Game[y + i][x + i] == teamID:
  
                if i == 3:

                    print("hurray men diagonal")

                    return True
                    
                else:
                    i += 1
            else:
                break

    elif ((x + 3) <= (Width - 1)) and (y - 3 >= 0):
        i = 0

        while True:
            if Game[y - i][x + i] == teamID:
  
                if i == 3:

                    print("hurray men diagonal")
                    return True
                    
                else:
                    i += 1
            else:
                break



def CheckVer(y, x, teamID):

    if (y + 3 <= Height - 1):
        i = 0

        while True:
            if Game[y + i][x] == teamID:
                if i == 3:

                    return True
                
                else:
                    i += 1
            
            else:
                break




def CheckHor(y, x, teamID):

    if ((x + 3) <= (Width - 1)):

        i = 0
                
        while True:
            
            if Game[y][x + i] == teamID: 

                if i == 3:

                    return True
                    
                else:
                    i += 1

            else:
                break


        

    else:
        print("Out of bounds") 

        
        
            



    # Martins hus
    i = len(Game) - 1

    while i >= 0:

        

        i -= 1

    #-------------------------










def PrintBoard():
    

    test = ""

    for i in range(1, Width + 1):
        test += f'|{i}'
    

    test += "|"

    print(test)


    for i in Game:
        result = ""

        andrei = []


        for g in range(0, len(i)):


            # print(f'Sistema: {i[g]}')
            # [x, teamID]
            # testData = [0, 1]

            # andrei.append(testData)

            if (i[g] == 0):
                andrei.append(0)
            elif (i[g] == 1):
                andrei.append(1)
                # print('\033[33m0\033[0m')
            elif (i[g] == 2):
                andrei.append(2)
                # print('\033[31m0\033[0m')
            else:
                print("FEJL")
            

        PrintRow(andrei)



        
        

def PrintRow(andrei):

    result = " "

    for test in andrei:
        if test == 0:
            result += f'{NoneColor}0 '
        if test == 1:
            result += f'{PlayerOneColor}0 {NoneColor}'
        if test == 2:
            result += f'{PlayerTwoColor}0 {NoneColor}'




    print(result)

            





# PutBrik(0, 1)
# PutBrik(0, 1)
# PutBrik(0, 1)
# PutBrik(0, 1)

# PutBrik(0, 1)
# PutBrik(1, 1)
# PutBrik(2, 1)
# PutBrik(3, 1)



CheckBoard(1)



PrintBoard()




    



def GameLoop():

    TurnIndex = 1


    while True:




        inp = -1

        while True:
            try:
                inp = int(input(f"Player {TurnIndex}'s turn: ").strip())
                
                if (inp <= Width):
                    
                    if (Game[0][inp - 1] != 0):
                        print("Sistemas hemmelighed")

                        PrintBoard()
                    else:
                        break

                else:
                    print("Input is out of bounds")

                    PrintBoard()

                

            
            except ValueError:
                print("The last regneopgaver")



        PutBrik(inp - 1, TurnIndex)

        PrintBoard()


        if (CheckBoard(TurnIndex)):
            print(f'Player {TurnIndex} won!')
            break

        if TurnIndex == 1:
            TurnIndex = 2
        else:
            TurnIndex = 1

        
            

        










GameLoop()





