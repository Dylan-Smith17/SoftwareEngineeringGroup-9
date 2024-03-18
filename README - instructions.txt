
# Code Description - README

## Running the Scripts ##
############################################################################################################
1.) Clone the repository

2.) Navigate to the repository file location, enter: chmod +x start.bash

3.) enter into console: .stat /start.bash

4.) enter into console: y    -> this will download all the dependencies

5.) If splash screen does not pop up-> enter into concole: pip install requests -> and re-run the start.bash

6.) Splash screen will pop up and close on its own

7.) The player entry screen will pop up; populate with players by name and ID, select a team. F12 to delete
    player entries, and F5 to close the screen, this will begin the timer and open the player action screen.

8.) a 30 second countdown will begin in the console and in a pop-up. At 15s audio begins.

9.) Player action screen will pop up with a 6 min timer, music will continue to play.
############################################################################################################












## Running the Scripts (Old) ##
## For reference only ##

1. Install Dependencies:
   - Ensure you have Python 3 installed.
   - Install required packages using the following commands:

     ```bash
     sudo apt-get install python3-tk
     sudo apt-get install python3-pol python3-pil.imagetk
     pip install supabase
     pip install python-dotenv
     ```

2. Run Player Entry Screen Script:
   - Open a terminal and navigate to the directory containing the script files.
   - Run the following command:

     ```bash
     python3 pl_entry_sc.py
     ```

   - Follow on-screen instructions for player entry.

3. Run Splash Screen Script:**
   - After the Player Entry Screen closes, run:

     ```bash
     python3 spl_sc.py
     ```

   - Follow any on-screen instructions or wait for the splash screen to complete.

4. Run Game Clock Script:**
   - Finally, run the game clock script:

     ```bash
     python3 game_clock.py
     ```

   - The game clock script (`game_clock.py`) adds an audio countdown experience before the game begins. It includes a 30-second initial countdown, playing random audio tracks using the `playsound` library. Afterward, it transitions to a 6-minute game duration countdown.

5. DP_Client.py and UDP_Server.py:
   - These scripts contain functions for the client-side and server-side implementation, respectively.
   - Detailed function descriptions, including parameters, return values, and examples, can be found inside these files.

6. Replace Placeholder UDP Code:
   - Ensure to replace any placeholder UDP code with the actual implementation for sending equipment codes via UDP in the `send_equipment_code_via_udp` function.

7. Contact the Team if something is not clear enough :
   - Feel free to contact the development team for any further assistance on how to run the code.

Software Engineering Group #9

Dylan-Smith17 -> Dylan Smith

BulgarianMineShaft -> Evan Ayres

jcmirandaz -> J.C Mirandaz

ajquinta -> Jacobi Quintanilla

AngelP17 -> Angel Pinzon

bem012 -> Blaze Moore

EkalbDlonra -> Blake Arnold
Bna002 -> Blake Arnold (dual accounts)
