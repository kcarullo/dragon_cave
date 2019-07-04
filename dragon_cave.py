import random 
import time

def displayIntro():
    print('You are in a land of dragons.')
    time.sleep(2)
    print('''In front of you, you see two caves.
          In one cave, the dragon is friendly and will share his treasure with you.
          The other dragon is greedy and hungry, and will eat you on sight.''', '\n')

def chooseCave():
    cave = " "
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
        
    return cave
    
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spook...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)
    
    friendlyCave = random.randint(1, 2)
    
    if chosenCave == str(friendlyCave):
        print('Gives you treasure!')
    else:
        print('Gobbles you down in one bite!')


playagain = 'yes'
while playagain == 'yes' or playagain == 'y':
    displayIntro()

    caveNumber = chooseCave() 
    
    checkCave(caveNumber)
    
    print('Do you want to play again? (yes or no)')
    playagain = input()
else:
    print('Thank you for playing.')    