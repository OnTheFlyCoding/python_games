#!/usr/bin/env python3
#Alien Blaster Game
#Just Trying to demonstrate hwo object interact with one another

class Player(object):
    ''' A player in a shooter game'''
    def blast(self,enemy):
        print('The player blasts an enemy. \n')
        enemy.die()
    
class Alien(object):
    ''' An alien in a shooter game'''
    def blast(self,enemy):
        print('The alien blasts a hero!')
        pass
    
    def die(self):
        print('The alien gasps and says \' Oh, this is it. This is the big one. \n Yes, its getting dark now. Tell my 1.6 million larvae that I loved them... \n Good bye.. cruel world. \' ')

print(' \t\t Death of an Alien \n')

hero = Player()
invader = Alien()
hero.blast(invader) 

input('\n\n Press any key to quit')
