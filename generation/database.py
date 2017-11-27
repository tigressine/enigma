"""
Author: Tiger Sachse
Version: 1.0.0
Release: 30 November 2017
"""
import sqlite3 as sql

F_ENIGMA_DATA = 'enigma.db'

def db_operation(operation):
    """
    Decorates database functions by opening the database, initializing
    the cursor, and committing and closing after the function executes.
    """
    def db_wrap(*args, **kwargs):
        db = sql.connect(F_ENIGMA_DATA)
        curse = db.cursor()

        result = operation(*args, curse, **kwargs)

        db.commit()
        db.close()
        return result

    return db_wrap

@db_operation
def create(curse):
    curse.execute("""CREATE TABLE daily_sheet (day int,
                                               rotor_inner int,
                                               rotor_middle int,
                                               rotor_outer int,
                                               rotor_inner_start int,
                                               rotor_middle_start int,
                                               rotor_outer_start int,
                                               reflector text,
                                               plugboard text)""")
    curse.execute("""CREATE TABLE rotors (rotor text)""") 

@db_operation
def append(table, data, curse):
    if table == 'daily_sheet':
        curse.execute("""INSERT INTO daily_sheet VALUES
                         (?,?,?,?,?,?,?,?,?)""", data)
    elif table == 'rotors':
        curse.execute("""INSERT INTO rotors VALUES (?)""", data)

@db_operation
def populate(daily_data, rotor_data, curse):
    for day in range(0, 31):
        data = (day,
                daily_data['rotors'][day][0],
                daily_data['rotors'][day][1],
                daily_data['rotors'][day][2],
                daily_data['positions'][day][0],
                daily_data['positions'][day][1],
                daily_data['positions'][day][2],
                daily_data['reflector'][day],
                daily_data['plugboard'][day])
        append('daily_sheet', data)
    for rotor in rotor_data:
        append('rotors', (rotor,))
