#!/usr/bin/env python3

#playing cards 2.0
#Demonstrating inheritence - Class extension

class Card(object):
    ''' A playing card'''
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
    
    SUITS = ['c', 'd', 'h', 's']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        rep = self.rank + self.suit
        return rep
    
class Hand(object):
    '''A collection of card objects'''
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        #if an instance of the hand obj pocesses any cards. The following executes:
        if self.cards:
            rep = ''
            for card in self.cards:
                # return the string method associated with the card obj that this hand has.
                #concatonate by converting them into strings. originally are string objs
                rep += str(card) + '\t'
        else:
            #if hand instance is empty, empty list:
            rep = '<empty>'
        return rep
    
    def add(self, card):
        self.cards.append(card)
        
    def clear(self):
        self.cards = []
        
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
#Demonstrating inheritence:
class Deck(Hand):
    # Deck class now has the same methods of Hand: __init, __str, clear(),
    # add(), give()
    # Bascially acts as the dealer. controlling the distribution of the cards to the players.
    ''' A deck of playing cards'''
    def populate(self):
        
        # For every possible value in the CONST list of SUITS, 4 iterations
        for suit in Card.SUITS:
            #for every one suit, assosiate it with every rank
            for rank in Card.RANKS:
                #adding the cards to the deck, one by one until every rank is in every suit
                # Card(rank, suit) -> since you iterated through both lists,
                # you have an index assc. with a rank and suit.
                # Since Card needs a rank and suit to instantiate, you do so here, with their
                # iterations.
                self.add(Card(rank, suit))
                
    def shuffle(self):
        # move the list of cards
        import random
        random.shuffle(self.cards)
        
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            #The following code executes once per round:
            for hand in hands:
                #per round, deal a card to each player
                #as long as the deck is not empty, execute the following:
                if self.cards:
                    # the first card in the deck
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Can\'t continue deal. Out of cards!')
                    
# Main
deck1 = Deck()
print('Created a new Deck')
print(f'Deck: {deck1}')
#checking populate method
deck1.populate()
print('\nPopulated the deck:')
print(deck1)
#checking shuffle method
deck1.shuffle()
print('\nShuffled the deck:')
print(deck1)
my_hand = Hand()
your_hand = Hand()
#list of two objects
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand=5)
print('\n\tDealt 5 cards to my hand and your hand.')
print(f'\nMy hand: {my_hand}')
print(f'\nYour hand: {your_hand}')
print(f'\nRemaining cards in the deck: {deck1}')
deck1.clear()
print('Cleared the deck.')
print('Deck:', deck1)

input('Press any key to exit: ')