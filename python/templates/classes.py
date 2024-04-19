import psycopg2

class Player:
    def __init__(self, name, surname, age, email, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.password = password

    def insert_casino_player(self):    
        conn = psycopg2.connect(
            dbname="casino_database",
            user = "postgres",
            password = "postgres",
            host = "localhost",
            port = "5433"
        )

        cur = conn.cursor()
        query = '''INSERT INTO casino_player (name, surname, age, email, password) VALUES (%s, %s, %s, %s, %s)'''
        cur.execute(query, (self.name, self.surname, self.age, self.email, self.password))
        conn.commit()
        conn.close()
