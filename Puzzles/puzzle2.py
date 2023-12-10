
list = []
reverse_list = []
for x in range(11, 100):
    num = str(x)
    list.append(num)
    reverse_list.append(num [::-1])

for x in range(0, 89):
    ab = int(list[x])
    ba = int(reverse_list[x])
    
    cdc = ab + ba
    
    if cdc > 100:
        print(f"{ab} + {ba} = {cdc}")