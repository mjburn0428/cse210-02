"Hilo Game Week 03"
"Class: CSE210 BYU-I"
"Authors: Joe Burner Chelsea Chngh, Shaun Vann; "
# Please add your name next to mine when collrabrating.

from Director import Director
from Director import Deck

director = Director()
deck = Deck()
keep_playing = 'y'

while keep_playing == 'y':
    card_deck = director.cards() 

    

    guess = input('Higher or lower? [h/l] ').lower()

    print("\t\t\t     ____________________")
    print("\t\t\t                         ")  
    print("\t\t\t     The Next Card was {}".format(card_deck[1]))   
    print("\t\t\t     ____________________")
    print("\t\t\t                         ") 

    

    if guess == 'h' and (card_deck[1] > card_deck[0]):
        deck.award_points()
        print("Your score is plus 100 now!")
    elif guess == 'h' and (card_deck[1] < card_deck[0]):
        deck.deduct_points()
        print("Your score is minus 75 now!")
    elif guess == 'l' and (card_deck[1] < card_deck[0]):
        deck.award_points()
        print("Your score is plus 100 now!")
    elif guess == 'l' and (card_deck[1] > card_deck[0]):
        deck.deduct_points()
        print("Your score is minus 75 now!")
    elif guess == 'h' and (card_deck[1] == card_deck[0]):
        deck.deduct_points()
        print(" Your score is minus 75 now!")
    elif guess == 'l' and (card_deck[1] == card_deck[0]):
        deck.deduct_points()
        print("Your score is minus 75 now!")


    card_deck.clear()
    

    
    deck.print_scoreboard()

        
    score = deck.game_over_score()

        
    if score <= 0:
        keep_playing = 'n'
        
    else:
        keep_playing = input('Play again? [y/n]: ').lower()

    print()