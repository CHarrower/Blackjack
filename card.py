import random
from PIL import Image, ImageTk

class Card:
    def __init__(self, suit, rank, card_img, back_img):
        self.suit = suit
        self.rank = rank 
        self.card_path = card_img
        self.back_card_path = back_img
        self.card_image = Image.open(card_img).convert("RGBA").resize((45,56))
        self.back_image = Image.open(back_img).convert("RGBA").resize((45,56))
        self.card_image_tk = ImageTk.PhotoImage(self.card_image)
        self.back_image_tk = ImageTk.PhotoImage(self.back_image)

class Deck:
    def __init__(self):
        self.suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
        self.ranks = [str(n) for n in range(1,11)] + ["J", "Q", "K"]
        self.deck = []
        self.back_card_path = "main_cards/back_4.png"
        self.initialise_deck

    def initialise_deck(self):
        for _ in range(6):
            for suit in self.suits:
                for rank in self.ranks:
                    card_path = f"main_cards/{suit}_card_{rank}.png"
                    card = Card(suit,rank, self.get_card_value(rank), card_path, self.back_card_path)
                    self.deck.append(card)
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop() if self.deck else None
    
    def get_card_value(self, rank):
        if rank.isdigit():
            return int(rank)
        elif rank in ["J", "Q", "K"]:
            return 10
        else: #<---- ACE
            return 11

if __name__ == "__main__":
    deck = Deck()
    card = deck.deal_card()