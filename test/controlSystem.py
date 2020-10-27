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
    splitString(answer)
    
#a method to get a value for how long the sub moves
def splitString(answer):
    if ',' in answer:
        blockCommand(answer)
    else:
        msg = [0]*2
        print(msg)
        msg = answer.split(' ')
        msg.append('0')
        print(msg)
        switch(msg[0], msg[1])    
    
#a method to display a popup window if the user inputs an unrecognized command    
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Command Not Recognized")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

#a method to take in multpile instructions
def blockCommand(answer):
    block = answer.split(' ')
    
    for i in range(len(block)):
        if ',' in block[i]:
            block[i] = block[i].replace(",", "")
            
    for j in range(len(block)):
        if block[j].isnumeric() or block[j+1].isnumeric():
            continue
        else:
            block.insert(j+1, "0")
    block.append("0")      
    """if len(block) % 2 != 0:
        block.append("0")
        for k in range(len(block)):
            if k % 2 == 1:
                switch(block[k-1], block[k])
            else:
                continue
            """
    print(block)
    #if len(block) % 2 == 0:
    for k in range(len(block)):
        if (block[k].isnumeric() == False) and (block[k+1].isnumeric() == True):
            switch(block[k], block[k+1])
            print(block[k], block[k+1])
    
#a switching method that contains the keywords to control the submarine      
def switch(choice, time):
    if choice.upper() == "LEFT":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveLeft(time)
    
    elif choice.upper() == "RIGHT":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveRight(time)
        
    elif choice.upper() == "BACK":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveBackward(time)
        
    elif choice.upper() == "FORWARD":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveForward(time)
        
    elif choice.upper() == "UP":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveUp(time)
       
    elif choice.upper() == "DOWN":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveDown(time)
        
    elif choice.upper() == "RECORD":
        sub = subMovement.Camera()
        sub.recordVideo()
        
    elif choice.upper() == "PICTURE" or "PHOTO":
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
