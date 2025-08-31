import pygame
import time

# Initialiser pygame mixer og pygame selv
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

# Opsæt skærm (kræves af pygame for input)
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Trommemaskine")

# Indlæs trommelyde her ved at deklarere en værdi, her med 1 eksempel:
# Find selv på flere!
kick_sound = pygame.mixer.Sound("Big_drum.wav")

# Opret en ordbog, der kortlægger taster til trommelyde, her er der et eksempel på at 'a' har en lyd.
#Find selv på flere ved at lægge lyde ind i din projektmappe <-----
#I kan bruge min mappe eller I kan selv finde lyde på freesound.org
key_to_sound = {
    pygame.K_a: kick_sound,
}

# Trommemaskinens hovedloop
running = True
while running:
    for event in pygame.event.get():
        # Luk programmet, hvis vinduet lukkes
        if event.type == pygame.QUIT:
            running = False

        # Tjek om en tast er trykket ned
        if event.type == pygame.KEYDOWN:
            # Afspil den tilsvarende lyd, hvis tasten findes i vores ordbog
            if event.key in key_to_sound:
                sound = key_to_sound[event.key]
                sound.play()

    # En lille forsinkelse for at undgå at bruge for meget CPU
    time.sleep(0.01)
pygame.quit()