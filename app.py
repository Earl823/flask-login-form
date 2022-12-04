from flask import Flask, render_template, request, redirect, url_for, session
import MySQLdb.cursors
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

app.secret_key = 'secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login_form'
 
mysql = MySQL(app)

#index page whre login form located
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']

		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password,))
		account = cursor.fetchone()

		if account:
			# session['loggedin'] = True
			# session['id'] = account['id']
			# session['email'] = account['email']

			return 'loggedin successfully'
		else:
			return 'not login'

	return render_template('index.html')

#signin page
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():

	if request.method == 'POST':
		email = request.form.get('sEmail')
		password = request.form.get('sPassword')

		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('INSERT INTO user VALUES (NULL, %s, %s)', (email,password,))
		mysql.connection.commit()
		cursor.close()

		return redirect(url_for('login'))

	return render_template('signUp.html')

if __name__ == '__main__':
	app.run(debug=True)

# print('hello')