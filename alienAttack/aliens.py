#!/usr/bin/env python3
#Alien Blaster Game
#Just Trying to demonstrate hwo object interact with one another

class Player(object):
    ''' A player in a shooter game'''
    def __init__(self,name):
        print('A new Hero has been born!\n')
        self.name = name
    
    def blast(self,enemy):
        print('The player blasts an enemy. \n')
        enemy.die()
    
    def die(self):
        print(' The hero has been hit! \n\'This can\'t be the way I go out.. \n pass me my last ciggarette... light me up... \n one last time...\'\n ')
        
class Alien(object):
    ''' An alien in a shooter game'''
    def __init__(self,name):
        print('A new alien has spawned!!\n')
        self.name = name
    
    def blast(self,enemy):
        print('The alien blasts a hero!')
        enemy.die()
    
    def die(self):
        print('The alien gasps and says\n \'Oh, this is it. This is the big one. \n Yes, its getting dark now. Tell my 1.6 million larvae that I loved them... \n Good bye.. cruel world.\'\n ')


def main():
    player_name = input('What would you like to name your Hero??: ')
    print('\n\n')
    hero = Player(player_name)
    alien_name = input('What would you like to name this specimen?: ')
    print('\n\n')
    invader = Alien(alien_name)
    print(' \t\t Death of an Alien \n')
    hero.blast(invader)
    print('\t\tThe death of a Hero\n')
    invader.blast(hero)
    

main()
input('\n\n Press any key to quit:')
