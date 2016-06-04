'''
    Simple socket server using threads
''' 
import socket
import sys
from thread import *
 
HOST = ''   		# Symbolic name meaning all available interfaces
PORT = 8989		# Arbitrary non-privileged port
 
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
d=0
t=0
ad=[]
i=0 
b=0
o=0
f=0
j=0
name=[]
def clientthread(conn):
        name1=[]
        v=0
        conn.send('Welcome to the server. Type something and hit enter. to chat with users type add and to end type rmv \n') 	#send only takes string
        for k in range(len(name)-1):
           conn.sendall('you are connected with ' + name[k] + '\n') 
        for l in range(len(name)-1):
           ad[l].sendall('new connected client is '+ user + '\n')
    
       # conn.sendall ('enter the client you want to chat with : \n')
        while True : 
           
                data = conn.recv(1024)
                if data == 'add':
                      conn.sendall ('enter the client you want to chat with : \n') 
                      for o in range(len(name)):
                        conn.send(str(o+1) + ')  ' + name[o] + '\n')
                      data = conn.recv(1024)
                      u1 = data
                      name1.append(name[int(data)-1])   
                      data= conn.recv(1024)
                elif data == 'exit':
                     for t in range(len(name)):
                       ad[t].send('\n\nA User has disconnected\nAvailable users are:\n')
                       for d in range(len(name)):
                         ad[d].send(name[d]+"\n")
                     break      

                       
                elif data == 'rmv':
                      conn.sendall ('enter the client you want to remove from chat : \n') 
                      for f in range(len(name1)):
                        conn.send(str(f+1) + ')  ' + name1[f] + '\n')
                      data = conn.recv(1024)
                      v=1
                      a = data
                      del name1[int(a)-1]   
                      
                
                 
               
                for b in range(len(name1)):
                        ad[name.index(name1[b])].send(name[ad.index(conn)]+": "+data)

            
        #conn.close()   





while 1:
    #wait to accept a connection - blocking call
    conn, addr= s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    #a.append(str(addr[1]))
    ad.append(conn)
    user=conn.recv(1024)
    name.append(user)
    print name
    
    start_new_thread(clientthread ,(conn,))		
    i+=1
s.close()
