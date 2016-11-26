"""
    Affine cipher DECRYPT/ENCRYPT
    (Caesar Cipher, a = 1)
    (ROT13 Cipher, ROT = 13, a = 1)
    13.11.2016 // By ALEX777RUSSIAN
    --
    Афинный шифр расшифровка/шивфровка
    Частные случаи: Шифр цезаря, ROT13
"""

import cryptomath


class Affine:
    def __init__(self, text='', rot=13, a=1, alphabet=''):
        self.text = text
        self.alphabet = alphabet

        self.rot = rot
        self.a = a

    def set_text(self, text):
        self.text = text

    def set_rot(self, rot):
        self.rot = rot

    def set_a(self, a):
        self.a = a

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def get_alphabet_len(self):
        return len(self.alphabet)

    def encode(self):                                                   # for each char call encode_char(char)
        e_text = ''
        for line in self.text:
            for l in line:
                e_text += self.encode_char(l)

        return e_text

    def encode_char(self, l):
        is_upper = False
        if l.isupper():
            l = l.lower()
            is_upper = True

        if l in self.alphabet:
            l = self.alphabet[(self.a * self.alphabet.find(l) + self.rot) % self.get_alphabet_len()]
        if is_upper:
            l = l.upper()
        return l

    def decode(self):                                                   # for each char call decode_char(char)
        d_text = ''
        a_mod_inverse = cryptomath.find_mod_inverse(self.a, self.get_alphabet_len())
        for line in self.text:
            for l in line:
                d_text += self.decode_char(l, a_mod_inverse)

        return d_text

    def decode_char(self, l, a):
        is_upper = False
        if l.isupper():
            l = l.lower()
            is_upper = True

        if l in self.alphabet:
            l = self.alphabet[(self.alphabet.find(l) - self.rot)*a % len(self.alphabet)]

        if is_upper:
            l = l.upper()

        return l

    def encode_all_caesar_rots(self):                                   # for each rot call encode()
        encodes = []
        for i in range(0, self.get_alphabet_len()):
            self.set_rot(i)
            encodes.append(self.encode())
        return encodes

    def encode_all_affine_as(self):                                     # for each a call encode_all_caesar_rots()
        encodes = []
        for i in range(1, self.get_alphabet_len()):
            if cryptomath.gcd(i, self.get_alphabet_len()) == 1:
                self.set_a(i)
                encodes.append(self.encode_all_caesar_rots())
        return encodes

    def decode_all_caesar_rots(self):                                   # for each rot call decode()
        decodes = []
        for i in range(0, self.get_alphabet_len()):
            self.set_rot(i)
            decodes.append(self.decode())
        return decodes

    def decode_all_affine_as(self):                                     # for each a call decode_all_caesar_rots()
        decodes = []
        for i in range(1, self.get_alphabet_len()):
            if cryptomath.gcd(i, self.get_alphabet_len()) == 1:
                self.set_a(i)
                decodes.append(self.decode_all_caesar_rots())
        return decodes












