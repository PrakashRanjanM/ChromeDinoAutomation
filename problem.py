import pyautogui

def hitkey(key):
    pyautogui.keyDown(key)



if __name__== "__main__":
    while pyautogui.keyDown('up'):
        hitkey('backspace')
