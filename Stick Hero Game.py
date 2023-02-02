import pyautogui
import time
from PIL import Image,ImageGrab
import keyboard
import win32api, win32con
def click(temp,temp3,linelen):
    temp4=(1/580)*(linelen)
    win32api.SetCursorPos((730,634))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(temp4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q') == False:
    temp=0
    temp2=0
    time.sleep(3)
    for i in range(730,634,-1):
        if pyautogui.pixel(i,632)[0]==227:
            temp=i
            break 
    for i in range(temp+10,1226):
        if pyautogui.pixel(i,673)[0]==253:
            temp2=i
            break
    linelen=temp2-(temp+10)
    temp3=673-linelen
    
    click(temp,temp3,linelen)
'''
temp=0
temp2=0
temp3=0
time.sleep(3)
for i in range(730,634,-1):
    if pyautogui.pixel(i,632)[0]==227:
        temp=i
        break 
for i in range(temp+10,1226):
    if pyautogui.pixel(i,673)[0]==253:
        temp2=i
        break
linelen=temp2-(temp+10)
temp3=673-linelen
print(linelen)
print(temp,temp2,temp3)
image=ImageGrab.grab().convert('L')
data=image.load()
for j in range(673,temp3,-1):
    data[temp+10,j]=300
image.show()
#'''
