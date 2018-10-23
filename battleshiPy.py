#23/10/2018
# Jerne Vingerhoets

### imports
import random

### definitions
boats = ['carrier','battleship','cruiser','submarine','destroyer']
lengths = [5,4,3,3,2]
found = False
tries = 0
hits = 0

# Board is a 5x5 square!
w, h = 4,4 
playerBoard = [[0 for i in range(5)] for i in range(5)]
pcBoard = [[0 for i in range(5)] for i in range(5)]


def pickLocationPC():
    for x in range(0,len(lengths)+1):
        randX = random.randint(0,w)
        randY = random.randint(0,h)
        pcBoard[randX][randY] = x
        found = True
    #printBoard('pc')
   
        

def markBoard(x,y,type):
    if type == 'miss':
        playerBoard[x][y] = 9
    elif type == 'hit':
        playerBoard[x][y] = 1
    
def printInfo():
    print('''Hello and welcome to \'Battleship - The Shitty Version!\'\nYou'll start with a zeroed out board. When you enter coordinates (x,y) ranging from 1-5\nyou'll either hit (1) a ship or just water (9). \nIdk, just have fun m'kay?''')
    print('\n\n\n') #Classy I know...



def printBoard(type):
    if type == 'player':
        print("Player playfield looks like: ")
        for x in range(0,5):
            print(playerBoard[x])
    elif type == 'pc':
        print("PC playfield looks like: ")
        for x in range(0,5):
            print(pcBoard[x])
    
      
      
def pickLocationPlayer():
    try: 
        x = (int(input("\nEnter a x-value: "))-1) #-1 because it's easier to play with 1-5 instead of 0-4!
        y = (int(input("Enter a y-value: "))-1)  
        if pcBoard[x][y] != 0:
                markBoard(x, y, 'hit')
                pcBoard[x][y] = 0
                print("\nHit!")
        else:
            markBoard(x, y, 'miss')
            print("\nMissed!")
            
        if hits == len(boats):
            found = True
            
        printBoard('player')
    except:
        print("Oof that wasn't supported!")
            

if __name__ == "__main__":
    printInfo()
    pickLocationPC()
    while not found:
        pickLocationPlayer()
        tries += 1 
