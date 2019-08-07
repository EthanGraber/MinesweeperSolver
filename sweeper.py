length = int(input("Board length: "))
width = int(input("Board width: "))

#Create the board

board = []
for x in range(width):
	row = []
	for x in range(length):
		row.extend('#') 
	board.append(row)

#Import the solution for reference
solved_board = []
f = open('map.txt', 'r')
opened_file = f.readlines()

for line in opened_file:
	line_list = []
	line = ''.join(line.split())
	line_list.extend(line)
	solved_board.append(line_list)

print(board)
print(solved_board)

def reveal(rowpos, colpos):
	revealed = solved_board[rowpos][colpos]
	print(revealed)
	prettyprint(board)
	print(board[rowpos][colpos])
	board[rowpos][colpos] = revealed 
	if revealed == 'B':
		print('~~~Game Over~~~')

	#Determines how many blank spaces need to be revealed
	#elif revealed == '&':
		#blankcheck()
		'''#Checks for more blank spaces to the right
		for box in range(length):
			col_position_holder = colpos+box+1 #to check the next box in positive direction (starts at 1 to not recount original box)
			if col_position_holder > length:
				break #If we reach the end of the board in the positive direction, stop
			next_revealed = solved_board[rowpos][col_position_holder]
			print(next_revealed)
			prettyprint(board)
			if next_revealed == '&':
				board[rowpos][col_position_holder] = next_revealed
			else:
				break

		#Checks for more blank spaces to the left
		for box in range(length):
			col_position_holder = colpos-box-1 #to check the next box in negative direction (starts at 1 to not recount original box)
			if col_position_holder < 0:
				break #If we reach the end of the board in the negative direction, stop
			next_revealed = solved_board[rowpos][col_position_holder]
			if next_revealed == '&':
				board[rowpos][col_position_holder] = next_revealed
			else:
				break
		
		#TODO Checks for more blank spaces down
		for box in range(width):
			row_position_holder = rowpos+box+1 #to check next box in NEG direction (1 to skip origin)
			if row_position_holder > width:
				break #Reached BOTTOM of board
			print(next_revealed)
			next_revealed = solved_board[row_position_holder][colpos]
			print(next_revealed)
			prettyprint(board)
			if next_revealed == '&':
				board[row_position_holder][colpos] = next_revealed
			else:
				break
		#TODO Checks for more blank spaces up
		for box in range(width):
			row_position_holder = rowpos-box-1 #to check next box in POS direction (1 to skip origin)
			if row_position_holder < 0:
				break #Reached TOP of board
			next_revealed = solved_board[row_position_holder][colpos]
			if next_revealed == '&':
				board[row_position_holder][colpos] = next_revealed
			else:
				break'''

def blankcheck():
	again = False
	for row in range(len(board)):
		for col in range(len(board[row])):
			#print("row: " + str(row))
			#print("col : " + str(col))
			#prettyprint(board)
			if board[row][col] == '&':
				if col+1 < length:
					if solved_board[row][col+1]=='&' and board[row][col+1]=='#':
						board[row][col+1] = solved_board[row][col+1]
						again = True
				if col-1 > -1:
					if solved_board[row][col-1]=='&' and board[row][col-1]=='#':
						board[row][col-1] = solved_board[row][col-1]
						again = True
				if row+1 < width:
					if solved_board[row+1][col]=='&' and board[row+1][col]=='#':
						board[row+1][col] = solved_board[row+1][col]
						again = True
				if row-1 > -1:
					if solved_board[row-1][col]=='&' and board[row-1][col]=='#':
						board[row-1][col] = solved_board[row-1][col]
						again = True
	if again:
		blankcheck()
def analyze():
	pass

def prettyprint(input_board):
	separator = " | "
	lines = []
	for row in range(len(input_board)):
		line = '| '
		for col in range(len(input_board[row])):
			line = line + input_board[row][col] + separator
		lines.append(line)
	for line in lines:
		print(line)


def play():
	on = True
	move_counter = 0
	total_boxes = length*width
	#TODO bombs read from file
	bombs = 21 #THIS IS THE VALUE FOR THE CURRENT MAP.TXT, ONLY HARDCODED FOR TESTING
	while on and move_counter < 300:
		if move_counter == 0:
			reveal(0, 3)
			prettyprint(board)
			on = False
		move_counter += 1

prettyprint(board)
print('\n')
prettyprint(solved_board)
print('\n')
play()
