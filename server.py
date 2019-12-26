import socket
import pickle
import functions
import random

HOST = "127.0.0.1"
PORT = functions.check_port(input("Порт: "))

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

p,g,A=pickle.loads(conn.recv(1024))
b=functions.prime_num()
B=functions.mod_num(g,p,b)
print("p {}\ng {}\nA {}\nb {} \nB {}".format(p,g,A,b,B))

sock.send(pickle.dumps(B))
K_server=functions.mod_num(A,p,b)

K_client=pickle.loads(conn.recv(1024))
if K_server==K_client:
    print("Одинаковый общий секрет")
conn.close()
