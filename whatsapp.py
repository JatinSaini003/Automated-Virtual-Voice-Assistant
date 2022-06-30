from pyautogui import *
from time import sleep
import keyboard as kb


def message (name, msg):
    i=0
    click(x=473, y=141)  #clicks on search bar
    for a in range(25):
        kb.press('BACKSPACE')
    kb.release('BACKSPACE')
    write(name)
    sleep(3)
    click(x=242, y=301)  # clicks on first search result
    click(x=985, y=990)  # clicks on message bar

    while i<1:
        write(msg)
        press("Enter")
        i+=1
        sleep(1)

def voice_call(name):
    click(x=473, y=141)  #clicks on search bar
    kb.press_and_release('CTRL + A')
    kb.press_and_release('BACKSPACE')
    write(name)
    sleep(3)
    click(x=242, y=301)  # clicks on first search result
    sleep(1)
    click(x=1720, y=70)  # voice call

def video_call(name):
    click(x=473, y=141)  #clicks on search bar
    for a in range(25):
        kb.press('BACKSPACE')
    kb.release('BACKSPACE')
    write(name)
    sleep(3)
    click(x=242, y=301)  # clicks on first search result
    sleep(1)
    click(x=1640, y=80)  # video call

def open_chat(name):
    click(x=473, y=141)  #clicks on search bar
    for a in range(25):
        kb.press('BACKSPACE')
    kb.release('BACKSPACE')
    write(name)
    sleep(3)
    click(x=242, y=301)  # clicks on first search result
    sleep(1)

def write_msg(msg):
    click(x=985, y=990)  # clicks on message bar
    write(msg)

def send():
    press('Enter')

def change_line():
    kb.press_and_release('Shift + Enter')

def del_msg():
    kb.press_and_release('CTRL + A')
    kb.press_and_release('BACKSPACE')

def del_word():
    kb.press_and_release('CTRL + BACKSPACE')





 
    