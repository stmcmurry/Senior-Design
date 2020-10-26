"""
Senior Design submarine methods for submarine movement and control
"""
import pyautogui
import time
from pynput.mouse import Button, Controller

"""
A program that defines two classes to control the Youcan submarine.
This is meant to be used with scrcpy.
Also use the following commands in the Anaconda command terminal:
    pip install pyautogui
    pip install pynput
"""

#This class controls the basic submarine movements and speed
class subMovement:
    def __init__(self):
        self.speed = "MEDIUM"
    
    #A method to make the submarine move left
    def moveLeft(self, duration):
        pyautogui.moveTo(344,700, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(221, 700, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        backToGUI()

    #A method to make the submarine move right
    def moveRight(self, duration):
        pyautogui.moveTo(344,700, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(481, 700, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        backToGUI()
    
    #A method to make the submarine move forward
    def moveForward(self, duration):
        pyautogui.moveTo(344,700, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(344, 580, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        backToGUI()
    
    #A method to make the submarine move backward
    def moveBackward(self, duration):
        pyautogui.moveTo(344,700, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(344, 850, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        backToGUI()
    
    #A method to make the submarine move up
    def moveUp(self, duration):
        pyautogui.moveTo(1491,775, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(1491, 750, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        backToGUI()
    
    #A method to make the submarine move down
    def moveDown(self, duration):
        pyautogui.moveTo(1491,775, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(1491, 825, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        backToGUI()
        
    #a method that changes speed from low, medium and high
    def speedUp(self, speed):
        pyautogui.click(1231, 875)
        if(speed.upper() == "LOW"):
            mouse = Controller()
            mouse.press(Button.left)
            pyautogui.dragTo(1227, 986, duration=0.3)
            mouse.release(Button.left)
        elif(speed.upper() == "MEDIUM"):
            mouse = Controller()
            mouse.press(Button.left)
            pyautogui.dragTo(1227, 832, duration=0.3)
            mouse.release(Button.left)
        elif(speed.upper() == "HIGH"):
            mouse = Controller()
            mouse.press(Button.left)
            pyautogui.dragTo(1227, 738, duration=0.3)
            mouse.release(Button.left)
        self.speed = speed
        backToGUI()

#A class that controls camera functionalit and lights  
class Camera:
    def __init__(self):
         self.power = True
         self.record = False
         self.picture = False
         self.maintainDepth = False
         self.stableImage = False
     
    #A method to take a photot with the submarine
    def takePhoto(self):
        pyautogui.click(1696, 387)
        backToGUI()
        
    #a method to record video
    def recordVideo(self):
        pyautogui.click(1695, 460)
        backToGUI()
     
    #a method to display battery life   
    def stabilizeImage(self):
        pyautogui.click(1694, 666)
        backToGUI()
     
    #a method to lock the submarine's controls   
    def lock(self):
        pyautogui.click(1638, 114)
        backToGUI()
    #a method to unlock the submarine's controls    
    def unlock(self):
        pyautogui.moveTo(687,533, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(1200, 533, duration=0.5)
        mouse.release(Button.left)
        backToGUI()
    
    #a method to maintain depth    
    def depthMaintain(self):
        pyautogui.click(686, 872)
        backToGUI()
    
    #a method to control the lights from dim, mid and bright
    def lights(self, lights):
        pyautogui.click(564, 877)
        time.sleep(0.3)
        if(lights.upper() == "DIM"):
            pyautogui.click(560,920)
        elif(lights.upper() == "MID"):
            pyautogui.click(560,813)
        elif(lights.upper() == "BRIGHT"):
            pyautogui.click(558,708)
        backToGUI()
        
#a method to return the window to the GUI            
def backToGUI():
    pyautogui.keyDown('alt')
    time.sleep(0.1)
    pyautogui.press('tab')
    time.sleep(0.1)
    pyautogui.keyUp('alt')