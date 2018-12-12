from sense_hat import SenseHat

from time import sleep

sense=SenseHat()

sense.clear()

# initialisation du demarage du jeu
x = 2
y = 5
x_sens = 1
y_sens = 1



paddle_y = 1
paddle_x = 1

x2 = 0
y2 = 1





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
    


def update_screen():
    
    sense.set_pixel(x2, y2, 255, 255, 255)
    sense.set_pixel(x2, y2+1, 255, 255, 255)
    sense.set_pixel(x2, y2+2, 255, 255, 255)

def clamp(value, min_value=0, max_value=5):
    return min(max_value, max(min_value, value))

def move_dot(event):
    global x2, y2
    if event.action in ('pressed', 'held'):

        y2 = clamp(y2 + {
            'up': -1,
            'down': 1,
            }.get(event.direction, 0))



  
        
          
  
while True:
  

  sense.clear()
  update_screen()
  sense.stick.direction_up = move_dot
  sense.stick.direction_down = move_dot
  sense.stick.direction_any = update_screen
  balle()
  sleep(0.10)
  
 
