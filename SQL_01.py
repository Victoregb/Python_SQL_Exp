#%%
import sqlite3
import pandas as pd
# %%

conect = sqlite3.connect('base_datos.db')
conect
# %%


def crear_tabla(formato, bd='base_datos.db'):
    conect = sqlite3.connect(bd)
    cursor = conect.cursor()
    cursor.execute(f"CREATE TABLE {formato}")
    conect.commit()


def añadir_dato(donde, dato, bd='base_datos.db'):
    conect = sqlite3.connect(bd)
    cursor = conect.cursor()
    cursor.execute(f"INSERT INTO {donde} VALUES {dato}")
    conect.commit()


# %%
crear_tabla('comidas(ingredientes, tiempo, dificultad)')

# %%
añadir_dato('comidas', ('sopa', '20 min', 'facil'))

# %%
crear_tabla('''lista_donuts (
           donut_nombre VARCHAR(10),
           donut_tipo VARCHAR(6)
           
           );'''

            )

# %%
crear_tabla('''gregs_list (
           apellido VARCHAR(30),
           nombre VARCHAR(15),
           correo VARCHAR(20),
           cumpleaños DATE,
           profesión VARCHAR(50),
           ciudad VARCHAR(50),
           estado VARCHAR(20),
           intereses VARCHAR(100),
           buscando VARCHAR(100)
           );'''

            )

# %%
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()

cursor.execute('DROP TABLE gregs_list;')

# %%

crear_tabla('''gregs_list (
           apellido VARCHAR(30) NOT NULL,
           nombre VARCHAR(15) NOT NULL,
           genero VARCHAR(10),
           correo VARCHAR(20),
           cumpleaños DATE,
           profesión VARCHAR(50),
           ciudad VARCHAR(50),
           estado VARCHAR(20),
           intereses VARCHAR(100),
           buscando VARCHAR(100)
           );'''

            )

# %%
