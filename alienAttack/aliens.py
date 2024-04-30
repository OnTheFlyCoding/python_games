#!/usr/bin/env python3
#Alien Blaster Game
#Just Trying to demonstrate hwo object interact with one another

class Player(object):
    ''' A player in a shooter game'''
    def __init__(self,name,health=100):
        print('A new Hero has been born!\n')
        self.name = name
        self.health = health
    
    def blast(self,enemy):
        print('The player blasts an enemy. \n')
        enemy.health -= 20
        print(f'You did 20xp worth of damage! Their health is now at {enemy.health}xp')
        #enemy.die()
    
    def die(self):
        print(' The hero has been hit! \n\'This can\'t be the way I go out.. \n pass me my last ciggarette... light me up... \n one last time...\'\n ')
        
class Alien(object):
    ''' An alien in a shooter game'''
    def __init__(self,name,health=100):
        print('A new alien has spawned!!\n')
        self.name = name
        self.health = health
    
    def blast(self,enemy):
        print('The alien blasts a hero!\n')
        enemy.health -= 20
        print(f'You did 20xp worth of damage! Their health is now at {enemy.health}xp')
        #enemy.die()
    
    def die(self):
        print('The alien gasps and says\n \'Oh, this is it. This is the big one. \n Yes, its getting dark now. Tell my 1.6 million larvae that I loved them... \n Good bye.. cruel world.\'\n ')


def main():
    player_name = input('What would you like to name your Hero??: ')
    print('\n')
    hero = Player(player_name)
    print(f'Starting Health for our hero: {hero.health}\n')
    alien_name = input('What would you like to name this Alien?: ')
    print('\n')
    invader = Alien(alien_name)
    print(f'Starting Health for our hero: {invader.health}\n')
    #print(' \t\t Death of an Alien\n')
    print('\t\tBegin Your Intergalactic Battle..')
    choice = None
    while choice != "0":
        print('''
              \tFight your enemy!
              
              Controls:
              0 - Quit
              1 - Blast enemy
              ''')
        choice = input('Choice: ')
        #print your choice
        print()
        
        #exit
        if choice == '0':
            print('Game over!')
        
        elif choice == '1':
            hero.blast(invader)
        
        else:
            print(f'\nSorry but, {choice} wasn\'t a valid choice')
        
    #print('\t\tThe death of a Hero\n')
    #invader.blast(hero)
    

main()
input('\n\n Press any key to quit:')
