# IS496: Computer Networks (Spring 2022)
# Programming Assignment 1 -  Starter Code 
# Name and Netid of each member:
# Member 1: 
# Member 2: 
# Member 3: 



# Note: 
# This starter code is optional. Feel free to develop your own solution to Part 1. 
# The finished code for Part 1 can also be used for Part 2 of this assignment. 



# Import any necessary libraries below
import socket
import sys, struct
from pg1lib import *


############## Beginning of Part 1 ##############
# TODO: define a buffer size for the message to be read from the UDP socket
BUFFER = 


def part1 ():
    print("********** PART 1 **********")
    # TODO: fill in the IP address of the host and the port number
    HOST = 
    PORT = 
    sin = (HOST, PORT)

    # TODO: create a datagram socket
    try:

    except socket.error as e:
        print('Failed to create socket.')
        sys.exit()


    # TODO: Bind the socket to address
    try:

    except socket.error as e:
        print('Failed to bind socket.')
        sys.exit()

    print("Waiting ...")

    # TODO: receive message from the client and record the address of the client socket




    # TODO: convert the message from byte to string and print it to the screen




    # TODO: 
    # 1. convert the acknowledgement (e.g., interger of 1) from host byte order to network byte order
    # 2. send the converted acknowledgement to the client




    # TODO: close the socket






############## End of Part 1 ##############




############## Beginning of Part 2 ##############
# Note: any functions/variables for Part 2 will go here 

def part2 ():



############## End of Part 2 ##############


if __name__ == '__main__':
    # Your program will go with function part1() if there is no command line input. 
    # Otherwise, it will go with function part2() to handle the command line input 
    # as specified in the assignment instruction. 
    if len(sys.argv) == 1:
        part1()
    else:
        part2()



