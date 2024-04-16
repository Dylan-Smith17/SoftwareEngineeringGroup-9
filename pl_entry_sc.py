import tkinter as tk
import os
from tkinter import messagebox
import socket
import json
import random
import sys
import os
from tkinter import simpledialog
cwd = os.getcwd()
sys.path.insert(0, cwd+'/DataBase')
import Player_Database#, UDP_Client, UDP_Server
from tkinter import messagebox, ttk
import socket

# Create the broadcast socket
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def add_player_to_database(player_name, id):
    Player_Database.addPlayer(player_name, id)

# Placeholder for UDP socket communication (replace with actual UDP code)
def send_equipment_code_via_udp(player_name, equipment_code):
    """Sends player name and equipment code to the server via UDP.

    Args:
        player_name (str): Name of the player.
        equipment_code (int): Equipment code for the player.
    """

    print(f"Sending {player_name}'s equipment code {equipment_code} via UDP")

    # Create a dictionary to store player data
    data_to_send = {"player_name": player_name, "equipment_code": equipment_code}

    # Convert data to JSON string
    json_data = json.dumps(data_to_send)

    # Specify server IP address
    server_ip = "127.0.1.1"  # Replace with the actual server IP if needed

    # Use UDP_Client.send_info_to_server to send the JSON data
    #UDP_Client.send_info_to_server(json_data, server_ip, 1024)


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

        

        # Label and entry for player names
        # self.player_name_label = tk.Label(self, text="Player Name:")
        # self.player_name_label.pack(pady=10)
        # self.player_name_entry = tk.Entry(self, width=50)
        # self.player_name_entry.pack(pady=10)

        # Label and entry for player IDs
        self.player_id_label = tk.Label(self, text="Player ID:")
        self.player_id_label.pack(pady=10)
        self.player_id_entry = tk.Entry(self, width=50)
        self.player_id_entry.pack(pady=10)

        # Label and entry for hardware IDs
        self.equipment_id_label = tk.Label(self, text="Equipment ID:")
        self.equipment_id_label.pack(pady=10)
        self.equipment_id_entry = tk.Entry(self, width=50)
        self.equipment_id_entry.pack(pady=10)
        

        self.key_label = tk.Label(self, text= "f5 to start, f12 to clear all names")
        self.key_label.pack(pady=10)
        self.entered_label = tk.Label(self, text= "")
        self.entered_label.pack(pady=10)

        # Buttons for adding players
        self.add_red_player_button = tk.Button(self, text="Add to Red Team", command=lambda: self.add_player('Red Team'))
        self.add_green_player_button = tk.Button(self, text="Add to Green Team", command=lambda: self.add_player('Green Team'))
        self.add_red_player_button.pack(side=tk.LEFT, padx=20)
        self.add_green_player_button.pack(side=tk.RIGHT, padx=20)


    def show_popup(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        user_input = simpledialog.askstring(title="New ID", prompt="Enter Codename :")
        if user_input is None:  # User clicked 'Cancel'
            user_input = ''
        print("User entered: ", user_input)
        return user_input



        

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

    def no_forbiddens(self, id): 
        forbidden_list = [7500, 7501, 202, 221, 53, 43]
        
        for i in forbidden_list:
            if id == i : return False
        return True
            
        
    def add_player(self, team):
        player_id = self.player_id_entry.get()
        equipment_id = self.equipment_id_entry.get()
        if player_id.isdigit() and equipment_id.isdigit():
                player_id = int(player_id)
                equipment_id = int(equipment_id)
                if  self.no_forbiddens(player_id) and self.no_forbiddens(equipment_id): #check for ids that are not valid:
                    if Player_Database.get_by_id(player_id) == '' : #if it's not a preexisting id
                        player_name = self.show_popup()
                        if player_name != '': #if the user typed in something
                            self.teams[team].insert('', 'end', values=(player_name, player_id))
                            add_player_to_database(player_name,player_id)
                        
                    else: 
                        self.teams[team].insert('', 'end', values=(Player_Database.get_by_id(player_id), player_id))
                else: messagebox.showwarning("Warning", "Invalid ID")
                
                
        else:
            messagebox.showwarning("Warning", "Invalid ID.")
    
    
    def clear_all_players(self):
        # Clear both team tables
        for team_name, tree in self.teams.items():
            tree.delete(*tree.get_children())

        # Clear entry fields for new input
        self.player_name_entry.delete(0, tk.END)
        self.player_id_entry.delete(0, tk.END)

    def run_until_f5(self):
        self.bind('<F5>', lambda event: self.destroy())  # Bind F5 to close the window
        self.bind('<F12>', lambda event: self.clear_all_players())  # Bind F12 to clear players
        self.mainloop()
if __name__ == "__main__":
    app = PlayerEntryScreen()
    app.run_until_f5()

Player_Database.write_data_to_json(Player_Database.readAll(), 'data.json')

#sudo apt-get install python3-tk