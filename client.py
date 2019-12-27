import socket
import pickle
import functions
import random

HOST = "127.0.0.1"
PORT = functions.check_port(input("Порт: "))
msg=input("Введите сообщение: ")

sock = socket.socket()
sock.connect((HOST, PORT))

p,g = functions.prime_num(),functions.prime_num()
a = random.randint(1,1000)
A = functions.mod_num(g,p,a)

print("p {}\ng {}\na {}\nA {} ".format(p,g,a,A))

sock.send(pickle.dumps((p,g,A)))
print("Переменные p, g, A отправлены")

B=pickle.loads(sock.recv(1024))
K_client=functions.mod_num(B,p,a) 
sock.send(pickle.dumps(K_client))
print("Клиентское значение K отправлено")

send_message=pickle.loads(sock.recv(1024)) 
if send_message:
    cyphered=functions.xor(msg,K_client)
    sock.send(pickle.dumps(cyphered))
    print("Зашифрованное сообщение отправлено")
sock.close()
