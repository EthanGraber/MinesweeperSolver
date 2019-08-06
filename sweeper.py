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
	pass
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


