# Akshaj Murhekar
# 1001752757

import socket
from time import *
import sys
import time


HOST= 8080
PORT= 12000
fileName = sys.argv[1]



clientSocket = socket.socket()

print('Client has been established')
server_add = ()

clientSocket.connect()
# connect the host and port to the socket
send_time = time.time()
clientSocket.send()


data=clientSocket.recv(1024)
recv_time = time.time()
RTT = recv_time - send_time
print('Data received by the client is', data)
print('RTT ', RTT)

"""Print other vvalues here"""

"""close socket"""
clientSocket.close()