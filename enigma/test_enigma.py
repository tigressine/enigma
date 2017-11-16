#! /usr/bin/env python3
import unittest
import engine
import database
import random

F_TEST_INPUT = 'test_input.txt'
E = engine.EnigmaMachine()
with open(F_TEST_INPUT, 'r') as f:
    remove_newline = lambda x: list(filter(lambda y: y != '', x.split('\n')))
    SAMPLE = remove_newline(f.read().upper())#temp

def double_translate(message, day=1):
    return E.translate(E.translate(message, day), day)

class TestEnigma(unittest.TestCase):
    
    def test_000_bulk_translation(self):
        for string in SAMPLE:
            self.assertEqual(double_translate(string), string)

    def test_001_custom_days(self):
        for i in range(1, 32):
            sample = random.choice(SAMPLE)
            self.assertEqual(double_translate(sample, i), sample)

    def test_002_custom_days_wrong(self):
        for i in range(1, 32):
            sample = random.choice(SAMPLE)
            self.assertNotEqual(double_translate(sample[::-1], i), sample)
    '''
    def test_002_rotor_set(self):
        self.e.rotors[0].set(20)
        self.assertEqual(self.e.rotors[0].sequence[0], self.e.rotors[0].original_sequence[20])
        self.sample = 'T'
        for i in range(1,32):
            self.e.translate(self.sample, day=i)
            for rotor in self.e.rotor_nums:
                first = self.e.rotors[rotor].sequence[0]
                o_first = self.e.rotors[rotor].original_sequence[
                                                self.e.rotor_start[self.e.rotor_nums.index(rotor)]]
                print(first, o_first)
                self.assertEqual(first, o_first)
    def test_002_rotor_rotation(self):
        print(len(self.sample)/27/27)
        self.e.translate(self.sample)
        for rotor in self.e.rotor_nums:
            print(self.e.rotors[rotor].original_sequence)
            print(self.e.rotors[rotor].sequence)
            self.e.rotors[rotor].set(self.e.rotor_start[0])
            print(self.e.rotors[rotor].sequence)
            break
    '''


if __name__ == '__main__':
    unittest.main()
