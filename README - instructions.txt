
# Code Description - README

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
