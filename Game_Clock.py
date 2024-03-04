import random
from playsound import playsound
import time
import os
import threading
cwd = os.getcwd()

def play_sound():
    x = random.randint(1,6)
    playsound(cwd+'/photon-main/photon_tracks/Track0'+str(x)+'.mp3')
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
time.sleep(1)
print('Begin')
for x in range(360, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)


