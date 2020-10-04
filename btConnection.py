# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:23:43 2020

@author: stmcm
"""


import socket
import serial
import pickle
import bluetooth

target_name = "My Phone"
target_address = "STMIP6S-64" #changes with device

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ",target_address)
else:
    print("could not find target bluetooth device nearby")