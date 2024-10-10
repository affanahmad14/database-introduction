import sqlite3

# Verbindung zu sqlite-DB (falls nicht vorhanden ist, dann wird die erstellt.)
conn = sqlite3.connect('studenden.db')

# Erstellung von Cursor um sql-Befehl durchzuführen. 
cursor = conn.cursor()

# Erstellung von Tabellen in studenden.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    age INTEGER NOT NULL, 
    course VARCHAR(32) NOT NULL
    );
''')
# Erste Funktion hinzufügen (CREATE)
def add_student(name, age, course):
    cursor.execute('''
    INSERT INTO Students (name, age, course) VALUES (?, ?, ?)
    ''', (name, age, course))
    conn.commit()
    print(f"{name} wurde hinzugefügt")

# Erstellung von READ funktion
def show_students():
    cursor.execute('SELECT name FROM Students')
    students = cursor.fetchall()
    for name in students:
        print(name)

show_students()
# add_student('Abdullah', 150, 'TECHSTARTER')