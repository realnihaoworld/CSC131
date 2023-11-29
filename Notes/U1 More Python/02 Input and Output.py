# Input
val = input("Give me a value: ")
a_number = int(input("Give me an integer: ")) # casting

# Output
print("Hello World")
print("Hello", end="") # no new line added

a_list = [0, 1, 2, 3, 4, 5]
print(a_list)

for item in a_list:
    print(item, end=",")

print(*a_list)  
print(a_list[0])
