import socket

msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)

# Replace with the actual IP address of your UDP server
serverAddress = ("192.168.1.100", 7500)

# Create a UDP socket at the client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

try:
    # Send the message to the server using the created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddress)

    # Receive the response from the server
    msgFromServer, serverAddress = UDPClientSocket.recvfrom(1024)

    # Decode the received bytes into a string
    msg = "Message from Server: {}".format(msgFromServer.decode('utf-8'))
    print(msg)

except Exception as e:
    print("Error:", e)

finally:
    UDPClientSocket.close()
