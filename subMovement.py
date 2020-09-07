"""
Senior Design submarine methods for submarine movement
"""
import tkinter
#import socket
import os

"""
Provide controls to go left, right, up, down, forward and backward
Tell the camera to take photos, start and stop recording, 
    control the movements and shooting of the camera, 
    and set the resolution of the video recording
Adjust the camera’s effects
Display all of the battery’s information
Go low, medium and high speeds
Maintain and calibrate its depth
Control the light’s brightness and provide auto-light adjustment

"""
class subMovement:
    def __init__(self, battery, speed):
        #self.s = socket.socket()
        self.battery = battery
        self.speed = speed
    
    #A method to check the battery life of the submarine.
    def batteryLife(self) :
        #battery = system.battery()
        return "Battery is at " + str(self.battery) + " percent."
    
    #A method to make the submarine move left
    def moveLeft(self):
        #code here
        if self.speed.upper() == "LOW":
            print('low speed')
        elif self.speed.upper() == "MEDIUM":
            print('medium speed')
        elif self.speed.upper() == "HIGH":
            print('high speed')
        print('hi 1')
    
    #A method to make the submarine move right
    def moveRight(self):
        #code here
        if self.speed.upper() == "LOW":
            print('low speed')
        elif self.speed.upper() == "MEDIUM":
            print('medium speed')
        elif self.speed.upper() == "HIGH":
            print('high speed')
        print('hi 2')
    
    #A method to make the submarine move forward
    def moveForward(self):
        #code here
        if self.speed.upper() == "LOW":
            print('low speed')
        elif self.speed.upper() == "MEDIUM":
            print('medium speed')
        elif self.speed.upper() == "HIGH":
            print('high speed')
        print('hi 3')
    
    #A method to make the submarine move backward
    def moveBackward(self):
        #code here
        if self.speed.upper() == "LOW":
            print('low speed')
        elif self.speed.upper() == "MEDIUM":
            print('medium speed')
        elif self.speed.upper() == "HIGH":
            print('high speed')
        print('hi 4')
    
    #A method to make the submarine move up
    def moveUp(self):
        #code here
        if self.speed.upper() == "LOW":
            print('low speed')
        elif self.speed.upper() == "MEDIUM":
            print('medium speed')
        elif self.speed.upper() == "HIGH":
            print('high speed')
        print('hi 5')
    
    #A method to make the submarine move down
    def moveDown(self):
        #code here
        if self.speed.upper() == "LOW":
            print('low speed')
        elif self.speed.upper() == "MEDIUM":
            print('medium speed')
        elif self.speed.upper() == "HIGH":
            print('high speed')
        print('hi 6')
        
class Camera:
    def __init__(self, zoom):
         self.zoom = zoom
     
    #A method to take a photot with the submarine
    def takePhoto(self):
        print('photo taken')
      
    #a method to zoom in with camera    
    def zoom(self):
        print('zoom')
        
    #a method to record video
    def record(self):
        print('record')