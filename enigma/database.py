#! /usr/bin/env python3
import sqlite3 as sql

F_DAILY_SHEET = 'daily_sheet.db'
F_RAW_DAILY_SHEET = 'daily_sheet_raw.txt'

def db_operation(operation):
    def db_wrap(*args, **kwargs):
        db = sql.connect(F_DAILY_SHEET)
        curse = db.cursor()

        result = operation(*args, curse, **kwargs)

        db.commit()
        db.close()
        return result

    return db_wrap

@db_operation
def read_column(day, column, curse):
    curse.execute('''SELECT * FROM daily_sheet WHERE day=?''', (day,))
    row = curse.fetchone()
    values = {'day' : row[0],
              'rotor_nums': (row[1], row[2], row[3]),
              'rotor_start': (row[4], row[5], row[6]),
              'reflector': row[7],
              'plugboard': row[8]}
    return values[column]


@db_operation
def create_database(curse):
    curse.execute("""CREATE TABLE daily_sheet (day int,
                                               rotor_inner int,
                                               rotor_middle int,
                                               rotor_outer int,
                                               rotor_inner_start int,
                                               rotor_middle_start int,
                                               rotor_outer_start int,
                                               reflector text,
                                               plugboard text)""")

@db_operation
def populate_database(curse):
    with open(F_RAW_DAILY_SHEET, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split('|')
            for i in range(7):
                data[i] = int(data[i])
            curse.execute("""INSERT INTO daily_sheet VALUES(?,?,?,?,?,?,?,?,?)""", tuple(data))

#create_database()
#populate_database()

print(read_column(2, 'rotor_nums'))
print(read_column(4, 'plugboard'))
