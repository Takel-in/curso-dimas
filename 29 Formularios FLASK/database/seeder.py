#Es necesario instalar Flas y Flas-SQLAlchemy
import sqlite3 as sql

DB_PATH = "C:\\Users\\frjoma\\python-learning\\curso-dimas\\29 Formularios FLASK\\database\\streamers.db"

def createDB():
    db = sql.connect(DB_PATH)
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE streamers (
            name text,
            subs integer,
            followers integer
        )
    """)
    db.commit()
    db.close()

def addValues():
    db = sql.connect(DB_PATH)
    cursor = db.cursor()
    data = [
        ('AlexElCapo', 10000, 8000000),
        ('Ibai', 25000, 7000000), 
        ('Elokas', 10000, 1000000), 
        ('Auronplay', 20000, 8000000),
        ('Cristinini', 5500, 3000000)]

    cursor.executemany("""
            INSERT INTO streamers 
            VALUES ( ?, ?, ?)
            """, data)
    db.commit()
    db.close()


if __name__== "__main__":
    createDB()
    addValues()