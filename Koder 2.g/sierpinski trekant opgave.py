import turtle

bob = turtle.Turtle()
bob.color ("black","red")
bob.speed(10)

startpunkt1 = (-200, -200)
startpunkt2 = (0, 200)
startpunkt3 = (200, -200)

def tegn_stor_trekant(startpunkt1, startpunkt2, startpunkt3):
    bob.begin_fill()
    bob.penup()
    bob.goto(startpunkt1)
    bob.pendown()
    bob.goto(startpunkt2)
    bob.goto(startpunkt3)
    bob.goto(startpunkt1)



def midpunkt(punkt1, punkt2):
    mid_x = (punkt1[0] + punkt2[0]) / 2
    mid_y = (punkt1[1] + punkt2[1]) / 2
    return(mid_x, mid_y)



def tegn_sierpinskitrekant(punkt1, punkt2, punkt3, niveau):
    if niveau == 0:
        tegn_stor_trekant(punkt1, punkt2, punkt3)
    else:
        midpunkt1 = midpunkt(punkt1, punkt2)
        midpunkt2 = midpunkt(punkt2, punkt3)
        midpunkt3 = midpunkt(punkt3, punkt1)

        tegn_sierpinskitrekant(punkt1, midpunkt1, midpunkt3, niveau - 1)
        tegn_sierpinskitrekant(midpunkt1, punkt2, midpunkt2, niveau - 1)
        tegn_sierpinskitrekant(midpunkt3, midpunkt2, punkt3, niveau - 1)
        
   
    
tegn_sierpinskitrekant(startpunkt1, startpunkt2, startpunkt3, 5)
turtle.done()