
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

# %%
