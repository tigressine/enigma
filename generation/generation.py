#! /usr/bin/env python3
import random
import database

def gen_chars():
    chars = []
    for char in range(32, 127):
        if char in [34, 36, 42, 92, 96]:
            continue
        else:
            chars.append(chr(char))
    return chars

def gen_rotors():
    chars = gen_chars()
    new_rotor = ''
    for each in range(len(chars)):
        char = random.choice(chars)
        new_rotor += char
        chars.remove(char)
    return new_rotor

def gen_reflector(total):
    chars = gen_chars()
    reflector = []
    while len(chars) > total:
        charz = random.sample(chars, 2)
        chars.remove(charz[0])
        chars.remove(charz[1])
        reflector.append(charz[0] + charz[1])
    return reflector

def gen_chart():
    for day in range(1, 2):
        rotors = random.sample(range(1, 6), 3)
        positions = random.sample(range(1, 92), 3)
        reflector = gen_reflector(0)
        plugboard = gen_reflector(20)
        print(day, rotors, positions, reflector, plugboard)
        print(len(reflector))
        print(len(plugboard))


rotor1 = gen_rotors()
#print(rotor1)
gen_chart()
# send generated shit to database .py
