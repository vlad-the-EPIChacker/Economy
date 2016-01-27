#imports
import sys
import time
import threading
import pygame
import colors
from pygame.locals import *

#global
shut=False
tm=0
f=0.1
output=''
lbuffer=3
buffer=[None]*lbuffer
index=0
#functions
def buffer_print():
    for i in range(0, lbuffer):
        print buffer[(index+i)%lbuffer]
def buffer_add(s):
    global buffer, index
    buffer[index%lbuffer]=s
    index += 1
    buffer_print()
def help(array):
    for key in commands.keys():
        print key ,':', commands[key][1]

def exit(array):
    global shut
    shut=True
    print colors.bcolors.OKBLUE + 'Exited Safely' + colors.bcolors.ENDC
    sys.exit()

def watch(array):
    hour=int(tm/5)
    day=hour/24
    year=day/365
    curhour=hour%24
    curday=day%365
    return str(year)+':'+str(curday)+':'+str(curhour)

def change(array):
    global f
    z=f
    f=float(array[1])
    print colors.bcolors.HEADER + 'Factor Successfully Changed From '+ str(z) +' to '+ str(f) + colors.bcolors.ENDC

def tmain():
    global tm
    global f
    print colors.bcolors.OKBLUE + 'Thread Main Started' + colors.bcolors.ENDC
    while not shut:
        time.sleep(f)
        tm=tm+1
    print colors.bcolors.OKBLUE + 'Thread Main Terminated' + colors.bcolors.ENDC

def open_window():
    global shut
    prompt='>'
    inpt=''
    (width, height) = (1300, 800)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    inptfont = pygame.font.SysFont("Menlo Regular", 50)
    timefont = pygame.font.SysFont("Menlo Regular", 26)
    while not shut:
        time.sleep(1./60.)
        screen.fill(colors.simple_color.black)
        #pygame.clock.tick(20)
        label = timefont.render(watch(None), 0, colors.simple_color.green)
        screen.blit(label, (0, 0))
        label = inptfont.render(prompt, 0, colors.simple_color.green)
        screen.blit(label, (0, 710))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shut=True
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(prompt) == 1:
                        prompt='>'
                    else:
                        prompt=prompt[:-1]
                elif event.key == SYSWMEVENT:
                    inpt=prompt[1:]
                    buffer_add(inpt)
                    prompt='>'
                else:
                    prompt=prompt+chr(event.key)

def input_thread():
    print colors.bcolors.OKBLUE + 'Thread Input Started' + colors.bcolors.ENDC
    while not shut:
        array=str(raw_input('> ')).split()
        c=array[0]
        if c in commands.keys():
            commands[c][0](array)
        else:
            print colors.bcolors.FAIL + 'ERROR : INVALID COMMAND' + colors.bcolors.ENDC
    print colors.bcolors.OKBLUE + 'Thread Input Terminated' + colors.bcolors.ENDC
#definitions

#main
commands={}
#commands['command']=(func, definition)
commands['/help']=(help, "Prints Commands")
commands['/exit']=(exit, "Exits Game")
commands['/time_change']=(change, "Decreases or Increases Speed of Time")

t = threading.Thread(target = tmain)
t.setDaemon(True)
t.start()

pygame.init()

t1 = threading.Thread(target = input_thread)
t1.setDaemon(True)
t1.start()

open_window()