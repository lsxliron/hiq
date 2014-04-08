from flask import render_template, url_for, request
from app import app
from Board import *
from Move import *
from hiq import *
import pdb


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template("game.html")

@app.route('/_find_solution/', methods=['GET', 'POST'])
def get_moves_for_solution():
	init_state = str(request.form['initialBoard'])
	
	#Convert init_state to list of integers
	position_list = list()
	init_state = init_state.split(",")
	
	for position in init_state:
		position_list.append(int(position))
	

	print "PROCESSING SOLUTION"
	
	#Create the board and get the list of moves towards solution
	brd = Board(position_list)
	moves = solve(brd)
	
	print moves
	
	#Strip the array of moves
	# if len(moves) != 0:
	# 	temp = "".join(str(moves)).strip('[]')
	# 	temp = temp.replace('(','')
	# 	temp = temp.replace(')','')
	# 	return temp

	# #If there is no solution return an empty string
	# else:
	# 	print "NO SOLUTION"
	# 	return ""

	if not moves:
		print "NO SOLUTION"
		return ""
	else:
		temp = "".join(str(moves)).strip('[]')
		temp = temp.replace('(','')
		temp = temp.replace(')','')
		return temp
