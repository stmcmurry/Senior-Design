"""
Senior Design submarine methods for submarine movement
"""
import socket
import pyautogui
import time
from pynput.mouse import Button, Controller

"""
Replace functionality of controller with laptop
This includes sub movement,
take photo
stop and start recording
depth maintenance
image stabilization
speed
"""
class subMovement:
    def __init__(self):
        self.s = socket.socket()
    
    #A method to check the battery life of the submarine.
    """def batteryLife(self) :
        #battery = system.battery()
        return "Battery is at " + str(self.battery) + " percent."""
    
    #A method to make the submarine move left
    def moveLeft(self):
        #code here
        pyautogui.moveTo(344,700, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(221, 700, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)

    #A method to make the submarine move right
    def moveRight(self):
        #code here
        pyautogui.moveTo(344,700, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(481, 700, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
    
    #A method to make the submarine move forward
    def moveForward(self):
        #code here
        pyautogui.moveTo(344,700, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(344, 580, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
    
    #A method to make the submarine move backward
    def moveBackward(self):
        #code here
        pyautogui.moveTo(344,700, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(344, 850, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        print('backward')
    
    #A method to make the submarine move up
    def moveUp(self):
        #code here
        pyautogui.moveTo(1491,775, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(1491, 750, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        print('up')
    
    #A method to make the submarine move down
    def moveDown(self):
        #code here
        pyautogui.moveTo(1491,775, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(1491, 825, duration=1.5)
        time.sleep(2)
        mouse.release(Button.left)
        print('down')
        
    #a method that changes speed from low, medium and high
    def speedUp(self, speed):
        #speed = 1231, 875
        #low = 1227, 986
        #med = 1227, 832
        #high = 1220, 738
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
        print('speed')

"""
take photo
stop and start recording
depth maintenance
image stabilization
speed
"""        
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
        print('Photo taken')
        
    #a method to record video
    def recordVideo(self):
        pyautogui.click(1695, 460)
        print("Recording video")
     
    #a method to display battery life   
    def stabilizeImage(self):
        pyautogui.click(1694, 666)
        print('Stabilize Image')
     
    #a method to turn the sub off    
    def lock(self):
        pyautogui.click(1638, 114)
        
    def unlock(self):
        pyautogui.moveTo(687,533, duration = 0)
        mouse = Controller()
        mouse.press(Button.left)
        pyautogui.dragTo(1200, 533, duration=0.5)
        mouse.release(Button.left)
    #a method to maintain depth    
    def depthMaintain(self):
        pyautogui.click(686, 872)
        print('Maintain depth')
    
    #a method to control the lights
    def lights(self, lights):
        #code here
        pyautogui.click(564, 877)
        time.sleep(0.3)
        if(lights.upper() == "DIM"):
            pyautogui.click(560,920)
        elif(lights.upper() == "MID"):
            pyautogui.click(560,813)
        elif(lights.upper() == "BRIGHT"):
            pyautogui.click(558,708)
        print("lights")