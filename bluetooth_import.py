# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:08:14 2020

@author: mikae
"""


from bluetooth import*
from getch import getch

MAC_ADR="meow"

client_socket = BluetoothSocket (RFCOMM)
client_socket.connect((MAC_ADR, 1))

print (connected)
print ("Press 'q' to quit")

key = 0;
while key != 'q':
    key = getch() #gets 1 key only
    print (key)
    client_socket.send(key)

# Close the connection
client_socket.close()