from deck import Deck
deck = Deck()

class Director:

    
    

    def __init__(self):
        
        self.card_deck = []

    def cards(self):
    
        
        first_card = deck.draw_card()
        print(f'Your drawn card is: {first_card}')

        second_card = deck.draw_card()

        self.card_deck.append(first_card)
        self.card_deck.append(second_card)

        return self.card_deck 