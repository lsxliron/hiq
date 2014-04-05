import pdb
from hashlib import md5
import sys
from termcolor import colored
import datetime


def main():
	b = Board(7,7)
	print str(b)	
	moves_list = solve(b)
	for item in moves_list:
		print item


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






def get_num_of_pegs(board, num):
	"""
	Returns true if there is only one peg on the board or false otherwise
	"""
	if (sum(item.count(1) for item in board.grid)) == num:
		return True
	return False






def hash(brd, mv):
	""" 
	Returns a md5 string constructed from the board and the next move string
	"""
	return md5(str(brd) + str(mv)).hexdigest()

def get_valid_moves(brd):
	"""
	Returns the VALID MOVES for the current state
	"""
	possible_moves = get_list_of_possible_moves(brd)
	valid_moves = list()
	for move in possible_moves:
		if brd.valid_move(move):
			valid_moves.append(move)

	return valid_moves


def solve(brd):
	"""
	Finds a solution for a board if exists, return false if it doesn't.
	In case the move is a dead end, the state will go into a hash table
	to skip identical cases.
	"""
	valid_moves = get_valid_moves(brd)  #Holds the valid moves for the current turn
	limit = len(valid_moves)			#The upper bound for the while loop
	counter = 0;						#Index of the current move
	hash_table = dict()					#Hash table for faster processing
	hashed_state = ""					#The hashed state
	moves_list = list()					#The moves which will provide solution
	
	

	while counter <= limit:
		valid_moves = get_valid_moves(brd)
		
		#Case we found a solution
		if get_num_of_pegs(brd, 1):
			print "FOUND SOLUTION!"
			return moves_list

		#Case valid moves exists
		if len(valid_moves) != 0 and counter < len(valid_moves):	
			next_move = valid_moves[counter]
			
			hashed_state = hash(brd, next_move)

			#Case the board and move combination is not a dead end
			if not hash_table.has_key(hashed_state):

				#Valid move- play the move
				if brd.valid_move(next_move):
					brd.play_move(next_move)
					moves_list.append(next_move)
					counter = 0
				
				#Invalid move- insert board and move comination to hash table
				else:
					last_move = moves_list.pop()
					brd.undo_move(last_move)
					hashed_state = hash(brd, last_move)
					hash_table[hashed_state]=""
					temp_valid_moves = get_valid_moves(brd)
					counter = set_counter(get_valid_moves(brd), last_move)


			#Case board and move combination exists in the hash table
			else:
				#Backtrack
				last_move = moves_list.pop()
				brd.undo_move(last_move)
				hashed_state = hash(brd, last_move)
				hash_table[hashed_state]=""
				counter = set_counter(get_valid_moves(brd), last_move)


		else:
			#Backtrack if we valid moves doesn't exist

			#Backtrack if possible
			if len(moves_list) != 0:
				last_move = moves_list.pop()
				brd.undo_move(last_move)
				hashed_state = hash(brd, last_move)
				hash_table[hashed_state]=""
				
				if temp_valid_moves !=  None:
					counter = set_counter(get_valid_moves(brd), last_move)
				
				else:
					counter = set_counter(get_valid_moves(brd), last_move)
			
			#Increment counter if backtrack is not possible
			else:
				counter = set_counter(get_valid_moves(brd), last_move)
				

		#Reset variables
		next_move = None
		temp_valid_moves = None

	print "NO SOUTION FOUND"
	return False


		
def set_counter(moves_list, move):
	"""
	Sets the counter to the correct value after backtracking
	"""
	for element in moves_list:
		if str(element) == str(move):
			return moves_list.index(move)+1


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


	def __eq__(self, other):
		if self.s1 == other.s1 and self.s2 == other.s2 and self.s3 == other.s3:
			return True
		return False

	def __repr__(self):
		return "({s1}, {s2}, {s3})".format(s1=self.s1, s2=self.s2, s3=self.s3)

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
		self.grid.append([-1, -1, 1, 1, 0, -1, -1])
		self.grid.append([1, 1, 1, 1, 0, 1, 0])
		self.grid.append([0, 0, 0, 0, 0, 0, 0])
		self.grid.append([0, 0, 0, 0, 0, 0, 0])
		self.grid.append([-1, -1, 0, 0, 0, -1, -1])
		self.grid.append([-1, -1, 0, 0, 0, -1, -1])

		"""(3 4 9 15 16 17 19 20 22 23 25 26 27 30 31 33 34 38 45 46)"""
		# self.grid.append([-1, -1, 0, 1, 1, -1, -1])
		# self.grid.append([-1, -1, 1, 0, 0, -1, -1])
		# self.grid.append([0, 1, 1, 1, 0, 1, 1])
		# self.grid.append([0, 1, 1, 0, 1, 1, 1])
		# self.grid.append([0, 0, 1, 1, 0, 1, 1])
		# self.grid.append([-1, -1, 0, 1, 0, -1, -1])
		# self.grid.append([-1, -1, 0, 0, 1, -1, -1])

		"""9 18 19 29 30 38"""

		# self.grid.append([-1, -1, 0, 0, 0, -1, -1])
		# self.grid.append([-1, -1, 1, 0, 0, -1, -1])
		# self.grid.append([0, 0, 0, 0, 1, 1, 0])
		# self.grid.append([0, 0, 0, 0, 0, 0, 0])
		# self.grid.append([0, 1, 1, 0, 0, 0, 0])
		# self.grid.append([-1, -1, 0, 1, 0, -1, -1])
		# self.grid.append([-1, -1, 0, 0, 0, -1, -1])

		"""2 3 4 9 10 14 15 16 17 19 20 21 NO SOLUTION"""
		# self.grid.append([-1, -1, 1, 1, 1, -1, -1])
		# self.grid.append([-1, -1, 1, 1, 0, -1, -1])
		# self.grid.append([1, 1, 1, 1, 0, 1, 1])
		# self.grid.append([1, 0, 0, 0, 0, 0, 0])
		# self.grid.append([0, 0, 0, 0, 0, 0, 0])
		# self.grid.append([-1, -1, 0, 0, 0, -1, -1])
		# self.grid.append([-1, -1, 0, 0, 0, -1, -1])
				



	def __str__(self):
		"""
		Format the output when printing a board to the display
		"""
		output = ""
		d=dict()
		d[-1] = "--"
		d[0] = "O"
		# d[1] = bcolors.WARNING + "X" + bcolors.ENDC
		d[1] = colored("X","magenta")
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

	
	def valid_move(self, mv):
		"""
		Returns true if a move is valid based on the current state
		or false otherwise
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
					return True
		
		return False

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

		if self.valid_move(mv):

			#perform move
			self.grid[i_start][j_start] = 0
			self.grid[i_middle][j_middle] = 0
			self.grid[i_end][j_end] = 1
			return True
		
		return False

	def undo_move(self, mv):
		"""
		Undo a move and return the board to the previous state
		"""
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



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''




if __name__ == '__main__':
	main()