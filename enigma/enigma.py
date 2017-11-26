import sqlite3 as sql

#F_ENIGMA_DATA = '/usr/share/enigma/enigma.db'
F_ENIGMA_DATA = 'enigma.db'

def db_operation(operation):
    def db_wrap(*args, **kwargs):
        db = sql.connect(F_ENIGMA_DATA)
        curse = db.cursor()

        result = operation(*args, curse, **kwargs)

        db.close()
        return result

    return db_wrap

@db_operation
def get_rotors(curse):
    curse.execute('SELECT * FROM rotors')
    return curse.fetchall()

class Machine():
    """
    """
    def __init__(self):
        self.rotors = get_rotors()

    def translate(self, message, day=1):
        r_message = ''

        self.read_chart(day)

        for rotor in self.rotor_nums:
            self.rotors[rotor].set(self.rotor_start[self.rotor_nums.index(rotor)])#PEP8

        for char in message:
            if char.isalpha() or char == ' ':
                char = self.sub_simple(char, self.plugboard)
                char = self.sub_rotor(char, self.rotor_nums, 'forwards')
                char = self.sub_simple(char, self.reflector)
                char = self.sub_rotor(char, self.rotor_nums, 'backwards')
                char = self.sub_simple(char, self.plugboard)
            r_message += char

            self.rotors[self.rotor_nums[0]].rotate()
            if self.rotors[self.rotor_nums[0]].position % 27 == 0:
                self.rotors[self.rotor_nums[1]].rotate()
                if self.rotors[self.rotor_nums[1]].position % 27 == 0:
                    self.rotors[self.rotor_nums[2]].rotate()

        return r_message
    
    @db_operation
    def read_chart(self, day, curse):
        curse.execute('SELECT * FROM daily_sheet WHERE day=?', (day,))
        row = curse.fetchone()
        self.rotor_nums = (row[1]-1, row[2]-1, row[3]-1)
        self.rotor_start = (row[4]-1, row[5]-1, row[6]-1)
        self.reflector = row[7]
        self.plugboard = row[8]

    def sub_rotor(self, char, rotor_nums, direction):
        inner = self.rotors[self.rotor_nums[0]].sequence
        middle = self.rotors[self.rotor_nums[1]].sequence
        outer = self.rotors[self.rotor_nums[2]].sequence
        
        if direction == 'forwards':
            char = outer[inner.index(char)]
            char = outer[middle.index(char)]
        elif direction == 'backwards':
            char = middle[outer.index(char)]
            char = inner[outer.index(char)]
        
        return char

    def sub_simple(self, char, board):
        for sub in board.split():
            if char in sub:
                if sub.index(char) == 0:
                    char = sub[1]
                else:
                    char = sub[0]
                break
        
        return char

class Rotor():
    """
    """
    def __init__(self, sequence):
        self.sequence = sequence
        self.original_sequence = self.sequence
        self.position = 1

    def rotate(self):
        self.sequence = self.sequence[1:] + self.sequence[:1]
        self.position += 1

    def set(self, position):
        self.sequence = self.original_sequence[position:] + self.original_sequence[0:position]
        self.position = 1
