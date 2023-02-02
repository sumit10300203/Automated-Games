import pyautogui
from PIL import Image,ImageGrab
import time
import keyboard
import win32api, win32con
#(x=618, y=498) x=618, y=718 x=752, y=498 
#print(pyautogui.position())
time.sleep(3)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(242,321)[0]<30:
        click(237,460)
    elif pyautogui.pixel(405,321)[0]<30:
        click(406,458)
    elif pyautogui.pixel(560,321)[0]<30:
        click(561,456)
    elif pyautogui.pixel(733,321)[0]<30:
        click(713,446)

