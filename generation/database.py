import sqlite3 as sql

F_DAILY_SHEET = 'daily_sheet.db'

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
    curse.execute("""CREATE TABLE daily_sheet (day int,
                                               rotor_inner int,
                                               rotor_middle int,
                                               rotor_outer int,
                                               rotor_inner_start int,
                                               rotor_middle_start int,
                                               rotor_outer_start int,
                                               reflector text,
                                               plugboard text)""")
    curse.execute("""CREATE TABLE rotors (rotor1 text, 
                                          rotor2 text,
                                          rotor3 text,
                                          rotor4 text,
                                          rotor5 text)""")

@db_operation
def append_database(table, data, curse):
    if table == 'daily_sheet':
        curse.execute("""INSERT INTO daily_sheet VALUES
                         (?,?,?,?,?,?,?,?,?)""", data)
    elif table == 'rotors':
        curse.execute("""INSERT INTO rotors VALUES (?,?,?,?,?)""", data)

@db_operation
def populate_database(daily_data, rotor_data, curse):
    pass
    #for loops, this will be called by other script

