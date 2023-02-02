import pyautogui
from PIL import Image,ImageGrab
import time
#x=459, y=729 ,x=570, y=716       x=468, y=999   (FACEBOOK CRICKET x=455, y=930)
#print(pyautogui.position())

def got(data):
    for i in range(415,600):
        for j in range(645,730):
            if data[i,j]<120:        #for checking balls
                pyautogui.click(x=468,y=999)
                return
    return 
time.sleep(3)
while True:
    image=ImageGrab.grab().convert('L')
    data=image.load()
    got(data)
'''
time.sleep(1)
image=ImageGrab.grab().convert('L')
data=image.load()
for i in range(415,600):
    for j in range(645,730):
        data[i,j]=120
image.show()
#break'''

