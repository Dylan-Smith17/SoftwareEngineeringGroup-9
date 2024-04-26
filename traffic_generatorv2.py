
import socket
import random
import time
import os
import sys
cwd = os.getcwd()
sys.path.insert(0, cwd + '/DataBase')
from UDP_Client import send_data_over_udp, receive_info_from_server

# Configuration
bufferSize = 1024
serverAddressPort = ("127.0.0.1", 7500)
clientAddressPort = ("127.0.0.1", 7501)

def simulated_start():
    send_data_over_udp('202')
def wait_for_start() -> None:
    print("\nWaiting for start from game software")
    received_data = ''
    while received_data != '202':
        received_data = receive_info_from_server()
        print(f"Received from game software: {received_data}")
# Function to simulate game end
def simulate_game_end():
    print("Simulating game end.")
    end_message = '221'
    for _ in range(3):  # Send the end code three times
        send_data_over_udp(end_message)

# Function to simulate a hit
def simulate_hit(sender, receiver):
    message = f"{sender}:{receiver}"
    print(f"Transmitting hit: {message}")
    send_data_over_udp(message)

# Function to simulate base hit
def simulate_base_hit(player_id, base_code):
    message = f"{player_id}:{base_code}"
    print(f"Transmitting base hit: {message}")
    send_data_over_udp(message)

# Main traffic generation logic
def generate_traffic(red_players, green_players):
    #simulated_start()
    wait_for_start()
    time.sleep(2)  # Wait for game software to process the start code

    for _ in range(30):  # Run the simulation for 30 interactions
        red_player = random.choice(red_players)
        green_player = random.choice(green_players)
        rand_temp = random.randint(0,1)
        if rand_temp == 0:
            simulate_hit(red_player, green_player)
        else:
            simulate_hit(green_player, red_player)
        
        # Simulate base hit after every 10 interactions
        if _ % 10 == 0:
            simulate_base_hit(random.choice(red_players), "43")
            simulate_base_hit(random.choice(green_players), "53")

        time.sleep(random.randint(1, 3))
    simulate_hit(1,3) #show that if player hits teammate: -10 points

    #simulate_game_end()

# Run the traffic generator
if __name__ == "__main__":
    red_players = [1,3]
    green_players = [2,4]
    generate_traffic(red_players, green_players)
