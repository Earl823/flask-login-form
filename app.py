from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

# database connection
def db_conn():
	conn = None
	try:
		conn = sqlite3.connect('user.sqlite')
	except sqlite3.error as e:
		print(e)
	return conn

@app.route('/', methods = ['GET', 'POST'])
def login():
	# conn = db_conn
	# cursor = conn.cursor()		

	return render_template('index.html')

@app.route('/signup', methods = ['GET', 'POST'])
def sign_up():
	conn = db_conn()
	cursor = conn.cursor()

	if request.method == 'POST':
		email = request.form.get('sEmail')
		password = request.form.get('sPassword')

		sql = """INSERT INTO USER (email, password) VALUES (?, ?)"""
		cursor.execute(sql, (email, password))
		conn.commit()
		return redirect(url_for('login'))

	return render_template('signUp.html')

if __name__ == '__main__':
	app.run(debug=True)

# print('hello')