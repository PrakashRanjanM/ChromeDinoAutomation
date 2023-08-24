import pyautogui
from PIL import Image, ImageGrab
import time
def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(190,310):
        for j in range(435,470):
            if data[i,j] < 100:
                return True
    return False

if __name__=="__main__":
    print("Hey .... Dino game is about to start in three sec")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if isCollide(data):
            hit('up')
        # for i in range(300,415):
        #     for j in range(600,650):
        #         data[i,j] = 0
        