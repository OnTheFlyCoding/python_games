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
    
# main
card1 = Card(rank = 'A', suit = 'c')
print('Printing a Card Object:', end =' ')
print(card1)

input('\n\nPress any key to exit: ')

    
