#!/usr/bin/env python3 

# Blackjack 1-7 players

import cards
import games

class BJ_Card(cards.Card):
    ''' A Black Jack Card'''
    #Since the ace is at the [0] of Card.Ranks
    ACE_VALUE = 1
    
    @property
    def value(self):
        # BJ_Card.value to be called
        if self.is_face_up:
            #Takes the index of the Rank and adds one to give the value
            #Ex.) '3d', rank =3, index=[2]. value = Ranks[index] +1
            v = BJ_Card.RANKS.index(self.rank) +1
            if v > 10:
                #ex.) 10 of any card as an index of 9, add 1 to get the true value.
                #If the index of the card object is passed 10
                v = 10
                
        else:
            #If card is faceing down
            v = None
        return v
    
class BJ_Deck(cards.Deck):
    def populate(self):
        ''' A Blackjack Deck'''
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                # instantiate each Card object and add it to the deck of cards.
                self.cards.append(BJ_Card(rank,suit))
                
class BJ_Hand(cards.Hand):
    #Overrride the __init__ method:
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        #^ The initalization of the self.cards list
        self.name = name
    # Override the __str__ method:
    def __str__(self):
        # Add self.name before displaying the auto string associated with the hand object of 
        # a specific player. The str should print every card ass. with the hand.
        rep = self.name + ':\t' + super(BJ_Hand,self).__str__()
        if self.total:
            rep += '(' + str(self.total) + ')'
        return rep
    
    @property
    def total(self):
        #** if a card in the hand has value of None, then total is None **
        for card in self.cards:
            #Checks all the cards in the hand prior to calculating a total, based on value prop.
            if not card.value:
                #If there is no value property assc. with the object, return None.
                # If card facing down return none.
                return None
            
        #**Continue code if all cards in a hand are able to be viewd, thus calculated
        # add up Card values, treat each ace as 1:**
        t = 0
        for card in self.cards:
            t += card.value
            
        # Determine if this hand has an Ace:
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        
        #**If hand contains an Ace and the total is low enough, treat ace as 11 by adding 10.
        # since we got to this portion of code, we added 1 for the ace before determing if
        # we should treat it as 11 or not.
        # ex.) combination of an ace and 10 would be 11 before this calculation
        # Treating the ace as an 11 when the other card is already 11, we would auto bust:(**
        if contains_ace and t <= 11:
            t += 10
        return t
    
    #Create a method that checks if we busted or not
    def is_busted(self):
        return self.total > 21
    
    # since cards.Hand is the og base class. it has to inherit from the updated hand object class
    # that refers to this game specifically.
    # Which would be the BJ_Hand class in this program.
class BJ_Player(BJ_Hand):
    # already has self.name assc w/ the BJ_Hand class
    ''' A Blackjack Player '''
    def is_hitting(self):
        response = games.ask_yes_no(f'\n{self.name}, do you want a hit? (Y/N): ')
        return response == 'y'
    
    def bust(self):
        print(self.name, 'busts..😐')
        self.lose()
        
    def lose(self):
        print(self.name, 'Loses :(')
        
    def win(self):
        print(self.name, 'Wins! :)')
        
    def push(self):
        print(self.name, 'Pushes👀')
        
        #Since the dealer also has to 'play the game' with ea. player, it too must inherit
        # from the same BJ_Hand class. Other wise it wouldnt be able to hold card
        # objects.
class BJ_Dealer(BJ_Hand):
    ''' A black jack dealer '''
    # Rules: since the dealer will only hit on anything lower than 17,
    # Must edit the is_hitting method so that it is more specific for the dealer and not
    # the other players
    def is_hitting(self):
        return self.total < 17
    
    def bust(self):
        print(self.name, 'Dealer busts🎉')
    
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
        # Since the card objects from BJ_Card gets instantiated in the deck, befroe its given,
        # the BJ_Dealer and BJ_Player class can both use the .flip method assc. with the Card class
        # the BJ_Dealer class communicates with the BJ_card class to invoke its method to the hard
        # the dealer is currently holding
        
        
# This class is used to create a single object that represents the blackjack game itself.

class BJ_Game(object):
    ''' A Blackjack Game '''
    def __init__(self, names):
        self.players = []
        for name in names:
            # INSTANTIATE the players
            player = BJ_Player(name)
            self.players.append(player)
            
        #INSTANTIATE Dealer
        self.dealer = BJ_Dealer('Dealer')
        #INSTANTIATE the Deck
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    
    @property
    def still_playing(self):
        sp =[]
        for player in self.players:
            # If we check the is_busted method for a given Hand (player)
            # if it returns negative, means they didnt bust and are still playing.
            if not player.is_busted():
                sp.append(player)
        return sp
    
    
                
        
        