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
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']
        player = Player(name, surname, age, email, password)
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
        player = Player(None, None, None, email, password)
        if player.login_authentication():
            message = 'Login successful'
            login_message = f'Player {email} logedd in!'
        else:
            message = 'Login incorrect'
    return render_template('index.html', message=message, login_message=login_message)

if __name__ == "__main__":
    app.run(debug=True)



