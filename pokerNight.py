import os

initial_guests = []
print('Welcome to Poker Night!\n')
print('We will begin taking attendance \n')
print('3 players are needed to begin this game\n')

def start_game():
    global initial_guests
    user = 'none'
    while initial_guests <3:
        user = input('Please enter name:')
    initital_guests.append(user)
        
start_game() 
guests = open('guests.txt', 'w')
#update text file
for i in initial_guests:
    guests.write( i + '\n')
guests.close()

#our table is going to look something like this
print('We have enough players to begin our game!\n')
print('Please introduce yourselves')
with open('guests.txt') as guests:
    for line in guests:
        print(line)
guests.close()
        
print('we have new guests arriving\n')
print('lets allow our guests a seat at the table\n')
new_guests = []

def add_player(user):
    global new_guests
    user = input('Enter new players name:')
    new_guests.append(user)
print(new_guests)

add_player()
add_player()


with open('guests.txt','a') as guests:
    for i in new_guests:
        guests.write(i + '\n')
guests.close()

#players are beginning to leave 
#removing players
temp_list = []
with open('guests.txt','r') as guests:
    for g in guests:
        temp_list.append(g.gstrip())


def remove_player(user):
    global temp_list
    with open('guests.txt','w') as guests:
        if user not in temp_list:
            print('Player must be playing in order to remove')
        else:
            guests.remove(user)
    guests.close()
    
remove_player()
print('here are the players that are still here:')
with open('guests.txt','r') as guests:
    for line in guests:
        print(line)
        
