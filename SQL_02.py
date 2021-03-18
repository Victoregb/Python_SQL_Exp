
#%% 
import sqlite3
import pandas as pd
import random
#%% 
#Con esto vamos a generar un DataFrame con el que poder jugar y hacer algunos de
# los ejercicios propuestos.
df = pd.DataFrame(columns=['nombre', 'ciudades', 'trabajo', 
                           'hijos','pelis', 'pelis al mes','referencia'])

nombre = ['Paco', 'Fernando', 'Javier', 'Matías', 'Alicia', 
          'Elena', 'Itsaso', 'Raquel']

ciudades = ['Donostia', 'Madrid', 'Granada', 'Valladolid', 'Murcia', 
            'Barcelona', 'Bilbao', 'Santiago de compostela']

pelis = ['Abyss', 'Avatar', 'Alien', 'Harry Potter', 'Hackers', 
         'La Momia', 'It\'s about time', 'La ola']

trabajo = ['Enfermería', 'Peluquería', 'Limpieza', 'Ingeniería', 
           'Telecomunicaciones', 'Análsis de datos', 'Psicología', 
           'Investigación']


for i in range(0,26):
        print(i)
        nuevo_dato = [nombre[random.randint(0, 7)], 
                      ciudades[random.randint(0, 7)], 
                      trabajo[random.randint(0, 7)],
                      random.randint(0,3), 
                      pelis[random.randint(0, 7)], 
                      random.randint(0, 60), 
                      random.randint(0, 999999)]
        nuevo_dato = pd.Series(nuevo_dato, index=df.columns)
        df = df.append(nuevo_dato, ignore_index=True)


df
# %%
#Como no lo vamos a lograr a la primera, y para evitar problemas en caso de
# volver a usar la celda.
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()
cursor.execute('''
               DROP TABLE IF EXISTS pelis_prestadas
               ''')
conect.commit()

#Experimento a ver como funciona.
df.to_sql(name='pelis_prestadas', con=conect)

# %%
#Si notas que repites mucho el proceso de conectar es que la práctica enseña,
# y es algo que traigo reciente de The Hard Way.
conect = sqlite3.connect('base_datos.db')
cursor = conect.cursor()
cursor.execute('''
               SELECT * FROM pelis_prestadas 
               ''')
datos = cursor.fetchall()
datos
conect.commit()

# %%
#Un método mucho más limpio para obtener los datos con Pandas desde luego.
datos = pd.read_sql('SELCT * FROM pelis_prestadas', conect)
datos
#Un vez hecho esto y jugado con Pandas y sqlite va siendo hora de volver al libro.
# %%
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, pelis FROM pelis_prestadas
               WHERE ciudades = 'Donostia';''')
datos = cursor.fetchall()
datos
# %%
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, pelis FROM pelis_prestadas
               WHERE ciudades = 'Donostia' AND hijos = 0;''')
datos = cursor.fetchall()
datos

# %%
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE ciudades <= 'M' AND hijos = 0;''')
datos = cursor.fetchall()
datos

# %%
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE ciudades <= 'M' AND hijos >= 3;''')
datos = cursor.fetchall()
datos

# %%
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE ciudades <= 'M' OR hijos >=3;''')
datos = cursor.fetchall()
datos

# %%
#El simbolo % en la busqueda con LIKE indica que hay un número indeterminado
# de elementos que pueden preceder a los terminos indicados.
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE trabajo LIKE '%ía';''')
datos = cursor.fetchall()
datos

# %%
#Por otro lado el uso de _ indica el número exacto de carácteres indeterminados,
# como podemos ver en el ejemplo 8 carácteres antes de 'ía'.
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE trabajo LIKE '________ía';''')
datos = cursor.fetchall()
datos

# %%
#Interesante, usando la busqueda por carácteres la busqueda no es inclusiva
# para la ultima letra (para incluir Psicología, la busqueda de I hasta Q, no P)
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE trabajo BETWEEN 'I' AND 'Q';''')
datos = cursor.fetchall()
datos

# %%
#La busqueda es inclusiva, los resultados incluye tanto 1 como 3 hijos.
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, hijos, pelis FROM pelis_prestadas
               WHERE hijos BETWEEN 1 AND 3;''')
datos = cursor.fetchall()
datos

# %%
#Se puede pasar una lista con IN
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE trabajo IN ('Psicología', 'Enfermería');''')
datos = cursor.fetchall()
datos

# %%
#O con NOT IN en caso de querer excluir elementos. 
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE trabajo NOT IN ('Psicología', 'Enfermería');''')
datos = cursor.fetchall()
datos

# %%
cursor = conect.cursor()
cursor.execute('''SELECT nombre, trabajo, ciudades, pelis FROM pelis_prestadas
               WHERE NOT trabajo LIKE 'Enfermería';''')
datos = cursor.fetchall()
datos

# %%
