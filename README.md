# HIQ (Peg Solitre) Solver #

## About This Project##
This web application was created as a project in AI course with another classmate.  
You can find a live demo of this project at [http://hiqsolver-csc44800.rhcloud.com](http://hiqsolver-csc44800.rhcloud.com).

This project is written in *python* and using the [Flask](http://flask.pocoo.org) framework.

If you are not familiar with this game you can read about at [wikipedia](http://en.wikipedia.org/wiki/Peg_solitaire)

#### Project Outline####
The goal of this project is find a solution for a traditional peg solitaire board (if one exists) or display an error message in case there is no solution.  
The method used for this project is [*backtracking*](http://en.wikipedia.org/wiki/Backtracking)

##Installation##
After cloneining the repository, navigate to the repository folder and type:
```
virtualenv --no-site-packages .hiq && source .hiq/bin/activate && pip install -r requirements.txt
```
##Usage##
Start the app by typing 
```
cd FlaskApp
python runserver.py
```

You can use one of the 3 examples which have a solution or generate your own board by clicking the pegs. Each clicked peg disappeared from the board.  
After you are done to set up the board just click **Find Solution**.

##Libraries in use
* Flask
* Jinja
* MarkupSafe
* Werkzeug
* itsdangerous
* termcolor
* wsgiref
