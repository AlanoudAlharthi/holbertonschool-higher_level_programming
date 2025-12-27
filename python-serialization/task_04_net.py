#!/usr/bin/python3
import socket
import json

def start_server():
    host = '127.0.0.1'
    port = 65432  # Arbitrary non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        with conn:
            try:
                # Receive data in chunks
                data = b""
                while True:
                    packet = conn.recv(4096)
                    if not packet:
                        break
                    data += packet
                
                # Deserialize JSON data
                received_dict = json.loads(data.decode('utf-8'))
                print("Received Dictionary from Client:")
                print(received_dict)
            except Exception as e:
                print(f"Error receiving or decoding data: {e}")

def send_data(data_dict):
    host = '127.0.0.1'
    port = 65432

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            # Serialize dictionary to JSON string and encode to bytes
            json_data = json.dumps(data_dict).encode('utf-8')
            client_socket.sendall(json_data)
    except Exception as e:
        print(f"Error sending data: {e}")
