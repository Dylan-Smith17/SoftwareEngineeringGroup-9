import tkinter as tk
import os
from tkinter import messagebox
import socket
import json
import random
import sys
import os
cwd = os.getcwd()
sys.path.insert(0, cwd+'/DataBase')
import Player_Database
from tkinter import messagebox, ttk


def add_player_to_database(player_name, id):
    Player_Database.addPlayer(player_name, id)

# Placeholder for UDP socket communication (replace with actual UDP code)
def send_equipment_code_via_udp(player_name, equipment_code):
    print(f"Sending {player_name}'s equipment code {equipment_code} via UDP")
    # Here you would have the code to send the equipment code via UDP
    # For now, it's just a print statement
    # Example: udp.send_equipment_code(player_name, equipment_code)

class PlayerEntryScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Player Entry Screen")
        self.geometry("800x600")

        # Define teams and Treeview columns
        self.teams = {'Red Team': [], 'Green Team': []}
        self.columns = ('player_name', 'player_id')

        # Create Treeview for each team
        self.create_team_table('Red Team', 'red')
        self.create_team_table('Green Team', 'green')

        # Entry for player names
        self.player_name_entry = tk.Entry(self, width=50)
        self.player_name_entry.pack(pady=20)

        # Buttons for adding players
        self.add_red_player_button = tk.Button(self, text="Add to Red Team", command=lambda: self.add_player('Red Team'))
        self.add_green_player_button = tk.Button(self, text="Add to Green Team", command=lambda: self.add_player('Green Team'))
        self.add_red_player_button.pack(side=tk.LEFT, padx=20)
        self.add_green_player_button.pack(side=tk.RIGHT, padx=20)

    def create_team_table(self, team_name, team_color):
        frame = tk.LabelFrame(self, text=team_name, fg=team_color, labelanchor='n', padx=5, pady=5)
        frame.pack(side=tk.LEFT if team_color == 'red' else tk.RIGHT, fill=tk.BOTH, expand=True)
        tree = ttk.Treeview(frame, columns=self.columns, show='headings')
        tree.heading('player_name', text='Player Name')
        tree.heading('player_id', text='Player ID')
        tree.column('player_name', width=120)
        tree.column('player_id', width=80)
        tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.teams[team_name] = tree  # Store the treeview in the teams dictionary

    def add_player(self, team):
        player_name = self.player_name_entry.get()
        if player_name:
            # player_id = f"ID-{random.randint(100, 999)}"
            player_id = random.randint(100, 999)
            # Insert the player into the treeview
            self.teams[team].insert('', 'end', values=(player_name, player_id))

            # Clear the entry field for the next input
            self.player_name_entry.delete(0, tk.END)
            add_player_to_database(player_name,player_id)
        else:
            messagebox.showwarning("Warning", "Player name cannot be empty.")

if __name__ == "__main__":
    app = PlayerEntryScreen()
    app.mainloop()

Player_Database.write_data_to_json(Player_Database.readAll())

#sudo apt-get install python3-tk
