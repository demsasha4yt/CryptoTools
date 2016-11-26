"""
    Cryptomath module
    13.11.2016 // By ALEX777RUSSIAN
"""

from math import gcd as math_gcd


def gcd(a, b):
    # gcd from math;

    return math_gcd(a, b)


def find_mod_inverse(a, m):
    # return x (the modular inverse of a mod m:
    # x * a % m = 1)

    if gcd(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q*v1), (u2 - q*v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
