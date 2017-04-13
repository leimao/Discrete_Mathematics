# Euclidean Algorithm
# Author: Lei Mao
# Date: 2017/4/13
# Content: The Euclidean Algorithm is used to find the greatest common divisor of two integers. 
# Lemma: Let a = bq + r, where a, b, q, and r are integers. Then gcd(a, b) = gcd(b, r)
# Theorem: Let a and b be positive integers. Then ab = gcd(a, b) * lcm(a, b)
# Reference: https://en.wikipedia.org/wiki/Euclidean_algorithm
# Usage: python euclidean_algorithm.py a b, where a and b are positive integers.

import sys
import os
import numpy as np

a = int(sys.argv[1])
b = int(sys.argv[2])

def gcd(a, b):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def lcm(a, b):
    return a * b / gcd(a, b)

print('The greatest common divisor of %d and %d is %d.' % (a, b, gcd(a, b)))
print('The least common multiple of %d and %d is %d.' % (a, b, lcm(a, b)))