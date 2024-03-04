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
    try:
        # Check if info is blank
        if not info:
            raise ValueError("Info cannot be blank")

        # Sending information to clients using the broadcast socket
        broadcast_socket.sendto(info.encode(), ('<broadcast>', broadcast_port))

    except ValueError as ve:
        print(f"Error: {ve}")
    except socket.error as se:
        print(f"Socket error: {se}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def receive_data(sock, mask):
    try:
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

    except socket.error as se:
        print(f"Socket error: {se}")
    except Exception as e:
        print(f"An error occurred while receiving data: {e}")

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

try:
    while True:
        for key, events in selector.select():
            callback = key.data
            callback(key.fileobj, events)
except KeyboardInterrupt:
    print("Receiver terminated by user.")
finally:
    broadcast_socket.close()
    receive_socket.close()
