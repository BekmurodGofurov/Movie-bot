import sqlite3 as sq

db = sq.connect('movies.db')
cur = db.cursor()

async def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS users_data(
              user_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name text,
              username text,
              added_at DATETIME DEFAULT CURRENT_TIMESTAMP)""") 
    cur.execute("""CREATE TABLE IF NOT EXISTS movie_data(
              movie_id taxt, 
              random_id taxt, 
              title text,
              description text,
              added_at DATETIME DEFAULT CURRENT_TIMESTAMP)""")  
    db.commit()            

def add_user(user_id, name, username):
    cur.execute("INSERT INTO users_data (user_id, name, username) VALUES (?,?,?)", (user_id, name, username))
    db.commit()    

def add_movie(movie_id, random_id, title, description):
    cur.execute("INSERT INTO movie_data (movie_id, random_id, title, description) VALUES (?,?,?,?)", (movie_id, random_id, title, description))
    db.commit() 

def get_user(user_id):
    cur.execute("SELECT * FROM users_data WHERE user_id = ?", (user_id,))
    row = cur.fetchone()

    if row:
        return row
    else:
        return None    

def get_movie(random_id):
    cur.execute("SELECT * FROM movie_data WHERE random_id = ?", (random_id,))
    row = cur.fetchone()

    if row:
        return row
    else:
        return None 
    
def update(new_chance, user_id):
    cur.execute('UPDATE users_data SET chance=? WHERE user_id=?', (new_chance, user_id))
    db.commit()    