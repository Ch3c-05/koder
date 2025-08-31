import time


def alarm_ringer():
    print("RING RING, ALARM, RING RING!")

 

def snooze():
    print("Snooze er aktiveret, alarm ringer igen om 10 sekunder.")
    time.sleep(10)
    alarm_ringer()


def alarm_w_snooze():

    while True: 
        alarm_ringer() 
        userinput = input("tast 'q' for at stoppe eller 's' for at snooze: ") 

        if userinput == 's': 
            snooze() 
            print("du har trykket snooze. Alarmen ringer igen om 10 sekunder.")

        elif userinput == 'q': 
            print("vækkeuret er afsluttet.")
            break 
        
        else:
            snooze() 

 

alarm_w_snooze()