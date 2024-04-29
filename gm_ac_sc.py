import queue
import time
import threading
from PIL import Image, ImageTk
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
from tkinter import messagebox, ttk
from Player import Player
# Get the current working directory and set path for database access
cwd = os.getcwd()
sys.path.insert(0, cwd + '/DataBase')


class PlayerActionScreen(tk.Tk):
    def __init__(self, event_queue, closing_timer=365):
        super().__init__()
        self.title("The Actions of Photon!")
        self.geometry("1280x720")
        self.configure(background='grey')
        self.configure(bg="black")

        self.transmit_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receive_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receive_socket.bind(('0.0.0.0', 7501))

        # Initialize the blinking flag
        self.blinking = False


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

        self.players = []

        self.alpha_green_players = []

        self.alpha_red_players = []

        self.player_names = {}

        self.scores = {}

        self.load_player_data()

        # Initialize event que  ue
        self.event_queue = event_queue
        # Load player data
        

        self.event_list = []




        # Create the GUI layout
        self.create_gui()


        self.start_timer()

    def load_player_data(self):
        try:
            with open('data.json', 'r') as file:
                players_data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "data.json file not found")
            players_data = {}
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format")
            players_data = {}
        players_list = []
        for player in players_data:
            temp = Player(players_data[player], 0, "")
            players_list.append(temp)
        self.player_names = players_data
        self.players = players_list





    def create_gui(self):
        
        self.init_frames()

        # Create designations to display text
        self.init_designations()

        # Display player names in team windows
        self.assign_players()

        # Create labels to display team scores
        self.red_score_label = tk.Label(self.frameRed, text="0", bg="black", font="Helvetica 20 bold", fg="red")
        self.red_score_label.grid(row=1, column=0, sticky="nsew")  # Add to frameRed using grid

        self.green_score_label = tk.Label(self.frameGreen, text="0", bg="black", font="Helvetica 20 bold", fg="green")
        self.green_score_label.grid(row=1, column=0, sticky="nsew")  # Add to frameGreen using grid

        # Ensure the parent frames (self.frameRed and self.frameGreen) are created and displayed properly in your code.

       


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

    def init_designations(self):
         # Create designation labels to display text
        Label(self.frameRed, text="ALPHA RED", bg="black", font=self.helvetica_Medium, fg="red").grid(row=0, column=0,
                                                                                                      sticky="nsew")
        Label(self.frameGreen, text="ALPHA GREEN", bg="black", font=self.helvetica_Medium, fg="green").grid(row=0,
                                                                                                            column=0,
                                                                                                            sticky="nsew")
        Label(self.frameEventBoxCenter, text="PHOTON EVENTS", bg="black", font=self.helvetica_Medium, fg="white").grid(
            row=0, column=1, sticky="new")

    def assign_players(self):
        if not self.players:
                print("No player data available.")
                return

        for player in self.players:
            
            # Assign teams to different frames based on some logic, for example, team names
            team_frame = self.frameRed if int(player.id) % 2 == 0 else self.frameGreen
            if int(player.id) % 2 == 0:
                player.color = 'red'
                self.alpha_red_players.append(player)
                team_frame = self.frameRed
            else:
                player.color = 'green'
                self.alpha_green_players.append(player)
                team_frame = self.frameGreen
    def display_players(self):
            # Check and display player names in team frames based on their data
        self.alpha_red_players = sorted(self.alpha_red_players, key=lambda player: player.score, reverse=True)
        #print(self.alpha_red_players)
        self.alpha_green_players = sorted(self.alpha_green_players, key=lambda player: player.score, reverse=True)
        #print(self.alpha_green_players)
        row = 2
        for r in self.alpha_red_players:
            temp_name = self.get_player_name(r.id)
            Label(self.frameRed, text=temp_name + " : " + str(r.score), bg="black", fg="white", font=self.helvetica_Medium).grid(row=row, column=0)
            row += 1  # Increment row for the next player label
        row = 2
        for g in self.alpha_green_players:
            temp_name = self.get_player_name(g.id)
            Label(self.frameGreen, text=temp_name + " : " + str(g.score), bg="black", fg="white", font=self.helvetica_Medium).grid(row=row, column=0)
            row += 1  # Increment row for the next player label



    def start_timer(self):
            # Start a thread to update the timer
            self.seconds = StringVar()
            Label(self.frameTimer, textvariable=self.seconds, bg="black", font="Helvetica 50", fg="yellow").grid(row=0, column=1, sticky="n")
            self.timer_update()

    def play_sound(self):
        x = random.randint(1, 8)
        playsound(cwd + '/photon-main/photon_tracks/Track0' + str(x) + '.mp3')  

    def receive_from_socket(self):
        raw_message, return_address = self.receive_socket.recvfrom(1024)
        decoded_message: str = raw_message.decode("utf-8")
        self.event_queue.put(decoded_message)
        print(decoded_message)

    def timer_update(self):
        # Update the timer every second until it reaches zero
        if self.closing_timer >= 0:
            self.seconds.set(self.minute_second_conv(self.closing_timer))
            if self.closing_timer == 375:
                t = threading.Thread(target=self.play_sound)
                t.start()
            if 365 <= self.closing_timer <= 360:
                time.sleep(.2)

            if self.closing_timer == 360: 
                self.transmit_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                self.transmit_socket.sendto(str.encode('202'), ('127.0.0.1', 7500))
                self.init_event_listener()

            if self.closing_timer < 360:
                r = threading.Thread(target=self.receive_from_socket)
                r.start()
                # Start blinking the team scores
                self.blink_scores()

            self.closing_timer -= 1

            self.display_players()


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

    def is_id(self, id, player_list):
        for player in player_list:
            if player.id == id:
                return player
        return None
    def event_listener(self):
        # Listen for events from the queue and update scores and events accordingly
        while True:
            event_data = self.event_queue.get().split(":")
            if int(event_data[1]) != 43 and int(event_data[1]) != 53:
                if int(event_data[0]) % 2 == 0:
                    self.alpha_red_score += 10
                    try:
                        player = self.is_id(int(event_data[0]), self.alpha_red_players)
                        if player:  # Check if player is not None
                            player.score += 10
                        lose_player = self.is_id(int(event_data[1]), self.alpha_red_players)
                        if lose_player:  # Check if player is not None
                            lose_player.score -= 10 
                    except (AttributeError, TypeError):
                        # Handle potential errors if is_id doesn't return a Player object
                        print("Error updating player score:", event_data[0])
                else:
                    self.alpha_green_score += 10
                    try:
                        player = self.is_id(int(event_data[0]), self.alpha_green_players)
                        if player:  # Check if player is not None
                            player.score += 10
                        lose_player = self.is_id(int(event_data[1]), self.alpha_green_players)
                        if lose_player:  # Check if player is not None
                            lose_player.score -= 10    
                    except (AttributeError, TypeError):
                        # Handle potential errors if is_id doesn't return a Player object
                        print("Error updating player score:", event_data[0])
                player_name_one = self.get_player_name(int(event_data[0]))
                player_name_two = self.get_player_name(int(event_data[1]))
                event_string = f"{player_name_one} hit {player_name_two}"
            else:
                    if int(event_data[1]) == 43:
                        self.alpha_red_score += 100
                        if int(event_data[0]) % 2 == 0:
                          try:
                            player = self.is_id(int(event_data[0]), self.alpha_red_players)
                            if player:  # Check if player is not None
                                player.score += 100
                          except (AttributeError, TypeError):
                              print("Error updating player score:", event_data[0])
                        player_name_one = self.get_player_name(int(event_data[0]))
                        event_string = f"{player_name_one} hit Green Base"
                              
                    if int(event_data[1]) == 53:
                        self.alpha_green_score += 100
                        if int(event_data[0]) % 2 == 1:
                          try:
                            player = self.is_id(int(event_data[0]), self.alpha_green_players)
                            if player:  # Check if player is not None
                                player.score += 100
                          except (AttributeError, TypeError):
                                print("Error updating player score:", event_data[0])
                        player_name_one = self.get_player_name(int(event_data[0]))
                        event_string = f"{player_name_one} hit Red Base"


            self.update_scoreboard()

            self.add_events(event_string)
            
            self.event_queue.task_done()
        

    def get_player_name(self, player_id):
        # Get the player name based on their ID
        for player in self.player_names:
            if int(self.player_names[player]) == player_id :
                return player
            
    def update_scoreboard(self):

        # Update the score labels with the latest scores
        self.red_score_label.config(text=str(self.alpha_red_score))
        self.green_score_label.config(text=str(self.alpha_green_score))

        # Schedule the method to run again after a short delay for continuous updating
        self.after(1000, self.update_scoreboard)


    def update_scoreboard_designations(self, frame, sorted_players, color):
         # Update the designations for displaying scores
        for widget in frame.winfo_children():
            widget.destroy()
            # # Load the image
            img = Image.open('B.png')
            img = img.resize((100, 100), Image.ANTIALIAS)  # Resize image if necessary
            img_tk = Image.PhotoImage(img)


         # Display player scores in the frame
        for i, player in enumerate(sorted_players):
            Label(frame, text=f"{player}: {sorted_players[player]}", bg="black", font="Helvetica 12",
            fg=color).grid(row=i + 1, column=1, sticky="new")
            label_img = Label(frame, image=img_tk)
            label_img.image = img_tk  # Keep a reference, very important in Tkinter!
            label_img.grid(row=i + 1, column=0, sticky="new")
            self.display_players()


    def add_events(self, event_string):
        # Add events to the event window and update the display
        # ... other code ...
        if len(self.event_list) > 8:
            self.event_list.pop(0)  # Remove the oldest event if exceeding limit
        self.event_list.append(event_string)
        # ... other code ...
       

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



    def blink_scores(self):
        # Check which team has the higher score
        if self.alpha_red_score > self.alpha_green_score:
            self.blink_label(self.red_score_label)
        elif self.alpha_red_score < self.alpha_green_score:
            self.blink_label(self.green_score_label)
        else:
            # If scores are equal, stop blinking
            self.stop_blinking()

    def blink_label(self, label):
        if self.blinking:
            label.config(state="disabled")
        else:
            label.config(state="normal")
        self.blinking = not self.blinking
        self.after(500, self.blink_scores)


    def stop_blinking(self):
        # Stop blinking the scores
        self.blinking = False
        self.green_score_label.fg = 'green'
        self.red_score_label.fg = 'red'



# For testing purposes
if __name__ == '__main__':

    
    event_queue = queue.Queue()    

    
    # Create and run the application
    app = PlayerActionScreen(event_queue)
    app.mainloop()
