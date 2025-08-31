# Importere pygame, math som libraries og bold som class
import pygame
import math
from bold import Ball

# Game World
running = True
WIDTH, HEIGHT = 800,600
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FLOOR = 500

# Spiller variabler
score = 0
lives = 3
polebounce = False 

# Bold variabler og konstanter
ball = Ball
ballradius = 15
STARTPOSITION = pygame.Vector2(200,400)
bounce = 0.66
gravity = 0.5

# Hastighedsudregningsvariabler
potentialvelocity = pygame.Vector2(0,0)
mousepos = pygame.Vector2(0,0)
dragging = False
angle = 0

def pointgraph(vinkel, iterations): # Her defineres en funktion til at udregne buen for bolden ud fra vinkel og iterationer
    points = [(ball.position)]

    for i in range(0,iterations): 
        points.append(velocity(i/(iterations*0.35),vinkel))

    return points

def velocity(tid, vinkel): # Her defineres en funktion for at finde hvor bolden kommer til at være ud fra vinkel og tid
    return [(7.6*potentialvelocity.length() * tid * math.cos(vinkel)) + ball.position.x, (0.5*gravity * 60 * tid**2 + 7.6*potentialvelocity.length() * math.sin(vinkel) * tid) + ball.position.y]

# Her initereres pygame og bolden
pygame.init()
pygame.font.init()
pygame.display.set_caption("Eksperimentelt Arbejde")
ball.___init___(ball,STARTPOSITION,pygame.Vector2(0,0),gravity,True,ballradius,FLOOR,bounce)
font = pygame.font.SysFont("Verdana", 30)

while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN: # Find musepositionen
            if ball.static and lives > 0:
                dragging = True
                mousepos = pygame.Vector2(pygame.mouse.get_pos())

        elif event.type == pygame.MOUSEBUTTONUP: # Hastighed udregnes ud fra fysikformler
            if ball.static and lives > 0:
                dragging = False
                ball.static = False
                ball.velocity = pygame.Vector2(potentialvelocity.length() * math.cos(angle), gravity + potentialvelocity.length() * math.sin(angle))
        
        elif event.type == pygame.KEYDOWN and lives <= 0:
            if event.key == pygame.K_n:
                running = False
            if event.key == pygame.K_j:
                ball.position =pygame.Vector2(200,400)
                lives = 3
                score = 0

    ball.update(ball) # Opdater boldens position
    if ball.position.y >= FLOOR - ball.radius: # Udregn boldens kollision med gulvet
        ball.position.y = FLOOR - ball.radius
        if ball.velocity.length() >= 5:
            ball.velocity.y = -ball.velocity.y*ball.bounce
            ball.velocity.x = ball.velocity.x*ball.bounce
        else: 
            lives -= 1
            ball.static = True
            ball.position = pygame.Vector2(200,400)

    if ball.position.x >= 640 - ball.radius and ball.position.x <= 650 and ball.position.y >= 200: # Udregn boldens kollision med pælen # Udregn boldens kollision med pælen
        ball.position.x = 640 - ball.radius
        polebounce = True
        if ball.velocity.length() >= 3:
            ball.velocity.y = ball.velocity.y*ball.bounce
            ball.velocity.x = -ball.velocity.x*ball.bounce
        else: 
            ball.velocity = pygame.Vector2(0,0)

    if ball.position.x >= WIDTH or ball.position.x <= 0 or ball.position.y <= 0:
        lives -= 1
        ball.static = True
        ball.position = pygame.Vector2(200,400)        

    if ball.check_collision(ball,pygame.Vector2(580,295),pygame.Vector2(60,45)): # Udregn om bolden har ramt målet
        if polebounce:
            score += 1
            polebounce = False
        else:
            score += 2
        ball.static = True
        ball.position = pygame.Vector2(200,400)

    # Tegn alle elementerne på skærmen
    SCREEN.fill(pygame.Color(61, 61, 61))
    if dragging == True:
        potentialvelocity = (-pygame.Vector2(pygame.mouse.get_pos()-mousepos))/5
        if potentialvelocity.x != 0 and potentialvelocity.y != 0:
            angle = math.atan2(potentialvelocity.y,potentialvelocity.x)
        pygame.draw.lines(SCREEN, "white", False, pointgraph(angle, 20),3)
        
    pygame.draw.circle(SCREEN, pygame.Color(247, 125, 54), ball.position, ballradius)
    pygame.draw.rect(SCREEN, "black", pygame.Rect(0, FLOOR, 1000, 200))
    pygame.draw.rect(SCREEN, "gray", pygame.Rect(580, 250, 60, 45))
    pygame.draw.rect(SCREEN, "black", pygame.Rect(640, 180, 20, 320))

    # Tegn teksten ud på skærmen
    SCREEN.blit(font.render(f"Score: {score}", True, (0,0,0)),(30,30))
    SCREEN.blit(font.render(f"Lives: {lives}", True, (0,0,0)),(30,70))
    if lives <= 0:
        SCREEN.blit(font.render(f"GAME OVER, RETRY?", True, (255,0,0)),(WIDTH/2,30))
        SCREEN.blit(font.render(f"YES(J) NO(N)", True, (0,0,0)),(WIDTH/2,70))
    
    pygame.display.flip()
    CLOCK.tick(60)
    
pygame.quit()



