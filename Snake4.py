# ==== Simplistic Snake Game In Turtle.Py ====

#MIT License

#Copyright (c) 2022 Kaitlyn Williams

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#=======================================================

# Imports & Setup
import turtle
import random
import time
import math

wn = turtle.Screen()
r = random.Random()

# ==== Turtles ====
tsnake = turtle.Turtle()
tfood = turtle.Turtle()
thud = turtle.Turtle()
tpoints = turtle.Turtle()

# ==== Player Settings ====
pSpeed = 0.2 # amount of time it takes to move forward (player speed)

# ==== Snake Playspace ====
mapSize = (-210, -210, # tuple for easy map change
                   -210, 210,
                   210, 210,
                   210, -210)

thud.speed(1000) # increase draw speed
thud.pu()
thud.goto(mapSize[0], mapSize[1]) # goto corner
thud.pd()

thud.fillcolor("Grey") # fill playspace as grey
thud.begin_fill()
thud.pensize(4)

for i in range(7):
    thud.goto(mapSize[i], mapSize[i+1]) # create sides    
thud.goto(mapSize[0], mapSize[1]) # return to corner

thud.end_fill()

# ==== User Graphics ====
wn.bgcolor("Brown")
thud.hideturtle() # hides the turtle for cleanliness

def createText(worker, txtPosX, txtPosY, font, fontsize, colour, text):
    worker.pu()
    worker.goto(txtPosX, txtPosY) # goto cords

    worker.color(colour)
    
    worker.write(str(text), move=True, align="center", font=(str(font), fontsize, "bold")) # create text
    worker.pd()

createText(thud, 0, 300, "Arial", 60, "White", "Simple-Snake") # game title

createText(thud, 0, -320, "Arial", 40, "White", "Move: W A S D, Collect Food!") # instructions

createText(thud, 250, -400, "Arial", 15, "White", "Kaitlyn Williams") # Signature

# ==== Movement Functions ====

def Up(): # go up
    tsnake.setheading(90)

def Down(): # go down
    tsnake.setheading(-90)

def Left(): # go left
    tsnake.setheading(180)

def Right(): # go right
    tsnake.setheading(0)

def QuitSnake(): # exit game
    wn.bye()

# ==== Keyboard Input ====
wn.listen() 

wn.onkey(Up, "w") # execute function onkeypress
wn.onkey(Down, "s")
wn.onkey(Left, "a")
wn.onkey(Right, "d")
wn.onkey(QuitSnake, "q") # q = close game

# ==== Snake food ====
score = 0

def createFood():
    tfood.color("Red") # setup pen
    tfood.pu()
    foodX = r.randrange(-200, 200) # get random cords within prams
    foodY = r.randrange(-200, 200)
    tfood.goto(foodX, foodY) # goto cords
    tfood.pd()
    tfood.shapesize(1, 1, 1) # create food graphic
    tfood.shape("circle")

# ==== Collision Detection ====
def tDistance(x1, x2, y1, y2):
    return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 )) # calculate distance

def distCollision(pointX1, pointY1, pointX2, pointY2, minDist):
    if(tDistance(pointX1, pointX2, pointY1, pointY2) < minDist): # check if distance is within dist
        return True # return true if within dist
    else:
        return False # if not return false

# ==== Snake Body ====
tsnake.color("Dark Green") # snake graphics
tsnake.pensize(20)
tsnake.speed(100) 

def snakeLength(score): # length of snake body  
    lastHeading = tsnake.heading() # save positions
    lastPos = tsnake.pos()

    tsnake.pd()
    length = score + 5 / 2 # set default length
    cout = 0
    while(cout < length): # draw snake
        tsnake.backward(5)
        cout = cout + 1
        
    tsnake.pu()
    tsnake.goto(lastPos) # reset position & heading
    tsnake.setheading(lastHeading)
def drawSnake(): # clear old snake, draw new
    tsnake.clear()
    snakeLength(score)

# ==== Points Box ====
tpoints.hideturtle() # hide turtle

thud.pu()
thud.color("Black")

thud.setpos(-450, 300) # goto location
#tpoints.setpos(-425, 275) 
thud.pd()

for q in range(4): # draw score panel
    thud.forward(100)
    thud.left(90)

createText(tpoints, -400, 310, "Arial", 50, "White", 0) # defualt score display

# ==== Game Loop ====
createFood()

while(1):
    time.sleep(pSpeed)
    if(distCollision(tfood.xcor(), tfood.ycor(), tsnake.xcor(), tsnake.ycor(), 15) == True):
        createFood()
        score = score + 5
        # print(str(score))

        tpoints.clear()
        createText(tpoints, -400, 310, "Arial", 50, "White", score)
    drawSnake()
    tsnake.forward(10)

# ==== Nolonger Proceeds ====
wn.exitonclick() 
