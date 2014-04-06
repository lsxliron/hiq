"""
Board.py
"""

from termcolor import colored
import pdb
class Board(object):
	"""
	This class represents a peg solitare board.
	"""

	# def __init__(self, pegs, length=7, width=7):
	def __init__(self, pegs=None, length=7, width=7):
		"""
		Initializer
		Parameters:
		pegs- list containing to initial board state
		length- the length of the board
		width- the width of the board
		"""
		



		self.length = length
		self.width = width
		self.grid= []
		counter = 0
		
		if pegs != None:	
			for i in range(0,length):
				self.grid.append(list())
				for j in range(0,width):
					self.grid[i].append(pegs[counter])
					counter += 1

				

		else:
			#Generate grid
			# for i in range(0,2):
			# 	self.grid.append([-1,-1, 1, 1, 1, -1, -1])

			# self.grid.append([1, 1, 1, 1, 1, 1, 1])
			# self.grid.append([1, 1, 1, 0, 1, 1, 1])
			# self.grid.append([1, 1, 1, 1, 1, 1, 1])

			# for i in range(0,2):
			# 	self.grid.append([-1,-1, 1, 1, 1, -1, -1])

			"""(2 3 4 9 10 14 15 16 17 19)"""
			# self.grid.append([-1, -1, 1, 1, 1, -1, -1])
			# self.grid.append([-1, -1, 1, 1, 0, -1, -1])
			# self.grid.append([1, 1, 1, 1, 0, 1, 0])
			# self.grid.append([0, 0, 0, 0, 0, 0, 0])
			# self.grid.append([0, 0, 0, 0, 0, 0, 0])
			# self.grid.append([-1, -1, 0, 0, 0, -1, -1])
			# self.grid.append([-1, -1, 0, 0, 0, -1, -1])

			"""(3 4 9 15 16 17 19 20 22 23 25 26 27 30 31 33 34 38 45 46)"""
			# self.grid.append([-1, -1, 0, 1, 1, -1, -1])
			# self.grid.append([-1, -1, 1, 0, 0, -1, -1])
			# self.grid.append([0, 1, 1, 1, 0, 1, 1])
			# self.grid.append([0, 1, 1, 0, 1, 1, 1])
			# self.grid.append([0, 0, 1, 1, 0, 1, 1])
			# self.grid.append([-1, -1, 0, 1, 0, -1, -1])
			# self.grid.append([-1, -1, 0, 0, 1, -1, -1])

			"""9 18 19 29 30 38"""

			self.grid.append([-1, -1, 0, 0, 0, -1, -1])
			self.grid.append([-1, -1, 1, 0, 0, -1, -1])
			self.grid.append([0, 0, 0, 0, 1, 1, 0])
			self.grid.append([0, 0, 0, 0, 0, 0, 0])
			self.grid.append([0, 1, 1, 0, 0, 0, 0])
			self.grid.append([-1, -1, 0, 1, 0, -1, -1])
			self.grid.append([-1, -1, 0, 0, 0, -1, -1])

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