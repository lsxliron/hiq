from hashlib import md5
from termcolor import colored
from Move import *
from Board import *


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
	last_move=None
	las_valid_moves = None

	# while counter <= limit and counter<=76:
	while str(las_valid_moves) != valid_moves and counter<100:
		valid_moves = get_valid_moves(brd)
		las_valid_moves = get_valid_moves(brd)
		
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
				
				#Invalid move- insert board and move combination to hash table
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
				# counter = set_counter(get_valid_moves(brd), last_move)
				counter += 1

			

				

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

if __name__ == '__main__':
	main()