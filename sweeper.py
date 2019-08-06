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




