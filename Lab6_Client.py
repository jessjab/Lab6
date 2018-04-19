'''
Created on Apr 8, 2018

@author: jessjab
'''
import sys
import socket 


if __name__ == '__main__':
    pass

#Retrieving data from user___________________________________________________________________________________________
if(len(sys.argv)-1 !=5):
    print "Incorrect number of arguments.(",len(sys.argv)-1, ")" 
    print "Enter: Servers IP address, port number, Time Delay, Number of executions,command."
    sys.exit()

SERVER_IP_ADDRESS = sys.argv[1]
PORT_NO = sys.argv[2]
PORT_NO_int = int(PORT_NO)
TIME_DELAY= sys.argv[3]
NUM_OF_EXECUTIONS= sys.argv[4]
COMMAND = " ".join(sys.argv[5:])
UDP_or_TCP = raw_input("UDP or TCP?: ")

print "You entered: ", SERVER_IP_ADDRESS, PORT_NO_int,TIME_DELAY,NUM_OF_EXECUTIONS, COMMAND, "and Message:", UDP_or_TCP


#Sending with UDP______________________________________________________________________________________________________
if UDP_or_TCP == "UDP":
    #Sending data to Server__________________________________________________________________________________________
    MESSAGE_TO_SEND_UDP = NUM_OF_EXECUTIONS + " " +TIME_DELAY + " " + COMMAND 
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = clientSock.sendto(MESSAGE_TO_SEND_UDP, (SERVER_IP_ADDRESS, PORT_NO_int))
    print >>sys.stderr, 'sent %s bytes to %s' % (sent, SERVER_IP_ADDRESS)
    
    #Receiving data from Server______________________________________________________________________________________
    while True:
        print >>sys.stderr, 'waiting to receive message from server'
        DATA_BACK, ADDR = clientSock.recvfrom(1024)
        print >>sys.stderr, 'received %s bytes back from %s' % (len(DATA_BACK), ADDR)
        print "Client received message from server: ", DATA_BACK
        clientSock.close()
        break
        
#Sending with TCP______________________________________________________________________________________________________
if UDP_or_TCP == "TCP":
     #Sending data to Server__________________________________________________________________________________________
    MESSAGE_TO_SEND_TCP = NUM_OF_EXECUTIONS + " " +TIME_DELAY + " " + COMMAND   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP_ADDRESS, PORT_NO_int))
    s.send(MESSAGE_TO_SEND_TCP)
    #print >>sys.stderr, 'sent %s bytes to %s' % (sent, SERVER_IP_ADDRESS)
    MESSAGE_BACK = s.recv(1024)
    #print >>sys.stderr, 'received %s bytes back from %s' % (len(DATA_BACK), ADDR)
    print "Client received message from server: ", MESSAGE_BACK
    s.close()

    
    
