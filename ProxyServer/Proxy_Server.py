import multiprocessing
import select
import socket
import ssl

def handle_client(client_socket):
    try:
        # Receive data from the client
        request = client_socket.recv(4096)
        print("Received request from client: " + str(request.decode()))

        # Forward the request to the destination server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_server_socket = ssl.wrap_socket(server_socket, ssl_version=ssl.PROTOCOL_TLSv1_2)
        ssl_server_socket.connect((str(request.decode())), 443)
        ssl_server_socket.send(request)

        # Receive data from the server
        response = ssl_server_socket.recv(4096)
        print("Received response from server: " + str(response.decode()))

        # Forward the response back to the client
        client_socket.send(response)

    except Exception as e:
        print(e)
    return ssl_server_socket

def run_server():
    # Create a listening socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()

    print('Proxy server listening on port 8000...')

    # Create a list of sockets to monitor for incoming data
    sockets = [server_socket]

    while True:
        # Use select system call to monitor sockets for incoming data
        read_sockets, write_sockets, error_sockets = select.select(sockets, [], [], 1)

        for sock in read_sockets:
            if sock == server_socket:
                # Accept a new client connection
                client_socket, client_address = server_socket.accept()
                print(f'New client connected: {client_address}')

                # Use multiprocessing to fork a new process to handle the client connection
                process = multiprocessing.Process(target=handle_client, args=(client_socket,))
                process.start()
                process.join()

            else:
                # Remove the client socket from the list of sockets to monitor
                sockets.remove(sock)
        return read_sockets
    
