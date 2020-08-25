# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:24:42 2020

@author: stmcm
"""
import subMovement
import os

def main():
    #while True:
        choice = input('What would you like the submarine to do: ')
        switch(choice)

def switch(choice):
    sub = subMovement.subMovement(15)
    if choice.upper() == "BATTERY LIFE":
        print(sub.batteryLife())
    elif choice.upper() == "MOVE LEFT":
        sub.moveLeft()
    elif choice.upper() == "MOVE RIGHT":
        sub.moveRight()
    elif choice.upper() == "MOVE FORWARD":
        sub.moveForward()
    elif choice.upper() == "MOVE BACKWARD":
        sub.moveBackward()
    elif choice.upper() == "MOVE UP":
        sub.moveUp()
    elif choice.upper() == "MOVE DOWN":
        sub.moveDown()
    elif choice.upper() == "EXIT":
        print("Have a nice day.")
    else:
        print("The command you selected does not exist. Please try another command.")
        main()

main()