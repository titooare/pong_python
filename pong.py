from sense_hat import SenseHat

from time import sleep

sense=SenseHat()

sense.clear()

# initialisation du demarage du jeu
x = 2
y = 5
x_sens = 1
y_sens = 1

def balle():
  global x, y, x_sens, y_sens
  x = x + x_sens
  y = y + y_sens
  sense.set_pixel(x, y, 255, 0, 0)
 
  if x == 0:
    x_sens = 1
 
  if x == 7:
    x_sens = -1
  if y == 7:
    y_sens = -1
  elif y == 0:
    y_sens = 1
    
          
        
          
  
while True:
  sense.clear()
  balle()
  sleep(0.10)
 
