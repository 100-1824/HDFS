import socket
import threading
import os
import json

class MasterServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.data_nodes = {}
        self.files = {}

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Master server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        request = client_socket.recv(1024).decode('utf-8')
        request_data = json.loads(request)

        if request_data['type'] == 'register':
            self.register_data_node(request_data['node_id'], client_socket)
        elif request_data['type'] == 'upload':
            self.handle_upload(request_data['filename'], request_data['data_node_id'])
        elif request_data['type'] == 'download':
            self.handle_download(request_data['filename'], client_socket)

    def register_data_node(self, node_id, client_socket):
        with threading.Lock():
            self.data_nodes[node_id] = client_socket
            print(f"Data node {node_id} registered.")

    def handle_upload(self, filename, data_node_id):
        if filename not in self.files:
            self.files[filename] = data_node_id
            print(f"File {filename} uploaded to data node {data_node_id}.")
        else:
            print(f"File {filename} already exists.")

    def handle_download(self, filename, client_socket):
        if filename in self.files:
            data_node_id = self.files[filename]
            data_node_socket = self.data_nodes[data_node_id]
            client_socket.send(f"Downloading {filename} from {data_node_id}.".encode('utf-8'))
            data_node_socket.send(filename.encode('utf-8'))
            data_node_socket.send(client_socket.recv(1024))  # Send acknowledgment to client
        else:
            client_socket.send(f"File {filename} not found.".encode('utf-8'))

if __name__ == "__main__":
    master_server = MasterServer('127.0.0.1', 5000)
    master_server.start_server()

