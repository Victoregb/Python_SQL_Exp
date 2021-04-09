#Aqui ya me estoy alejando un poco de los contenidos del libro ya que se
# centran en MySQL en lugar de SQLite3 que es lo que estoy interesado.
# Los principios no parecen muy diferentes a los que emplea pandas.

#%%
import sqlite3
import pandas as pd
# %%
conect = sqlite3.connect('base_datos.db')
df = pd.read_sql('SELECT * FROM info_payaso', conect)
df
# %%

df = pd.read_sql('SELECT rowid, * FROM info_payaso', conect)
df

# %%
cursor = conect.cursor()
cursor.execute("DROP TABLE libro_payaso")
cursor.execute("CREATE TABLE libro_payaso (nombre_payaso, titulo)")
conect.commit()
# %%
libros = [('Elsie', 'El señor de los anillos'), 
          ('Pickles', 'El señor de las moscas'),
          ('Snuggles', 'La montaña del destino'),
          ('Mr. Hobo', 'Que hace un payaso'),
          ('Clarabelle', 'Chistes 101'),
          ('Scooter', 'Globofléxia: Un modo de vida'),
          ('Zippo', 'Dejar de fumar en 30 sencillos pasos'),
          ('Babe', 'Niños y como aguantarlos'),
          ('Bonzo', 'Expeiencias de un monje'),
          ('Sniffles', 'Perros y cachorros')]

cursor.executemany('INSERT INTO libro_payaso VALUES (?,?)', libros)
conect.commit()
# %%
df = pd.read_sql('SELECT rowid, * FROM libro_payaso', conect)
df
# %%
df2 = pd.read_sql('SELECT rowid, * FROM info_payaso', conect)
df2

# %%
cursor.execute('''
               SELECT nombre, descripción, titulo FROM info_payaso 
               INNER JOIN libro_payaso ON nombre_payaso = nombre
               ''')
datos = cursor.fetchall()
datos

# %%
df2 = pd.read_sql('SELECT rowid, * FROM aseos', conect)
df3 = pd.read_sql('SELECT rowid, * FROM poblacion', conect)

# %%
df3
# %%
#Uno de los problemas que he tenido ha sido llamar a una variable Provincias y a la
# otra provicia, lo que me ha llevado a equivocos. Para la proxima usar el mismo,
# nombre o dejarlo más claro. Tambien he aprendido a emplear el nom_tabla.columna
# lo cual no se diferencia mucho de Pandas.
cursor.close()
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()
cursor.execute('''
               SELECT aseos.aseos, poblacion.Provincias, poblacion.Total FROM aseos
               INNER JOIN poblacion ON poblacion.Provincias LIKE '%'||aseos.provincia||'%' 
               ''')
datos = cursor.fetchall()
cursor.close()
datos
# %%
df4 = pd.DataFrame(datos, columns=['Aseos', 'Provincias', 'Población'])
df4
# %%
