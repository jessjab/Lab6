'''
Created on Apr 8, 2018

@author: jessjab
'''
import os
import sys
import socket
import time
from time import gmtime, strftime

if __name__ == '__main__':
    pass
#Retrieving data from user_______________________________________________________________________________________
if(len(sys.argv)-1 !=1):
    print "Incorrect number of arguments.(",len(sys.argv)-1, ")" 
    print "Enter: port number"
    sys.exit()
PORT_NO = sys.argv[1]
PORT_NO_int = int(PORT_NO)
UDP_or_TCP = raw_input("UDP or TCP?: ")

print "You entered: ",PORT_NO_int


if UDP_or_TCP == "UDP":
    
      #Receiving data from Client_________________________________________________________________________________________
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_HOST_NAME =socket.gethostname()
    SERVER_IP_ADDRESS=socket.gethostbyname(UDP_HOST_NAME)
    print "SERVER IP ADDRESS:", SERVER_IP_ADDRESS 
    serverSock.bind((SERVER_IP_ADDRESS , PORT_NO_int))
    
    while True:
        print 'waiting to receive message from client'
        CLIENT_DATA, ADDR = serverSock.recvfrom(1024)
        TIME_RECIEVED = time.asctime(time.localtime(time.time()))
        CLIENT_DATA_split = CLIENT_DATA.split()
        COMMAND = " ".join(CLIENT_DATA_split[2:])
        print TIME_RECIEVED, "Client Address:", ADDR, "Command:", COMMAND, "connected."
        
        NUM_OF_EXECUTIONS = CLIENT_DATA_split[0] 
        TIME_DELAY =CLIENT_DATA_split[1]
        COMMAND_START_TIME = time.time()
           
        for i in range(0,int(NUM_OF_EXECUTIONS)):
            os.system(COMMAND)
            time.sleep(float(int(TIME_DELAY)))
        COMMAND_END_TIME =time.time()
        COMMAND_RUN_TIME =COMMAND_END_TIME-COMMAND_START_TIME
        DISCONNECT_TIME = time.asctime(time.localtime(time.time()))
        
        RETURN_MESSAGE = "The command took"  + str(COMMAND_RUN_TIME) + " seconds to run"
        serverSock.sendto(RETURN_MESSAGE, ADDR)
        
        print DISCONNECT_TIME, "address", ADDR, "disconnected"
        
if UDP_or_TCP == "TCP":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_HOST_NAME = socket.gethostname()
    SERVER_IP_ADDRESS = socket.gethostbyname(TCP_HOST_NAME)
    s.bind((SERVER_IP_ADDRESS, PORT_NO_int))
    
    BUFFER_SIZE = 1024  

    while True:
        s.listen(5)
        
        conn, addr = s.accept()
        print 'Connection address:', addr
        while 1:
            data = conn.recv(BUFFER_SIZE)
            TIME_RECIEVED = time.asctime(time.localtime(time.time()))
            CLIENT_DATA_split = data.split()
            COMMAND = " ".join(CLIENT_DATA_split[2:])
            print TIME_RECIEVED, "Client Address:", addr, "Command:", COMMAND, "connected."
            NUM_OF_EXECUTIONS = CLIENT_DATA_split[0] 
            TIME_DELAY =CLIENT_DATA_split[1]
            COMMAND_START_TIME = time.time()
               
            for i in range(0,int(NUM_OF_EXECUTIONS)):
                os.system(COMMAND)
                time.sleep(float(int(TIME_DELAY)))
                
            COMMAND_END_TIME =time.time()
            COMMAND_RUN_TIME =COMMAND_END_TIME-COMMAND_START_TIME
            
            RETURN_MESSAGE = "The command took "  + str(COMMAND_RUN_TIME) + " seconds to run"
            
            
            conn.sendto(RETURN_MESSAGE,addr)
            DISCONNECT_TIME = time.asctime(time.localtime(time.time()))
            print DISCONNECT_TIME, "address", addr, "disconnected"

    conn.close()
