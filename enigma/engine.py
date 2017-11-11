import database

class EnigmaMachine():
    """

    """
    def __init__(self):
        self.rotors = [Rotor('AUNGHOVBIPWCJQXDKRY ELSZFMT'),
                       Rotor('O JETYCHMRWAFKPUZDINSXBGLQV'),
                       Rotor('FBDHJLNPRTVXZACEGI KMOQSUWY'),
                       Rotor('HKPDEAC WTVQMYNLXSURZOJFBGI'),
                       Rotor('YDNGLCIQVEZRPTAOXWBMJSUHK F')]

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

    def read_chart(self, day):
        self.rotor_nums = database.read_column(day, 'rotor_nums')
        self.rotor_start = database.read_column(day, 'rotor_start')
        self.reflector = database.read_column(day, 'reflector')
        self.plugboard = database.read_column(day, 'plugboard')


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
