
# Splash and Player Entry Screen Instructions

## Running the Scripts

1. Install Dependencies:
   - Ensure you have Python 3 installed.
   - Install required packages using the following commands:

     ```bash
     sudo apt-get install python3-tk
     sudo apt-get install python3-pol python3-pil.imagetk
     pip install supabase
     pip install python-dotenv
     ```

2. Run Scripts:
   - Open a terminal and navigate to the directory containing the script files.
   - Run the following commands:

     ```bash
     python3 pl_entry_sc.py
     ```

   - After the Player Entry Screen closes, run:

     ```bash
     python3 spl_sc.py
     ```

   - Finally, run the game clock script:

     ```bash
     python3 game_clock.py
     ```

3. Game Clock:
   - The game clock script (`game_clock.py`) adds an audio countdown experience before the game begins. It includes a 30-second initial countdown, playing random audio tracks using the `playsound` library. Afterward, it transitions to a 6-minute game duration countdown.

## Code Explanation

The game clock script (`game_clock.py`) uses the `playsound` library to play random audio tracks, signaling events during the countdown. The countdown consists of two phases: a 30-second initial countdown and a 6-minute game duration countdown.

Ensure to replace any placeholder UDP code with the actual implementation for sending equipment codes via UDP in the `send_equipment_code_via_udp` function.

Feel free to contact the development team for any further assistance on how to run the code.
