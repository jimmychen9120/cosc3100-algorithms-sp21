def print_it(board):
    for i in range(nr_blocks):
        print(board[i])

def is_complete(board):
    for i in range(nr_blocks):
        for j in range(pts_per_block):
            if board[i][j]==0:
                return False
    return True

def is_valid(board, num):
    for i in range(nr_blocks):
        numbers=[]
        for j in range(pts_per_block):
            if board[i][j] in numbers and board[i][j]!=0:
                print("duplicated numbers")
                return False
            else:
                numbers.append(board[i][j])

    
    #validating whether an element will appear no more than 5 times
    elCount=0
    for i in range(nr_blocks):
        for j in range(pts_per_block):
            if board[i][j]==num:
                elCount+=1
            if elCount>blks_with_point:
                return False
        
    #validating whether an a pair will appear no more than 2 times
    for partner in range(1, nr_elements+1):
        if num!=partner:
            pairCount=0
            for group in board:
                #for y in range(pts_per_block):
                if num in group and partner in group:
                        pairCount+=1
                if pairCount>distinct:
                    return False
    return True

def find_first_empty(board):
    for i in range(nr_blocks):
        for j in range(pts_per_block):
            if board[i][j]==0:
                return i, j

nr_blocks=10
pts_per_block=3
nr_elements=6
distinct=2
blks_with_point=5

bibd_list=[pts_per_block*[0] for _ in range(nr_blocks)]

def bibd(blocks):
    if is_complete(blocks):
        return blocks
    blk, i=find_first_empty(blocks)
    #max(blk) is not iterable for some reason
    for num in range(max(bibd_list[blk])+1,nr_elements+1):
        blocks[blk][i]=num
        #print(blocks)
        if is_valid(blocks, num):
            result=bibd(blocks)
            if is_complete(result):
                return result
        blocks[blk][i]=0
    return blocks

print_it(bibd(bibd_list))		
