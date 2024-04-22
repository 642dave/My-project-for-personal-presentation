import psycopg2, bcrypt

class Player:
    def __init__(self, name, surname, age, email, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.password = password

    # Convert the password to a hash
    def password_to_hash(self, password):
        try:  
            password_bytes = self.password.encode('utf-8')
            hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            return hash 
        except Exception as e:
            print(f'Password setting error {e}')
            return None

    # Inserts data from the user into the database
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

            hash = self.password_to_hash(self.password)

            cur.execute(query, (self.name, self.surname, self.age, self.email, hash))
            conn.commit()
            conn.close()
        except psycopg2.DatabaseError as e:
            print(f'Database error {e}')
        except Exception as e:
            print(f'General error {e}')
        else:
            print('User successfully added')

   # Get the hash from the database
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
            query = '''SELECT password FROM casino_player WHERE email = %s'''
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
        
    # Check if the user is in the database
    def login_authentication(self):
        try:
            hash = self.get_hash_from_database()
            password_byte = bytes(self.password, 'utf-8')
            if bcrypt.checkpw(password_byte, hash):
                print('Login successful')
                return True
            else:
                print('Login failed')
                return False
        except Exception as e:
            print(f'Error {e}')       

            

