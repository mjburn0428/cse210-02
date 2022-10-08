import random
import random

class Deck:
    def __init__(self):
        self.card = 0 #This is the random starting card number
        self.score = 300 # This is the starting player score
    
    def draw_card(self):
        self.card = random.randint(1,13) #This creates a card with a random number between 1-13
        return int(self.card)
      

    def award_points(self):
        self.score += 100 # 100 points are awarded if the player guess is correct
    
    def deduct_points(self):
        self.score = self.score - 75 # 75 points deducted if the player guess is incorrect
        
    
    
    def game_over_score(self):
        game_over = self.score
        return int(game_over)

    
    
    def print_scoreboard(self):
   
        print("\t\t\t")
        print("\t\t\t")
        if self.score <= 0:
            print("\t\t\t Your Score is = {}".format(self.score))
        else:   
            print("\t\t\t Your Score is = {}".format(self.score))
          
        print("\t\t\t")
