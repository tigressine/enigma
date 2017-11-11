import sqlite3 as sql

F_DAILY_SHEET = 'data/daily_sheet.db'
F_RAW_DAILY_SHEET = 'data/raw.txt'

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
def create_database(curse):
    curse.execute("""CREATE TABLE daily_sheet
                     (day int, rotor_inner int, rotor_middle int,
                      rotor_outer int, rotor_inner_start int,
                      rotor_middle_start int, rotor_outer_start int,
                      reflector text, plugboard text)""")

@db_operation
def populate_database(curse):
    with open(F_RAW_DAILY_SHEET, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split('|')
            curse.execute("""INSERT INTO daily_sheet
                             VALUES(?,?,?,?,?,?,?,?,?)""", tuple(data))

@db_operation
def read_column(day, column, curse):
    curse.execute("""SELECT * FROM daily_sheet WHERE day=?""", (day,))
    row = curse.fetchone()
    data = {'day' : row[0],
            'rotor_nums': (row[1]-1, row[2]-1, row[3]-1),
            'rotor_start': (row[4]-1, row[5]-1, row[6]-1),
            'reflector': row[7],
            'plugboard': row[8]}
    
    return data[column]

def print_database():
    for i in range(1, 32):
        print(read_column(i, 'day'), ' ', end='')
        print(read_column(i, 'rotor_nums'), ' ', end='')
        print(read_column(i, 'rotor_start'), ' ', end='')
        print(read_column(i, 'reflector'), ' ', end='')
        print(read_column(i, 'plugboard'), ' ')
