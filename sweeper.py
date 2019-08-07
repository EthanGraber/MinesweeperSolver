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

def reveal(rowpos, colpos):
	revealed = solved_board[rowpos][colpos]
	board[rowpos][colpos] = revealed
	if revealed == 'B':
		print('~~~Game Over~~~')

	#Determines how many blank spaces need to be revealed
	elif revealed == '&':
		blankcheck()
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
	#For loops iterate through each row and each column within each row
	for row in range(len(board)):
		for col in range(len(board[row])):
			if board[row][col] == '&':
				#Checks column in right direction for blank
				if col+1 < length:
					#If blank to right, reveals it and tells loop to run again
					if solved_board[row][col+1]=='&' and board[row][col+1]=='#':
						board[row][col+1] = solved_board[row][col+1]
						again = True
					#If the program can't find a blank to the right, reveals tile
					elif board[row][col+1] == '#':
						board[row][col+1] = solved_board[row][col+1]
				#Checks column in left direction for blank
				if col-1 > -1:
					#If blank to left, reveals it and tells loop to run again
					if solved_board[row][col-1]=='&' and board[row][col-1]=='#':
						board[row][col-1] = solved_board[row][col-1]
						again = True
					#If the program can't find a blank to the left, reveals tile
					elif board[row][col-1] == '#':
						board[row][col-1] = solved_board[row][col-1]
				#Checks row above for blank
				if row+1 < width:
					#If blank above, reveals it and tells loop to run again
					if solved_board[row+1][col]=='&' and board[row+1][col]=='#':
						board[row+1][col] = solved_board[row+1][col]
						again = True
					#If the program can't find a blank above, reveals tile
					elif board[row+1][col] == '#':
						board[row+1][col] = solved_board[row+1][col]
				#Checks row below for blank
				if row-1 > -1:
					#If blank below, reveals it and tells loop to run again
					if solved_board[row-1][col]=='&' and board[row-1][col]=='#':
						board[row-1][col] = solved_board[row-1][col]
						again = True
					#If the program can't find a blank below, reveals tile
					elif board[row-1][col] == '#':
						board[row-1][col] = solved_board[row-1][col]
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
			reveal(0, 0)
			prettyprint(board)
			on = False
		move_counter += 1

prettyprint(board)
print('\n')
prettyprint(solved_board)
print('\n')
play()
