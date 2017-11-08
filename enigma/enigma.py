#!/usr/bin/env python3

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

        for rotor in rotor_nums:
            self.rotors[rotor].set(rotor_start[rotor_nums.index(rotor)])

        for char in message:
            if char.isalpha() or char == ' ':
                char = self.sub_simple(char, plugboard)
                char = self.sub_rotor(char, rotor_nums, 'forwards')
                char = self.sub_simple(char, reflector)
                char = self.sub_rotor(char, rotor_nums, 'backwards')
                char = self.sub_simple(char, plugboard)
            r_message += char

            self.rotors[rotor_nums[0]].rotate()
            if self.rotors[rotor_nums[0]].position % 27 == 0:
                self.rotors[rotor_nums[1]].rotate()
                if self.rotors[rotor_nums[1]].position % 27 == 0:
                    self.rotors[rotor_nums[2]].rotate()

        return r_message

    def sub_rotor(self, char, rotor_nums, direction):
        inner = self.rotors[rotor_nums[0]].sequence
        middle = self.rotors[rotor_nums[1]].sequence
        outer = self.rotors[rotor_nums[2]].sequence
        
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

    def rotate(self, shifts=1):
        self.sequence = self.sequence[1:] + self.sequence[:1]
        self.position += 1

    def set(self, position):
        self.sequence = self.original_sequence[position:] + self.original_sequence[0:position]
        self.position = 1


### ALL BELOW IS TRASH ###

plugboard = 'ab cd ef gh ij kl mn op qr st'.upper()
reflector = 'ac bd ef gh iz ml kn oq pr st ux wv'.upper()
rotor_nums = [4,0,1]
rotor_start = [2,21,17]

e = EnigmaMachine()

with open('input.txt', 'r') as f:
    inputt = f.read().upper()
    #print(inputt)

outputt = e.translate(inputt, day=1)

with open('output.txt', 'w') as f:
    f.write(outputt)

outputt2 = e.translate(outputt, day=1)
with open('output2.txt', 'w') as f:
    f.write(outputt2)

print(inputt)
print(outputt)
print(outputt2)
'''
print(e.translate('TUESDAY TUESDAY TUESDAY TUESDAY TUESDAY TUESDAY TUESDAY', day=1))
print(e.translate('CMDI  RHCMNJ CRDKDLIDLZAYCSJQWIRITFKBUEA EEJJDKXVFWODZC', day=1))
'''
