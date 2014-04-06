"""
Move.py
"""

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
		return str("({s1}, {s2}, {s3})".format(s1=self.s1, 
											   s2=self.s2, 
											   s3=self.s3))


	def __eq__(self, other):
		if self.s1 == other.s1 and \
		   self.s2 == other.s2 and \
		   self.s3 == other.s3:
			return True
		return False

	def __repr__(self):
		return "({s1}, {s2}, {s3})".format(s1=self.s1, s2=self.s2, s3=self.s3)

	