from tkinter import*
HEIGHT = 500
WIDTH = 800
window.title('Bubble Blaster')
c = Canvas(window.title('Bubble Blaster')
c.pack()
ship_id = c.create_polygon(5,5,5,25,30,15, fill='red')
ship_id2 = c.create_oval(0,0,30,30,outline='red')
SHIP_R = 5
MID_X = WIDTH / 2
MID_Y=HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
SHIP_SPD = 10
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, ship_SPD)
    elif event.keysym == 'Down':
           c.move(ship_id, 0, SHIP_SPD)
           c.move(ship_id2, 0, SHIP_SPD)
    elif event.keysym == 'Left':
           c.move(ship_id,-SHIP_SPD,0)
           c.move(ship_id2,-SHIP_SPD,0)
     elif event.keysym == 'Right':
           c.move(ship_id, SHIP_SPD, 0)
           c.move(ship_id2,SHIP_SPD,0)
c.bind_all('<Key>', move_ship
from random import randint
bub_id = list()
bub_r = list()
bub_speed=list()
MIN_BUB_SPD = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100
def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 + c.create_oval(x-r,y-r,x+r,y+r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))
def move_bubbles():
    for i in range(len(bub_id)):
      c.move(bub_id[i], -bub_speed[i],0)
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x,y
    
