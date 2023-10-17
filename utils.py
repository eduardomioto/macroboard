import os
from constants import LINUX_OS
import pyautogui

def increase_volume():
    os.system('amixer sset Master 5%+')
    
def reduce_volume():
    os.system('amixer sset Master 5%-')

def move_workspace_forward():
    pyautogui.hotkey('ctrl', 'alt', 'right')    

def move_workspace_backward():
    pyautogui.hotkey('ctrl', 'alt', 'left')

def mute_microphone():
    os.popen('amixer set Capture nocap').read()

def unmute_microphone():
    os.popen('amixer set Capture cap').read()