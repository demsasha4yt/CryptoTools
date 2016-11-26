from Substitution import Substitution
from Affine import Affine
from alphabets import *


cipher = Substitution()
cipher.set_alphabet(LOWER_ENG)
cipher.set_key('lfwoayuisvkmnxpbdcrjtqeghz')
cipher.set_text("If a man is offered a fact which goes against his instincts")
print(cipher.encode())


string = input("Введите строку: ")

cipher = Affine()

cipher.set_text(string)
cipher.set_alphabet(LOWER_ENG)
cipher.set_rot(25)
cipher.set_a(3)
print(cipher.encode())





