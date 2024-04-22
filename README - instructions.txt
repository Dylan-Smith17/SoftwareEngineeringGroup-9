
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

10.) Upon completion of the initial game countdown, the software will send out code 202.

11.) At the conclusion of the game, code 221 will be sent out three times by the software.

*** IF THE SOCKET IS STILL OPEN IF YOU ARE TRYING TO RUN IT A SECOND TIME THEN RUN THESE COMMANDS***********
$ lsof -i :7500
$ kill -9 <PID>
************************************************************************************************************
############################################################################################################


Software Engineering Group #9

Dylan-Smith17 -> Dylan Smith

BulgarianMineShaft -> Evan Ayres

jcmirandaz -> J.C Mirandaz

ajquinta -> Jacobi Quintanilla

AngelP17 -> Angel Pinzon

bem012 -> Blaze Moore

EkalbDlonra -> Blake Arnold
Bna002 -> Blake Arnold (dual accounts)
