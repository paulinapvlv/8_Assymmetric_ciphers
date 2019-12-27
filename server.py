import socket
import pickle
import functions
import random

HOST = "127.0.0.1"
PORT = functions.check_port(input("Порт: "))

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    request_msg=bool()

    p,g,A=pickle.loads(conn.recv(1024))
    b=functions.prime_num()
    B=functions.mod_num(g,p,b)
    print("p {}\ng {}\nA {}\nb {} \nB {}".format(p,g,A,b,B))

    conn.send(pickle.dumps(B))
    print("B отправлено".format(B))
    K_server=functions.mod_num(A,p,b)

    K_client=pickle.loads(conn.recv(1024))
    print("K серверное {},K клиентское {}".format(K_server,K_client))

    if K_server==K_client:
        print("Одинаковое K")
        request_msg=True
    else:
        print("Неодинаковое K")
        request_msg=False
    conn.send(pickle.dumps(request_msg))

    if request_msg:
       cyphered=pickle.loads(conn.recv(1024))
       print("Зашифрованное сообщение (получено с клиента) {}".format(cyphered))
       decyphered=functions.xor(cyphered,K_server)
       print("Дешифрованное сообщение {}".format(decyphered))
    conn.close()
