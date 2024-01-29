from random import randint, seed, Random

# Definition: A pseudo-random process is one that appears to be random
# but is technically deterministic in nature (the pattern is predictable)

# Def: A seed is a value used to initialize a pseudo-random process

print(randint(0, 100))
print(randint(0, 100))
print()

seed(123456)
print(randint(0, 100))
print(randint(0, 100))
print()

# An aside on random library, you can have multiple seeds
# You can have multiple seeds by instantiating a Random() object
r1 = Random()
r1.seed(1234)
r1.randint(0, 100)

r2 = Random()
r2.seed(123)
r2.randint(0, 100)