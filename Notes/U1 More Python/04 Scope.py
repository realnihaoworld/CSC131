# Scope - the region of code that a variable is accessible in

# Global variables - are accessible everywhere
# Local - only accessible within a region of the code

a = 10 # globally defined, not inside anything

def my_func(x):
    a = 11 # defined locally
    print(f"Inside function: {a}")
    
print(a)

my_func(6)


b = 20

def func_2():
    global b
    b += 3
    print(f"inside: {b}")

