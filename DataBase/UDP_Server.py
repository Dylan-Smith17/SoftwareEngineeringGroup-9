# UDP
#
# Team 9
#
# 02/18/24

import socket

localIP = "127.255.255.255" # this ip address is a general address to test on the same
                            # machine. If you want to use your local ip specifically
                            # on your computer then use this line of code
                            # localIP = socket.gethostbyname(socket.gethostname())
broadcast_port = 7500
receive_port = 7501

# Set up broadcast socket
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set up receiving socket
receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_socket.bind(("", receive_port))

print(f"Broadcast socket up and listening on {localIP}:{broadcast_port}")
print(f"Receive socket up and listening on {localIP}:{receive_port}")

#######################################################################################
#######################################################################################

# EXAMPLE EXAMPLE EXAMPLE
# EXAMPLE EXAMPLE EXAMPLE
def send_info_to_client(info):
    # Sending information to the server
    broadcast_socket.sendto(info.encode(), ('<broadcast>', broadcast_port))

# Example: Call the function from another file
message_to_broadcast = "Broadcast message from server"
send_info_to_client(message_to_broadcast)
# EXAMPLE EXAMPLE EXAMPLE
# EXAMPLE EXAMPLE EXAMPLE

#######################################################################################
#######################################################################################

while True:
    # Receiving messages
    data, client_address = receive_socket.recvfrom(1024)
    print(f"Received message from {client_address}: {data.decode()}")



