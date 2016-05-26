'''
    Simple socket server using threads
''' 
import socket
import sys
from thread import *
 
HOST = ''   		# Symbolic name meaning all available interfaces
PORT = 9989		# Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
l=0
k=0
m=0
address =0
new=0   
n=0  
p={}
ad=[]
i=0 
a=[]
def clientthread(conn):
    						
    
    conn.send('Welcome to the server.\n') 	#send only takes string
    for k in range(i-1):
        conn.sendall('you are connected with ' + a[k] + '\n') 
    
    for l in range(i-1):
        ad[l].sendall('new connected client is '+str(new)) 

    conn.sendall ('enter the client you want to chat with : \n')
    address = conn.recv(1024)

    if address:   
	    p[0]=conn
	   
	    for m in range(n):
		if (a[m]==address):
			p[1]=ad[m]
	    
	    while True:
		#receiving from client
		data = conn.recv(1024)
		
		if conn == p[0]:
			p[1].send('client1>>'+ data)
		else:
			p[0].send('client2>>'+ data)
			#came out of loop   
                if not data:
			break
    conn.close()   


while 1:
    #wait to accept a connection - blocking call
    conn, addr= s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    a.append(str(addr[1]))	
    new= addr[1]
    n+=1
    ad.append(conn)
    start_new_thread(clientthread ,(conn,))		
    i+=1
s.close()
