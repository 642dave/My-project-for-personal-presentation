import psycopg2, bcrypt

class Player:
    def __init__(self, name, surname, age, email, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.password = password

    def password_to_hash(password):
        try:  
            password_bytes = password.encode('utf-8') 
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
            query = '''INSERT INTO casino_player (name, surname, age, email, password) VALUES (%s, %s, %s, %s, %s)'''

            hash = Player.password_to_hash(self.password)

            cur.execute(query, (self.name, self.surname, self.age, self.email, hash))
            conn.commit()
            conn.close()
        except psycopg2.DatabaseError as e:
            print(f'Database error {e}')
        except Exception as e:
            print(f'General error {e}')
        else:
            print('User successfully added')
