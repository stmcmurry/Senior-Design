"""
controlSystem.py
This is the program that should be run in order to control the Youcan submarine.
The file is meant to work in tandem with scrcpy
"""

#python packages to be used
import subMovement #import subMovement.py
import tkinter as tk #python GUI toolkit
from tkinter import ttk
import time as t
import pyautogui

#a method to use the Submit button with the 'enter' key
def onclick(event=None):
    answer = entry.get() #gets input from user for submarine command to do
    splitString(answer) #method that splits the user's input
    
#a method that splits the user's input
def splitString(answer):
    if ',' in answer: #if a comma is found within the user input, then it'll be recognized as a "block" command
        blockCommand(answer)
    else:
        msg = [0]*2 #list of size 2
        print(msg) #print message
        msg = answer.split(' ') #split input based on spaces within the input and place inside msg list
        msg.append('0') #add 0
        print(msg) #print out message
        switch(msg[0], msg[1]) #does submarine command with numerical values representing length of time
        backToGUI() #hard code to display GUI
    
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
 
#a method to return the window to the GUI      
def backToGUI():
    pyautogui.keyDown('alt')
    t.sleep(0.1)
    pyautogui.press('tab')
    t.sleep(0.1)
    pyautogui.keyUp('alt')

#a method that takes in multiple instrucions
def blockCommand(answer):
    block = answer.split(' ') #when a block command is recognized, split the user answer based on spaces
    
    for i in range(len(block)): #for loop with i equaling the # of characters within the block
        if ',' in block[i]: #if a comma is found, take the comma out
            block[i] = block[i].replace(",", "")
    
    print(block)       #print command
    for j in range(len(block)): 
        try:
            if block[j].isnumeric() or block[j+1].isnumeric(): #if a character is numerical or if the character in j+1 is numerical
                continue
            else:
                block.insert(j+1, "0") #otherwise insert a 0 value
        except:
            block.append("0")
    
    block.append("0")      

    print(block) 
    for k in range(len(block)):
        if (block[k].isnumeric() == False) and (block[k+1].isnumeric() == True): #if the character is not numeric but the next characer is
            switch(block[k], block[k+1]) #do the submarine command 
            print(block[k], block[k+1])

    backToGUI() #hardcode to pop GUI back up
    
#a switching method that contains the keywords to control the submarine      
def switch(choice, time):
    print("yay")
    if choice.upper() == "LEFT":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveLeft(time) #moves submarine to the left for the alloted amount of time chosen by the user
    
    elif choice.upper() == "RIGHT":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveRight(time) #moves submarine to the right for the alloted amount of time chosen by the user
        
    elif choice.upper() == "BACK":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveBackward(time) #moves submarine backwards for the alloted amount of time chosen by the user
        
    elif choice.upper() == "FORWARD" or choice.upper() == "STRAIGHT":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveForward(time) #moves submarine forward for the alloted amount of time chosen by the user
        
    elif choice.upper() == "UP":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveUp(time) #moves submarine upwards for the alloted amount of time chosen by the user
       
    elif choice.upper() == "DOWN":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveDown(time) #moves submarine downwards for the alloted amount of time chosen by the user
 #records video
#user types in "record" to start video - if video recording wants to be stopped, then user must input "record" again       
    elif choice.upper() == "RECORD":
        sub = subMovement.Camera()
        sub.recordVideo()
#takes a photo through the submarine's vision            
    elif choice.upper() == "PHOTO" or choice.upper() == "PICTURE":
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