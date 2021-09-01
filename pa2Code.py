#recursive method that shifts one over to count set bits
def countOnes(x):
    if(x==0):
        return 0
    else:
        return (x & 1) + countOnes(x >> 1)
	
print(countOnes(300))

#returns the inverted number of 64b
def flip(x):
	return (x ^ 0xffffffffffffffff)

#prints binary normal as is
print(bin(100002045))
#prints binary inverted
print(bin(flip(100002045)))

#'sudoku' is a matrix
sudoku=[[0,5,0,0,0,8,0,4,0],
		[0,4,0,3,0,0,0,7,0],
		[0,3,1,7,2,0,8,9,0],
		[3,0,0,0,0,0,7,8,0],
		[0,0,5,0,0,0,1,0,0],
		[0,6,2,0,0,0,0,0,3],
		[0,2,6,0,4,7,9,3,0],
		[0,8,0,0,0,6,0,2,0],
		[0,9,0,8,0,0,0,1,0]]

def house(sudoku, row, col, val):
	count=0;
#this if funciton examines which subgrid to look at
	if (row//3)<1:
		if (col//3)<1:
			for a in range(3):
				for b in range(3):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
		elif (col//3)<2:
			for a in range(3):
				for b in range(3,6):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
		elif (col//3)<3:	
			for a in range(3):
				for b in range(6,9):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
	elif (row//3)<2:
		if (col//3)<1:
			for a in range(3,6):
				for b in range(3):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
		elif (col//3)<2:
			for a in range(3,6):
				for b in range(3,6):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
		elif (col//3)<3:
			for a in range(3,6):
				for b in range(6,9):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
	elif (row//3)<3:
		if (col//3)<1:
			for a in range(6,9):
				for b in range(3):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
		elif (col//3)<2:
			for a in range(6,9):
				for b in range(3,6):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
		elif (col//3)<3:
			for a in range(6,9):
				for b in range(6,9):
					if sudoku[a][b]==val and sudoku[a][b]!=0:
						count+=1
	return count;


def validSudo(sudoku):
	#first for-loop indicates which value will be examined
	for i in range(1,10):
		#this loop goes through the rows of the entire sudoku game
		for x in range(9):
			rowCount=0
			colCount=0
			houseCount=0
			#this loop goes through the columns of the entire sudoku game
			for y in range(9):
				if sudoku[x][y]==i and sudoku[x][y]!=0:
					rowCount+=1
				if sudoku[y][x]==i and sudoku[y][x]!=0:
					colCount+=1
				houseCount=house(sudoku, x, y, i)
			if rowCount>1 or colCount>1 or houseCount>9:
				return False
	return True


print(validSudo(sudoku))