import random
from playsound import playsound
import time
import os
import threading
from tkinter import Tk, StringVar, Label
from PIL import Image, ImageTk

cwd = os.getcwd()

# Create Tkinter window
root = Tk()
root.title("Countdown Timer")

# StringVar to hold countdown time
countdown_var = StringVar()

# Label to display countdown
countdown_label = Label(root, textvariable=countdown_var, font=("Arial", 40))
countdown_label.pack()

def play_sound():
  x = random.randint(1, 6)
  playsound(cwd + '/photon-main/photon_tracks/Track0' + str(x) + '.mp3')
# Function for countdown thread
def countdown_thread():
    for x in range(30, 0, -1):
        seconds = x % 60
        if(seconds == 15):
            t = threading.Thread(target=play_sound)
            t.start()
        minutes = int(x / 60) % 60
        print(f"{seconds:02}")
        if (seconds > 5):
            time.sleep(1)
        else: 
            time.sleep(1.2)
        countdown_var.set(f"{minutes:02}:{seconds:02}")
    time.sleep(1)
    print('Begin')
    for x in range(360, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        countdown_var.set(f"{minutes:02}:{seconds:02}")
        print(f"{seconds:02}")
        time.sleep(1)

# Start countdown thread
countdown_thread = threading.Thread(target=countdown_thread)
countdown_thread.start()

# Keep the window running
root.mainloop()

# Rest of your code for playing sound during the 30-minute countdown can be placed here
