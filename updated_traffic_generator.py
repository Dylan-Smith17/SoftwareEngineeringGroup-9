
import socket
import random
import time

# Configuration
bufferSize = 1024
serverAddressPort = ("127.0.0.1", 7500)
clientAddressPort = ("127.0.0.1", 7501)

# Initialize UDP sockets
UDPServerSocketReceive = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind server socket
UDPServerSocketReceive.bind(serverAddressPort)

# Function to simulate game start
def simulate_game_start():
    print("Simulating game start.")
    start_message = '202'
    UDPClientSocketTransmit.sendto(start_message.encode(), clientAddressPort)

# Function to simulate game end
def simulate_game_end():
    print("Simulating game end.")
    end_message = '221'
    for _ in range(3):  # Send the end code three times
        UDPClientSocketTransmit.sendto(end_message.encode(), clientAddressPort)

# Function to simulate a hit
def simulate_hit(sender, receiver):
    message = f"{sender}:{receiver}"
    print(f"Transmitting hit: {message}")
    UDPClientSocketTransmit.sendto(message.encode(), clientAddressPort)

# Function to simulate base hit
def simulate_base_hit(player_id, base_code):
    message = f"{player_id}:{base_code}"
    print(f"Transmitting base hit: {message}")
    UDPClientSocketTransmit.sendto(message.encode(), clientAddressPort)

# Main traffic generation logic
def generate_traffic(red_players, green_players):
    simulate_game_start()
    time.sleep(2)  # Wait for game software to process the start code

    for _ in range(30):  # Run the simulation for 30 interactions
        red_player = random.choice(red_players)
        green_player = random.choice(green_players)
        simulate_hit(red_player, green_player)

        # Simulate base hit after every 10 interactions
        if _ % 10 == 0:
            simulate_base_hit(random.choice(red_players), "43")
            simulate_base_hit(random.choice(green_players), "53")

        time.sleep(random.randint(1, 3))

    simulate_game_end()

# Run the traffic generator
if __name__ == "__main__":
    red_players = [input('Enter equipment id of red player 1 ==> '), input('Enter equipment id of red player 2 ==> ')]
    green_players = [input('Enter equipment id of green player 1 ==> '), input('Enter equipment id of green player 2 ==> ')]
    generate_traffic(red_players, green_players)
