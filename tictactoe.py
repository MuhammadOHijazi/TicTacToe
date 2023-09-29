"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    check_initial_state = initial_state()
    if board == check_initial_state:
        return X
    count = checkfullboard(board)
    if count == 9:
        return
    if count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set ofall possible actions (i, j) available  on the board.
    """
    count = checkemptyboard(board)
    if count == 0:
        return
    action = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                action.add((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winer = checkxwins(board)
    if winer:
        return X
    winer = checkowins(board)
    if winer:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = checkemptyboard(board)
    if winner(board) is not None or count == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    return move


def min_value(board):
    v = float('inf')
    if terminal(board):
        return utility(board), None
    move = None
    for action in actions(board):
        # v, move = min(v, max_value(result(board, action)))
        temp, none = max_value(result(board, action))
        if temp < v:
            v = temp
            move = action
            if v == -1:
                return v, move
    return v, move


def max_value(board):
    v = float('-inf')
    if terminal(board):
        return utility(board), None
    move = None
    for action in actions(board):
        temp, none = min_value(result(board, action))
        if temp > v:
            v = temp
            move = action
            if v == 1:
                return v, move
    # v, move = max(v, min_value(result(board, action)))
    return v, move


def checkfullboard(board):
    counter = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] != EMPTY:
                counter += 1
    return counter


def checkemptyboard(board):
    counter = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                counter += 1
    return counter


def checkowins(board):
    if board[0][0] == board[0][1] == board[0][2] == O:
        return True
    if board[1][0] == board[1][1] == board[1][2] == O:
        return True
    if board[2][0] == board[2][1] == board[2][2] == O:
        return True

    if board[0][0] == board[1][0] == board[2][0] == O:
        return True
    if board[0][1] == board[1][1] == board[2][1] == O:
        return True
    if board[0][2] == board[1][2] == board[2][2] == O:
        return True

    if board[0][0] == board[1][1] == board[2][2] == O:
        return True
    if board[0][2] == board[1][1] == board[2][0] == O:
        return True

    return False


def checkxwins(board):
    if board[0][0] == board[0][1] == board[0][2] == X:
        return True
    if board[1][0] == board[1][1] == board[1][2] == X:
        return True
    if board[2][0] == board[2][1] == board[2][2] == X:
        return True

    if board[0][0] == board[1][0] == board[2][0] == X:
        return True
    if board[0][1] == board[1][1] == board[2][1] == X:
        return True
    if board[0][2] == board[1][2] == board[2][2] == X:
        return True

    if board[0][0] == board[1][1] == board[2][2] == X:
        return True
    if board[0][2] == board[1][1] == board[2][0] == X:
        return True

    return False
