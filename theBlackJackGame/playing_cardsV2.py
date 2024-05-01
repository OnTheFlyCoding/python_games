#!/usr/bin/env python3

#playing cards 2.0
#Demonstrating inheritence - Class extension

class Card(object):
    ''' A playing card'''
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'J', 'K', 'Q']
    
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
                return rep
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