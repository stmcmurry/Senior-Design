# -*- coding: utf-8 -*-

import subMovement
import os
try:  # import as appropriate for 2.x vs. 3.x    
    import tkinter as tk 
except:    
    import Tkinter as tk 

def main():
    #while True:
        answer = entry.get()
        getSpeed(answer)
        #choice = input('What would you like the submarine to do: ')
        
def getSpeed(answer):
    speed = scale.get()
    switch(answer, speed)
       
#switching algorithm to choose command
def switch(choice, speed):
    """if choice.upper() == "BATTERY LIFE":
        sub = subMovement.subMovement(15, "medium")
        print(sub.batteryLife())
        #main()"""
    if choice.upper() == "MOVE LEFT":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(speed)
        sub.moveLeft()
        #main()
    elif choice.upper() == "MOVE RIGHT":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(speed)
        sub.moveRight()
        #main()
    elif choice.upper() == "MOVE FORWARD":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(speed)
        sub.moveForward()
        #main()
    elif choice.upper() == "MOVE BACKWARD":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(speed)
        sub.moveBackward()
        #main()
    elif choice.upper() == "MOVE UP":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(speed)
        sub.moveUp()
       # main()
    elif choice.upper() == "MOVE DOWN":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(speed)
        sub.moveDown()
        #main()
    elif choice.upper() == "EXIT":
        print("Have a nice day.")
    else:
        print("The command you selected does not exist. Please try another command.")

#main is where GUI will be developed
#def GUI():
top = tk.Tk()
camera = subMovement.Camera()

bwidth = 22
bheight = 3
cameraIcon = tk.PhotoImage(file = r"C:\Users\stmcm\OneDrive\Documents\Senior Design\Python Scripts\images\camera-512.png")
#recordIcon
#stabilizeIcon
#depthIcon

title = tk.Label(text = "Submarine Control System")
"""stream = tk.Label(
    text="Video Stream",
    fg="white",
    bg="black",
    width=100,
    height=30
)"""
record = tk.Button(
    text="Record Video",
    width=bwidth,
    height=bheight,
    bg="gray",
    fg="white",
    command = camera.recordVideo
)
picture = tk.Button(
    text="Take Picture",
    width=bwidth,
    height=bheight,
    bg="gray",
    fg="white",
    #image = cameraIcon,
    #compound = tk.TOP,
    command = camera.takePhoto
)
battery = tk.Button(
    text="Stabilize Image",
    width=bwidth,
    height=bheight,
    bg="gray",
    fg="white",
    command = camera.stabilizeImage
)
power = tk.Button(
    text="Maintain Depth",
    width=bwidth,
    height=bheight,
    bg="gray",
    fg="white",
    command = camera.depthMaintain
)
entry = tk.Entry(top,
                 bg = "white")
submit = tk.Button(
    text = "Submit",
    width = 10,
    height = 2,
    bg = "black",
    fg = "white",
    command = main
)
scale = tk.Scale(
    label = 'speed',
    from_ = 3,
    to_ = 1,
    orient = tk.VERTICAL
)

title.pack()
record.pack(side = tk.TOP)
picture.pack(side = tk.TOP)
battery.pack(side = tk.TOP)
power.pack(side = tk.TOP)
submit.pack(side = tk.BOTTOM)
entry.pack(side = tk.BOTTOM)
scale.pack(side = tk.RIGHT)

top.mainloop()
