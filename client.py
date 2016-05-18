#!usr/bin/python
import socket               # Import socket module

s = socket.socket()         
host = socket.gethostname()
port = 8297                # Reserve a port for your service.

s.connect((host, port))
reply= s.recv(1024)

print reply
#s.send("hi")

   
   

while True:
  
  msg= raw_input("")
  
  if msg:  
       s.send(msg)
       
       if not msg:
          break
  
  reply1= s.recv(1024)
  if reply1:
      print reply1
      if not reply1:
          break

   
   
  
   
   

s.close()                     # Close the socket when done
