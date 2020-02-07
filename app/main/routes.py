from flask import render_template
from datetime import datetime
from app.main import bp

@bp.route('/')
def test():
	return render_template('home.html')

@bp.route('/about')
def about():
	return render_template('about.html')

@bp.route('/calendar')
def calendar():
	date = datetime.now().strftime("%A, %B %d")
	habits = ['Exercise', 'Meditate', 'Study']
	return render_template('calendar.html', date=date, habits=habits)

@bp.route('/contract')
def contract():
	return render_template('contract.html')

@bp.route('/reflection')
def reflection():
	return render_template('reflection.html')