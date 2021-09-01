di = 6
dj = 6
configuration = [{(0,0), (1,0), (0,1), (2,0)},
				{(2,1), (3,1), (3,0), (4,0), (5,0)},
				{(0,2), (1,1), (1,2), (1,3), (2,2)},
				{(4,1), (4,2)},
				{(5,1), (5,2), (5,3), (4,4), (5,4)},
				{(3,2), (2,3), (3,3), (4,3), (3,4)},
				{(0,3), (0,4), (0,5), (1,4), (2,4)},
				{(1,5), (2,5), (3,5), (4,5), (5,5)}
				]

matrix = [[0 for j in range(dj)] for i in range(di)]
matrix[0][0]=4
matrix[4][0]=5
matrix[2][2]=4
matrix[3][3]=2
matrix[4][3]=3
matrix[4][4]=5
matrix[2][5]=1

def print_it(board):
	for i in range(di):
		print(board[i])

def done(board):
	for i in range(di):
		for j in range(dj):
			if board[i][j]==0:
				return False
	return True

def find_empty(board):
	for i in range(di):
		for j in range(dj):
			if board[i][j]==0:
				return i,j

def valid_so_far(board, setup):
	#a)no two non-zero integers are next to each other, even diagonally
	for i in range(di):
		for j in range(dj):
			for horz in range(-1,2):
				horzCells=i+horz
				for vert in range(-1,2):
					vertCells=j+vert
					if not (horz==0 and vert==0):
						if horzCells >= 0 and horzCells < di and vertCells >=0 and vertCells < dj:
							if board[horzCells][vertCells] == board[i][j] and board[i][j] != 0:
								return False

	#b)each area contains only numbers larger than 0 once and not larger than the number of cells in the area
	for block in range(len(setup)):
		cellNum=[]
		for cell in setup[block]:
			if board[cell[0]][cell[1]]>0:
				if board[cell[0]][cell[1]]>len(setup[block]) or board[cell[0]][cell[1]] in cellNum:
					return False
				else:
					cellNum.append(board[cell[0]][cell[1]])

	return True

def backtrack(board, setup):
	if done(board):
		return board
	row,col=find_empty(board)
	for i in range(1, len(setup)+1):
		board[row][col]=i
		if valid_so_far(board, setup):
			result=backtrack(board, setup)
			if done(result):
				return result
		board[row][col]=0
	return board

print("Beginning Matrix:")
print_it(matrix)
print()
final_matrix=backtrack(matrix, configuration)
print("Final Matrix:")
print_it(final_matrix)
