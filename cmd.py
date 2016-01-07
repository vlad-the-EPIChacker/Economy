#imports
import sys
import time
import threading
import pygame


#global
shut=False
tm=0
f=1
#functions
def help(array):
    for key in commands.keys():
        print key ,':', commands[key][1]

def exit(array):
    global shut
    shut=True
    print bcolors.OKBLUE + 'Exited Safely' + bcolors.ENDC
    sys.exit()

def show(array):
    hour=int(tm/5)
    day=hour/24
    year=day/365
    curhour=hour%24
    curday=day%365
    print year, ':', curday, ':', curhour

def change(array):
    global f
    z=f
    f=float(array[1])
    print bcolors.HEADER + 'Factor Successfully Changed From '+ str(z) +' to '+ str(f) + bcolors.ENDC

def tmain():
    global tm
    global f
    print bcolors.OKBLUE + 'Thread Main Started' + bcolors.ENDC
    while not shut:
        time.sleep(f)
        tm=tm+1
    print bcolors.OKBLUE + 'Thread Main Terminated' + bcolors.ENDC

def open_window():
    global shut
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    while not shut:
        #pygame.clock.tick(20)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shut=True
                pygame.quit()
                sys.exit()

def input_thread():
    print bcolors.OKBLUE + 'Thread Input Started' + bcolors.ENDC
    while not shut:
        array=str(raw_input('> ')).split()
        c=array[0]
        if c in commands.keys():
            commands[c][0](array)
        else:
            print bcolors.FAIL + 'ERROR : INVALID COMMAND' + bcolors.ENDC
    print bcolors.OKBLUE + 'Thread Input Terminated' + bcolors.ENDC
#definitions
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class simple_color:
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    darkBlue = (0,0,128)
    white = (255,255,255)
    black = (0,0,0)
    pink = (255,200,200)

#main
commands={}
#commands['command']=(func, definition)
commands['/help']=(help, "Prints Commands")
commands['/exit']=(exit, "Exits Game")
commands['/time_show']=(show, "Displays Time")
commands['/time_change']=(change, "Decreases or Increases Speed of Time")

t = threading.Thread(target = tmain)
t.setDaemon(True)
t.start()

pygame.init()

t1 = threading.Thread(target = input_thread)
t1.setDaemon(True)
t1.start()

open_window()