board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def freespace(pos):
    return board[pos] == ' '


def printBoard(board):
    print('  |  |')
    print((' ' + board[1] + '| ' + board[2] + '| ' + board[3]))
    print('  |  |')
    print('----------')
    print('  |  |')
    print((' ' + board[4] + '| ' + board[5] + '| ' + board[6]))
    print('  |  |')
    print('----------')
    print('  |  |')
    print((' ' + board[7] + '| ' + board[8] + '| ' + board[9]))
    print('  |  |')


def Winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        move = eval(input('Please Select Position to place X (1-9): '))
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freespace(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('This Space is Occupied')
            else:
                print('Please type number in the range')
        except:
            print("Please Type a number")


def CompMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if Winner(boardcopy, let):
                move = i
                return move

    corners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    if len(corners) > 0:
        move = selectRandom(corners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    edges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edges.append(i)
    if len(edges) > 0:
        move = selectRandom(edges)
    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Hey This is Tic Tac Toe')
    printBoard(board)

    while not (isBoardfull(board)):
        if not (Winner(board, 'o')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's won this time")
            break


        if not (Winner(board, 'x')):
            move = CompMove()
            if move == 0:
                print('Tie Game')
            else:
                insertLetter('O', move)
                print(('Computer Placed an O in position', move, ':'))
                printBoard(board)
        else:
            print("Yeh You won this time, Congratulations ")
            break

    if isBoardfull(board):
        print('This Game is Draw!!')

main()
board = {' ' for x in range(10)}


def insertLetter(letter, pos):
    board[pos] = letter


def freespace(pos):
    return board[pos] == ' '


def printBoard(board):
    print('  |  |')
    print(('  ' + board[1] + ' |  ' + board[2] + ' |  ' + board[3]))
    print('  |  |')
    print('----------')
    print('  |  |')
    print((' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]))
    print('  |  |')
    print('----------')
    print('  |  |')
    print((' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]))
    print('  |  |')


def Winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or \
           (bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or \
           (bo[2] == le and bo[5] == le and bo[8] == le) or \
           (bo[3] == le and bo[6] == le and bo[9] == le) or \
           (bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        move = eval(input('Please Select Position to place X (1-9): '))
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freespace(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('This Space is Occupied')
            else:
                print('Please type number in the range')
        except:
            print("Please Type a number")


def CompMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if Winner(boardcopy, let):
                move = i
                return move

    corners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    if len(corners) > 0:
        move = selectRandom(corners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    edges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edges.append(i)
    if len(edges) > 0:
        move = selectRandom(edges)
    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Hey This is Tic Tac Toe')
    printBoard(board)

    while not (isBoardfull(board)):
        if not (Winner(board, 'o')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's won this time")
            break


        if not (Winner(board, 'x')):
            move = CompMove()
            if move == 0:
                print('Tie Game')
            else:
                insertLetter('O', move)
                print(('Computer Placed an O in position', move, ':'))
                printBoard(board)
        else:
            print("Yeh You won this time, Congratulations ")
            break

    if isBoardfull(board):
        print('This Game is Draw!!')

main()
