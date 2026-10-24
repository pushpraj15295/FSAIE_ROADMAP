# what is iterator?
#  an iterator is an object that contains a countable number of values.
#  an iterator is an object that allows you to iterate over a collection of data without having to store all the values in memory at once.

# what is iterable object?
#  an iterable object is an object that can be iterated over.

# what is iteration ?
#  iteration is the process of traversing a collection of data one element at a time.



#  getsizeof() is a function that returns the size of an object in bytes.

# example 
import sys

l = [ x for x in range(1,1000000)]
print(sys.getsizeof(l)) # 8000000 bytes

# but if we use a generator, we can save memory. [ iterator object ]

x = (x for x in range(1,1000000))
print(sys.getsizeof(x)) # 48 bytes


# how for loop works ?

# step 1 : [1,2,3] is an iterable object.
# step 2 : [1,2,3] is converted to an iterator object.
# step 3 : the iterator object is passed to the for loop.
# step 4 : the for loop calls the __next__() method on the iterator object.
# step 5 : the __next__() method returns the next element in the iterator object. [ 1 ]
# step 6 : the __next__() method returns the next element in the iterator object. [ 2 ]
# step 7 : the __next__() method returns the next element in the iterator object. [ 3 ]
# step 8 : the __next__() method returns the next element in the iterator object. [ StopIteration ]


# how to create a custom iterator ?

def my_iterator(iterable):
    iterator = iter(iterable)
    while True:
        try:
           print(next(iterator))
        except StopIteration:
            break

my_iterator([1,2,3,4,5])





