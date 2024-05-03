import psycopg2
import bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class Player:
    def __init__(self, name, surname, nickname, age, email, password_hash):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.age = age
        self.email = email
        self.password_hash = password_hash  

    def password_to_hash(self):
        try:  
            password_bytes = self.password_hash.encode('utf-8')
            hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            return hash 
        except Exception as e:
            print(f'Password setting error {e}')
            return None

    def insert_casino_player(self):
        try:    
            conn = psycopg2.connect(
                dbname="casino_database",
                user = "postgres",
                password = "postgres",
                host = "localhost",
                port = "5433"
            )

            cur = conn.cursor()
            query = '''INSERT INTO casino_player (name, surname, nickname, age, email, password_hash) VALUES (%s, %s, %s, %s, %s, %s)'''

            hash = self.password_to_hash()

            cur.execute(query, (self.name, self.surname, self.nickname, self.age, self.email, hash))
            conn.commit()
            conn.close()
        except psycopg2.DatabaseError as e:
            print(f'Database error {e}')
        except Exception as e:
            print(f'General error {e}')
        else:
            print('User successfully added')
            return True

    def get_hash_from_database(self):
        try:
            conn = psycopg2.connect(
                dbname="casino_database",
                user = "postgres",
                password = "postgres",
                host = "localhost",
                port = "5433"
            )
            cur = conn.cursor()
            query = '''SELECT password_hash FROM casino_player WHERE email = %s'''
            cur.execute(query, (self.email,))
            user_hash_password = cur.fetchone()
            conn.close()

            if user_hash_password:
                return bytes.fromhex(user_hash_password[0][2:])  
            else:
                return b''
        except psycopg2.DatabaseError as e:
            print(f'Database error {e}')    
        except Exception as e:
            print(f'General error {e}')
            return b''

    def nickname_from_database(self):
        try:
            conn = psycopg2.connect(
                dbname="casino_database",
                user = "postgres",
                password = "postgres",
                host = "localhost",
                port = "5433"
            )
            cur = conn.cursor()
            query = '''SELECT nickname FROM casino_player WHERE email = %s'''
            cur.execute(query, (self.email,))
            nickname = cur.fetchone()
            conn.close()
            if nickname:
                return nickname[0]
            else:
                return ''
        except psycopg2.DatabaseError as e:
            print(f'Database error {e}')
        except Exception as e:
            print(f'General error {e}')
            return ''

    def login_authentication(self):
        try:
            hash = self.get_hash_from_database()
            password_byte = bytes(self.password_hash, 'utf-8')
            if bcrypt.checkpw(password_byte, hash):
                return True
            else:
                return False
        except Exception as e:
            print(f'Error {e}')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Submit')

            

