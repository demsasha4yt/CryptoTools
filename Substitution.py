"""
    Simple Substitution cipher DECRYPT/ENCRYPT
    13.11.2016 // By ALEX777RUSSIAN
    --
    Шифр простой замены Шифровка /Дешифровка
"""


class Substitution:
    def __init__(self, text='', key='', alphabet=''):
        self.text = text
        self.alphabet = alphabet
        self.key = key

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def get_text_len(self):
        return len(self.text)

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def get_alphabet(self):
        return self.alphabet

    def get_alphabet_len(self):
        return len(self.alphabet)

    def check_valid_key(self):
        key_list = list(self.key.lower())
        alphabet_list = list(self.alphabet.lower())

        key_list.sort()
        alphabet_list.sort()

        return key_list == alphabet_list

    def encode(self):
        if not self.check_valid_key():
            return None
        else:
            return self.translate(0)

    def decode(self):
        if not self.check_valid_key():
            return None
        else:
            return self.translate(1)

    def translate(self, mode):
        #   Translate function. Функция замены
        #   mode = 0 - encode. Шифровка
        #   mode - 1 - decode. Расшифровка

        translated = ''
        alphabet = self.alphabet                            # copy of alphabet and key( mb refactor )
        key = self.key

        if mode == 1:                                       # mode = decode
            alphabet, key = key, alphabet

        for line in self.text:
            for l in line:
                is_upper = False
                if l.isupper():
                    l = l.lower()
                    is_upper = True

                if l in alphabet:
                    l = key[alphabet.find(l)]

                if is_upper:
                    l = l.upper()

                translated += l
        return translated

