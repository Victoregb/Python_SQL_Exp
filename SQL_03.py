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
    return print(f'''
                   INSERT INTO {donde} VALUES {dato}
                   ''')

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
payaso4 = ('Mr. Hobo', 'BG Circus', 'M, cigar, black hair, tiny hat', 'violin')
payaso5 = ('Clarabelle', 'Belmont Senior Center', 'F, pink hair, huge flower, blue dress', 'yelling, dancing')
payaso6 = ('Scooter', 'Oakland Hospital', 'M, blue hair, red suit, huge nose', 'balloons')
payaso7 = ('Zippo', 'Millstone Mall', 'F, orange suit, baggy pants', 'dancing')
payaso8 = ('Babe', 'Earl  Autos', 'F, all pink and sparkly', 'balancing, little car')
payaso9 = ('Bonzo', 'M, in drag, polka dotted dress', 'singing, dancing')
payaso10 = ('Sniffles', 'Tracy\'s', 'M, green and purple suit, pointy nose')

lista_payasos = [payaso1, payaso2, payaso3, payaso4, payaso5, 
                 payaso6, payaso7, payaso8, payaso9, payaso10]
donde = ["info_payaso ('nombre', 'visto_ult_vez', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'visto_ult_vez', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'visto_ult_vez', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'visto_ult_vez', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'visto_ult_vez', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'visto_ult_vez', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'visto_ult_vez', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'visto_ult_vez', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'descripción', 'actividades')",
            "info_payaso ('nombre', 'visto_ult_vez', 'descripción')"]

#Por un despiste en ligar de emplear la variable contador había dejado
# el valor 0. Normal que no funcionara.
contador = 0
for i in lista_payasos:
#    print(donde[contador])
#    print(i)
    intro_dato(donde[contador], i)
    contador += 1

# %%
conect = sqlite3.connect('base_datos.db')
df = pd.read_sql('SELECT * FROM info_payaso', conect)
df

# %%
cursor = conect.cursor()
cursor.execute('''
               INSERT INTO info_payaso
               VALUES ('Bonzo', 'Dickson Park', 'M, in drag, polka dotted dress', 'singing, dancing')
               ''')
conect.commit()
# %%
cursor.execute('''
               INSERT INTO info_payaso
               VALUES ('Zippo', 'Millstone Mall', 'F, orange suit, baggy pants', 'dancing, singing')
               ''')
conect.commit()

cursor.execute('''
               INSERT INTO info_payaso
               VALUES ('Snuggles', 'Ball?Mart', 'F, yellow shirt, baggy blue pants', 'horn, umbrella')
               ''')
conect.commit()

cursor.execute('''
               INSERT INTO info_payaso
               VALUES ('Sniffles', 'Tracy''s', 'M, green and purple suit, pointy nose', 'tiny car')
               ''')
conect.commit()

cursor.execute('''
               INSERT INTO info_payaso
               VALUES ('Mr. Hobo', 'Party for Eric Gray', 'M, cigar, black hair, tiny hat', 'violin')
               ''')
conect.commit()

# %%
df=pd.read_sql("SELECT * FROM info_payaso WHERE nombre = 'Zippo'", conect)
df
# %%
cursor.execute('''
               DELETE FROM info_payaso
               WHERE actividades = 'dancing'
               ''')
conect.commit()
# %%
df = pd.read_sql('SELECT * FROM info_payaso', conect)
df

# %%
#Mi error era añadir comillas al nombre de las columnas, lo que hacía que 
# el codigo no reconociera la columna. Tengo que tener cuidado con ese 
# habito de pandas.
#Uso de UPDATE SET
cursor.execute("UPDATE info_payaso SET visto_ult_vez = 'Plaza Mayor' WHERE visto_ult_vez IS NULL;")
conect.commit()
df = pd.read_sql('SELECT * FROM info_payaso', conect)
df
# %%
df = pd.read_sql("SELECT * FROM info_payaso WHERE actividades IS NULL ", conect)
df

# %%

