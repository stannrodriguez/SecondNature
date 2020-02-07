from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
	app = Flask(__name__)

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	@app.route('/')
	def test():
		return 'Testing Second Nature Application'

	@app.route('/home')
	def home():
		import os
		wd = os.getcwd()
		return wd

	return app