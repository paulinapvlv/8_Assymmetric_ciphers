import socket
import pickle
import functions
import random

HOST = "127.0.0.1"
PORT = functions.check_port(input("Порт: "))
msg=input("Введите сообщение")

sock = socket.socket()
sock.connect((HOST, PORT))
conn, addr = sock.accept()

p,g,a = functions.prime_num(),functions.prime_num(),functions.prime_num()
A = functions.mod_num(p,g,a)

print("p {}\ng {}\na {}\nA {} ".format(p,g,a,A))

sock.send(pickle.dumps((p,g,A)))

B=pickle.loads(conn.recv(1024))
K_client=functions.mod_num(B,p,a)
sock.send(pickle.dumps(K_client)) 
   
sock.close()
