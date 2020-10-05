"""
Senior Design submarine methods for submarine movement
"""
import tkinter
import socket
import os
import serial

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
    def __init__(self, speed):
        self.s = socket.socket()
        self.speed = speed
    
    #A method to check the battery life of the submarine.
    """def batteryLife(self) :
        #battery = system.battery()
        return "Battery is at " + str(self.battery) + " percent."""
    
    #A method to make the submarine move left
    def moveLeft(self):
        #code here
        self.speedUp()
        print('hi 1')

    #A method to make the submarine move right
    def moveRight(self):
        #code here
        self.speedUp()
        print('hi 2')
    
    #A method to make the submarine move forward
    def moveForward(self):
        #code here
        self.speedUp()
        print('hi 3')
    
    #A method to make the submarine move backward
    def moveBackward(self):
        #code here
        self.speedUp()
        print('hi 4')
    
    #A method to make the submarine move up
    def moveUp(self):
        #code here
        self.speedUp()
        print('hi 5')
    
    #A method to make the submarine move down
    def moveDown(self):
        #code here
        self.speedUp()
        print('hi 6')
        
    #a method that changes speed from low, medium and high
    def speedUp(self):
        #low
        if self.speed == 1:
            print('slow')
        #medium
        elif self.speed == 2:
            print('medium')
        #high
        elif self.speed == 3:
            print('fast')

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
         self.stabilieImage = False
     
    #A method to take a photot with the submarine
    def takePhoto(self):
        print('Photo taken')
        
    #a method to record video
    def recordVideo(self):
        print("Recording video")
     
    #a method to display battery life   
    def stabilizeImage(self):
        print('Stabilize Image')
     
    """#a method to turn the sub off    
    def power(self):
        print('power')"""
    
    #a method to maintain depth    
    def depthMaintain(self):
        print('Maintain depth')