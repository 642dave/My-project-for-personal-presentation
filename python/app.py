from flask import Flask, render_template, request
from templates.classes import Player

app = Flask(__name__)

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
        else:
            message = 'Login incorrect'
        nickname = player.nickname_from_database()
        login_message = f'Welcome {nickname}!'
    return render_template('index.html', message=message, login_message=login_message)

if __name__ == "__main__":
    app.run(debug=True)



