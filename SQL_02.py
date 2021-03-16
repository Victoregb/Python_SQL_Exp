'''
Estos ejercicios estan sacados de SQL Head First.
Como actividad introductoria al SQL.
Habría que comprobar si añadir un ; a todas las instrucciones se considera
Zen o no.
'''
#%% 
import sqlite3
import pandas as pd
#%%
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()

#Buscar que es PRAGMA.
cursor.execute('PRAGMA table_info(gregs_list)')
# %%


cursor.execute('''INSERT INTO gregs_list 
               VALUES ('Gil', 'Victor', 'Varón', 'uno@dos.tres', '23/07/1686', 
               'Psicólogo', 'Donostia', 'Casado', 'No pasar hambre', 'Trabajo')
               
               ;''')
conect.commit()

cursor.execute('''INSERT INTO gregs_list (apellido, nombre, genero, correo, 
               cumpleaños, profesión, ciudad, estado, intereses, buscando)
               
               VALUES ('Gil', 'Victoria', 'Mujer', 'dos@dos.tres', '15/07/1698', 
               'Psicólogo', 'Valladolid', 'Casado', 'No pasar hambre', 'Trabajo')
               
               ;''')
conect.commit()

cursor.execute('''INSERT INTO gregs_list (apellido, nombre, genero, correo, 
               cumpleaños, profesión, estado, intereses, buscando)
               VALUES ('Gal', 'Vactor', 'Varón', 'tres@dos.tres', '19/07/1698', 
               'analista', 'Soltero', 'Hacer cosas', 'Trabajo')
               
               ;''')
conect.commit()
cursor.execute('''INSERT INTO gregs_list (apellido, nombre, genero, correo, 
               cumpleaños, profesión, ciudad, estado, intereses, buscando)
               VALUES ('Gal', 'Vactor', 'Varón', 'cuatro@dos.tres', 
               '23/07/1698', 'analista', 'Donostia','Soltero', 'Hacer cosas', 
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
cursor.execute("INSERT INTO ciudad VALUES('Valladolid', 350000, 'Valladolid');")
conect.commit()
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()


# %%
cursor.execute('SELECT * FROM ciudad')
# %%
datos = cursor.fetchall()
datos

# %%
