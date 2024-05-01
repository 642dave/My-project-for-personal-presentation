from flask import Flask, render_template, request, session, redirect, url_for, flash
from templates.classes import Player, RegistrationForm
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registry', methods=['GET', 'POST'])
def register_form():
    form = RegistrationForm()
    message = session.pop('message', '')
    if request.method == 'POST':
        if form.validate_on_submit():
            player = Player(form.name.data, form.surname.data, form.nickname.data, form.age.data, form.email.data, form.password.data)
            if player.insert_casino_player():
                session['message'] = 'Registration successful!'
                return redirect(url_for('register_form'))
            else:
                message = 'Registration failed!'
    return render_template('registry.html', form=form, message=message)

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

@app.route('/blackjack')
def blackjack():
    return render_template('blackjack.html')

@app.route('/logout')
def log_out():
     session.pop('logged_in', None)
     session.pop('nickname', None)
     return redirect(url_for('login'))

if __name__ == "__main__":
     app.run(debug=True)


            

