#This project is split into different parts for easy organization and readability for future reference.
#The code should have a natural flow.
#Sections

#0  color selection
#1. Jingles & marker change
#2. Randomizer
#3. Shape Algorithms
#4. Wall avoidance
#5 Executor


#randint is built into myro and works differently then import Random
from Myro import *
initialize("com4")



#0. Choose color##########################################################################################################
###############################################################################################################################################################
###############################################################################################################################################################


def choosecolor():
 gen= randint(1, 5)
 if (gen==1):
  print("You need white paper, a light blue marker, a red marker, and a orange marker")
 elif (gen==2):
  print("You need white paper, a black marker, a green blue marker, and a brown marker.")
 elif (gen==3):
  print("You need white paper, a grey marker,a black marker, and a blue marker.")
 elif (gen==4):
  print("You need yellow paper, an orange marker, a black marker, and a blue marker.")
 elif (gen==5):
  print("You need yellow paper, a red marker, a blue marker and black marker.")
 
 print("Use the colors successively, when asked to change, and on until the program sounds its ending progression jingle.")
 

#1. Jingles###############################################################################################################################################################
###############################################################################################################################################################

def markerchange():
 jingleemajor()
 input("\n\nWhen you have the markers ready, press enter.")
 setLED("left", "on")
 setLED("right", "on")
 setLED("left", "off")
 setLED("right", "off")
 setLED("left", "on")
 setLED("right", "on")
 setLED("left", "off")
 setLED("right", "off")
 setLED("left", "on")
 setLED("right", "on")
 setLED("left", "off")
 setLED("right", "off")
 setLED("left", "on")
 setLED("right", "on")
 setLED("left", "off")
 setLED("right", "off")
 setLED("left", "on")
 setLED("right", "on")
 setLED("left", "off")
 setLED("right", "off")
 setLED("left", "on")
 setLED("right", "on")
 setLED("left", "off")
 setLED("right", "off")


def jingleamajor():
 beep(.3, 1760)
 beep(.3, 3951.1) #B
 beep(.3, 2217.3) #C#
 beep(.3, 1760, 3951.1) #A & B

def jingleemajor():
 #in E, next blues prog, one octave up
 beep(.3, 2637)
 beep(.3, 2960)  
 beep(.3, 3322.4)
 beep(.3, 2637)

def jinglebmajor():
#in b third of the blues prog       bbb bc#d#b bbb bc#d#f bbb bc#d#b bbb f#d#c#b 
 beep(.3, 3951.1)
 beep(.3, 2217.3)
 beep(.3, 2489)
 beep(.3, 3951.1)



 ###########################################################################################################################
 
  ###########################################################################################################################
#2.Shape Randomizer
#Ratios for each shape are stored here as well as a way to randomly:
#all the inches are divided by twelve to create feet since all the input is in feet
#Limit is 7inches to keep the shapes on the size of the paper though this can be adjusted.

def shaperandomizer():
 gen= randint(1, 12) 
 if (gen==1 or 8):
  print("We will now try a circle.")
  circradius= randint(3, 7)/12
  circle(circradius)
 elif (gen==2 or 7):
  print("We will now try a triangle.")
  tris= randint(1, 7)/12
  triangle(tris)
 elif (gen==3):
  print("We will now try a rectangle.")
  recxx= randint(2, 7)/12
  recyy= randint(2, 7)/12
  rectangle(recxx,recyy)
 elif (gen==4):
  print("We will now try a square.")
  squarex= randint(2, 7)/12
  square(squarex)
 elif(gen==5):
  print("We will now try a straight line.")
  styy= randint(1, 7)/12
  straightline(styy)
 elif(gen==6):
  print("We will now try a koch snowflake.")
  br1level=randint(2,3)
  br1size=randint(1,2)*0.6
  brokenfractal1(br1level,br1size)
  
 elif(gen==7):
  print("We will try the first broken fractal.")
  br1level=randint(1,3)
  br1size=randint(1,2)*0.6
  brokenfractal2(br1level,br1size)                 
  
 elif(gen==8):
  print("We will now try the second broken fractal.")
  br1level=randint(1,3)
  br1size=randint(1,2)*0.6
  brokenfractal3(br1level,br1size)
  
 elif (gen==9):
  print("We will now try a flower.")
  circradius= randint(1, 7)/12
  flower(circradius)
  
 elif (gen==10):
  print("We will now try three circles.")
  circradius= randint(3, 7)/12
  threecirc(circradius)
  
 elif (gen==11):
  print("We will now try half a circle.")
  circradius= randint(3, 7)/12
  halfcirc(circradius)
  
 elif (gen==12):
  print("We will now try a dot.")
  dot()
  

  


###########################################################################################################################
###########################################################################################################################
###########################################################################################################################
#3. Shape Algorithms

def circle(radius):
 conv=radius*25.4
 arc(360, conv)

 
 #This is an equilateral triangle
 #Function does sides in feet
 #2
def triangle(x):
 move= x*11.2
 forward(0.25,move)
 turnLeft(3,1.4)
 checkwall() 
 forward(0.25,move)
 turnLeft(3,1.4)
 checkwall() 
 forward(0.25,move)
 turnLeft(3,1.4)
 
 
#In feet
#3
def rectangle(x,y):
 movex= x*11.2
 movey= y*11.2
 forward(0.25,movey)
 checkwall() 
 turnBy(90)
 forward(0.25,movex)
 checkwall() 
 turnBy(90)
 forward(0.25,movey)
 checkwall() 
 turnBy(90)
 forward(0.25,movex)
 
#In feet
#4
def square(x):
 side= x*11.2
 checkwall() 
 forward(0.25,side)
 turnBy(90)
 checkwall() 
 forward(0.25,side)
 turnBy(90)
 checkwall() 
 forward(0.25,side)
 turnBy(90)
 checkwall() 
 forward(0.25,side)
 
def straightline(straisize):
 forward(0.25, straisize*11.2)
 
def sideformula(lev, size):
 try:
  if (lev==0):
   forward(size*0.25, size*4)
  else:
   sideformula(lev-1, size/3)
   turnBy(60)                #turns left by 60 degrees
   checkwall() 
   sideformula(lev-1, size/3)
   turnBy(-120)              
   checkwall() 
   sideformula(lev-1, size/3)
   turnBy(60)
   sideformula(lev-1, size/3)
 except:
  print("Array likely overloaded")


def brokenfractal1(l, siz):
 try:
  sideformula(l, siz)
  checkwall() 
  turnBy(-120) 
  checkwall() 
  sideformula(l, siz)
  turnBy(-120)
  checkwall() 
  sideformula(l, siz) 
 except:
  print("Array likely overloaded")
  #This causing it to go in circles
  
def sideformula2(lev, size):
 try:
  if (lev==0):
   forward(size*0.25, size*4)
  else:
   sideformula(lev-1, size/3)
   turnBy(60)                #turns left by 60 degrees
   sideformula(lev-1, size/3)
   turnBy(-90)              #turns rightby 120     
 except:
  print("Array likely overloaded")

def brokenfractal2(l, siz):
 try:
  sideformula2(l, siz)
  turnBy(-120) 
  sideformula2(l, siz) 
  turnBy(-120)
  sideformula2(l, siz) 
 except:
  print("Array likely overloaded")
  
def sideformula3(lev, size):
 try:
  if (lev==0):
   forward(size*0.25, size*4)
  else:
   sideformula(lev-1, size/2)
   checkwall() 
   turnBy(60)                #turns left by 60 degrees
   sideformula(lev-1, size/3)
   checkwall() 
   turnBy(-120)              #turns rightby 120    
   sideformula(lev-1, size/2)
   checkwall() 
   turnBy(60)
   sideformula(lev-1, size/3)
 except:
  print("Array likely overloaded")

def brokenfractal3(l, siz):
 sideformula3(l, siz)

def flower(radsize):
  radsize=radsize*25.4
  arc(360, radsize)
  checkwall() 
  turnBy(15)
  arc(360, radsize)
  turnBy(15)
  arc(360, radsize)
  turnBy(60)
  arc(360, radsize)
  turnBy(15)
  arc(360, radsize)
  turnBy(15)
  arc(360, radsize)
  checkwall() 
  turnBy(60)
  arc(360, radsize)
  turnBy(15)
  arc(360, radsize)
  turnBy(15)
  arc(360, radsize)
 
def threecirc(radsize):
  radsize=radsize*25.4
  arc(360, radsize)
  turnBy(15)
  checkwall() 
  arc(360, radsize)
  turnBy(15)
  arc(360, radsize)
 
 
def halfcirc(radius):
 conv=radius*25.4
 arc(180, conv)
 
def dot():
 turnBy(360)
 turnBy(-360)
 turnBy(360)
 turnBy(-360)
 
 
##################################################################################################
#4. Wall Avoidance Algorithm
####################################################################################################
#####################################################################################################

def checkwall():
 if(getObstacle('left')>1800 and getObstacle('left')>getObstacle('right')): 
  turnBy(-90)
 if(getObstacle('right')> 1800 and getObstacle('right')>getObstacle('left')):          
  turnBy(90)
 if(getObstacle('center')>1800):															
  turnBy(180) 

 
 
 ###########################################################################################################################
# 5. ###########################################################################################################################
 #################THIS SECTION RUNS ALL THE FUNCTIONS AND THE PROGRAM###########################
#This part will ask or predetermine a number of shapes.
#Then it will call functions to choose colors and draw shapes.

print("Welcome Abstract Automatica 1.0. Be prepared to pick up some markers and paper") 
print("It is suggested that the user lets the program choose its own number of shapes.")
print()
choosenum=int(input("Enter 0 if you'd a prechosen number of shapes or 1 if you'd like to choose your own: "))
if choosenum==0:
 numshapes= randint(8, 12)
else:
 numshapes=int(input("How many shapes would you like??"))
setIRPower(140)
print(numshapes,"shapes will be drawn. Next to choose colors.")
print()
print()

jingleemajor()
choosecolor()
print()
input("\n\nWhen you have the markers ready, press enter.")
xit=0
#variable to work with number of shapes for the while loop below.

while (xit<numshapes):	
 print("Now for shape",xit,".")																		
 try:
   checkwall() 
 except:
  print("Likely an issue with object sensor overload.")
 shaperandomizer()
 if (xit==2 or xit==4 or xit==6 or xit==8 or xit==10 or xit==12):
  markerchange()
 xit=xit+1																			
 																											


print("The robot is finished")
jingleemajor()   ##EE A E B A E
jingleemajor()
jingleamajor()
jingleemajor()
jinglebmajor()
jingleamajor()
jingleemajor()

#Blues chord progression.
