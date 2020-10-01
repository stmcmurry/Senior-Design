# -*- coding: utf-8 -*-
"""


"""
import subMovement
import os
import tkinter as tk


def main():
    #while True:
        answer = entry.get()
        #choice = input('What would you like the submarine to do: ')
        switch(answer)
       
#switching algorithm to choose command
def switch(choice):
    if choice.upper() == "BATTERY LIFE":
        sub = subMovement.subMovement(15, "medium")
        print(sub.batteryLife())
        #main()
    elif choice.upper() == "MOVE LEFT":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15)
        sub.moveLeft()
        #main()
    elif choice.upper() == "MOVE RIGHT":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15)
        sub.moveRight()
        #main()
    elif choice.upper() == "MOVE FORWARD":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15)
        sub.moveForward()
        #main()
    elif choice.upper() == "MOVE BACKWARD":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15)
        sub.moveBackward()
        #main()
    elif choice.upper() == "MOVE UP":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15)
        sub.moveUp()
       # main()
    elif choice.upper() == "MOVE DOWN":
        #speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15)
        sub.moveDown()
        #main()
    elif choice.upper() == "EXIT":
        print("Have a nice day.")
    else:
        print("The command you selected does not exist. Please try another command.")
        #main()
#main is where GUI will be developed
#def GUI():
top = tk.Tk()
camera = subMovement.Camera()
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
    width=22,
    height=3,
    bg="red",
    fg="white",
    command = camera.record
)
picture = tk.Button(
    text="Take Picture",
    width=22,
    height=3,
    bg="red",
    fg="white",
    command = camera.takePhoto
)
battery = tk.Button(
    text="Battery Display",
    width=22,
    height=3,
    bg="red",
    fg="white",
    command = camera.batteryDisplay
)
power = tk.Button(
    text="Power",
    width=22,
    height=3,
    bg="red",
    fg="white",
    command = camera.power
)
entry = tk.Entry(top,
                 bg = "white")
submit = tk.Button(
    text = "Submit",
    width = 15,
    height = 3,
    bg = "black",
    fg = "white",
    command = main
)
scale = tk.Scale(
    label = 'speed',
    from_ = 1,
    to_ = 3,
    orient = tk.VERTICAL
)

title.pack()
#stream.pack()
record.pack(side = tk.TOP)
picture.pack(side = tk.TOP)
battery.pack(side = tk.TOP)
power.pack(side = tk.TOP)
entry.pack(side = tk.BOTTOM)
submit.pack(side = tk.BOTTOM)
scale.pack(side = tk.RIGHT)

top.mainloop()
