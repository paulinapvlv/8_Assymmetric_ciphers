import socket
import pickle
import num_generator
import random

HOST = '127.0.0.1'
PORT = 8080

while True:
    sock = socket.socket()
    sock.connect((HOST, PORT))
    
    p, g, a = num_generator.big_num(),num_generator.big_num(),num_generator.big_num()
    A = num_generator.mod_num(p,g,a)
    print(p,g,a)
    sock.send((p, g, A).encode())
    
sock.close()
