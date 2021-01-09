import pyautogui
from PIL import Image,ImageGrab
import time

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image

def draw(data):
    for i in range(300,375):
        for j in range(560,662):
            data[i,j] = 0
    return data

def isCollide(data):
    for i in range(320,477):
        for j in range(560,662):
            if data[i,j] >= 83 and data[i,j] <= 150:
                return True
    return False

if __name__ == "__main__":
    time.sleep(3)
    pyautogui.press("space")
    '''while True:
        image = takeScreenshot()
        data = image.load()
        if isCollide(data):
            pyautogui.press("space")'''
    image = takeScreenshot()
    data = image.load()
    draw(data)
    image.show()