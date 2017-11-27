import sqlite3 as sql

F_ENIGMA_DATA = '/usr/local/share/enigma/enigma.db'

def db_operation(operation):
    def db_wrap(*args, **kwargs):
        db = sql.connect(F_ENIGMA_DATA)
        curse = db.cursor()

        result = operation(*args, curse, **kwargs)

        db.close()
        return result

    return db_wrap

class Machine():
    """
    """
    def __init__(self):
        self.get_all_rotors()

    def translate(self, message, day=0):
        r_message = ''

        self.read_chart(day)
        self.daily_rotors = [self.all_rotors[self.rotor_nums[0]],
                             self.all_rotors[self.rotor_nums[1]],
                             self.all_rotors[self.rotor_nums[2]]]

        for rotor, start in enumerate(self.rotor_start):
            self.daily_rotors[rotor].set(start)#Check this

        for char in message:
            try:
                char = self.sub_simple(char, self.plugboard)
                char = self.sub_rotor(char, self.rotor_nums, 'forwards')
                char = self.sub_simple(char, self.reflector)
                char = self.sub_rotor(char, self.rotor_nums, 'backwards')
                char = self.sub_simple(char, self.plugboard)
                r_message += char
            except ValueError:
                if char == '\n':
                    r_message += char
                else:
                    print("Message contains invalid character: ` \ \" or $")
                    quit()

            self.daily_rotors[0].rotate()
            if self.daily_rotors[0].position % 91 == 0:#check num
                self.daily_rotors[1].rotate()
                if self.daily_rotors[1].position % 91 == 0:
                    self.daily_rotors[2].rotate()

        return r_message

    @db_operation
    def get_all_rotors(self, curse):
        curse.execute('SELECT * FROM rotors')
        self.all_rotors = [Rotor(rotor[0]) for rotor in curse.fetchall()]
    
    @db_operation
    def read_chart(self, day, curse):
        curse.execute('SELECT * FROM daily_sheet WHERE day=?', (day,))
        row = curse.fetchone()
        self.rotor_nums = (row[1], row[2], row[3])
        self.rotor_start = (row[4], row[5], row[6])
        self.reflector = row[7]
        self.plugboard = row[8]

    def sub_rotor(self, char, rotor_nums, direction):
        inner = self.daily_rotors[0].sequence
        middle = self.daily_rotors[1].sequence
        outer = self.daily_rotors[2].sequence
        
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
        self.position = 0

    def rotate(self):
        self.sequence = self.sequence[1:] + self.sequence[:1]
        self.position += 1

    def set(self, position):
        self.sequence = self.original_sequence[position:] + self.original_sequence[0:position]#PEP8
        self.position = 0
