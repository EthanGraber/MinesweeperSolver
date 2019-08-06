length = int(input("Board length: "))
width = int(input("Board width: "))

#Create the board
row = []
board = []
for x in range(length):
	row.extend('#')

for x in range(width):
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
		on = False
		print('~~~Game Over~~~')

	#Determines how many blank spaces need to be revealed
	elif revealed == '&':
		#Checks for more blank spaces to the right
		for box in range(length):
			col_position_holder = colpos+box+1 #to check the next box in positive direction (starts at 1 to not recount original box)
			if col_position_holder > length:
				break #If we reach the end of the board in the positive direction, stop
			next_revealed = solved_board[rowpos][col_position_holder]
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
		
		#TODO Checks for more blank spaces up
		#TODO Checks for more blank spaces down
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

on = True
def play():
	move_counter = 0
	total_boxes = length*width
	#TODO bombs read from file
	bombs = 21 #THIS IS THE VALUE FOR THE CURRENT MAP.TXT, ONLY HARDCODED FOR TESTING
	while on and move_counter < 300:
		if move_counter == 0:
			reveal(0, 0)
		move_counter += 1


