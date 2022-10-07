## This Readme file elaborate on how this script work as follow:
### deck.py
 1. First, the script will initalize main parameters and assign its value based on project requirement. For instance original score, win score, lost score and card value. See "def__init__(self)"

2. Second, the script will pass this valye to function script that perform all the logic. See card(self) and receive return value from deck script to determine if score is 0 and then game is over. Additionally, it will prompt the user, if the want to continue to play the game or not.

### function
1. The init function inherit all the objects from deck.py script. 

2. display function will perform the logic which will prompt for user input, read random value and do conditional check as in userInputCheck

3. userInputCheck, will read userinput and set the score value based on "h - High" and "l - Lower" parameters and then return the score to     display

### To use this script
Python 3 deck.py

