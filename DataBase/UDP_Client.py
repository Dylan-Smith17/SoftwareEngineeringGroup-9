# UDP
#
# Team 9
#
# 02/18/24
#
# sender.py

import socket

def send_info_to_server(info, serverIP, send_port):
<<<<<<< HEAD
    try:
        # Check if info is blank
        if not info:
            raise ValueError("Info cannot be blank")

        # Set up sending socket
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Sending information to the server
        send_socket.sendto(info.encode(), (serverIP, send_port))
        send_socket.close()

    except ValueError as ve:
        print(f"Error: {ve}")
    except socket.error as se:
        print(f"Socket error: {se}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def receive_info_from_server(serverIP):
    try:
        broadcast_port = 7500
        # Set up broadcast socket for listening
        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcast_socket.bind((serverIP, broadcast_port))
        # Listening for broadcast messages
        data, server_address = broadcast_socket.recvfrom(1024)
        print(f"Received broadcast message from {server_address}: {data.decode()}")
        # Close the receiving socket after use
        broadcast_socket.close()

    except socket.error as se:
        print(f"Socket error: {se}")
    except Exception as e:
        print(f"An error occurred while receiving information: {e}")
=======
    # Sends information to a server using UDP.
    #
    # Parameters:
    # info (str): The information to be sent.
    # serverIP (str): The IP address of the server.
    # send_port (int): The port on the server to which the information will be sent.

    # Set up sending socket
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Sending information to the server
    send_socket.sendto(info.encode(), (serverIP, send_port))
    send_socket.close()

def receive_info_from_server():
    # Function to receive information from the server using UDP broadcast.
    #
    # This function sets up a broadcast socket to listen for messages from the server
    # and prints the received message along with the server address.
    #
    # Note: Make sure `serverIP` is defined before calling this function.
    #
    # Parameters:
    # None
    #
    # Returns:
    # None

    broadcast_port = 7500
    # Set up broadcast socket for listening
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_socket.bind((serverIP, broadcast_port))
    # Listening for broadcast messages
    data, server_address = broadcast_socket.recvfrom(1024)
    print(f"Received broadcast message from {server_address}: {data.decode()}")
    # Close the receiving socket after use
    broadcast_socket.close()
>>>>>>> 9bbfdf71f9b011635da06743ef6d89f5ccf1cebb

# Example: Call the function from another file
info_to_send = "hello"
serverIP = "0.0.0.0"  # this IP address is a general address to test on the same
                    # machine. If you want to use the server IP, then use this
                    # line of code
                    # serverIP = "192.168.1.100"
send_port = 7501

# Send information to the server
send_info_to_server(info_to_send, serverIP, send_port)

# Receive information from the server
receive_info_from_server(serverIP)





