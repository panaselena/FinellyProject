import socket
from time import sleep
slTime=10

while True:
    try:
        with open('C:\\Users\Lena\Desktop\status.txt', 'r') as f:
            a = f.read()
            print(a,type(a))

    except IOError:
        print("No file by that name")


    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:

         client.connect(('127.0.0.1', 12345))
    except:
        print("Could not connect")
        break

    print("Connected")

    client.send(a.encode())

    print(client.recv(1024).decode())

    # client.close()
    sleep(slTime)


