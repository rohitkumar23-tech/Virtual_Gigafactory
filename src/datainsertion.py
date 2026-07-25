import pandas as pd
import sqlite3 as sql

connection=sql.connect('../database/gigafactory.db')

cursor=connection.cursor()

production_data=pd.read_excel('../raw_data/gigafactory_production_10000.xlsx')
quality_data=pd.read_csv('../raw_data/quality.csv')

cursor.execute("""DROP TABLE IF EXISTS Production""")
cursor.execute("""DROP TABLE IF EXISTS Quality""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Quality
               (Cell_ID TEXT PRIMARY KEY NOT NULL,
               Machine TEXT,
               OCV REAL,
               DCIR REAL,
               Capacity TEXT,
               Final_Result TEXT,
               Defect_Type TEXT
               )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Production
               (Cell_ID TEXT PRIMARY KEY NOT NULL,
               Voltage REAL,
               Current REAL,
               Temperature REAL,
               Machine TEXT,
               Shift TEXT,
               Operator TEXT,
               Production_Date DATE,
               OCV REAL,
               DCIR REAL,
               Capacity REAL,
               Status TEXT
               )""")
column_names_production=production_data.columns
column_names_quality=quality_data.columns

place_values=','.join(['?']*len(column_names_production))
query=f'INSERT INTO Production VALUES({place_values})'


for index,row in production_data.iterrows():
    values=[row[col] for col in column_names_production]
    cursor.execute(query,values)

place_values=','.join(['?']*len(column_names_quality))
query=f'INSERT INTO Quality VALUES({place_values})'

for index,row in quality_data.iterrows():
    values=[row[col] for col in column_names_quality]
    cursor.execute(query,values)

connection.commit()
connection.close()