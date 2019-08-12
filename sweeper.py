#Create the board
def createboard(length, width):
	board = []
	for i in range(width):
		row = []
		for i in range(length):
			row.extend('#') 
		board.append(row)
	return board
board = []

#Create the probabilty measurements storage
probability = []
for i in range(width):
	row = []
	for i in range(length):
		row.append({'probability':0, 'terms':[]}) #TODO http://nothings.org/games/minesweeper/
	probability.append(row)

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
				#Checks row below for blank
				if row+1 < width:
					#If blank below, reveals it and tells loop to run again
					if solved_board[row+1][col]=='&' and board[row+1][col]=='#':
						board[row+1][col] = solved_board[row+1][col]
						again = True
					#If the program can't find a blank below, reveals tile
					elif board[row+1][col] == '#':
						board[row+1][col] = solved_board[row+1][col]
				#Checks row above for blank
				if row-1 > -1:
					#If blank above, reveals it and tells loop to run again
					if solved_board[row-1][col]=='&' and board[row-1][col]=='#':
						board[row-1][col] = solved_board[row-1][col]
						again = True
					#If the program can't find a blank above, reveals tile
					elif board[row-1][col] == '#':
						board[row-1][col] = solved_board[row-1][col]
	if again:
		blankcheck()
def analyze():
	again = False
	for row in range(len(board)):
		for col in range(len(board[row])):
			value = board[row][col]

			#Doesn't process blank space (&), unknowns (#), or flagged bombs (F)
			if value == '&' or value == '#' or value == 'F':
				continue

			#Finds neighbors and counts how many unknown values and bombs are neighbors
			neighbors = getneighbors(row, col)
			bomb_counter = 0
			unknown_counter = 0
			unknowns = []
			for key in neighbors:
				try:
					if neighbors[key][0] == '#':
						unknown_counter += 1
						unknowns.append(key)
					elif neighbors[key][0] == 'F':
						bomb_counter += 1 
				except(IndexError):
					pass
			#If there are exactly as many unknowns as bombs left, flags as bomb
			if (int(value)-bomb_counter) == unknown_counter and unknown_counter > 0:
				for key in unknowns:
					rowval = neighbors[key][1] #[0] is value, [1] row, [2] col
					colval = neighbors[key][2]
					board[rowval][colval] = 'F' #Flags it as a bomb
				again = True
			#If all bombs are accounted for, reveals unknowns
			elif int(value) == bomb_counter and unknown_counter > 0:
				for key in unknowns:
					rowval = neighbors[key][1]
					colval = neighbors[key][2]
					reveal(rowval, colval)
				again = True
			elif (int(value)-bomb_counter) < unknown_counter:
				pass
			elif unknown_counter == 0:
				pass
			else:
				print("This shouldn't happen") 
	if again:
		analyze()

def getneighbors(row, col):
	#Declares variables with a value of 0
	up = []
	down = []
	left = []
	right = []
	upleft = []
	upright = []
	downleft = []
	downright = []
	#Checks if there's a row above the value
	if row-1 > -1:
		up.append(board[row-1][col])
		up.append(row-1)
		up.append(col)
		#Checks if there's space to the left and right in the columns above
		if col-1 > -1:
			upleft.append(board[row-1][col-1])
			upleft.append(row-1)
			upleft.append(col-1)
		if col+1 < length:
			upright.append(board[row-1][col+1])
			upright.append(row-1)
			upright.append(col+1)
	#Checks if there's a row below the value
	if row+1 < width:
		down.append(board[row+1][col])
		down.append(row+1)
		down.append(col)
		#Checks if there's space to the left and right in the columns below
		if col-1 > -1:
			downleft.append(board[row+1][col-1])
			downleft.append(row+1)
			downleft.append(col-1)
		if col+1 < length:
			downright.append(board[row+1][col+1])
			downright.append(row+1)
			downright.append(col+1)
	#Checks right
	if col+1 < length:
		right.append(board[row][col+1])
		right.append(row)
		right.append(col+1)
	#Checks left
	if col-1 > -1:
		left.append(board[row][col-1])
		left.append(row)
		left.append(col-1)
	neighbors = {
		'upleft':upleft,
		'up':up,
		'upright':upright,
		'left':left,
		'right':right,
		'downleft':downleft,
		'down':down,
		'downright':downright}
	return neighbors

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

def probbomb(value, neighbors, unknowns, bombs): #TODO create 'advanced' bomb finding 
	unknown_neighbors = []
	for unknown in unknowns:
		#Gets the neighbors for the unknowns
		unknown_neighbors.append(getneighbors(unknown[1], unknown[2])) #[1] is row, [2] is col
	

def play():
	on = True
	move_counter = 0
	total_boxes = length*width
	#TODO bombs read from file
	bombs = 23 #THIS IS THE VALUE FOR THE CURRENT MAP.TXT, ONLY HARDCODED FOR TESTING
	while on and move_counter < 300:
		if move_counter == 0:
			reveal(0, 0)
			prettyprint(board)
			analyze()
		r = int(input("Reveal row: "))
		c = int(input("Reveal col: "))
		reveal(r, c)
		analyze()
		prettyprint(board)
		
		f_counter = 0
		for row in range(len(board)):
			for col in range(len(board[row])):
				if board[row][col] == 'F':
					f_counter += 1
		if f_counter == bombs:
			print('win!')
			on = False

		move_counter += 1

prettyprint(board)
print('\n')
prettyprint(solved_board)
print('\n')
play()
