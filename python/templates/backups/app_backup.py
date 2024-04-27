from flask import Flask, render_template, request, session
from templates.classes import Player
from flask import redirect, url_for
import secrets

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registry')
def registry():
    return render_template('registry.html')

@app.route('/blackjack')
def blackjack():
    return render_template('blackjack.html')

@app.route('/register', methods=['POST'])
def register():
    message = ''
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        nickname = request.form['nickname']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']
        player = Player(name, surname, nickname, age, email, password)
        if player.insert_casino_player():
            message = 'Registration successful!'
        else:
            message = 'Registration failed!'
    return render_template('registry.html', message=message)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    login_message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        player = Player(None, None, None, None, email, password)
        if player.login_authentication():
            message = 'Login successful'
            session['logged_in'] = True
            session['nickname'] = player.nickname_from_database()
            login_message = f'Welcome {session["nickname"]}!'
        else:
            message = 'Login incorrect'
    return render_template('index.html', message=message, login_message=login_message)

@app.route('/logout')
def log_out():
     session.pop('logged_in', None)
     session.pop('nickname', None)
     return redirect(url_for('login'))

if __name__ == "__main__":
     app.run(debug=True)



