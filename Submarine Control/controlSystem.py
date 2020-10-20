# -*- coding: utf-8 -*-

import subMovement
try:  # import as appropriate for 2.x vs. 3.x    
    import tkinter as tk 
except:    
    import Tkinter as tk 

def onclick(event=None):
    print("You clicked the button")
    answer = entry.get()
    switch(answer)
    #main()


"""def main():
    #while True:
        answer = entry.get()
        switch(answer)"""
        
def switch(choice):
    if choice.upper() == "LEFT":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement()
        sub.moveLeft()
        #main()
    elif choice.upper() == "RIGHT":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement()
        sub.moveRight()
        #main()
    elif choice.upper() == "FORWARD":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement()
        sub.moveForward()
        #main()
    elif choice.upper() == "BACKWARD":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement()
        sub.moveBackward()
        #main()
    elif choice.upper() == "UP":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement()
        sub.moveUp()
       # main()
    elif choice.upper() == "DOWN":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
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
        print("The command you selected does not exist. Please try another command.")

#main is where GUI will be developed
#def GUI():
top = tk.Tk()
camera = subMovement.Camera()

top.bind('<Return>', onclick)

bwidth = 22
bheight = 3
#cameraIcon = tk.PhotoImage(file = r"C:\Users\stmcm\OneDrive\Documents\Senior Design\Python Scripts\images\camera-512.png")
#depthIcon = tk.PhotoImage(file = r"C:\Users\stmcm\OneDrive\Documents\Senior Design\Python Scripts\images\depth.png")
#recordIcon
#stabilizeIcon
#depthIcon

title = tk.Label(text = "Submarine Control System")

entry = tk.Entry(top,
                 bg = "white")

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
#scale.pack(side = tk.RIGHT)

top.mainloop()
