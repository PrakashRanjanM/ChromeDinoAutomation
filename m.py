import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def isColloid(data):
        for j in range(355,390):
            if data[i,j] < 100:
                hit('down')
                return 
    for i in range(160,190):
        for j in range(392,475):
            if data[i,j] < 100:
    for i in range(130,150):
                hit('up')
                return 
    return False
    
    return image
if __name__ == "__main__":
    print('Starting in 3sec')
    time.sleep(3)   
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isColloid(data)
        '''
        for i in range(150,170):
            for j in range(392,475):
                data[i,j] = 0
        for i in range(130,150):
            for j in range(355,390):
                data[i,j] = 0
        image.show()
        break'''