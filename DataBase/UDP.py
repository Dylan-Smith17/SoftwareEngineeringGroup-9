# UDP
#
# Team 9
#
# 02/18/24

import socket
# Server side
server_ip = '127.0.0.1'
server_port = 7500
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))
while True:
    data, client_address = server_socket.recvfrom(1024)
    # Handle incoming data and send response back to the client
# Client side
client_ip = '192.168.86.70'
client_port = 7501
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Send message to server
server_address = (server_ip, server_port)
message = "Hello, server!"
client_socket.sendto(message.encode(), server_address)
# Receive response from server
response, server_address = client_socket.recvfrom(1024)
# Handle response
