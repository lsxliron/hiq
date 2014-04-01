import sys
import pdb

def main():
	b = Board(7,7)
	print str(b)

	a=get_list_of_possible_moves(b)
	for t in a:
		print str(t)

	print "total: {t}".format(t=len(a))


def get_list_of_possible_moves(board):
	moves = list()
	for i in range(0, board.length):
		for j in range(0, board.width):
			# if (i * board.length) + j == 32:
				# pdb.set_trace()
			#Horizonatl moves
			if (j<board.length-2):
				if board.grid[i][j] != -1:
					if board.grid[i][j+1] != -1:
						if board.grid[i][j+2] != -1:
							#Create 2 moves (forward and backward)
							moves.append(move((board.length*i) + j,
											  (board.length*i) + j+1,
											  (board.length*i) + j+2))
							
							moves.append(move((board.length*i) + j+2,
											  (board.length*i) + j+1,
											  (board.length*i) + j))

				#Vertical moves:
			if (i<board.width-2):	
				if board.grid[i][j] != -1:
					if board.grid[i+1][j] != -1:
						if board.grid[i+2][j] != -1:
							moves.append(move((i * board.length) + j,
											  (i * board.length) + j + board.length,
											  (i * board.length) + j + 2*board.length))

							moves.append(move((i * board.length) + j + (2*board.length),
											  (i * board.length) + j + board.length,
											  (i * board.length) + j))
	return moves









class move(object):
	def __init__(self, s1, s2, s3):
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3



	def __str__(self):
		return str("({s1}, {s2}, {s3})".format(s1=self.s1, s2=self.s2, s3=self.s3))

class Board(object):
	def __init__(self, length, width):
		self.length = length
		self.width = width
		self.grid= list()
		#Generate grid
		for i in range(0,2):
			self.grid.append([-1,-1, 1, 1, 1, -1, -1])

		self.grid.append([1, 1, 1, 1, 1, 1, 1])
		self.grid.append([1, 1, 1, 0, 1, 1, 1])
		self.grid.append([1, 1, 1, 1, 1, 1, 1])

		for i in range(0,2):
			self.grid.append([-1,-1, 1, 1, 1, -1, -1])

				



	def __str__(self):
		output = ""
		d=dict()
		d[-1] = "--"
		d[0] = "O"
		d[1] = "X"
		for i in range(0, self.length):
			for j in range(0, self.width):
				output+="{v}({loc})\t".format(v=d[self.grid[i][j]], loc=i*self.length+j)

			output += "\n"
		return output



if __name__ == '__main__':
	main()