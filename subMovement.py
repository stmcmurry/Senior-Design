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
    def __init__(self, battery):
        #self.s = socket.socket()
        self.battery = battery
    
    #A method to check the battery life of the submarine.
    def batteryLife(self) :
        #battery = system.battery()
        return self.battery
    
    def moveLeft(self):
        #code here
        print('hi 1')
    
    def moveRight(self):
        #code here
        print('hi 2')
    
    def moveForward(self):
        #code here
        print('hi 3')
    
    def moveBackward(self):
        #code here
        print('hi 4')
    
    def moveUp(self):
        #code here
        print('hi 5')
    
    def moveDown(self):
        #code here
        print('hi 6')