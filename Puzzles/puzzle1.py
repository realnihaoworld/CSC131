# Name: Danison
# Date: 12/4/23

num_list = []
total = 0

one_million = 1000001

for x in range(1, one_million):
    y = str(x)
    total += y.count('0')

print(total)
print("I'm Danison")


