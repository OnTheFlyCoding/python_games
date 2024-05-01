#!/usr/bin/env python3
#Demonstrates combining objects

class Card(object):
    ''' A playing card. '''
    RANKS = ['A', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'J', 'K', 'Q']
    
    SUITS = ['c', 'd', 'h', 's']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        # this will return a string of the the rank and
        # suit of each card object. each card will be different.
        
        rep = self.rank + self.suit
        return rep
    
class Hand(object):
    ''' A hand containing multiple different cards'''
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        ''' Allows for each Hand object to print and display the cards
        associated with a player'''
        if self.cards: #if not empty
            rep = ''
            for card in self.cards:
                rep += str(card) + ' '
        else:# if no cards dealt
            rep = '<empty>'
        return rep
    
    # Methods for the hand class:
    
    def clear(self):
        ''' Re-assigns the list of cards assc. w/ the hand obj.'''
        self.cards = []
    
    def add(self, card):
        ''' hand.add(card obj to be added to list self.cards)'''
        self.cards.append(card)
    
    def give(self, card, other_hand):
        ''' remove the card obj from your hand and reassign to another hand'''
        self.cards.remove(card)
        other_hand.add(card)
        
        
        
# main
card1 = Card(rank = 'A', suit = 'c')
print('Printing a Card Object:')
print(card1)

card2 = Card(rank = '2', suit = 'd')
print(card2)
card3 = Card(rank = '4', suit = 's')
print(card3)
card4 = Card(rank = 'K', suit = 's')
print(card4)
card5 = Card(rank = '2', suit = 'd')
print(card5)


my_hand = Hand()
print(f'\nPrinting my hand before I add any cards:')
print(my_hand)
input('continue? (y/n): ')
my_hand.add(card1)
print(my_hand)
my_hand.add(card2)
print(my_hand)
my_hand.add(card3)
print(my_hand)
my_hand.add(card4)
print(my_hand)
my_hand.add(card5)
print(my_hand)

input('\n\nPress any key to exit: ')

    
