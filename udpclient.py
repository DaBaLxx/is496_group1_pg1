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
import sys, struct, time
from pg1lib import *


############## Beginning of Part 1 ##############
# TODO: define a buffer size for the message to be read from the UDP socket
BUFFER = 


def part1 ():
    print("********** PART 1 **********")
    # TODO: fill in the hostname and port number 
    hostname = 
    PORT = 

    # A dummy message (in bytes) to test the code
    message = b"Hello World"

    # TODO: convert the host name to the corresponding IP address
    HOST = 
    sin = (HOST, PORT)


    # TODO: create a datagram socket
    try:
        
    except socket.error as msg:
        print('Failed to create socket.')
        sys.exit()


    # TODO: convert the message from string to byte and send it to the server




    # TODO: 
    # 1. receive the acknowledgement from the server 
    # 2. convert it from network byte order to host byte order 




    # TODO: print the acknowledgement to the screen




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
