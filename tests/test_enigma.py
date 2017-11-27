#! /usr/bin/env python3
import enigma
import random
import unittest

class TestEnigma(unittest.TestCase):

    def test_000_translate_bulk(self):
        sample = generate_sample(100000)
        self.assertEqual(double_translate(sample), sample)

    def test_001_translate_by_day_true(self):
        for day in range(0, 31):
            sample = generate_sample(1000)
            self.assertEqual(double_translate(sample, day), sample)

    def test_002_translate_by_day_false(self):
        for day in range(0, 31):
            sample = generate_sample(1000)
            self.assertNotEqual(double_translate(sample[::-1], day), sample)

    def test_003_rotate_rotors(self):
        rotations = random.randint(8281, 100000)
        sample = generate_sample(rotations)
        E.translate(sample)
        self.assertEqual(E.daily_rotors[0].position, rotations)
        self.assertEqual(E.daily_rotors[1].position, rotations//91)
        self.assertEqual(E.daily_rotors[2].position, rotations//91//91)

    def test_004_handle_special_char(self):
        sample = generate_sample(10) + '$' + generate_sample(10)
        with self.assertRaises(SystemExit):
            E.translate(sample)

def double_translate(message, day=0):
    return E.translate(E.translate(message, day), day)

def generate_sample(length):
    sample = ''
    bad_ASCII = [34, 36, 92, 96]
    chars = [chr(char) for char in range(32, 127) if char not in bad_ASCII]

    for letter in range(length):
        sample += random.choice(chars)
    return sample

E = enigma.Machine()
unittest.main(buffer=True)
