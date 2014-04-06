from flask import render_template, url_for, request
from app import app
from Board import *
from Move import *
from hiq import *
import pdb


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template("test.html")

@app.route('/_find_solution/', methods=['GET', 'POST'])
def get_moves_for_solution():
	init_state = str(request.form['initialBoard'])
	
	#Convert init_state to list of integers

	position_list = list()
	init_state = init_state.split(",")
	
	for position in init_state:
		position_list.append(int(position))
	print position_list
	brd = Board(position_list)
	
	moves = solve(brd)

	print moves


	
	 
	temp = "".join(str(moves)).strip('[]')
	temp = temp.replace('(','')
	temp = temp.replace(')','')
	return temp
