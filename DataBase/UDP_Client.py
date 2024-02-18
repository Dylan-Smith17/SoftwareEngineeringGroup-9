# UDP
#
# Team 9
#
# 02/18/24

import socket

serverIP = "0.0.0.0"    # this ip address is a general address to test on the same
                        # machine. If you want to use server ip then us this
                        # line of code
                        # serverIP = "192.168.1.100"
broadcast_port = 7500
send_port = 7501

# Set up broadcast socket for listening
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.bind((serverIP, broadcast_port))

# Set up sending socket
send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Broadcast socket for listening on {serverIP}:{broadcast_port}")
print(f"Send socket up and ready to send messages to {serverIP}:{send_port}")

print(f"Broadcast socket for listening on {serverIP}:{broadcast_port}")
print(f"Send socket up and ready to send messages to {serverIP}:{send_port}")

#######################################################################################
#######################################################################################

# EXAMPLE EXAMPLE EXAMPLE
# EXAMPLE EXAMPLE EXAMPLE
def send_info_to_server(info):
    # Sending information to the server
    send_socket.sendto(info.encode(), (serverIP, send_port))

# Example: Call the function from another file
info_to_send = "Hello from client"
send_info_to_server(info_to_send)
# EXAMPLE EXAMPLE EXAMPLE
# EXAMPLE EXAMPLE EXAMPLE

#######################################################################################
#######################################################################################

while True:
    # Listening for broadcast messages
    data, server_address = broadcast_socket.recvfrom(1024)
    print(f"Received broadcast message from {server_address}: {data.decode()}")






