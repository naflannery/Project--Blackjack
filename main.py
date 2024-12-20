import random

suits = ["Clubs","Hearts","Spades","Diamonds"]
ranks = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
values = {'Ace':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}

#Define a card to create card class, cards have a value (numeric), value(string) and a suit
class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'The {self.rank} of {self.suit}'



def main():
    my_card = Card('Two','Hearts')
    print(my_card)
    print(my_card.value)
if __name__ == "__main__":
    main()