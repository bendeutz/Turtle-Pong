from turtle import *
from turtle import Screen
import time
lives=3
#global lives
"""
a=input("Did you feel that earthquake in Nevada?y/n")
if a=="y":
  print("Ok, get out of your house and don't play turtle pong. It isn't safe to play video games during a earthquake. Don't play, kids.")
else:
  print("Have fun. If you're not having fun, I'm going to steal your cookies and sue you $9e100")
"""
sc1=Screen()
sc=Screen()
t1=Turtle()
t2=Turtle()
t2.shape("circle")
t2.fillcolor("yellow")
#
t1.speed(0)
t2.penup()
# user
t3=Turtle()
t3.shape("turtle")
#wall



#b=Turtle()
#b.shape("circle")
"""#b.penup()
x,y=t2.position()
x1,y1=b.position()
xspeed=1
yspeed=1
xspeed1=1
yspeed1=1
def wall():
  t1.penup()
  t1.goto(-150,-100)
  t1.pendown()
  t1.goto(-150,100)
  t1.goto(150,100)
  t1.goto(150,-100)
  t1.goto(-150,-100)
  t1.hideturtle()
"""
def user():
  t3.penup()
  t3.goto(0,-80)


def ball_move():
  global x,y,xspeed,yspeed
  x=x+xspeed
  y=y+yspeed
  t2.setposition(x,y)
  
  if x <-145 or x >145:
    xspeed =- xspeed
  if y > 95 or y < -95:
    yspeed = - yspeed
  if t2.distance(t3) < 20:
    yspeed = - yspeed
  sc.ontimer(ball_move,20)

def bomb_move():
    global x1,y1,xspeed1,yspeed1
    
    x1=x1+xspeed1
    y1=y1+yspeed1
    b.setposition(x1,y1)
    
    if x1 <-145 or x1 >145:
      xspeed1 =- xspeed1
    if y1 > 95 or y1 < -95:
      yspeed1 = - yspeed1
    if b.distance(t3) < 20:
      yspeed1 = - yspeed1
      #if lives=>0:
    #    bye()
        
     # else:
      #  lives=-1
    sc1.ontimer(bomb_move,20)

def user_left():
  t3.backward(5)
  
def user_right():
  t3.forward(5)

def user_up():
  t3.sety(turtle.ycor() + 5)
  
def user_down():
  t3.sety(turtle.ycor() - 5)
  
sc.onkey(user_left,"left")
sc.onkey(user_right,"right")
sc.onkey(user_up,"up")
sc.onkey(user_down,"down")

def main():
 
  userx,usery=t3.position()
  wall()
  user()
  sc.listen()

  
  x,y=t2.position()
  
  xspeed=1
  yspeed=1
  ball_move()
 
  x1,y1=b.position()
  xspeed1=1
  yspeed1=1
  #bomb_move()


main()

# homework
# make sure turtle does not get out of box
# BONUS - add a score to your game
# BONUS2 - add up and down arrow keys