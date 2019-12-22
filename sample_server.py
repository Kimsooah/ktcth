"""Viết chương trình nhập vào một xâu ký tự từ client, truyền sang server theo phương thức UDP. Server hiển thị zâu và tính số lượng chữ thương trong xâu rồi báo lại cho client.
"""

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

def echo_server(port):
    """A simple echo server.
    
    Args:
        port ([type]): [description]
    """
    # create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # enalbe reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the socket to the port
    server_address = (host, port)
    print(f"Starting up echo server on {host} port {port}.")
    sock.bind(server_address)

    # listen to clients, 
    # backlog argument specifies the max number of queued connections
    sock.listen(backlog)

    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()

        data = client.recv(data_payload)

        if data:
            print(f"Data: {data}")
            client.send(data)
            print(f"Sent {data} bytes back to {address}")

        # end connection
        client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()

    port = given_args.port

    echo_server(port)