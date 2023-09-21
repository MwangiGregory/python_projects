import socket

host = '127.0.0.1'
port = 5000

client = socket.socket()
client.connect((host, port))

message = input("Enter some text to send: ")

while message != 'q':
    client.send(message.encode())

    data = client.recv(1024).decode()
    print(f"SERVER {host}: {data}")

    message = input("==>>: ")
    client.close()
