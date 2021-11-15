import pyinputplus as pyip

board = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
         'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
         'BOT-L': ' ', 'BOT-M': ' ', 'BOT-R': ' '}
turn = 0

def checkWinner():
    if(board['TOP-L'] == 'O' and board['TOP-M'] == 'O'and board['TOP-R'] == 'O'):   #top row
        return 'O'
    elif(board['MID-L'] == 'O' and board['MID-M'] == 'O'and board['MID-R'] == 'O'):    #middle row
        return 'O'
    elif (board['BOT-L'] == 'O' and board['BOT-M'] == 'O' and board['BOT-R'] == 'O'):  #bottom row
        return 'O'
    elif (board['TOP-L'] == 'O' and board['MID-L'] == 'O' and board['BOT-L'] == 'O'):  #left column
        return 'O'
    elif (board['TOP-M'] == 'O' and board['MID-M'] == 'O' and board['BOT-M'] == 'O'):  #middle column
        return 'O'
    elif (board['TOP-R'] == 'O' and board['MID-R'] == 'O' and board['BOT-R'] == 'O'):  #right column
        return 'O'
    elif (board['TOP-L'] == 'O' and board['MID-M'] == 'O' and board['BOT-R'] == 'O'):  #top left to bottom right
        return 'O'
    elif (board['BOT-L'] == 'O' and board['MID-M'] == 'O' and board['TOP-R'] == 'O'):  #bottom left to top right
        return 'O'
    if (board['TOP-L'] == 'X' and board['TOP-M'] == 'X' and board['TOP-R'] == 'X'):  #top row
        return 'X'
    elif (board['MID-L'] == 'X' and board['MID-M'] == 'X' and board['MID-R'] == 'X'):  # middle row
        return 'X'
    elif (board['BOT-L'] == 'X' and board['BOT-M'] == 'X' and board['BOT-R'] == 'X'):  # bottom row
        return 'X'
    elif (board['TOP-L'] == 'X' and board['MID-L'] == 'X' and board['BOT-L'] == 'X'):  # left column
        return 'X'
    elif (board['TOP-M'] == 'X' and board['MID-M'] == 'X' and board['BOT-M'] == 'X'):  # middle column
        return 'X'
    elif (board['TOP-R'] == 'X' and board['MID-R'] == 'X' and board['BOT-R'] == 'X'):  # right column
        return 'X'
    elif (board['TOP-L'] == 'X' and board['MID-M'] == 'X' and board['BOT-R'] == 'X'):  # top left to bottom right
        return 'X'
    elif (board['BOT-L'] == 'X' and board['MID-M'] == 'X' and board['TOP-R'] == 'X'):  # bottom left to top right
        return 'X'
    else:
        return 'Tie'

def resetboard():
    global board, turn
    board = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ',
            'MID-L': ' ', 'MID-M': ' ', 'MID-R': ' ',
            'BOT-L': ' ', 'BOT-M': ' ', 'BOT-R': ' '}
    turn = 0


def taketurn(user_input):
    global turn
    if turn%2== 0:
        board[user_input.upper()] = 'O'
    else:
        board[user_input.upper()] = 'X'
    turn+= 1


def checkinput(user_input):
    return user_input.upper() in board.keys() and board[user_input.upper()] == ' '


def printboard():
    print(board['TOP-L'] + ' | ' + board['TOP-M'] + ' | ' + board['TOP-R'])
    print('- + - + -')
    print(board['MID-L'] + ' | ' + board['MID-M'] + ' | ' + board['MID-R'])
    print('- + - + -')
    print(board['BOT-L'] + ' | ' + board['BOT-M'] + ' | ' + board['BOT-R'])




user_input = ' '
print('Welcome')
while user_input != 'q' or  user_input != 'quit':
    printboard()
    if turn >= 9:
        winner = checkWinner()
        if winner == 'Tie':
            print('Its a tie no one won!')
        else:
            print('The winner is ' + winner + '!')
        resetboard()
        print('Board has been reset!')
        printboard()
    if turn >= 4 and (checkWinner() == 'O' or checkWinner() == 'X'):
        print('The winner is ' + checkWinner() + '!')
        resetboard()
        print('Board has been reset!')
        printboard()

    print('Example inputs: TOP-R, BOT-L, MID-M, BOT-R')
    user_input = pyip.inputStr("Enter your input: ")
    print(user_input)

    if not checkinput(user_input):
        print('Invalid input')
        continue

    taketurn(user_input)
printboard()
print('Program finished. Goodbye.')





