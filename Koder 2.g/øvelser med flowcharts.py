import time

snooze_interval = 10
max_snooze_count = 3
snooze_count = 0


def vækkeur(snooze_interval = 5, max_snooze_count = 3):
    snooze_count = 0
    print ("Alarm ringer!")

def snooze():
    print("Snooze er aktiviret")
    time.sleep(5)


choice = input("Vil du trykke på snooze knappet? ja/nej: ")

while True:
    if choice == "ja":
        snooze()
        print(f"Venter tidd er: {snooze_interval} minutter")

    else: 
        choice == "nej"
        print("Alarm slukkes")
        break
  



       