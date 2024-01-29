# program that shows the number of times each sum occurs when rolling
# two dice

possible_sums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

counts = [0] * 11

for die1 in range(1, 7):
    for die2 in range(1, 7):
        dice_sum = die1 + die2
        counts[dice_sum - 2] += 1
        
for i in range(len(possible_sums)):
    sum_ = possible_sums[i]
    count = counts[i]
    probability = count / sum(counts)
    print(sum_, count, f"{probability:.3f}", sep="\t")
    