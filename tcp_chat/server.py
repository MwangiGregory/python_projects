mport socket

host = '127.0.0.1'
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
client, addr = server.accept()

print(f"Yay, received connection request from {addr}")

while True:
    data = client.recv(1024).decode()

    if not data:
        break

    print(f"CLIENT {addr}: {data}")

    message = input("==>>: ")

    if message is not None:
        client.send(message.encode())

server.close()
