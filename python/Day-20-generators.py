#  a generator is a function that returns an iterator that produces a sequence of values when iterated over.
#  in simple words, a generator is a function that returns an iterator.
# generator is function that don't have return statement, but have yield statement.
# yield statement is used to produce a value and pause the function execution.

# example ------------------------------------------------------------
def my_generator():
    yield 1
    yield 2
    yield 3

for i in my_generator():
    print(i)

# or we can use next() function to get the next value from the generator.
print(next(my_generator())) # 1
print(next(my_generator())) # 2
print(next(my_generator())) # 3

# what is the difference between a generator and a function?   
# a generator is a function that returns an iterator that produces a sequence of values when iterated over.
# a function is a function that returns a value.

# what is the differnece between yield and return statement?
# yield statement is used to produce a value and pause the function execution.
# return statement is used to return a value and exit the function.

# example 2 ------------------------------------------------------------

def square_numbers(numbers):
    for i in numbers:
        yield i * i

numbers = [1,2,3,4,5]

print(next(square_numbers(numbers))) # 1
print(next(square_numbers(numbers))) # 4
# we can use for loop to iterate over the generator.
# after the generator is exhausted, it will raise StopIteration exception.
for i in square_numbers(numbers):
    print(i)




# how to create a iterator from a generator ? ------------------------------------------------------------

def my_generator(start, end):
    for i in range(start, end):
        yield i

my_iterator = iter(my_generator(1, 10))

# or we can use for loop to iterate over the iterator.
for i in my_iterator:
    print(i)


# using generator expression ------------------------------------------------------------
my_generator = (x * x for x in range(1, 10))
for i in my_generator:
    print(i)


# imporatant of generators ------------------------------------------------------------
# 1. Generators are memory efficient.
# 2. Generators are faster than lists.
# 3. Generators are lazy.
# 4. Generators are iterable.
# 5. Generators are immutable.
# 6. Generators are thread safe.
# 7. Generators are reentrant.

