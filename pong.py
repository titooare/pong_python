from sense_hat import SenseHat

from time import sleep

sense=SenseHat()

sense.clear()

x = 0

y = 0

while x >0 and y >0 or x < 7 and y < 7:

  while x < 7 and y < 7 :
    x = x + 1
    y = y + 1
  
 
  
  
    sense.clear()
    sense.set_pixel(x, y, 255, 0, 0)
    sleep(0.10)
  
  

  while x >0 and y >0:
    x = x - 1
    y = y - 1
  
 
  
  
    sense.clear()
    sense.set_pixel(x, y, 255, 0, 0)
    sleep(0.10)
