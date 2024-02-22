from socket import socket

HOST: str = "localhost"

PORT: int = 3000


# Created a new socket object
server_socket = socket()

# bind the sokcet object to the host and port
server_socket.bind((HOST, PORT))

# start listening for new connection
server_socket.listen()

print("Server is listening on", HOST, PORT)