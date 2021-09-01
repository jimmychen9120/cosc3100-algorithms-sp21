def is_complete(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True

def is_valid(board):
    numbers = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                if board[i][j] in numbers:
                    #print('numbers not different')
                    return False
                else:
                    numbers.append(board[i][j])
    #all numbers are different
    for i in range(3):
        if board[i][0] and board[i][1] and board[i][2]:
            if board[i][0]+board[i][1]+board[i][2]!=15:
                #print('rows')
                return False
    for j in range(3):
        if board[0][j] and board[1][j] and board[2][j]:
            if board[0][j]+board[1][j]+board[2][j] !=15:
                #print('cols')
                return False
    if board[0][0] and board[1][1] and board[2][2]:
        if board[0][0]+board[1][1]+board[2][2] != 15:
            #print('main diagonal')
            return False
    if board[0][2] and board[1][1] and board[2][0]:
        if board[0][2]+board[1][1]+board[2][0] != 15:
            #print('opp diagonal')
            return False
    return True

def find_first_free_cell(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    

def print_it(matrix):
    for i in range(3):
        print('{} {} {}'.format(matrix[i][0], matrix[i][1], matrix[i][2]))

def back_track(matrix):
    if is_complete(matrix):
        return matrix
    i, j = find_first_free_cell(matrix)
    for num in range(1,9+1):
        matrix[i][j] = num
        if is_valid(matrix):
            result = back_track(matrix)
            if is_complete(result):
                return result
        matrix[i][j] = 0
    return matrix
    

matrix = [ [0 for i in range(3)] for j in range(3) ]
##matrix[0][0] = 8
##matrix[0][1] = 1
##matrix[0][2] = 6
##matrix[1][0] = 3
##matrix[1][1] = 5
##matrix[1][2] = 7
##matrix[2][0] = 4
##matrix[2][1] = 9
##matrix[2][2] = 2
              

        
