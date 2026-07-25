import sqlite3 as sql
connection=sql.connect('../database/gigafactory.db')
cursor1=connection.cursor()

cursor1.execute('''SELECT Cell_ID, Voltage, Temperature 
                FROM Production 
                WHERE Status="NG"
                ORDER BY Temperature DESC
                ''')
rows=cursor1.fetchall()
cursor1.execute('''SELECT AVG(Temperature)
                FROM Production''')
Average_Temperature=cursor1.fetchone()[0]

# print(Average_Temperature)

# print(rows[0:5])


cursor1.execute("""SELECT Machine, AVG(Temperature) AS Avg_Temp
                FROM Production
                GROUP BY Machine
                HAVING Avg_Temp>32.5
                ORDER BY Avg_Temp DESC
                """)

# print(cursor1.fetchall())

cursor1.execute("""SELECT COUNT(Cell_ID)
                FROM Production
                """)

# print(cursor1.fetchone()[0])
cursor1.execute("""SELECT Machine, COUNT(Cell_ID) AS NG_Count
                FROM Production
                WHERE Status="NG"
                GROUP BY Machine
                ORDER BY NG_Count DESC""")
# print(cursor1.fetchall())

cursor1.execute("""SELECT Machine, AVG(Temperature) AS Avg_Temp,
                MAX(Voltage) AS Max_Voltage,
                COUNT(Cell_ID) AS Cell_Count
                FROM Production
                GROUP BY Machine
                ORDER BY Avg_Temp DESC""")
# print(cursor1.fetchall())


cursor1.execute("""SELECT * 
                FROM Production
                JOIN Quality
                On Production.Cell_ID=Quality.Cell_ID""")

# print(cursor1.fetchall()[0:5][0])
cursor1.execute('''SELECT Quality.Cell_ID,Quality.Machine,Voltage,Quality.Capacity,Final_Result,Defect_Type
                    FROM Production
                    JOIN Quality
                    ON Production.Cell_ID=Quality.Cell_ID
                    WHERE Final_Result='FAIL'
                    ''')

# print(cursor1.fetchmany(5)[0])

cursor1.execute('''SELECT Quality.Machine,COUNT(*) as Failed_Count
                    FROM Production
                    JOIN Quality
                    ON Production.Cell_ID=Quality.Cell_ID
                    WHERE Final_Result='FAIL'
                    GROUP BY Quality.Machine
                    ORDER BY Failed_Count DESC 
                    ''')
# print(cursor1.fetchall())
cursor1.execute('''SELECT Quality.Machine,ROUND(AVG(Quality.Capacity),4) as Avg_Capacity
                    FROM Production
                    JOIN Quality
                    ON Production.Cell_ID=Quality.Cell_ID
                    GROUP BY Quality.Machine 
                    ''')
# info=cursor1.fetchall()
# print(info)
cursor1.execute('''SELECT Machine,Shift,COUNT(*) AS Cell_Count
                    FROM Production

                    GROUP BY Machine,Shift 
                    ''')
# print(cursor1.fetchall())
cursor1.execute('''SELECT 
                        Quality.Machine,
                        Production.Shift, 
                        ROUND(
                            SUM(
                                CASE
                                    WHEN Final_Result='FAIL' THEN 1
                                    ELSE 0
                                END
                            )*100.0 / COUNT(*),
                            3
                        ) AS Failure_Rate
                    FROM Production
                    JOIN Quality 
                        ON Production.Cell_ID=Quality.Cell_ID
                    GROUP BY 
                        Quality.Machine,
                        Production.Shift 
                    HAVING Failure_rate>5
                    ''')
# print(cursor1.fetchall())


cursor1.execute('''SELECT Cell_ID, 
                          Capacity
                    FROM Production
                    WHERE Capacity>
                    (
                        SELECT AVG(Capacity) 
                        FROM Production
                    )
                ''')

# print(cursor1.fetchmany(5))

cursor1.execute('''SELECT Machine,
                          ROUND(AVG(Capacity),3) AS Avg_Capacity
                          FROM Production
                          GROUP BY Machine
                          HAVING Avg_Capacity>
                                (
                                    SELECT ROUND(AVG(Capacity),3)
                                    FROM Production                                
                                )
                          ORDER BY Avg_Capacity DESC
                 ''')
# print(cursor1.fetchmany(5))

cursor1.execute('''SELECT Machine,
                          Cell_ID,
                          Capacity
                    FROM Production P1
                    WHERE Capacity>
                        (
                            SELECT AVG(Capacity)
                            FROM Production P2
                            WHERE P2.Machine=P1.Machine
                        )
                
                ''')

# print(cursor1.fetchmany(5))
cursor1.execute(''' SELECT DISTINCT Machine
                    FROM Production P1
                    WHERE
                    (
                        SELECT COUNT(*)
                        FROM Production P2
                        JOIN Quality
                            ON P2.Cell_ID=Quality.Cell_ID
                        WHERE Final_Result='FAIL' AND 
                              P2.Machine=P1.Machine
                    )>
                    0
                
                ''')
# print(cursor1.fetchall())
cursor1.execute(''' SELECT M.Machine
                    FROM 
                    (
                        SELECT DISTINCT Machine
                        FROM Production
                    ) AS M 
                    WHERE EXISTS
                    (
                        SELECT *
                        FROM Quality Q
                        JOIN Production P
                            ON Q.Cell_ID=P.Cell_ID
                        WHERE P.Machine=M.Machine AND 
                              Final_Result='FAIL'
                        
                    ) 
                
                ''')
# print(cursor1.fetchall())

cursor1.execute('''SELECT Cell_ID, ROUND(Voltage,2)
                    FROM (SELECT
                            Cell_ID,Voltage,
                            CASE
                                WHEN Voltage<3.6 THEN 'Low'
                                WHEN Voltage<3.8 THEN 'Normal'
                                ELSE 'High'
                            END AS Status
                        FROM Production)
                    WHERE Status='Low'
                ''')

# print(cursor1.fetchmany(5))

