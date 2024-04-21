import time
import tkinter as tk
from tkinter import Label, Frame, StringVar
import threading
from queue import Queue
import os
from tkinter import messagebox
import socket
import json
import random
import sys
from playsound import playsound

# Get the current working directory and set path for database access
cwd = os.getcwd()
sys.path.insert(0, cwd + '/DataBase')

# Import required module (Player_Database) for database interaction
# import Player_Database

from tkinter import messagebox, ttk


class PlayerActionScreen(tk.Tk):
    def __init__(self, player_data, event_queue, closing_timer=390):
        super().__init__()
        self.title("The Actions of Photon!")
        self.geometry("1280x720")
        self.configure(background='grey')
        self.configure(bg="black")

# Define font styles
        self.helvetica_Small = ("Helvetica", 10, "bold")
        self.helvetica_Medium = ("Helvetica", 20, "bold")
        self.helvetica_Large = ("Helvetica", 30, "bold")

        # Define dimensions for player frames
        self.player_frame_x = 720 / 2
        self.player_frame_y = 1442 / 3

        # Initialize scoreboard and timer settings
        self.alpha_red_score = 0
        self.alpha_green_score = 0
        self.closing_timer = closing_timer

        # Store player and event queue data
        self.players = player_data
        self.event_queue = event_queue

        # Create the GUI layout
        self.create_gui()

        # Start the timer and event listener threads
        self.start_timer()
        self.init_event_listener()
        #flash highest score
        self.flash_highest_score()
        # Close the window after the timer expires
        self.window_timer()

    def load_player_data(self):
        # Load player data from data.json
        try:
            with open('data.json', 'r') as file:
                players_data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "data.json file not found")
            players_data = []
        return players_data

    def create_gui(self):
        # Create frames for different sections of the GUI
        self.init_frames()

        # Create designations to display text
        self.init_designations()

        # Display player names in team windows
        self.display_players()

    def init_frames(self):
        # Create frames for different sections of the GUI
        self.frameRed = Frame(self, width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20, bg="black",
                              highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameGreen = Frame(self, width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20,
                                bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameTimer = Frame(self, width=self.player_frame_y, height=self.player_frame_x, padx=70, pady=20,
                                bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameEventBoxLeft = Frame(self, width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20,
                                       bg="black")
        self.frameEventBoxCenter = Frame(self, width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20,
                                         bg="black")
        self.frameEventBoxRight = Frame(self, width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20,
                                        bg="black")

        # Arrange frames in the grid layout
        self.frameRed.grid(row=0, column=0, sticky="nsew")
        self.frameGreen.grid(row=0, column=2, sticky="nsew")
        self.frameTimer.grid(row=0, column=1, sticky="nsew")
        self.frameEventBoxLeft.grid(row=1, column=0, sticky="nsew")
        self.frameEventBoxCenter.grid(row=1, column=1, sticky="nsew")
        self.frameEventBoxRight.grid(row=1, column=2, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
    def flash_highest_score(self):
        # Get the highest score and corresponding team color
        highest_score = max(self.alpha_red_score, self.alpha_green_score)
        team_color = "red" if self.alpha_red_score > self.alpha_green_score else "green"

        # Flash the score label of the team with the highest score
        if team_color == "red":
            score_label = self.red_score_label
        else:
            score_label = self.green_score_label

        # Toggle the score label between visible and invisible with a short delay
        if highest_score > 0:
            self.toggle_score_label(score_label)
            self.after(500, self.flash_highest_score)

    def toggle_score_label(self, label):
        current_state = label.cget("state")
        new_state = "normal" if current_state == "hidden" else "hidden"
        label.config(state=new_state)


    def init_designations(self):
        # Create designation labels to display text
        Label(self.frameRed, text="ALPHA RED", bg="black", font=self.helvetica_Medium, fg="red").grid(row=0, column=0,
                                                                                                      sticky="nsew")
        Label(self.frameGreen, text="ALPHA GREEN", bg="black", font=self.helvetica_Medium, fg="green").grid(row=0,
                                                                                                            column=0,
                                                                                                            sticky="nsew")
        Label(self.frameEventBoxCenter, text="PHOTON EVENTS", bg="black", font=self.helvetica_Medium, fg="white").grid(
            row=0, column=1, sticky="new")

    def display_players(self):
    # Iterate through each team and their players
        for team, players in self.players.items():
            for player in players:
                # Check if 'player' is a dictionary and has 'id' and 'codename' keys
                if isinstance(player, dict) and 'id' in player and 'codename' in player:
                    # Assign teams to different frames based on some logic, for example, team names
                    team_frame = self.frameRed if 'red' in team.lower() else self.frameGreen
                    Label(team_frame, text=player['codename'], bg="black", fg="white", font=self.helvetica_Medium).pack()
                else:
                    print(f"Invalid player data: {player}")


    def start_timer(self):
        # Start a thread to update the timer
        self.seconds = StringVar()
        Label(self.frameTimer, textvariable=self.seconds, bg="black", font="Helvetica 50", fg="yellow").grid(row=0, column=1, sticky="n")
        self.timer_update()



    def play_sound(self):
        x = random.randint(1, 6)
        x = random.randint(1, 8)
        playsound(cwd + '/photon-main/photon_tracks/Track0' + str(x) + '.mp3')  

    def timer_update(self):
        # Update the timer every second until it reaches zero
        if self.closing_timer >= 0:
            self.seconds.set(self.minute_second_conv(self.closing_timer))
            if self.closing_timer == 375:
                t = threading.Thread(target=self.play_sound)
                t.start()
            if 365 <= self.closing_timer <= 360:
                time.sleep(.2)
            self.closing_timer -= 1
            self.after(1000, self.timer_update)
        else:
            self.destroy()

    def minute_second_conv(self, seconds):
        # Convert seconds to minutes and seconds format
        if seconds > 360:
            seconds -= 360
            return f"{seconds:02d}"
        minutes = seconds // 60
        seconds %= 60
        return f"{minutes:02d}:{seconds:02d}"

    def init_event_listener(self):
        # Start a thread to listen for events
        self.event_listener_thread = threading.Thread(target=self.event_listener)
        self.event_listener_thread.daemon = True
        self.event_listener_thread.start()

    def event_listener(self):
        # Listen for events from the queue and update scores and events accordingly
        while True:
            event_data = self.event_queue.get().split(":")
            player_name_one = self.get_player_name(event_data[0])
            player_name_two = self.get_player_name(event_data[1])
            event_string = f"{player_name_one} hit {player_name_two}"

            if "red" in event_data[0]:
                self.alpha_red_score += 10
            else:
                self.alpha_green_score += 10

            self.update_scoreboard()
            self.add_events(event_string)
            self.event_queue.task_done()

    def get_player_name(self, player_id):
        # Get the player name based on their ID
        for team in self.players.values():
            for player in team:
                if str(player["id"]) == player_id:
                    return player["player_name"]

    def update_scoreboard(self):
        # Sort players by their scores from highest to lowest
        sorted_players = sorted(self.players["alpha_red_users"] + self.players["alpha_green_users"],
                                key=lambda x: x["score"], reverse=True)

        # Update the scoreboard for both teams
        self.update_scoreboard_designations(self.frameEventBoxLeft, sorted_players, "red")
        self.update_scoreboard_designations(self.frameEventBoxRight, sorted_players, "green")

    def update_scoreboard_designations(self, frame, sorted_players, color):
        # Update the designations for displaying scores
        for widget in frame.winfo_children():
            widget.destroy()

        # Display player scores in the frame
        for i, player in enumerate(sorted_players):
            if player["color"] == color:
                Label(frame, text=f"{player['player_name']}: {player['score']}", bg="black", font="Helvetica 12",
                      fg=color).grid(row=i + 1, column=1, sticky="new")

    def add_events(self, event_string):
        # Add events to the event window and update the display
        self.update_event_designations()
        if len(self.event_list) > 8:
            self.event_list.pop(0)
        self.event_list.append(event_string)
        for i, event in enumerate(self.event_list):
            Label(self.frameEventBoxCenter, text=event, bg="black", font=self.helvetica_Medium,
                  fg="red" if "red" in event else "green").grid(row=i + 1, column=1, sticky="n")

    def update_event_designations(self):
        # Update the label for the event window
        for widget in self.frameEventBoxCenter.winfo_children():
            widget.destroy()
        Label(self.frameEventBoxCenter, text="PHOTON EVENTS", bg="black", font=self.helvetica_Medium, fg="white").grid(
            row=0, column=1, sticky="n")

    def window_timer(self):
        # Close the window after the timer expires
        self.after((self.closing_timer + 1) * 1000, self.destroy)


# For testing purposes
if __name__ == '__main__':
    # Sample player data and event queue
    player_data = {
        "alpha_red_users": [{"id": 1, "player_name": "Alpha_Red_Player_1"}, {"id": 2, "player_name": "Alpha_Red_Player_2"}],
        "alpha_green_users": [{"id": 3, "player_name": "Alpha_Green_Player_1"}, {"id": 4, "player_name": "Alpha_Green_Player_2"}]
    }
    event_queue = Queue()

    # Create and run the application
    app = PlayerActionScreen(player_data, event_queue)
    app.mainloop()
