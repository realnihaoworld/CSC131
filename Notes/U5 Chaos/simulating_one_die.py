# A simulation of rolling a 6 sided die

from random import randint

values = [1, 2, 3, 4, 5, 6]
counts = [0] * 6    # list containing number of times each value is rolled
frequencies = [0] * 6 # the frequence for rolling each value

NUM_ROLLS = 10000000
for i in range(NUM_ROLLS):
    value = randint(1, 6)
    counts[value - 1] += 1

for i in range(len(frequencies)):
    frequencies[i] = counts[i] / NUM_ROLLS

print(counts)
print(frequencies)