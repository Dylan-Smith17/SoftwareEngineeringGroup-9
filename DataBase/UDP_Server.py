import socket
import selectors
from supabase import create_client
import os
from Player_Database import get_supabase

# Set up Supabase client
supabase = get_supabase()

def send_info_to_client(info, broadcast_socket, broadcast_port):
    try:
        if not info:
            raise ValueError("Info cannot be blank")
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

        # Parse received data
        received_data = data.decode().split(':')
        transmitter_id = int(received_data[0])
        receiver_id = int(received_data[1])

        # Fetch player information from the database
        transmitter_name = get_by_id(transmitter_id)
        receiver_name = get_by_id(receiver_id)

        if transmitter_name and receiver_name:
            print(f"Transmitter: {transmitter_name}, Receiver: {receiver_name}")

            # Handle different codes
            if transmitter_id == receiver_id:
                # Player tags themselves on their own team
                send_info_to_client(str(transmitter_id), broadcast_socket, broadcast_port)
            else:
                # Player hit another player
                send_info_to_client(str(receiver_id), broadcast_socket, broadcast_port)

                # Check if scoring event
                if transmitter_id == 53 and receiver_id == 43:
                    # Red base scored
                    update_score(transmitter_id, 100)
                elif transmitter_id == 43 and receiver_id == 53:
                    # Green base scored
                    update_score(transmitter_id, 100)

    except socket.error as se:
        print(f"Socket error: {se}")
    except Exception as e:
        print(f"An error occurred while receiving data: {e}")

def update_score(player_id, points):
    # Update player's score in the database
    player = supabase.table('player').select('*').eq('id', player_id).execute()
    if player['count'] > 0:
        current_score = player['data'][0]['score']
        new_score = current_score + points
        supabase.table('player').update({'score': new_score}).eq('id', player_id).execute()
        print(f"Updated score of player {player_id} to {new_score}")

def get_by_id(player_id):
    # Retrieve player's name from the database using ID
    player = supabase.table('player').select('codename').eq('id', player_id).execute()
    if player['count'] > 0:
        return player['data'][0]['codename']
    else:
        return None

print("Server is listening...")

# Set up broadcast socket
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set up receiving socket
receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receive_port = 7501
broadcast_port = 7500
receive_socket.bind(("", receive_port)) 

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

