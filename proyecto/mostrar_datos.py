<<<<<<< HEAD
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

=======
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

>>>>>>> df1e5e06a9a7e9cd37b6b9e54bf6110a6644e78a
connection_db.close()