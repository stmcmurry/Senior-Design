"""
This is the progrom that should be run in order to control the Youcan submarine.
The file is meant to work in tandem with scrcpy
controlSystem.py
"""
#python packages to be used
import subMovement #import subMOvement
import tkinter as tk #python GUI toolkit to be used for the GUI
from tkinter import ttk
import time as t
import pyautogui

#a method to use the Submit button with the 'enter' key
def onclick(event=None):
    answer = entry.get() #gets input from user for submarine command to do
    splitString(answer) #splits the user input
    
#a method to get a value for how long the sub moves
def splitString(answer):
    if ',' in answer: #if there is a comma within the input
        blockCommand(answer) #recognizes that the user is trying to do a "block" of commands
    else: #otherwise, instantiate a list that has two spaces
        msg = [0]*2
        msg = answer.split(' ') #add the user answer into the list, being sure to parse each value by spaces
        msg.append('0') #add a 0 at the end of the list
        switch(msg[0], msg[1]) #then do the command that is found in list index 0 for the duration found in list index 1
        backToGUI() #hard code for the GUI to pop back onto the screen after the user is done inputting commands
    
#a method to display a popup window if the user inputs an unrecognized command    
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

#a method to take in multiple instructions
def blockCommand(answer): #takes in the user input
    block = answer.split(' ') #splits user input based on spaces found within the input
#a nested for loop that features the variables i, j, and k
#for int i = the numerical character length of the block command
    for i in range(len(block)):
        if ',' in block[i]: #if there is a comma found within the block
            block[i] = block[i].replace(",", "") #the comma will be taken out
#for int j = the numerical character length of the block command         
    for j in range(len(block)):
        try:
            if block[j].isnumeric() or block[j+1].isnumeric(): #if the character at position j within the block or the next character has a nunerical value
                continue #keep parsing the user input command character by character
            else:
                block.insert(j+1, "0") #otherwise add a 0, this signals that this is the last command to be done
        except:
            block.append("0") #if no numerical values are found in either position, just add a 0
    
    block.append("0")      #add a 0 to signal that this is the last command to be done wihin the block

    print(block) #print out the block
#for int k = numerical character length of the block command
    for k in range(len(block)):
#if the first character is not numeric however if the next character is numeric        
        if (block[k].isnumeric() == False) and (block[k+1].isnumeric() == True):
            switch(block[k], block[k+1]) #go ahead and do the submarine command the user asked for
            print(block[k], block[k+1]) #print the command out

    backToGUI() #hardcode the GUI to pop back up
    
#a switching method that contains the keywords to control the submarine      
def switch(choice, time):
    if choice.upper() == "LEFT":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveLeft(time) #moves submarine to the left for the alloted amount of time chosen by the user
    
    elif choice.upper() == "RIGHT":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveRight(time) #moves submarine to the righ for the alloted amount of time chosen by the user
        
    elif choice.upper() == "BACK" or choice.upper() == "BACKWARD" or choice.upper() == "BACKWARDS":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveBackward(time) #moves submarine backwards for the alloted amount of time chosen by the user
        
    elif choice.upper() == "FORWARD" or choice.upper() == "STRAIGHT":
        sub = subMovement.subMovement()
        time = float(time)
        sub.moveForward(time) #moves submarine forwards for the alloted amount of time chosen by the user
        
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
#focus the camera      
    elif choice.upper() == "STABLE":
        sub = subMovement.Camera()
        sub.stabilizeImage()
#tells subarmine to maintain a certain depth when submerged into the water        
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
        popupmsg("The '"+ choice + "' command you selected does not exist. Please try another command.")
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