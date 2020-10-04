# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:04:16 2020

@author: stmcm
"""


import bluetooth

bd_addr = "34:F3:9A:1E:90:24"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()