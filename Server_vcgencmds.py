'''VCGECMDS Server'''
# Jeremy Domino (100919249)
# Server_vcgencmds.py -- Area and Volume Calculator.
# TPRG2131 Section 02
# November 21, 2024
# This program is strictly my own work. Any material beyond course learning
# materials that is taken from the Web or other sources is properly cited,
# giving credit to the original author(s).
#
# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

import socket
import os, time
import json

# Creates the socket
s = socket.socket()
host = '' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)


#gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
#gets from the os, using vcgencmd - the core-temperature
t = os.popen('vcgencmd measure_temp').readline()
#gets from the os, using vcgencmd - the core-voltage
volts = os.popen('vcgencmd measure_volts ain1').readline()
#gets from the os, using vcgencmd - the core-pwm
pwm = os.popen('vcgencmd measure_clock core').readline()
#gets from the os, using vcgencmd - the core-memory
get_mem = os.popen('vcgencmd get_mem gpu').readline()
#gets from the os, using vcgencmd - the core-clock
get_arm = os.popen('vcgencmd get_mem arm').readline()

# initialising json object string
ini_string = {
    "Temperature": t,
    "Voltage": volts,
    "PWM": pwm,
    "Memory": get_mem,
    "Clock": get_arm}
# converting string to json
f_dict = json.dumps(ini_string) # The eval() function evaluates JavaScript code represented as a string and returns its completion value.


# This is the server
def main():
    """This is the server"""
    while True:
        c, addr = s.accept()
        print ('Got connection from',addr)
        res = bytes(str(f_dict), 'utf-8') # needs to be a byte
        c.send(res)
        c.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Bye...')
        exit()
