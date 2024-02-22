# Splash and Entry Player Screen Readme

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

3. Game Clock:
   - The game clock will start automatically when the Player Entry Screen closes.

## Code Explanation

The provided Python scripts include a Player Entry Screen and a Splash Screen for a Laser Tag game. The Player Entry Screen allows adding players to Red and Green teams, storing data in a database. The Splash Screen displays the game logo.

Ensure to replace any placeholder UDP code with the actual implementation for sending equipment codes via UDP in the `send_equipment_code_via_udp` function.

Feel free to contact the development team for any further assistance on how to run the code.

