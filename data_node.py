import socket
import threading
import os

class DataNode:
    def __init__(self, node_id, host, port):
        self.node_id = node_id
        self.host = host
        self.port = port

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Data node {self.node_id} listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        filename = client_socket.recv(1024).decode('utf-8')
        file_path = f"{self.node_id}/{filename}"

        with open(file_path, 'wb') as file:
            data = client_socket.recv(1024)
            while data:
                file.write(data)
                data = client_socket.recv(1024)

        print(f"Received {filename} on data node {self.node_id}.")
        client_socket.send(f"File {filename} received on data node {self.node_id}.".encode('utf-8'))

if __name__ == "__main__":
    data_node = DataNode('node1', '127.0.0.1', 6001)
    data_node.start_server()

