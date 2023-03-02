# Akshaj Murhekar
# 1001752757


# Import socket module
import socket

# Import thread module
import _thread


# Create a TCP server socket


serverSocket = socket.socket()  

# Assign a port number
serverPort = 12000


# Bind the socket to server address and server port

serverSocket.bind()

# Listen to at most 5 connection at a time

serverSocket.listen()

# Server should be up and running and listening to the incoming connections

def multi_thread(connectionSocket):
    try:

        # Extract the path of the requested object from the message

        message = connectionSocket.recv(1024).decode('utf-8')

        f = open(message,'rb')

        # Store the entire contenet of the requested file in a temporary buffer

        outputdata = f.read()


        # Send the HTTP response header line to the connection socket
        # send Header line to the connection socket



        # Send the content of the requested file to the connection socket
    except IOError:
        # Send HTTP response message for file not found
        # Close the client connection socket

        connectionSocket.close()


    # Close the socket in case of some issues 
    connectionSocket.close()


while True:
    '''This part is for multi threading'''
    print 'Ready to serve'
    '''Start the new thread'''







