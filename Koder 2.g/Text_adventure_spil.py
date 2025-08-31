def show_room_0():
    print("Velkomen til Remis hus!")
    print("Du er Remi og du har lige vågnet op! Du lægger under dynen i dit soverværelse med slukket lys og garinerne for!")
    print("Hvad gøre du så?")

def show_room(room_num):
    if room_num == 0:
        show_room_0()
    else:
        print("You are out of bounds. Room", room_num, "does not exist.")    


def game_loop():

    current_room = 0
    show_room(current_room)

    while True:
        user_choice = input("> ")

        if(user_choice == "tænd lyset"):
            print("Lyset er tændt")
            print("Du ser din telefon som er ved siden af din seng op dit natbord.")
            print("Du ser døren til stuen lukket foran dig og døren til badeværelse på klem til din højre")

        if(user_choice == "tag telefon"):
            print("En enkel viser sig og siger at du skylder 1.4 millioner kroner til den danske statskasse.")
            print("Hvis du ikke betaler beløbet, du blivet sat i retten!")
        
        elif(user_choice == "ring til Ivan"):
            

        elif(user_choice == "tag tøj på"):
            print("s")