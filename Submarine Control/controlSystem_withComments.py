"""
This is the program that should be run in order to control the Youcan submarine.
The file is meant to work in tandem with scrcpy
"""

#python packages to be used
import subMovement #import subMovement.py
import tkinter as tk #python GUI toolkit
from tkinter import ttk

#a method to use the Submit button with the 'enter' key
def onclick(event=None):
    answer = entry.get() #gets input from user for submarine command to do
#if the user decides to do multiple commands at once, the block "command" can be used
#if statement that will look to see if input starts with block
#if input starts with block it will store answer and then split the answer with splitString() method
    
    if answer.upper() == "BLOCK": 
        blockCommand(answer)
    splitString(answer)
    
#a method that splits the input via spaces, adds a 0 to the end of each submarine command
def splitString(answer):
    msg = [0]*2
    print(msg)
    msg = answer.split(' ')
    msg.append('0')
    print(msg)
    switch(msg[0], msg[1])    
    
#a method to display a popup window if the user inputs an unrecognized command
#informs the user that the command is not recognized and to try another command    
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Command Not Recognized")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

#a method that will store user inputs into a list if the user chooses to do so to be split and parsed later
def blockCommand(answer):
    block = []
    block.append(answer)

#a switching method that contains the keywords to control the submarine      
def switch(choice, time):
    if choice.upper() == "LEFT": 
        sub = subMovement.subMovement()
        sub.moveLeft(time) #moves submarine to the left for the alloted amount of time chosen by the user
    
    elif choice.upper() == "RIGHT":
        sub = subMovement.subMovement()
        sub.moveRight(time) #moves submarine to the right for the alloted amount of time chosen by the user
        
    elif choice.upper() == "FORWARD":
        sub = subMovement.subMovement()
        sub.moveForward(time) #moves submarine forward for the alloted amount of time chosen by the user
        
    elif choice.upper() == "BACK":
        sub = subMovement.subMovement()
        sub.moveBackward(time) #moves submarine backwards for the alloted amount of time chosen by the user
        
    elif choice.upper() == "UP":
        sub = subMovement.subMovement()
        sub.moveUp(time) #moves submarine upwards for the alloted amount of time chosen by the user
       
    elif choice.upper() == "DOWN":
        sub = subMovement.subMovement()
        sub.moveDown(time) #moves submarine downwards for the alloted amount of time chosen by the user
        
#records video
#user types in "record" to start video - if video recording wants to be stopped, then user must input "record" again
    elif choice.upper() == "RECORD": 
        sub = subMovement.Camera() 
        sub.recordVideo()
#takes a photo through the submarine's vision        
    elif choice.upper() == "PICTURE" or "PHOTO":
        sub = subMovement.Camera()
        sub.takePhoto()
#allows the camera to focus        
    elif choice.upper() == "STABLE":
        sub = subMovement.Camera()
        sub.stabilizeImage()
#tells the submarine to maintain a certain depth when submerged into the water       
    elif choice.upper() == "DEPTH":
        sub = subMovement.Camera()
        sub.depthMaintain()    
#changes the speed of the submarine based on 3 options - low, medium, and high       
    elif choice.upper() == "LOW":
        sub = subMovement.subMovement()
        sub.speedUp(choice)
        
    elif choice.upper() == "MEDIUM":
        sub = subMovement.subMovement()
        sub.speedUp(choice)
        
    elif choice.upper() == "HIGH":
        sub = subMovement.subMovement()
        sub.speedUp(choice)
#lock allows for the submarine motors to be shut off        
    elif choice.upper() == "LOCK":
        sub = subMovement.Camera()
        sub.lock()
#unlocks the submarine to be ready for use        
    elif choice.upper() == "UNLOCK":
        sub = subMovement.Camera()
        sub.unlock()
#changes the brightness of the camera based on 3 options - dim, mid, and bright      
    elif choice.upper() == "DIM":
        sub = subMovement.Camera()
        sub.lights(choice)
        
    elif choice.upper() == "MID":
        sub = subMovement.Camera()
        sub.lights(choice)
        
    elif choice.upper() == "BRIGHT":
        sub = subMovement.Camera()
        sub.lights(choice)
#tells user the command they input does not exist        
    else:
        popupmsg("The command you selected does not exist. Please try another command.")
#GUI set up using Python TKINTER package        
top = tk.Tk()
camera = subMovement.Camera()

top.bind('<Return>', onclick)

bwidth = 22
bheight = 3

title = tk.Label(text = "Submarine Control System")

#entry widget to input command words
entry = tk.Entry(top,
                 bg = "white")
#button for submitting a command
submit = tk.Button(
    text = "Submit",
    width = 10,
    height = 2,
    bg = "black",
    fg = "white",
    command = onclick
)

title.pack()
submit.pack(side = tk.BOTTOM)
entry.pack(side = tk.BOTTOM)

top.mainloop()