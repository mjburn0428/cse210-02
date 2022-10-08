## This Readme file elaborate on how this script work as follow:
### main.py
 1. First, the script will initalize main parameters and assign its value based on project requirement. For instance original score, win score, lost score and card value. See "keep_playing"

2. Second, the script will pass this valye to function script that perform all the logic. See card_deck[1] and receive return value from deck script to determine if score is 0 and then game is over. Additionally, it will prompt the user, if the want to continue to play the game or not.

3. userInputCheck, will read userinput and set the score value based on "h - High" and "l - Lower" parameters and then return the score to display

### deck
1. The init function inherit all the objects from deck.py script. Here, we assign it as "self".  See "def__init__(self)

2. display function will perform the logic which will prompt for user input, read random value and do conditional check as in userInputCheck

### rules
1. The player will guess the card number is h or l. And the player will continue play until the game score show 0. 

2. The player can continue playing the game by reply yes or no.

### To use this script
Python 3 main.py

