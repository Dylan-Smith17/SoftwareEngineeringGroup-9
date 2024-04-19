# UDP_Client.py
#
# Team 9
#
# 03/17/24
#
# sender.py

######################################################################################
# Sends information to a server using UDP.
#
# Parameters
#------------
# info (str): The information to be sent.
# serverIP (str): The IP address of the server.
# send_port (int): The port on the server to which the information will be sent.
######################################################################################

import socket
import json

# Function to send data over UDP
def send_data_over_udp(json_data, host='192.168.1.100', port=7500):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        json_bytes = json.dumps(json_data).encode('utf-8')
        sock.sendto(json_bytes, (host, port))

def main():
    # Example: Define information to send
    info_to_send = "1"

    try:
        # Send information to server using UDP
        send_data_over_udp(info_to_send)
        print(f"Sent '{info_to_send}' to server.")

    except Exception as e:
        print(f"An error occurred while sending data: {e}")

if __name__ == "__main__":
    main()
