# https://www.youtube.com/watch?v=zMtGfCMW0Kg

from os import system
import pytesseract
import mouse
import cv2
import pyscreenshot as ImageGrab
from PIL import Image
import os
import matplotlib.pyplot as plt 

oldWords= []
dw = []


def data2Graph(list):
    x = []
    for i in range(len(list)):
        x += [i+1]
    plt.plot(x, list)
    plt.show()    

def image2Str(img1):
    text = pytesseract.image_to_string(img1)
    return text

def screen2Image():
    im = ImageGrab.grab(bbox=(673, 321, 1221, 407))  # X1,Y1,X2,Y2
    #im.save("fullscreen.png")  
    return im

def isClick(oldOrNew): #888 472 / 1000 472    
    if oldOrNew:
        mouse.move(888, 472, absolute=True, duration=0.00001)
    else:
        mouse.move(1000, 472, absolute=True, duration=0.00001)
    mouse.click(button='left')    

def isWordIn(new, list):
    if new not in list:
        return False
    else:
        return True
  
def addWord2List(rd, zeList):
    zeList.append(rd)
    return oldWords
    
def endRound():
    print('Continue? Blank for yes')
    if input() == '':
        return True
    else:
        return False
        
def data2File(list):
    f = open("data.txt", "w+") 
    for i in range(len(list)):
        f.write(str(i+1)+":"+str(list[i])+"\n")


    #######                   

while True:
    max = int(input('How many time: '))
    i = 0
    while True:        
        word = image2Str(screen2Image())
        if isWordIn(word, oldWords):
            isClick(True)
        else:
            oldWords = addWord2List(word, oldWords)
            isClick(False)
        dw.append(len(oldWords))
        if i == max:
            break
        else:
            i += 1
    if endRound():
        continue
    else:
        break
data2File(dw)
data2Graph(dw)
input()
