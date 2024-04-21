import socket
import random
import time

bufferSize  = 1024
serverAddressPort   = ("127.0.0.1", 7501)  # Matching UDP server's address and port

print('This program will generate some test traffic for 2 players on the red team as well as 2 players on the green team')
print('')

red1 = input('Enter equipment id of red player 1 ==> ')
red2 = input('Enter equipment id of red player 2 ==> ')
green1 = input('Enter equipment id of green player 1 ==> ')
green2 = input('Enter equipment id of green player 2 ==> ')

# Create datagram socket
UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Wait for start from game software
print ("")
print ("Waiting for start from game_software")

received_data = ' '
while received_data != '202':
    received_data, address = UDPClientSocketTransmit.recvfrom(bufferSize)
    received_data = received_data.decode('utf-8')
    print ("Received from game software: " + received_data)
print ('')

# Create events, random player and order
counter = 0

while True:
    if random.randint(1,2) == 1:
        redplayer = red1
    else:
        redplayer = red2

    if random.randint(1,2) == 1:
        greenplayer = green1
    else: 
        greenplayer = green2    

    if random.randint(1,2) == 1:
        message = str(redplayer) + ":" + str(greenplayer)
    else:
        message = str(greenplayer) + ":" + str(redplayer)
        
    # After 10 iterations, send base hit
    if counter == 10:
        message = str(redplayer) + ":43"
    if counter == 20:
        message = str(greenplayer) + ":53"
        
    print("Transmitting to game: " + message)
    
    UDPClientSocketTransmit.sendto(str.encode(str(message)), serverAddressPort)
    
    # Receive answer from game software
    received_data, address = UDPClientSocketTransmit.recvfrom(bufferSize)
    received_data = received_data.decode('utf-8')
    print ("Received from game software: " + received_data)
    print ('')
    
    counter = counter + 1
    if received_data == '221':
        break
    time.sleep(random.randint(1,3))
    
print("Program complete")
