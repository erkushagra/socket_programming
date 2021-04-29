import socket
import sys

def socket_create(): # To create a socket that connects a server and client

    try:
        global host
        global port
        global s
        host = ""
        port = 9999

        s = socket.socket() # Creating a socket

    except socket.error as msg: # If any error give message to the user
        
        print("Socket Creation Error:",str(msg))


def socket_bind(): # To bind a socket with a port

    try:
        
        print("Binding Socket to Port"+str(port))
        
        s.bind((host,port)) # binding port with a socket
        
        s.listen(5) # socket needs to listen client connection and there can be a maximum 5 connection

    except socket.error as msg: # If any error give message to the user
        
        print('Socket Binding Error'+str(msg))
        
        socket_bind() # If any error try to call a function again 


def socket_accept(): # To accept a connection from Client by socket

    conn,address = s.accept() # Accept the connection required details in conn and address variable
    
    print("Connection Established | " + "IP:" +address[0] + "| Port: " + str(address[1])) # Here, 'IP' is of the server and output the port number  
    
    send_command(conn) # send commands to our client cmd
    
    conn.close() #after sending close the connection

def send_command(conn):

    while True:
        cmd = input()

        if cmd == 'exit':
            
            conn.close()
            
            s.close()
            
            sys.exit()

        if len(cmd)>0:
            
            conn.send(str.encode(cmd)) # send comment to the client 
            
            client_response = (conn.recv(1024).decode("utf-8")) #output the string as bits
            
            print(client_response,end="")

def main():
    
    socket_create()
    
    socket_bind()
    
    socket_accept()

main()





