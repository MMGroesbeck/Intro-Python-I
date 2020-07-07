import math
import sys

# is_prime: takes integer as argument, returns true if prime, false otherwise
def is_prime(i):
    fact = 2
    while fact <= math.sqrt(i):
        # If no factors are found at or below sqrt(i), i is prime
        if i % fact == 0:
            return False
        else:
            fact += 1
    return True

if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        if is_prime(int(sys.argv[1])):
            print(f"{sys.argv[1]} is prime.")
        else:
            print(f"{sys.argv[1]} is not prime.")
    else:
        print("Integer entry on command line only.")

# print(is_prime(11))#True
# print(is_prime(45))#False
# print(is_prime(49))#False

# This could be made more efficient by only checking primes as potential factors.
# However, finding a list of primes to use is non-trivial.

# Sieve of Eratosthenes: three implementations
# First two functions start by initializing a list of integers from 2 to the max (passed as an argument)
# Third version uses an array of booleans, then returns an array of primes

# sieve1 is slightly shorter, but moves primes from the initial array to a second array
# (second array, of primes, is returned)
def sieve1(top):
    allnums = [i + 2 for i in range(top-1)]
    primes = []
    while len(allnums) > 0:
        fact = allnums[0]
        current = fact
        primes.append(fact)
        while current <= top:
            if current in allnums:
                allnums.remove(current)
            current += fact
    return primes

# sieve2 removes non-primes from initial array and leaves primes
def sieve2(top):
    allnums = [i + 2 for i in range(top-1)]
    fact = 2
    while fact <= top:
        current = fact * 2
        while current <= top:
            if current in allnums:
                allnums.remove(current)
            current += fact
        if allnums.index(fact) < len(allnums) - 1:
            fact = allnums[allnums.index(fact) + 1]
        else:
            fact = top + 1
    return allnums

#sieve3 is closer to the "CS version" of the algorithm
def sieve3(top):
    checklist = [False, False]
    checklist2 = [True for i in range(top-1)]
    # checklist[n] represents potential prime status of n
    # for a non-prime number x or less, at least one factor will be <= sqrt(x):
    ceiling = int(math.sqrt(top))
    checklist.extend(checklist2)
    for n in range(ceiling + 1):
        if checklist[n]:
            current = 2*n
            while current <= top:
                checklist[current] = False
                current += n
    return [x for x in range(top+1) if checklist[x]]

#demonstration:
maxallowed = 100
print(sieve1(maxallowed))
print(sieve2(maxallowed))
print(sieve3(maxallowed))