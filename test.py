# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 12:48:22 2020

@author: stmcm
"""


"""import socket

HOST = '198.162.0.5'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)"""
import bluetooth

target_name = "My Phone"
target_address = "STMIP6S-64"

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address ",target_address)
else:
    print("could not find target bluetooth device nearby")