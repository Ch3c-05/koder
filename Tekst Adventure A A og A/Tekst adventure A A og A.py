### Helper functions til at vise rummene ###
import time

ring_ivan = False
tøj_på = False
set_ivan = False
lyset_tændt = False
telefon_taget = False
tjek_besked = False
havrefras_taken = False
tandbørste_taken = False
børstet_tænder = False
barber_taken = False
buzzcut_done = False
ivan_ubevidst = False

def show_room_0():
    # Viser rum 0 (soveværelset)
    if not lyset_tændt:
        print("Velkommen til Remis hus! ")
        print("Du er Remi, og du har lige vågnet op! Du ligger under dynen uden tøj på i dit soveværelse med slukket lys og gardinerne for. ")
        print("Hvad vil du gerne lave nu? ")
    else:
        print("Du er i soveværelset. ")
        if not telefon_taget:
            print("Lyset er tændt. Du ser din telefon ved siden af sengen på natbordet. ")
        else:
            print("Lyset er tændt. ")
        print("Døren til stuen er lukket foran dig, og døren til badeværelset står på klem til højre. ")


def show_room_1():
    #Viser rum 1 (stuen)
    print("Du er i stuen. Du ser en sofa, et sofabord hvorpå der ligger en kniv. Der er også et tændt fjernsyn og Ivan sidder i sofaen. ")
    if not tøj_på:
        print("Du har dog ikke tøj på og vender derfor om for at være lidt mere selskabsvenlig. ")
        time.sleep(3)
        show_room_0()
    if ring_ivan:
        if not set_ivan:
            print("Du undrer dig over hvorfor du ringede til Ivan, nu når han sidder lige her. ")
            print("Ivan spørger dig om du vil se med på fjernsynet.")
        else:
            print("Ivan er stadig i sofaen. ")

    else:
        print("Du er overrasket over Ivans tilstedeværelse. ")
        print("Ivan spørger dig om du vil se med på fjernsynet. ")

def show_room_2():
    print("Du går ud til køkkenet (rum 2)")
    print("Du ser et køleskab, men kan ikke helt se hvad der er inde i køleskabet.")
    print("Du ser også nogle madrester på køkkenbordet.")

def show_room_3():
    #Viser rum 3 
    print("Du åbner døren og går ind på badeværelset. ")
    print("Du ser et toilet hvor der står, \"IKKE SKYL UD\". ")
    print("Der er et spejl over vasken hvor du kan berundre dit smukke selv. ")
    print("Du ser også en tandbørste der ligger ved vasken. ")
    print("Der ligger også en barbermaskine, håret sidder hulter til bulter og du tænker over din buzzcut-ide du fik ikke så længe siden. ")  
      


def show_room(room_num):
    """Display the contents of the given room.
    Input:
    - room_num : int, the number of the room to show.
    """
    if room_num == 0:
        show_room_0()
    elif room_num == 1:
        show_room_1()  
    elif room_num == 2:
        show_room_2()  
    elif room_num == 3:
        show_room_3()
    else:
        print("You are out of bounds. Room", room_num, "does not exist. ")

### The main game loop ### 

def game_loop():
    """Main loop of the game - this is where the fun happens."""
    global lyset_tændt, telefon_taget, tjek_besked, havrefras_taken, tøj_på, set_ivan, ring_ivan, tandbørste_taken, børstet_tænder, barber_taken, buzzcut_done, ivan_ubevidst

    # Vi starter i rum 0
    current_room = 0

    # Viser rummet vi starter i
    show_room(current_room)

    # Main loopet hvor der er et input til brugeren
    while True:
        user_inp = input("> ").strip().lower()
        if user_inp == "quit":
            break
# Soveværelset, rum(0)
        elif user_inp in ["gå ind på værelset", "gå til værelset"]:
            if current_room in [0, 2]:
                print("Du kan ikke gå ind på værelset fra din nuværende position. ")
            else:
                if tandbørste_taken:
                    print("Du lægger tandbørsten fra dig ved vasken igen. ")
                    tandbørste_taken = False
                current_room = 0
                show_room(0)
        
        elif user_inp == "tænd lyset":
            if not lyset_tændt:
                lyset_tændt = True
                print("Lyset er tændt")
                if not telefon_taget:
                    print("Du ser din telefon som er ved siden af din seng op dit natbord.")
                print("Du ser døren til stuen lukket foran dig og døren til badeværelse på klem til din højre")
            else:
                print("Lyset er allerede tændt.")

        
        elif user_inp in [ "tag telefon" , "tag telefonen"]:
            if lyset_tændt:
                if not telefon_taget:
                    telefon_taget = True
                    print("Du tager telefonen.")
                else:
                    print("Du har allerede taget telefonen.")
            else:
                print("Det er for mørkt til at finde det")


        elif user_inp in ["tjek beskeder", "tjek besked"]:
            if telefon_taget:
                if not tjek_besked:
                    tjek_besked = True
                    print("En enkel viser sig og siger at du skylder 1.4 millioner kroner til den danske statskasse.")
                    print("Hvis du ikke betaler beløbet, bliver du sat i retten!")
                else:
                    print("Du har allerede tjekket beskederne.")
            else:
                print("Du har ikke telefonen endnu. Tag telefonen først")


        elif user_inp in ["ring til Ivan" , "Ring Ivan"]:
            if telefon_taget:
                if tjek_besked:
                    print("Ivan tager telefonen og taler. ")
                    print("Ivan: Hej Remi, hva' så? ")
                    print("Du foklarer at du skylder ret mange penge og råber om hjælp. ")
                    print("Ivan lytter og foreslår, at du mødes med ham i stuen. ")
                else:
                    print("Ivan tager telefonen og taler. ")
                    print("Ivan: Hej Remi, hva' så? ")
                    print("Du siger bare hej og lægger på. ")
            else:
                print("Du har ikke din telefon endnu. Tag telefonen først. ")
            
        
        elif user_inp == "tag tøj på":
            print("Du tager tøj på og du ser nice ud. ")
            tøj_på = True

# Stuen, rum(1)
        elif user_inp in ["gå ind i stuen", "gå til stuen"]:
            if current_room in [1, 3]:
                print("Du kan ikke gå ind i stuen fra din nuværende postition. ")
            else:
                current_room = 1
                show_room(1)
                set_ivan = True

        elif user_inp in ["sid ned ved ivan", "sid ned i sofaen", "sid ved ivan", "sid i sofaen"]:
            if not ivan_ubevidst:
                print("Du sætter dig ved siden af Ivan, hvor Ivan meget hurtigt samler kniven op og dræber dig blodigt ved at stikke dig i hjertet. (Ending #3)")
                break
            else:
                print("Ivan er væltet til siden og blokerer sofaen.")
                print("Du prøver at flytte på ham, men han er enten for tung eller så er du for slap. ")
        
        elif user_inp in ["slå ivan i baghovedet", "slå ivan", "dask ivan", "slå ivan i hovedet", "dræb ivan"]:
            if not ivan_ubevidst:
                print("Du slog Ivan i baghovedet med din lukkede knytnæve og gjorde ham bevidstløs.")
                ivan_ubevidst = True
            else:
                print("Du har nok hallucineret, fordi du slår ud efter Ivan igen og svinger bare gennem luften, selvom han jo bare lægger bevidstløs i sofaen. ")


# Køkkenet, rum(2)        
        elif user_inp in ["gå ind i køkkenet", "gå til køkkenet"]:
            if current_room in [0, 2, 3]:
                print("Du kan ikke gå ind i køkkenet fra din nuværende position. ")
            else:
                current_room = 2
                show_room(2)

        elif user_inp in ["gå til køleskab", "gå til køleskabet"]:
            print("Du går over til køleskabet og ser noget havrefras og mælk, du ser også at der er plads til at du kan sætte dig ind i køleskabet.")

        elif user_inp in ["tag havrefras og mælk", "tag havrefras,", "tag mælk"]:
            if not havrefras_taken:
                print("Du tog noget havrefras og mælk, lavede dig en skål og spiste det. Der skete ingenting...")
                havrefras_taken = True
            else:
                print("Du har allerede taget havrefras og mælk. Der er ikke mere tilbage. ")
        
        elif user_inp == "sid i køleskabet":
            print("Du satte dig i køleskabet og døde af kulde (#Ending 4).")
            break  
        
        elif user_inp in ["gå over til resterne", "gå til resterne"]:
            print("Du går over til resterne. Du kan stadig ikke se, hvor gamle resterne er; du kan kun se en eller anden form for lidt grønt kød.")
        
        elif user_inp in ["spis resterne i køkkenet", "spis resterne", "spis rester"]:
            print("Du spiste resterne og døde on the spot, da du fandt ud af, at det var Ivans rådne fødder (Ending #5).")
            break  
        
        elif user_inp == "lade vær med at spise resterne":
            print("Efter et bedre kig på resterne vælger du ikke at spise dem.")

# Badeværelset, rum(3)
        elif user_inp in ["gå ind på badeværelset", "gå til badeværelset"]:
            if current_room in [1, 2, 3]:
                print("Du kan ikke gå ind på badeværelset fra din nuværende position. ")
            else:
                current_room = 3
                show_room(3)

        elif user_inp in ["tag tandbørsten", "saml tandbørsten op", "tag tandbørste"]:
            if tandbørste_taken:
                print("Du har allerede tandbørsten.")
            else:
                print("Du samler tandbørsten op.")
                tandbørste_taken = True
        
        elif user_inp in ["børst tænder", "børst tænderne", "børst dine tænder"]:
            if not børstet_tænder:
                print("Du børster dine tænder og har nu ikke længere natmadrester siddende i tænderne. ")
                børstet_tænder = True
            else:
                print("Du børster dine tænder igen, men det gør sjovt nok ikke noget. ")
        
        elif user_inp in ["skyl ud i toilettet", "skyl ud", "skyl ud i toilet"]:
            print("Du skal til at skylle ud i toillet, men tænker over om du vil bruge det store eller lille skyl. ")
        
        elif user_inp in ["brug det store skyl", "skyl stort", "skyl ud stort", "skyl stort ud", "stort skyl" ]:
            print("Du bruger det store skyl på toilettet på trods af advarslen og toilettet eksploderer og dræber dig. (Ending #2)")
            break
        
        elif user_inp in ["brug det lille skyl", "skyl småt", "skyl ud småt", "skyl småt ud", "lille skyl"]:
            print("Du skylder småt ud i toilettet og en lille guldfisk svømmer kortvarigt op og derefter forsvinder ned igen. ")
        
        elif user_inp in ["tag barbermaskine", "tag barbermaskinen", "saml barbermaskinen op"]:
            print("Du samler barbermaskinen op. ")
            barber_taken = True
        
        elif user_inp in ["lav et buzzcut", "buzzcut", "klip buzzcut", "buzzcut håret", "buzzcut hår", "klip hår"]:
            if barber_taken:
                print("Du giver dig selv et buzzcut og det tager et par minutter, hvorefter du ligger barbermaskinen tilbage på vasken. Ser det godt ud? Du kan prøve at kigge i spejlet. ")
                buzzcut_done = True
                barber_taken = False
            else:
                print("Du har ikke barbermaskinen. ")

        elif user_inp in ["kig i spejlet", "kig på spejlet", "brug spejlet", "kig på spejlet"]:
            if buzzcut_done:
                print("Du kigger på dig selv i spejlet, falder simpelthen om fordi du ser så godt ud og rammer desværre dit hoved på vasken på vej ned og dør af et kraniebrud. Ending #1 ")
                break
            else:
                print("Du kigger dig selv i spejlet og håret sidder stadig hulter til bulter. ")
        elif user_inp in ["kig rundt", "observer", ]:
            show_room(current_room)
                 
# Fejlbesked 
        else:
            print("Det tror jeg sku ikke lige jeg fatter... altså, :", user_inp)
        

# Starter spillet
game_loop()
