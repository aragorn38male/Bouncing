from machine import LCD, Sprite, Map, Pin
import sys
import time
import math
import random

lcd = LCD()

n=100
balls=[[]]*n
for _ in range(n):
    balls[_]=[random.randint(0,317),10+random.randint(5,238),random.randint(-5,5),random.randint(-5,5)]

def generator():
    balls=[[]]*n
    for _ in range(n):
        balls[_]=[random.randint(0,317),10+random.randint(5,238),random.randint(-5,5),random.randint(-5,5)]
    return balls

gravity=.1

STICK_LEFT = Pin(Map.WIO_5S_LEFT, Pin.IN)
STICK_RIGHT = Pin(Map.WIO_5S_RIGHT, Pin.IN)
STICK_UP = Pin(Map.WIO_5S_UP, Pin.IN)
STICK_DOWN = Pin(61, Pin.IN)
FIRE_BUTTON = Pin(Map.WIO_KEY_C, Pin.IN)
START_BUTTON = Pin(Map.WIO_KEY_B, Pin.IN)
HALT_BUTTON = Pin(Map.WIO_KEY_A, Pin.IN)

def draw(x,y):
    lcd.drawPixel(x, y, 0x07E0)

def erase(x,y):
    lcd.drawPixel(x, y, 0x0)

def main_loop():
    global n, gravity
    lcd.fillScreen(lcd.color.BLACK)
    c=0
    balls=generator()

    while True:
        for _ in range(n):
            erase(balls[_][0],balls[_][1])
            balls[_][3]+=gravity
            balls[_][3]=math.ceil(balls[_][3])
            balls[_][0]+=balls[_][2]
            balls[_][1]+=balls[_][3]

            if balls[_][0] >= 317:
                balls[_][0] = 317
                balls[_][2]*=-1
            if balls[_][1] >= 238:
                balls[_][1] = 238
                balls[_][3]*=-1
            if balls[_][0] <= 0:
                balls[_][0] = 0
                balls[_][2]*=-1

            if balls[_][1] <= 0:
                balls[_][1] = 0
                balls[_][3]*=-1

            if balls[_][3] == -1 and balls[_][1] == 238:
                    balls[_][2]=0
                    c+=1
            if c>15000:
                time.sleep(1)
                main_loop()


            draw(balls[_][0],balls[_][1])
        #time.sleep(0.005)

        if HALT_BUTTON.value() == 0:
            main_loop()

main_loop()