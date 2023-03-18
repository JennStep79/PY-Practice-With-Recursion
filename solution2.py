# Activity 2-3

def name_args(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])

# name_args(name="Jeff", age="23")

def all_true(itr):
    return all(itr)

# print(all_true([1, 2, True]))

def one_true(itr):
    return any(itr)

# print(one_true([0, 2, True]))

def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
    
# print(recursive_factorial(4))

def recursive_reverse(string, i =0):
    if i == len(string) -1:
        return string[0]
    else:
        return string[-1-i] + recursive_reverse(string, i +1)
    
print(recursive_reverse("test"))