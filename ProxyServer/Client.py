import socket
SERVER_ADDRESS = ('localhost', 8000)

def client():
# Create a TCP socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    # Send a message to the server
    request = "tcp"
    client_socket.send(request.encode())

    # Receive a response from the server
    response = client_socket.recv(4096)
    print(response.decode())

    return client_socket
