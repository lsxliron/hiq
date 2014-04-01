import pdb
from hashlib import md5
import sys
sys.setrecursionlimit(10000)

def main():
	b = Board(7,7)
	print str(b)

	a=get_list_of_possible_moves(b)
	moves_list = list()
	ht = dict()
	moves_list = solve(b,a, moves_list,ht)
	# for t in a:
		# print str(t)

	# print "total: {t}".format(t=len(a))

	# m = Move(10,17,24)
	# b.play_move(m)
	# print str(b)


def get_list_of_possible_moves(board):
	"""
	Returns a list of the valid moves which exist on a board.
	It does not mean that each move in that list is valid in every state
	"""
	moves = list()
	for i in range(0, board.length):
		for j in range(0, board.width):

			#Horizontal moves
			if (j<board.length-2):
				if board.grid[i][j] != -1:
					if board.grid[i][j+1] != -1:
						if board.grid[i][j+2] != -1:
							#Create 2 moves (forward and backward)
							moves.append(Move((board.length*i) + j,
											  (board.length*i) + j+1,
											  (board.length*i) + j+2))
							
							moves.append(Move((board.length*i) + j+2,
											  (board.length*i) + j+1,
											  (board.length*i) + j))

			#Vertical moves:
			if (i<board.width-2):	
				if board.grid[i][j] != -1:
					if board.grid[i+1][j] != -1:
						if board.grid[i+2][j] != -1:
							#Create 2 moves (top down and bottom up)
							moves.append(Move((i * board.length) + j,
											  (i * board.length) + j + board.length,
											  (i * board.length) + j + 2*board.length))

							moves.append(Move((i * board.length) + j + (2*board.length),
											  (i * board.length) + j + board.length,
											  (i * board.length) + j))
	return moves






def final_state(board):
	"""
	Returns true if there is only one peg on the board or false otherwise
	"""
	if (sum(item.count(1) for item in board.grid)) == 1:
		return True
	return False



def solve(brd, valid_moves, moves_list, hash_t):
	counter = 0
	
	while counter<len(valid_moves):

		if (final_state(brd)):
			print "YYYYYEEEEEESSSSS"
			return moves_list

		#Play the next move
		next_move_valid = brd.play_move(valid_moves[counter])
		
		if not hash_t.has_key(md5(str(brd))):
			if next_move_valid:
				moves_list.append(valid_moves[counter])
				counter = -1

		else:
			#counter == len(valid_moves):
			counter = 0
			hash_t[md5(str(brd))] = brd
			brd.undo_move(moves_list[len(moves_list)-1])
			moves_list.pop()

		counter+=1


	return False









class Move(object):
	"""
	This class represents a move on a solitare board. 
	A move consists of 3 consecutive squares (horizonatl or vertical)
	"""
	def __init__(self, s1, s2, s3):
		"""
		Initializer
		Parameters:
		s1- the first square to move from
		s2- the second square (on the move)
		s3- the goal square
		"""
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3



	def __str__(self):
		return str("({s1}, {s2}, {s3})".format(s1=self.s1, s2=self.s2, s3=self.s3))

class Board(object):
	"""
	This class represents a peg solitare board.
	"""

	def __init__(self, length, width):
		"""
		Initializer
		Parameters:
		length- the length of the board
		width- the width of the board
		"""
		self.length = length
		self.width = width
		self.grid= list()
		#Generate grid
		# for i in range(0,2):
		# 	self.grid.append([-1,-1, 1, 1, 1, -1, -1])

		# self.grid.append([1, 1, 1, 1, 1, 1, 1])
		# self.grid.append([1, 1, 1, 0, 1, 1, 1])
		# self.grid.append([1, 1, 1, 1, 1, 1, 1])

		# for i in range(0,2):
		# 	self.grid.append([-1,-1, 1, 1, 1, -1, -1])

		"""(2 3 4 9 10 14 15 16 17 19)"""
		self.grid.append([-1, -1, 1, 1, 1, -1, -1])
		self.grid.append([-1, -1, 0, 1, 0, -1, -1])
		self.grid.append([1, 1, 1, 1, 0, 1, 0])
		self.grid.append([0, 0, 0, 0, 0, 0, 0])
		self.grid.append([0, 0, 0, 0, 0, 0, 0])
		self.grid.append([-1, -1, 0, 0, 0, -1, -1])
		self.grid.append([-1, -1, 0, 0, 0, -1, -1])

				



	def __str__(self):
		"""
		Format the output when printing a board to the display
		"""
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

	def __eq__(self, other):
		"""
		Checks boards equality
		"""
		if self.length != other.length or self.width != other.width:
		   return False

		 #Check elements
		for i in range(0,self.length):
			for j in range(0, self.width):
		  		if (self.grid[i][j] != other.grid[i][j]):
		  			return False

		  	return True

	def play_move(self, mv):
		"""
		Change the board according to the move and return true.
		If the move is invalid, return false
		"""

		#Get the move position route
		i_start = mv.s1 / self.length
		j_start = mv.s1 - (i_start * self.width)

		i_middle = mv.s2 / self.length
		j_middle = mv.s2 - (i_middle * self.width)

		i_end = mv.s3 / self.length
		j_end = mv.s3 - (i_end * self.width)

		#check if move is valid
		if self.grid[i_start][j_start] == 1:
			if self.grid[i_middle][j_middle] == 1:
				if self.grid[i_end][j_end] == 0:
					#perform move
					self.grid[i_start][j_start] = 0
					self.grid[i_middle][j_middle] = 0
					self.grid[i_end][j_end] = 1
					return True
		
		return False

	def undo_move(self, mv):
		#Get the move position route
		i_start = mv.s1 / self.length
		j_start = mv.s1 - (i_start * self.width)

		i_middle = mv.s2 / self.length
		j_middle = mv.s2 - (i_middle * self.width)

		i_end = mv.s3 / self.length
		j_end = mv.s3 - (i_end * self.width)

		if self.grid[i_start][j_start] == 0:
			self.grid[i_start][j_start] = 1
		else:
			self.grid[i_start][j_start] = 0;

		if self.grid[i_middle][j_middle] == 0:
			self.grid[i_middle][j_middle] = 1
		else:
			self.grid[i_middle][j_middle] = 0;

		if self.grid[i_end][j_end] == 0:
			self.grid[i_end][j_end] = 1
		else:
			self.grid[i_end][j_end] = 0;






if __name__ == '__main__':
	main()