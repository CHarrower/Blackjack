import os
import random

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Game Logic Class
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
class GameLogic:
    def __init__(self, card_images):
        self.card_images = card_images
        self.player_cards = []
        self.dealer_cards = []
        self.player_score = 0
        self.dealer_score = 0
#------------------------------------------------------------------------------------------------------------->

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # Draw the cards
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def draw_card(self, for_dealer=False):
        card_path = random.choice(self.card_images)
        if for_dealer:
            self.dealer_cards.append(card_path)
        else:
            self.player_cards.append(card_path)
        return card_path
    #------------------------------------------------------------------------------------------------------------->

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # Get the card values
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def get_card_value(self, card_path):
        card_name = os.path.basename(card_path).split('.')[0]
        value = card_name.split('_')[0]  
        if value in ['J', 'Q', 'K']:
            return 10
        elif value == 'A':
            return 11
        else:
            return int(value)
    #------------------------------------------------------------------------------------------------------------->

    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # Calculating the scores 
    #/////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def calculate_score(self, for_dealer=False):
        score = 0
        ace_count = 0
        cards = self.dealer_cards if for_dealer else self.player_cards
        for card_path in cards:
            value = self.get_card_value(card_path)
            if value == 11:
                ace_count += 1
            score += value

        while score > 21 and ace_count:
            score -= 10
            ace_count -= 1

        if for_dealer:
            self.dealer_score = score
        else:
            self.player_score = score
        return score
    #------------------------------------------------------------------------------------------------------------->