# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:24:42 2020

@author: stmcm
"""
import subMovement
import os
import tkinter as tk

#main is where GUI will be developed
def GUI():
    top = tk.Tk()
    camera = subMovement.Camera(10)
    title = tk.Label(text = "Submarine Control System")
    stream = tk.Label(
        text="Video Stream",
        fg="white",
        bg="black",
        width=100,
        height=30
    )
    record = tk.Button(
        text="Record Video",
        width=22,
        height=3,
        bg="red",
        fg="white",
        command = camera.record,
    )
    picture = tk.Button(
        text="Take Picture",
        width=22,
        height=3,
        bg="red",
        fg="white",
        command = camera.takePhoto,
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
    w = tk.Entry(top)
    title.pack()
    stream.pack()
    record.pack(side = tk.LEFT)
    picture.pack(side = tk.LEFT)
    battery.pack(side = tk.RIGHT)
    power.pack(side = tk.RIGHT)
    w.pack(side = tk.RIGHT)
    
    top.mainloop()

def main():
    #while True:
        choice = input('What would you like the submarine to do: ')
        switch(choice)

#switching algorithm to choose command
def switch(choice):
    if choice.upper() == "BATTERY LIFE":
        sub = subMovement.subMovement(15, "medium")
        print(sub.batteryLife())
        main()
    elif choice.upper() == "MOVE LEFT":
        speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15, speed)
        sub.moveLeft()
        main()
    elif choice.upper() == "MOVE RIGHT":
        speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15, speed)
        sub.moveRight()
        main()
    elif choice.upper() == "MOVE FORWARD":
        speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15, speed)
        sub.moveForward()
        main()
    elif choice.upper() == "MOVE BACKWARD":
        speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15, speed)
        sub.moveBackward()
        main()
    elif choice.upper() == "MOVE UP":
        speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15, speed)
        sub.moveUp()
        main()
    elif choice.upper() == "MOVE DOWN":
        speed = str(input('How fast would you like the submarine to go (low, medium, high): '))
        sub = subMovement.subMovement(15, speed)
        sub.moveDown()
        main()
    elif choice.upper() == "EXIT":
        print("Have a nice day.")
    else:
        print("The command you selected does not exist. Please try another command.")
        main()

GUI()