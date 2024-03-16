import time
import tkinter as tk
from tkinter import Label, Frame, StringVar
import threading
from queue import Queue
#
import os
from tkinter import messagebox
import socket
import json
import random
import sys
cwd = os.getcwd()
sys.path.insert(0, cwd+'/DataBase')
#import Player_Database
from tkinter import messagebox, ttk




class PlayerActionScreen(tk.Tk):
    def __init__(self, players, event_queue, warning_timer_seconds=6*60):
        super().__init__()
        self.title("The Actions of Photon!")  # Sets the title of the window
        self.geometry("1280x720")  # Sets the dimensions of the window
        self.configure(background='grey')  # Sets background color
        self.helveticaBig = ("Helvetica", 20, "bold")  # Defines font style
        self.helveticaSmall = ("Helvetica", 10, "bold")
        self.helveticaHuge = ("Helvetica", 30, "bold")
        self.configure(bg="black")  # Sets background color

        # Defines dimensions for player frames
        self.player_frame_heights = 720 / 2
        self.player_frame_widths = 1442 / 3

        # Initializes scores and timer settings
        self.red_score = 0
        self.green_score = 0
        self.warning_timer_seconds = warning_timer_seconds

        # Stores player and event queue data
        self.players = players
        self.event_queue = event_queue

        # Creates the GUI layout
        self.create_layout()

        # Starts the timer and event listener threads
        self.start_timer_thread()
        self.start_event_listener_thread()

        # Closes the window after the timer expires
        self.close_window_after_timer()

    def create_layout(self):
        # Creates the frames for different sections of the GUI
        self.create_frames()

        # Creates labels to display text
        self.create_labels()

    def create_frames(self):
        # Creates frames for different sections of the GUI
        self.frameRed = Frame(width=self.player_frame_widths, height=self.player_frame_heights, padx=20, pady=20, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameGreen = Frame(width=self.player_frame_widths, height=self.player_frame_heights, padx=20, pady=20, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameTimer = Frame(width=self.player_frame_widths, height=self.player_frame_heights, padx=70, pady=20, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
        self.frameEventBoxLeft = Frame(width=self.player_frame_widths, height=self.player_frame_heights, padx=20, pady=20, bg="black")
        self.frameEventBoxCenter = Frame(width=self.player_frame_widths, height=self.player_frame_heights, padx=20, pady=20, bg="black")
        self.frameEventBoxRight = Frame(width=self.player_frame_widths, height=self.player_frame_heights, padx=20, pady=20, bg="black")

        # Arranges frames in the grid layout
        self.frameRed.grid(row=0, column=0, sticky="nsew")
        self.frameGreen.grid(row=0, column=2, sticky="nsew")
        self.frameTimer.grid(row=0, column=1, sticky="nsew")
        self.frameEventBoxLeft.grid(row=1, column=0, sticky="nsew")
        self.frameEventBoxCenter.grid(row=1, column=1, sticky="nsew")
        self.frameEventBoxRight.grid(row=1, column=2, sticky="nsew")

    def create_labels(self):
        # Creates labels to display text
        Label(self.frameRed, text="ALPHA RED", bg="black", font=self.helveticaBig, fg="red").grid(row=0, column=0, sticky="e")
        Label(self.frameGreen, text="ALPHA GREEN", bg="black", font=self.helveticaBig, fg="green").grid(row=0, column=0, sticky="w")
        Label(self.frameEventBoxCenter, text="PHOTON EVENTS", bg="black", font=self.helveticaBig, fg="white").grid(row=0, column=1, sticky="new")

    def start_timer_thread(self):
        # Starts a thread to update the timer
        self.seconds = StringVar()
        Label(self.frameTimer, textvariable=self.seconds, bg="black", font="Helvetica 50", fg="yellow").grid(row=0, column=1, sticky="n")
        self.update_timer()

    def update_timer(self):
        # Updates the timer every second until it reaches zero
        if self.warning_timer_seconds >= 0:
            self.seconds.set(self.get_minute_second_string(self.warning_timer_seconds))
            self.warning_timer_seconds -= 1
            self.after(1000, self.update_timer)
        else:
            self.destroy()

    def get_minute_second_string(self, seconds):
        # Converts seconds to minutes and seconds format
        minutes = seconds // 60
        seconds %= 60
        return f"{minutes:02d}:{seconds:02d}"

    def start_event_listener_thread(self):
        # Starts a thread to listen for events
        self.event_listener_thread = threading.Thread(target=self.listen_for_events)
        self.event_listener_thread.daemon = True
        self.event_listener_thread.start()

    def listen_for_events(self):
        # Listens for events from the queue and update scores and events accordingly
        while True:
            event_data = self.event_queue.get().split(":")
            codename_one = self.get_codename(event_data[0])
            codename_two = self.get_codename(event_data[1])
            event_string = f"{codename_one} hit {codename_two}"

            if "red" in event_data[0]:
                self.red_score += 10
            else:
                self.green_score += 10

            self.update_scores()
            self.add_events_to_window(event_string)
            self.event_queue.task_done()

    def get_codename(self, player_id):
        # Gets the codename of the player based on their ID
        for team in self.players.values():
            for player in team:
                if str(player["id"]) == player_id:
                    return player["codename"]

    def update_scores(self):
        # Updates the scores displayed on the GUI
        self.update_score_label(self.frameEventBoxLeft, self.red_score, "red")
        self.update_score_label(self.frameEventBoxRight, self.green_score, "green")

    def update_score_label(self, frame, score, color):
        # Updates the label for displaying scores
        for widget in frame.winfo_children():
            widget.destroy()
        Label(frame, text=score, bg="black", font="Helvetica 50", fg=color).grid(row=1, column=1, sticky="new")

    def add_events_to_window(self, event_string):
        # Adds events to the event window and update the display
        self.update_events_label()
        if len(self.event_list) > 8:
            self.event_list.pop(0)
        self.event_list.append(event_string)
        for i, event in enumerate(self.event_list):
            Label(self.frameEventBoxCenter, text=event, bg="black", font=self.helveticaBig, fg="red" if "red" in event else "green").grid(row=i + 1, column=1, sticky="n")

    def update_events_label(self):
        # Updates the label for the event window
        for widget in self.frameEventBoxCenter.winfo_children():
            widget.destroy()
        Label(self.frameEventBoxCenter, text="PHOTON EVENTS", bg="black", font=self.helveticaBig, fg="white").grid(row=0, column=1, sticky="n")

    def close_window_after_timer(self):
        # Closes the window after the timer expires
        self.after((self.warning_timer_seconds + 1) * 1000, self.destroy)

if __name__ == '__main__':
    # Samples player data and event queue
    players_data = {
        "red_users": [{"id": 1, "codename": "RedPlayer1"}, {"id": 2, "codename": "RedPlayer2"}],
        "green_users": [{"id": 3, "codename": "GreenPlayer1"}, {"id": 4, "codename": "GreenPlayer2"}]
    }
    event_queue = Queue()

    # Creates and runs the application
    app = PlayerActionScreen(players_data, event_queue)
    app.mainloop()
