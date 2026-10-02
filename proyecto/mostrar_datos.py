import sqlite3

connection_db = sqlite3.connect('bd_nueva.db')

cursor = connection_db.cursor()

cursor.execute(
    '''
        SELECT * FROM Usuarios
    '''
)

resultado = cursor.fetchall()

for res in resultado:
    print(res)

connection_db.commit()

cursor.close()

connection_db.close()