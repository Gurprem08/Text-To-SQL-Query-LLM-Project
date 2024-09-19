import sqlite3


with sqlite3.connect("student.db") as conn :

    cursor = conn.cursor()


    table_info = '''

    CREATE table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
    '''

    cursor.execute(table_info)




    cursor.execute('''INSERT INTO STUDENT VALUES('Krish', 'Data Science', 'A', 90)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Sudhanshu', 'Data Science', 'B', 100)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Darius', 'Data Science', 'A', 86)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Vikas', 'DEVOPS', 'A', 50)''')
    cursor.execute('''INSERT INTO STUDENT VALUES('Dipesh', 'DEVOPS', 'B', 35)''')

    print("The insert records are ...")

    data =cursor.execute('''Select * from STUDENT''')


    for row in data :
        print(row)

    conn.commit