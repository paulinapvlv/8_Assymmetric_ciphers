import socket
import pickle
import num_generator
import random

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    
    g,p,A = conn.recv(1024).decode()
    print(g,p,A)
    b=num_generator.big_num()
    B=num_generator.mod_num(g,p,b)
    
conn.close()
