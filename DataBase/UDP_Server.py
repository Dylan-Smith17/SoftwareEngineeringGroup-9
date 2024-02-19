# UDP
#
# Team 9
#
# 02/18/24
#
# receiver.py

import socket
import selectors

def send_info_to_client(info, broadcast_socket, broadcast_port):
    # Sending information to clients using the broadcast socket
    broadcast_socket.sendto(info.encode(), ('<broadcast>', broadcast_port))

def receive_data(sock, mask):
    data, client_address = sock.recvfrom(1024)
    print(f"Received message from {client_address}: {data.decode()}")

    # Example
    if data.decode() == "hello":
            # Broadcast "Hello there" to all clients
            send_info_to_client("Hello there", broadcast_socket, broadcast_port)

    # Example
    if data.decode() == "hi":
            # Broadcast "Hello there" to all clients
            send_info_to_client("Sup", broadcast_socket, broadcast_port)

# Set up broadcast socket
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set up receiving socket
receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_port = 7501
broadcast_port = 7500
receive_socket.bind(("", receive_port)) 
                            # this ip address is a general address to test on the same
                            # machine. If you want to use your local ip specifically
                            # on your computer then use this line of code
                            # localIP = socket.gethostbyname(socket.gethostname())

selector = selectors.DefaultSelector()
selector.register(receive_socket, selectors.EVENT_READ, receive_data)

while True:
    for key, events in selector.select():
        callback = key.data
        callback(key.fileobj, events)
