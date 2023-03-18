# Write code for algorithm 1 below
def count_down(n):
    if n == 0:
        return
    else:
        print(n)
        count_down(n-1)

# count_down(5)

def natural_numbers(n, i=1):
    if i > n:
        return
    else:
        print(i)
        natural_numbers(n, i+1)

# natural_numbers(3)

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(6))

def exponent(a, b):
    if b == 1:
        return a
    else:
        return a * exponent(a, b-1)
    
# print(exponent(3,2))

def palindrome(string):
    if len(string) == 1 or len(str) == 0:
        return True
    else:
        return (string[0] == string[-1]) and palindrome(string[1:-1])
    
# print(palindrome("racecar"))