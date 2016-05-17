
from socket import *

from thread import *

# Defining server address and port
host = ''  # 'localhost' or '127.0.0.1' or '' are all same
port = 52300 


sock = socket()

# Binding socket to a address. bind() takes tuple of host and port.
sock.bind((host, port))

# Listening at the address
sock.listen(2)  
a = []



def clientthread(conn, a):
    while True:

            data = conn[1].recv(1024)
            print ("raceived message", repr(data))
            reply1 = raw_input("reply:")
            conn[2].sendall(data)


while True:
    # Accepting incoming connections
    conn, addr = sock.accept()
    print('connect from:', addr)
    a.append((addr))
    conn.append((conn))
# Creating new thread. Calling clientthread function for this function and passing conn as argument.
    start_new_thread(clientthread, (conn,a))  

conn.close()
sock.close()
