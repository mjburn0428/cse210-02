"Hilo Game Week 03"
"Class: CSE210 BYU-I"
"Authors: Joe Burner Chelsea Chngh, Shaun Vann;"
#Please add your name to authors.

from Director import Director
from Director import Deck

director = Director()
deck = Deck()
keep_playing = 'y'

while keep_playing == 'y':
    card_deck = director.cards() 

    

    guess = input('Guess Higher or Lower? [h/l] ').lower()

    print("\t\t\t     ____________________")
    print("\t\t\t                         ")  
    print("\t\t\t     Your next card was {}".format(card_deck[1]))   
    print("\t\t\t     ____________________")
    print("\t\t\t                         ") 

    

    if guess == 'h' and (card_deck[1] > card_deck[0]):
        deck.award_points()
        print("Congratulations you won 100 points.")
    elif guess == 'h' and (card_deck[1] < card_deck[0]):
        deck.deduct_points()
        print("Bummer, you lost 75 points.")
    elif guess == 'l' and (card_deck[1] < card_deck[0]):
        deck.award_points()
        print("Yay! You earned 100 points!")
    elif guess == 'l' and (card_deck[1] > card_deck[0]):
        deck.deduct_points()
        print("Better luck next time! You lost 75 points!")
    elif guess == 'h' and (card_deck[1] == card_deck[0]):
        deck.deduct_points()
        print("You lost 75 points! Get em next time!")
    elif guess == 'l' and (card_deck[1] == card_deck[0]):
        deck.deduct_points()
        print("Boo you lost 75 points! Good luck next time!")


    card_deck.clear()
    

    
    deck.print_scoreboard()

        
    score = deck.game_over_score()

        
    if score <= 0:
        keep_playing = 'n'
        
    else:
        keep_playing = input('Would you like to play again? [y/n]: ').lower()

    print()