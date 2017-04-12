# Sieve of Eratosthenes
# Author: Lei Mao
# Date: 2017/4/12
# Content: The sieve of Eratosthenes is used to find all prime integers not exceeding a specified positive interger. 
# Theorem: If n is a composite integer, then n has a prime divisor less than or equal to sqrt(n)
# Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Usage: python sieve_of_eratosthenes.py n, where n is a positive integer.

import sys
import os
import numpy as np

n = int(sys.argv[1])
# Prime integer index
# 0: composite, 1: prime
prime = np.full(n+1, 1, dtype = int)
# 2 is the first prime integer
prime[0] = 0
prime[1] = 0
prime[2] = 1

# Remove composite in the integer list
for i in xrange(2,n+1):
    for j in xrange(int(np.sqrt(i))+1):
        if (prime[j] == 1) and (i%j == 0):
            # i is a composite
            prime[i] = 0
            break

# Save the prime integers found
result_directory = 'data/'
if not os.path.exists(result_directory):
    os.makedirs(result_directory)
data_file = '2-' + str(n) + '.txt'
fhand = open(result_directory + data_file, "w")

print('The prime integers between 2 and %d are:' %n)
for i in xrange(n+1):
    if prime[i] == 1:
        print(i)
        fhand.write(str(i))
        fhand.write('\n')
fhand.close()
