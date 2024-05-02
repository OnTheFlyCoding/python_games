#!/usr/bin/env python3

#Playing cards 3.0
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
# More inheritence
class Unprintable_Card(Card):
    # Overriding the old __str__()
    def __str__(self):
        return '<Unprintable>'
    
# New class that needs a new attribute. Similar set up as Card Class.
class Positionable_card(Card):
    def __init__(self, rank, suit, face_up = True):
        # added face_up as a new attribute and set it to true.
        # super refers to the parent class of the new class, pos_card
        super(Positionable_card, self).__init__(rank, suit)
        # The new instance of Pos_card, wants to invoke the .__init__()
        # of the parent class, passing the values of rank and suit to the new instance of Pos_card
        self.is_face_up = face_up
        # Adding a new attribute in this construcor of an inhertied class. 
        
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_card,self).__str__()
            # Gets the same string returned like Card.__str__()
        
        else:
            rep = 'XX'
        return rep
    
    # New method
    
    def flip(self):
        #changes boolean value
        self.is_face_up = not self.is_face_up
        

# Main
card1 = Card('A', 'c')
card2 = Unprintable_Card('A', 'd')
card3 = Positionable_card('A', 'h')
print('Printing the card obj: ')
print(card1)
print('Printing an unprintable card: ')
print(card2)
print('\nPrinting a positionable card: ')
print(card3)
print('Flipping that same positional card')
card3.flip()
print('\nPrinting the positional card after flipping: ')
print(card3)
input('\n\n\t\tPress any key to exit: ')