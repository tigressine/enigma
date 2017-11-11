#! /usr/bin/env python3
import unittest
import engine
import database

F_TEST_INPUT = 'test_input.txt'

class TestEnigma(unittest.TestCase):
    
    def setUp(self):
        self.e = engine.EnigmaMachine()
        with open(F_TEST_INPUT, 'r') as f:
            self.sample = f.read().upper()#temp

    def test_000_bulk_translation(self):
        self.encoded_text = self.e.translate(self.sample)
        self.decoded_text = self.e.translate(self.encoded_text)
        self.assertEqual(self.decoded_text, self.sample)

    def test_001_custom_days(self):
        self.sample = self.sample.split('\n')[0].upper()#temp
        for i in range(1,32):
            self.encoded_text = self.e.translate(self.sample, day=i)
            self.decoded_text = self.e.translate(self.encoded_text, day=i)
            self.assertEqual(self.decoded_text, self.sample)

    def test_002_rotor_set(self):
        '''
        self.e.rotors[0].set(20)
        self.assertEqual(self.e.rotors[0].sequence[0], self.e.rotors[0].original_sequence[20])
        '''
        self.sample = 'T'
        for i in range(1,32):
            self.e.translate(self.sample, day=i)
            for rotor in self.e.rotor_nums:
                first = self.e.rotors[rotor].sequence[0]
                o_first = self.e.rotors[rotor].original_sequence[
                                                self.e.rotor_start[self.e.rotor_nums.index(rotor)]]
                print(first, o_first)
                self.assertEqual(first, o_first)
    '''
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
