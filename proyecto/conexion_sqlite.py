import sqlite3

connection_db = sqlite3.connect('bd_nueva.db')

cursor = connection_db.cursor()

cursor.execute(
    '''
        CREATE TABLE Usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(25) NOT NULL,
            contrasenia VARCHAR(25) NOT NULL
        )
    '''
)

nombre = "sergio"
contrasenia = "12345678"

cursor.execute(
    '''
        INSERT INTO Usuarios (nombre, contrasenia)
        VALUES (?, ?)
    ''',
    (nombre, contrasenia)
)

connection_db.commit()

cursor.close()

connection_db.close()

print("Se ejecuto correctamente todo, la creacion de la base de datos")