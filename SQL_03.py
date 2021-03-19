#%%
import sqlite3
import pandas as pd
# %%
def crear_tabla(nombre, columnas, db = 'base_datos.db'):
    conect = sqlite3.connect('base_datos.db')
    cursor = conect.cursor()
    cursor.execute(f'''
                   CREATE TABLE IF NOT EXISTS {nombre}({columnas});
                   ''')
    conect.commit()
    return print(f'Tabla {nombre} creada!')

def intro_dato(donde, dato, db='base_datos.db'):
    conect = sqlite3.connect('base_datos.db')
    cursor = conect.cursor()
    cursor.execute(f'''
                   INSERT INTO {donde} VALUES {dato}
                   ''')
    conect.commit()
    return print('Dato in')

def borrar_tabla(nombre, db = 'base_datos.db'):
    conect = sqlite3.connect('base_datos.db')
    cursor = conect.cursor()
    cursor.execute(f'''
               DROP TABLE IF EXISTS {nombre}
               ''')
    conect.commit()
    return print(f'Tabla {nombre} borrada.')
# %%
borrar_tabla('info_payaso')
crear_tabla('info_payaso', '''
            nombre VARCHAR(50) DEFAULT NULL,
            visto_ult_vez VARCHAR(50) DEFAULT NULL,
            descripción VARCHAR(50) DEFAULT NULL,
            actividades VARCHAR(50) DEFAULT NULL
            ''')
# %%
columnas = ['nombre', 'visto_ult_vez', 'descripción', 'actividades']
payaso1 = ('Elsie', 'Cherry Hill Senior Center', 'F, red hair, green dress, huge feet', 'balloons, little car')
payaso2 = ('Pickles', 'Jack Green\'s party', 'M, orange hair, blue suit, huge feet', 'mime')
payaso3 = ('Snuggles', 'Ball?Mart', 'F, yellow shirt, baggy red pants', 'horn, umbrella')
payaso4 = ('Mr. Hobo', 'Party for Eric Gray', 'M, cigar, black hair, tiny hat', 'violin')
payaso5 = ('Clarabelle', 'Belmont Senior Center', 'F, pink hair, huge flower, blue dress', 'yelling, dancing')
payaso6 = ('Scooter', 'Oakland Hospital', 'M, blue hair, red suit, huge nose', 'balloons')
payaso7 = ('Zippo', 'Millstone Mall', 'F, orange suit, baggy pants', 'dancing')
payaso8 = ('Babe', 'Earl  Autos', 'F, all pink and sparkly', 'balancing, little car')
payaso9 = ('Bonzo', '', 'M, in drag, polka dotted dress', 'singing, dancing')
payaso10 = ('Sniffles', 'Tracy\'s', 'M, green and purple suit, pointy nose', '')

lista_payasos = [payaso1, payaso2, payaso3, payaso4, payaso5, 
                 payaso6, payaso7, payaso8, payaso9, payaso10]

for i in lista_payasos:
    intro_dato('info_payaso', i)

# %%

