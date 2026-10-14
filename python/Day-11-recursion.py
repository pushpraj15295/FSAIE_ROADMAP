# recursion is a function that calls itself

# example 1: factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 5 * factorial(4)
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * factorial(1)
# 1


# example 2: fibonacci ------------------------------------------------------------
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

# fibonacci(4) + fibonacci(3)
# fibonacci(3) + fibonacci(2)
# fibonacci(2) + fibonacci(1)
# fibonacci(1) + fibonacci(0)  
# 1 + 0
# 1
# 1 + 1
# 2
# 2 + 1
# 3
# 3 + 2
# 5
# 5 + 3
# 8


# example 3: palindrome ------------------------------------------------------------
def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

print(palindrome("racecar"))    # True

# racecar   
# r == r
# a == a   

# optimal solution in the recursion -----------------------------------------------

import time

def Memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m] = m * Memo(m-1,d)
        return d[m]

start_time = time.time()
print(Memo(5, {}))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")


print(Memo(10, {}))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

# for all big numbers, the time taken is much less than the normal recursion
# because the memoization is storing the results of the function calls
# so that the same results are not calculated again

