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

# Get the current working directory and set path for database access
cwd = os.getcwd()
sys.path.insert(0, cwd+'/DataBase')

# Import required module (Player_Database) for database interaction
# import Player_Database

from tkinter import messagebox, ttk

class PlayerActionScreen(tk.Tk):
    def __init__(self, players, event_queue, closing_timer=6*60):
        super().__init__()
        # Set window title, size, and background color
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
        self.players = players
        self.event_queue = event_queue

        # Create the GUI layout
        self.create_gui()

        # Start the timer and event listener threads
        self.start_timer()
        self.init_event_listener()

        # Close the window after the timer expires
        self.window_timer()

    def create_gui(self):
        # Create frames for different sections of the GUI
        self.init_frames()

        # Create designations to display text
        self.init_designations()

    def init_frames(self):
        # Create frames for different sections of the GUI
        self.frameRed = Frame(width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameGreen = Frame(width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameTimer = Frame(width=self.player_frame_y, height=self.player_frame_x, padx=70, pady=20, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameEventBoxLeft = Frame(width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20, bg="black")
        self.frameEventBoxCenter = Frame(width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20, bg="black")
        self.frameEventBoxRight = Frame(width=self.player_frame_y, height=self.player_frame_x, padx=20, pady=20, bg="black")

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

    def init_designations(self):
        # Create designation labels to display text
        Label(self.frameRed, text="ALPHA RED", bg="black", font=self.helvetica_Medium, fg="red").grid(row=0, column=0, sticky="nsew")
        Label(self.frameGreen, text="ALPHA GREEN", bg="black", font=self.helvetica_Medium, fg="green").grid(row=0, column=0, sticky="nsew")
        Label(self.frameEventBoxCenter, text="PHOTON EVENTS", bg="black", font=self.helvetica_Medium, fg="white").grid(row=0, column=1, sticky="new")

    def start_timer(self):
        # Start a thread to update the timer
        self.seconds = StringVar()
        Label(self.frameTimer, textvariable=self.seconds, bg="black", font="Helvetica 50", fg="yellow").grid(row=0, column=1, sticky="n")
        self.timer_update()

    def timer_update(self):
        # Update the timer every second until it reaches zero
        if self.closing_timer >= 0:
            self.seconds.set(self.minute_second_conv(self.closing_timer))
            self.closing_timer -= 1
            self.after(1000, self.timer_update)
        else:
            self.destroy()

    def minute_second_conv(self, seconds):
        # Convert seconds to minutes and seconds format
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
        # Update the scores displayed on the GUI
        self.update_scoreboard_designations(self.frameEventBoxLeft, self.alpha_red_score, "red")
        self.update_scoreboard_designations(self.frameEventBoxRight, self.alpha_green_score, "green")

    def update_scoreboard_designations(self, frame, score, color):
        # Update the designations for displaying scores
        for widget in frame.winfo_children():
            widget.destroy()
        Label(frame, text=score, bg="black", font="Helvetica 50", fg=color).grid(row=1, column=1, sticky="new")

    def add_events(self, event_string):
        # Add events to the event window and update the display
        self.update_event_designations()
        if len(self.event_list) > 8:
            self.event_list.pop(0)
        self.event_list.append(event_string)
        for i, event in enumerate(self.event_list):
            Label(self.frameEventBoxCenter, text=event, bg="black", font=self.helvetica_Medium, fg="red" if "red" in event else "green").grid(row=i + 1, column=1, sticky="n")

    def update_event_designations(self):
        # Update the label for the event window
        for widget in self.frameEventBoxCenter.winfo_children():
            widget.destroy()
        Label(self.frameEventBoxCenter, text="PHOTON EVENTS", bg="black", font=self.helvetica_Medium, fg="white").grid(row=0, column=1, sticky="n")

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

