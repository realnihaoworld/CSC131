

def num_pairs(num_people):
    # base case
    if num_people == 1:
        return 0
    # recursive step
    else:
        return (num_people - 1) + num_pairs(num_people - 1)
        
def factorial(x):
    # base case
    if x == 0:
        return 1
    # recursive step
    else:
        return x * factorial(x - 1)
        
def pow(x, n):
    # base case
    if n == 0:
        return 1
    # recursive step
    else:
        return x * pow(x, n-1)

def fibonacci(n):
    # base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1
    # recursive steps
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    