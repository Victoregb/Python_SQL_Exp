'''
Estos ejercicios estan sacados de SQL Head First.
Actividad introductoria al SQL.
Habría que comprobar si añadir un ; a todas las instrucciones se considera
Zen o no.
'''

#%%
import sqlite3
import pandas as pd
# %%

conect = sqlite3.connect('base_datos.db')
conect
# %%


def crear_tabla(nombre, columnas, bd='base_datos.db'):
    conect = sqlite3.connect(bd)
    cursor = conect.cursor()
    cursor.execute(f"CREATE TABLE {nombre}({columnas});")
    conect.commit()
    return 


def añadir_dato(donde, dato, bd='base_datos.db'):
    conect = sqlite3.connect(bd)
    cursor = conect.cursor()
    cursor.execute(f"INSERT INTO {donde} VALUES {dato};")
    conect.commit()
    return 


def ver_data(nombre, bd='base_datos.db'):
    conect = sqlite3.connect(bd)
    cursor = conect.cursor()
    cursor.execute(f'SELECT * FROM {nombre};')
    datos = cursor.fetchall()
    return datos

# %%
crear_tabla('comidas', 'ingredientes, tiempo, dificultad')

# %%
añadir_dato('comidas', ('sopa', '20 min', 'facil'))

# %%
crear_tabla('lista_donuts','''
           donut_nombre VARCHAR(10),
           donut_tipo VARCHAR(6)
            '''

            )

# %%
crear_tabla('gregs_list','''
           apellido VARCHAR(30),
           nombre VARCHAR(15),
           correo VARCHAR(20),
           cumpleaños DATE,
           profesión VARCHAR(50),
           ciudad VARCHAR(50),
           estado VARCHAR(20),
           intereses VARCHAR(100),
           buscando VARCHAR(100)
           '''

            )

# %%
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()

cursor.execute('DROP TABLE gregs_list;')

# %%

crear_tabla('gregs_list','''
           apellido VARCHAR(30),
           nombre VARCHAR(15),
           genero VARCHAR(10),
           correo VARCHAR(20),
           cumpleaños DATE,
           profesión VARCHAR(50),
           ciudad VARCHAR(50),
           estado VARCHAR(20),
           intereses VARCHAR(100),
           buscando VARCHAR(100)
           '''

            )

# %%
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()

#Buscar que es PRAGMA.
#PRAGMA viene a ser una especie de DESCR / DESCRIBE
cursor.execute('PRAGMA table_info(gregs_list)')
# %%

#Si no declaras todas las columnas tienes que añadir todos los datos en el 
# orden correcto. 
cursor.execute('''INSERT INTO gregs_list 
               VALUES ('Gil', 'Victor', 'Varón', 'uno@dos.tres', '23/07/1686', 
               'Psicólogo', 'Donostia', 'Casado', 'No pasar hambre', 'Trabajo')
               
               ;''')
conect.commit()

#Si declaras las columnas a las que vas a añadir datos puedes alterar el orden
cursor.execute('''INSERT INTO gregs_list (apellido, nombre, genero, correo, 
               cumpleaños, profesión, ciudad, estado, intereses, buscando)
               
               VALUES ('Gil', 'Victoria', 'Mujer', 'dos@dos.tres', '15/06/1698', 
               'Psicólogo', 'Valladolid', 'Casado', 'No pasar hambre', 'Trabajo')
               
               ;''')
conect.commit()

#Puedes elegir en que columnas añadir los datos.
cursor.execute('''INSERT INTO gregs_list (apellido, nombre, genero, correo, 
               cumpleaños, profesión, estado, intereses, buscando)
               VALUES ('Gal', 'Vactor', 'Varón', 'tres@dos.tres', '19/07/1798', 
               'analista', 'Soltero', 'Hacer cosas', 'Trabajo')
               
               ;''')
conect.commit()

cursor.execute('''INSERT INTO gregs_list (apellido, nombre, genero, correo, 
               cumpleaños, profesión, ciudad, estado, intereses, buscando)
               VALUES ('Gal', 'Vactor', 'Varón', 'cuatro@dos.tres', 
               '24/08/1898', 'analista', 'Bilbao','Soltero', 'Hacer cosas', 
               'Trabajo')
               
               ;''')
conect.commit()

# %%

cursor.execute('''INSERT INTO gregs_list 
                VALUES ('Paquez', 'Paco', 'Varón', 'cuatro@dos.tres', 
                        '16/06/1688', 'analista', 'Valladolid', 'Casado', 
                        'No pasar hambre', 'Trabajo')
               
               ;''')
conect.commit()

# %%

conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()
cursor.execute('PRAGMA table_info(gregs_list)')
datos = cursor.fetchall()
datos

# %%

conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()
cursor.execute('SELECT * FROM gregs_list')
datos = cursor.fetchall()
datos

# %%
df = pd.DataFrame(datos, columns=['apellido', 'nombre', 'genero', 'correo',
                                  'cumpleaños', 'profesión', 'ciudad', 'estado',
                                  'intereses', 'buscando'])
df

# %%
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()

# %%
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()
#El error cometido es tratar de crear una tabla sin tener en cuenta
# que hace falta tambien declarar las columnas.
cursor.execute("""CREATE TABLE ciudad(nombre, población, provincia);
               """)
conect.commit()

# %%
cursor.execute(
    "INSERT INTO ciudad VALUES('Valladolid', 350000, 'Valladolid');")
conect.commit()
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()


# %%
cursor.execute('SELECT * FROM ciudad')
# %%
datos = cursor.fetchall()
datos

# %%
añadir_dato("gregs_list (apellido, nombre, profesión)", 
            ('Gómez', 'David', 'Arquitecto'))
# %%
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()
cursor.execute('SELECT * FROM gregs_list')
cursor.fetchall()
# %%
#Vamos a evitar que se puedan dejar variables sin añadir.
crear_tabla('contactos', 
            '''
            apellidos VARCHAR (30) NOT NULL,
            nombre VARCHAR (30) NOT NULL,
            genero VARCHAR(10) NOT NULL,
            correo VARCHAR(20) NOT NULL, 
            cumpleaños DATE NOT NULL,
            profesión VARCHAR(50) NOT NULL,
            ciudad VARCHAR(50) NOT NULL,
            estado VARCHAR(20) NOT NULL,
            intereses VARCHAR(100) NOT NULL,
            buscando VARCHAR(100) NOT NULL
            ''')


# %%
cursor.execute('DROP TABLE lista_donuts;')

#%%
#Se pueden tener valores añadidos por defecto. ¡Como con las funciones!
crear_tabla('lista_donuts', '''
            nombre_donut VARCHAR(10) NOT NULL,
            tipo_donut VARCHAR(10) NOT NULL,
            precio_donut DEC(3,2) NOT NULL DEFAULT 1.00
            ''')
# %%
añadir_dato('lista_donuts', ('Chapata', 'dulce', '2'))
añadir_dato('lista_donuts', ('Carpanta', 'dulce', '2'))
añadir_dato('lista_donuts(nombre_donut, tipo_donut)', ('Anacleto', 'salado'))
añadir_dato('lista_donuts(nombre_donut, tipo_donut)', ('Filemón', 'majo'))

ver_data('lista_donuts')
# %%
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()
cursor.execute('PRAGMA table_info(lista_donuts)')
cursor.fetchall()
# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
