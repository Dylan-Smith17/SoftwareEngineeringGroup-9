import random
import time
from UDP_Client import send_data_over_udp
from Player_Database import addPlayer, getPlayer

# Function to simulate adding players
def add_players():
    # Example player data
    players = [
        {"id": 1, "name": "Player 1", "score": 0},
        {"id": 2, "name": "Player 2", "score": 0},
        {"id": 3, "name": "Player 3", "score": 0},
        {"id": 4, "name": "Player 4", "score": 0}
    ]

    for player in players:
        addPlayer(player['name'], player['id'])
        print(f"Added player: {player['name']}")

# Function to simulate team scores
def simulate_team_scores():
    # Example team scores
    teams = {"red": 0, "blue": 0, "green": 0}

    for team, score in teams.items():
        # Simulate sending team scores over UDP
        send_data_over_udp({"team": team, "score": score})
        print(f"Sent team score for Team {team}: {score}")

# Function to get player names
def get_player_names(player_ids):
    player_names = getPlayer(player_ids)
    for player_id, player_name in player_names.items():
        print(f"Player ID: {player_id}, Name: {player_name}")

# Main function
def main():
    # Add players
    print("Adding players...")
    add_players()

    # Simulate team scores
    print("\nSimulating team scores...")
    simulate_team_scores()

    # Get player names
    print("\nGetting player names...")
    player_ids = [1, 2, 3, 4]  # Example player IDs
    get_player_names(player_ids)

    print("\nTest completed successfully.")

if __name__ == "__main__":
    main()
