import socket
import json

class DFSClient:
    def __init__(self, master_host, master_port):
        self.master_host = master_host
        self.master_port = master_port

    def upload_file(self, filename, data_node_id):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as master_socket:
            master_socket.connect((self.master_host, self.master_port))
            request_data = {
                'type': 'upload',
                'filename': filename,
                'data_node_id': data_node_id
            }
            master_socket.send(json.dumps(request_data).encode('utf-8'))

    def download_file(self, filename):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as master_socket:
            master_socket.connect((self.master_host, self.master_port))
            request_data = {
                'type': 'download',
                'filename': filename
            }
            master_socket.send(json.dumps(request_data).encode('utf-8'))
            response = master_socket.recv(1024).decode('utf-8')
            print(response)

if __name__ == "__main__":
    client = DFSClient('127.0.0.1', 5000)

    # Simulate file upload
    client.upload_file('example.txt', 'node1')

    # Simulate file download
    client.download_file('example.txt')

