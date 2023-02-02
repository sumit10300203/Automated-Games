#Student no:-785469
#Name-$umit

#Topic-Automate Dino Game
import pyautogui
from PIL import Image,ImageGrab
import time
#x=185
#print(pyautogui.position())
#280 420 563 650
#
def got(data):
    for i in range(145 , 300):
        for j in range(395, 445):
            if data[i,j]<100:        #for checking cactus and birds
                pyautogui.keyDown("space")
                return
    return 
time.sleep(3)
while True:
    image=ImageGrab.grab().convert('L')
    data=image.load()
    got(data)
    '''
time.sleep(3)
image=ImageGrab.grab().convert('L')
data=image.load()
for i in range(174,300):
    for j in range(400,445):
        data[i,j]=163
image.show()
#break'''
                  
