'''VCGECMDS Client'''
# Jeremy Domino (100919249)
# Client_vcgencmds.py -- This client calls the Server_vcgencmds.py
# TPRG2131 Section 02
# November 21, 2024
# This program is strictly my own work. Any material beyond course learning
# materials that is taken from the Web or other sources is properly cited,
# giving credit to the original author(s).
#
# Modified from code provided by Prof. Phil Jarvis
#
# This client sends the 5 arguments from the Pi to the Server_vcgencmds.py

import socket
import json
# Creates the socket
s = socket.socket()
host = '192.168.2.47'
# host = '127.0.0.1'
port = 5000
s.connect((host, port))

try:
# JSON object call to server
    jsonReceived = s.recv(1024).decode()
# Prints the json received
    print('\n','Json received (byte type)-->', jsonReceived, '\n')
    if jsonReceived == b'':
        print('Ooops')
        exit()

# Converts json to dictionary
    data = json.loads(jsonReceived)
    ret = json.dumps(data, indent=4)
    ret1 = data['Temperature']
    ret2 = data['Voltage']
    ret3 = data['PWM']
    ret4 = data['Memory']
    ret5 = data['Clock']
# Prints the values
    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print(ret5)

except socket.gaierror: # = short form for getaddrinfo()
    print('There was an error resolving the host\n')
    s.close()
finally:
    print('Sorry lost connection\n')
    exit()
