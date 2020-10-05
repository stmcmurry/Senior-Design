# -*- coding: utf-8 -*-


import bluetooth

bd_addr = "34:F3:9A:1E:90:24"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()