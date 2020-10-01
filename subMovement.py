"""
Senior Design submarine methods for submarine movement
"""
import tkinter
#import socket
import os

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
    def __init__(self, battery):
        #self.s = socket.socket()
        self.battery = battery
    
    #A method to check the battery life of the submarine.
    def batteryLife(self) :
        #battery = system.battery()
        return "Battery is at " + str(self.battery) + " percent."
    
    #A method to make the submarine move left
    def moveLeft(self):
        #code here
        print('hi 1')
    
    #A method to make the submarine move right
    def moveRight(self):
        #code here
        print('hi 2')
    
    #A method to make the submarine move forward
    def moveForward(self):
        #code here
        print('hi 3')
    
    #A method to make the submarine move backward
    def moveBackward(self):
        #code here
        print('hi 4')
    
    #A method to make the submarine move up
    def moveUp(self):
        #code here
        print('hi 5')
    
    #A method to make the submarine move down
    def moveDown(self):
        #code here
        print('hi 6')
        
class Camera:
    def __init__(self):
         self.power = True
         self.record = False
         self.picture = False
         self.battery = False
         self.speed = 2
     
    #A method to take a photot with the submarine
    def takePhoto(self):
        print('photo taken')
      
    #a method to zoom in with camera    
    def zoom(self):
        print('zoom')
        
    #a method to record video
    def record(self):
        print('video recording')
     
    #a method to display battery life   
    def batteryDisplay(self):
        print('battery display')
     
    #a method to turn the sub off    
    def power(self):
        print('power')
        
    #a method that changes speed from low, medium and high
    def speed(self, speed):
        #low
        if speed == 1:
            self.speed = 1
        #medium
        elif speed == 2:
            self.speed = 2
        #high
        elif speed == 3:
            self.speed = 3