#!/usr/bin/python3
import socket, sys
s = socket.socket()
#host = "demo2server.in"
def do_scan(port):
    try:
       s.connect((sys.argv[1],port))
       return True
    except:
        return False
for x in range(20,81):
    if do_scan(x):
        print("Port {} is open".format(x))
    else:
        print("Port {} is close".format(x))
#python3 scannport.py 192.168.47.103
