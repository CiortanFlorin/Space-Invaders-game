from turtle import Screen
from ship import Ship
from alien_manager import AlienManager
from laser import Laser
from alien_laser_manager import AlienLaser
import time
import random

#Create screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("AlienInvaders")
rows = range(-380,200,50)
columns = [100, 150, 200, 250]

#Stop screen from auto-updating
screen.tracer(0)


laser = Laser()
ship = Ship()


#A function witch makes a dictionary of alien objects and a list with their numbers
aliens={}
aliens_list=[]
def create_aliens():
    i=0
    for c in columns:
        for n in rows:
            aliens[i]=AlienManager(n,c)
            aliens_list.append(i)
            i+=1


#Creates lasers from the aliens which are not dead
alien_lasers=[]
def alien_fire():
    x=random.choice(aliens_list)
    alien_laser=AlienLaser(aliens[x].xcor(), aliens[x].ycor()-10)
    alien_lasers.append(alien_laser)

#Make the player laser go back to ship front
def advance():
    if laser.ycor()>300:
        x= ship.xcor()
        y= ship.ycor()
        laser.goto(x,y+10)

def game_reset():
    global aliens, alien_lasers, r
    for alien in aliens:
        aliens[alien].speed("fastest")
        aliens[alien].goto(-900,900)
    aliens = {}
    aliens_list = []
    for n in alien_lasers:
        n.goto(0, -900)
    alien_lasers = []
    ship.goto(0, -250)
    laser.goto(0, 320)
    r=0
    create_aliens()

#Make screen react to keyboard press of a and d
screen.listen()
screen.onkey(ship.move_left, "a")
screen.onkey(ship.move_right, "d")
screen.onkey(advance, "space")

create_aliens()
game_on=True
r=0
while game_on:
    screen.update()
    time.sleep(0.1)


    #Killing of aliens
    for alien in aliens:
        if laser.distance(aliens[alien])<40:
            aliens[alien].speed("fastest")
            aliens[alien].goto(-900,900)
            aliens_list.remove(alien)
            laser.goto(800,800)

    #This makes the aliens move
    if r==42:
        r=0
    if r in range(0, 19):
        for alien in aliens:
            aliens[alien].goto((aliens[alien].xcor()+10),aliens[alien].ycor())
    elif r == 20 or r == 41:
        for alien in aliens:
            aliens[alien].goto(aliens[alien].xcor(),(aliens[alien].ycor()-10))
    elif r in range(21, 40):
        for alien in aliens:
            aliens[alien].goto((aliens[alien].xcor() - 10), aliens[alien].ycor())
    r+=+0.25

    #Create alien fire from random aliens and make them move
    if r in range(0, 40, 3):
        alien_fire()
    for x in alien_lasers:
        x.go_on()
    for x in alien_lasers:
        if ship.distance(x)<10:
            game_reset()

    #Player laser movement
    laser.advance()

screen.exitonclick()