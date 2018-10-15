#----------------------------Welcome--------------------------------
#Tic-tac-toe game
#Author ------- Satyam sinha
#IDE used Pycharm

#here I have declared a list which contains the position of the tic-tac-toe game
ch=['1','2','3','4','5','6','7','8','9']
def check1():#This function checks the winning condition of the game when the user chooses player 1 as (X)
    if ch[0]==ch[4] and ch[4]==ch[8]:
        if ch[0]=='X':
            print('Player 1 wins')
            exit(0)
        elif ch[0]=='O':
            print('Player 2 wins')
            exit(0)
    elif ch[2] == ch[4] and ch[4] == ch[6]:
        if ch[2] == 'X':
            print('Player 1 wins')
            exit(0)
        elif ch[2] == 'O':
            print('Player 2 wins')
            exit(0)
    elif ch[1] == ch[4] and ch[4] == ch[7]:
        if ch[1] == 'X':
            print('Player 1 wins')
            exit(0)
        elif ch[1] == 'O':
            print('Player 2 wins')
            exit(0)
    elif ch[0] == ch[3] and ch[3] == ch[6]:
        if ch[0] == 'X':
            print('Player 1 wins')
            exit(0)
        elif ch[0] == 'O':
            print('Player 2 wins')
            exit(0)
    elif ch[2] == ch[5] and ch[5] == ch[8]:
        if ch[2] == 'X':
            print('Player 1 wins')
            exit(0)
        elif ch[2] == 'O':
            print('Player 2 wins')
            exit(0)
    elif ch[0] == ch[1] and ch[1] == ch[2]:
        if ch[0] == 'X':
            print('Player 1 wins')
            exit(0)
        elif ch[0] == 'O':
            print('Player 2 wins')
            exit(0)
    elif ch[3] == ch[4] and ch[4] == ch[5]:
        if ch[3] == 'X':
            print('Player 1 wins')
            exit(0)
        elif ch[3] == 'O':
            print('Player 2 wins')
            exit(0)
    elif ch[6] == ch[7] and ch[7] == ch[8]:
        if ch[6] == 'X':
            print('Player 1 wins')
            exit(0)
        elif ch[6] == 'O':
            print('Player 2 wins')
            exit(0)
def check2():#This function checks the winning condition of the game when player 1 is (O)
    if ch[0]==ch[4] and ch[4]==ch[8]:
        if ch[0]=='O':
            print('Player 1 wins')
            exit(0)
        elif ch[0]=='X':
            print('Player 2 wins')
            exit(0)
    elif ch[2] == ch[4] and ch[4] == ch[6]:
        if ch[2] == 'O':
            print('Player 1 wins')
            exit(0)
        elif ch[2] == 'X':
            print('Player 2 wins')
            exit(0)
    elif ch[1] == ch[4] and ch[4] == ch[7]:
        if ch[1] == 'O':
            print('Player 1 wins')
            exit(0)
        elif ch[1] == 'X':
            print('Player 2 wins')
            exit(0)
    elif ch[0] == ch[3] and ch[3] == ch[6]:
        if ch[0] == 'O':
            print('Player 1 wins')
            exit(0)
        elif ch[0] == 'X':
            print('Player 2 wins')
            exit(0)
    elif ch[2] == ch[5] and ch[5] == ch[8]:
        if ch[2] == 'O':
            print('Player 1 wins')
            exit(0)
        elif ch[2] == 'X':
            print('Player 2 wins')
            exit(0)
    elif ch[0] == ch[1] and ch[1] == ch[2]:
        if ch[0] == 'O':
            print('Player 1 wins')
            exit(0)
        elif ch[0] == 'X':
            print('Player 2 wins')
            exit(0)
    elif ch[3] == ch[4] and ch[4] == ch[5]:
        if ch[3] == 'O':
            print('Player 1 wins')
            exit(0)
        elif ch[3] == 'X':
            print('Player 2 wins')
            exit(0)
    elif ch[6] == ch[7] and ch[7] == ch[8]:
        if ch[6] == 'O':
            print('Player 1 wins')
            exit(0)
        elif ch[6] == 'X':
            print('Player 2 wins')
            exit(0)
def printBoard() :#Here is the full playground of the game tic-tac-toe
    print(f'        |        |          ')
    print(f' {ch[0]}      |   {ch[1]}    |   {ch[2]}    ')
    print(f'------------------------------')
    print(f'        |        |          ')
    print(f' {ch[3]}      |   {ch[4]}    |  {ch[5]}        ')
    print(f'------------------------------')
    print(f'        |        |          ')
    print(f' {ch[6]}      |   {ch[7]}    |  {ch[8]}        ')
def pl1():#By using this function user takes his turn when player 1 is (X)
    while True:
        i=1
        while i<2:
            printBoard()
            c=int(input('Player 1 turn..'))
            ch[c-1]='X'
            i+=1
        check1()
        j=1
        while j<2:
            printBoard()
            d = int(input('Player 2 turn..'))
            ch[d - 1] = 'O'
            j+=1
        check1()
def pl2():#By using this function user takes his turn when player 1 is (O)
    while True:
        i = 1
        while i < 2:
            printBoard()
            c = int(input('Player 1 turn..'))
            ch[c - 1] = 'O'
            i += 1
        check2()
        j = 1
        while j < 2:
            printBoard()
            d = int(input('Player 2 turn..'))
            ch[d - 1] = 'X'
            j += 1
        check2()

# program begins here by choosing the team and then directed to the desired function
Team=input('Enter your team(X/O)')
if Team == 'X':
        pl1()
elif Team == 'O':
        pl2()


#--------------------------------------thanks---------------------------------


