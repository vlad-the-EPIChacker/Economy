#imports
import sys
import time
import threading
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
    f=int(array[1])
    print bcolors.HEADER + 'Factor Successfully Changed From '+ str(z) +' to '+ str(f) + bcolors.ENDC

def tmain():
    global shut
    global tm
    global f
    print bcolors.OKBLUE + 'Thread Started' + bcolors.ENDC
    while True:
        time.sleep(f)
        tm=tm+1
        if shut:
            break
    print bcolors.OKBLUE + 'Thread Terminated' + bcolors.ENDC

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
#main
commands={}
#commands['command']=(func, definition)
commands['/help']=(help, "Prints Commands")
commands['/exit']=(exit, "Exits Game")
commands['/time_show']=(show, "Displays Time")
commands['/time_change']=(change, "Decreases or Increases Speed of Time")
t = threading.Thread(target = tmain)
t.start()
while True:
    array=str(raw_input('> ')).split()
    c=array[0]
    if c in commands.keys():
        commands[c][0](array)
    else:
        print bcolors.FAIL + 'ERROR : INVALID COMMAND' + bcolors.ENDC