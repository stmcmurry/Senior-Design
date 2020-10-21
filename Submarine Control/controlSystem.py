"""
This is the progrom that should be run in order to control the Youcan submarine.
The file is meant to work in tandem with scrcpy
"""

import subMovement
import tkinter as tk
from tkinter import ttk

#a method to use the Submit button with the 'enter' key
def onclick(event=None):
    answer = entry.get()
    switch(answer)
     
#a method to display a popup windo if the user inputs an unrecognized command    
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Command Not Recognized")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

#a switching method that contains the keywords to control the submarine      
def switch(choice):
    if choice.upper() == "LEFT":
        sub = subMovement.subMovement()
        sub.moveLeft()
    
    elif choice.upper() == "RIGHT":
        sub = subMovement.subMovement()
        sub.moveRight()
        
    elif choice.upper() == "FORWARD":
        sub = subMovement.subMovement()
        sub.moveForward()
        
    elif choice.upper() == "BACKWARD":
        sub = subMovement.subMovement()
        sub.moveBackward()
        
    elif choice.upper() == "UP":
        sub = subMovement.subMovement()
        sub.moveUp()
       
    elif choice.upper() == "DOWN":
        sub = subMovement.subMovement()
        sub.moveDown()
        
    elif choice.upper() == "RECORD":
        sub = subMovement.Camera()
        sub.recordVideo()
        
    elif choice.upper() == "PICTURE":
        sub = subMovement.Camera()
        sub.takePhoto()
        
    elif choice.upper() == "STABLE":
        sub = subMovement.Camera()
        sub.stabilizeImage()
        
    elif choice.upper() == "DEPTH":
        sub = subMovement.Camera()
        sub.depthMaintain()
        
    elif choice.upper() == "LOW":
        sub = subMovement.subMovement()
        sub.speedUp(choice)
        
    elif choice.upper() == "MEDIUM":
        sub = subMovement.subMovement()
        sub.speedUp(choice)
        
    elif choice.upper() == "HIGH":
        sub = subMovement.subMovement()
        sub.speedUp(choice)
        
    elif choice.upper() == "LOCK":
        sub = subMovement.Camera()
        sub.lock()
        
    elif choice.upper() == "UNLOCK":
        sub = subMovement.Camera()
        sub.unlock()
        
    elif choice.upper() == "DIM":
        sub = subMovement.Camera()
        sub.lights(choice)
        
    elif choice.upper() == "MID":
        sub = subMovement.Camera()
        sub.lights(choice)
        
    elif choice.upper() == "BRIGHT":
        sub = subMovement.Camera()
        sub.lights(choice)
        
    else:
        popupmsg("The command you selected does not exist. Please try another command.")
        
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
