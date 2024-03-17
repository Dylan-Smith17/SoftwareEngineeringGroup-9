#!/bin/bash 
sudo apt install python3-pip
sudo apt-get install python3-tk
sudo apt-get install python3-tk python3-pil python3-pil.imagetk
pip install playsound Pillow
sudo apt-get install python3-pol python3-pil.imagetk

pip install supabase
pip install python-dotenv
pip install playsound
pip install Pillow
python3 spl_sc.py
python3 pl_entry_sc.py
# when player entry screen closes, start game clock
python3 Game_Clock.py
