# sorting in python ------------------------------------------------------------
# 1. sort() method
# 2. sorted() function
# 3. bubble sort
# 4. selection sort
# 5. insertion sort
# 6. merge sort
# 7. quick sort
# 8. heap sort
# 9. radix sort
# 10. bucket sort
# 11. counting sort
# 12. shell sort
# 13. tree sort
# 14. pigeonhole sort
# 15. cycle sort
# 16. cocktail shaker sort
# 17. comb sort
# 18. gnome sort
# 19. stooge sort
# 20. bitonic sort
# 21. pigeonhole sort

# 1. sort() method ------------------------------------------------------------
# sort method use to sort the same list [O(n^2)]

l = [3, 2, 1, 4, 5]
l.sort()
print("sort() method",l)

# 2. sorted() function ------------------------------------------------------------
# sorted function use to sort the list and return a new list [O(n log n)]

l = [3, 2, 1, 4, 5]
l1 = sorted(l)
print("sorted() function",l1)

# 3. bubble sort [O(n^2)]------------------------------------------------------------
# bubble sort is a simple sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

print("bubble sort",bubble_sort([3, 2, 1, 4, 5]))

# 4. selection sort [O(n^2)]------------------------------------------------------------
# selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part and putting it at the beginning.


def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1,len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index],l[i]
    return l

print("selection sort",selection_sort(l))


# 5. insertion sort [O(n^2)]------------------------------------------------------------
# insertion sort is a simple sorting algorithm that works by repeatedly inserting the unsorted element at the correct position in the sorted part.

def insertion_sort(l):
    for i in range(len(l)):
        key = l[i]
        j = i - 1

        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

print("insertion sort",insertion_sort([3,4,5,1,2]))


# 6. merge sort [O(n log n)]------------------------------------------------------------
# merge sort is a divide and conquer algorithm that works by dividing the list into two halves, sorting each half, and then merging the two sorted halves.

def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right): # merge the two sorted halves
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else: # if the current element in the right half is smaller than the current element in the left half, then add the current element in the right half to the merged list
                l[k] = right[j]
                j += 1
            k += 1
        while i < len(left): # add the remaining elements in the left half to the merged list
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j] # add the remaining elements in the right half to the merged list
            j += 1
            k += 1
        return l

print("merge sort",merge_sort([3, 2, 1, 4, 5]))


# 7. quick sort [O(n log n)]------------------------------------------------------------
# quick sort is a divide and conquer algorithm that works by selecting a pivot element 
# and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.

def quick_sort(l): # recursive function
    if len(l) <= 1:
        return l
    pivot = l[len(l) // 2]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]
    return quick_sort(left) + middle + quick_sort(right) 

print("quick sort",quick_sort([3, 2, 1, 4, 5]))

# 8. heap sort [O(n log n)]------------------------------------------------------------ 
# heap sort is a comparison based sorting technique based on Binary Heap data structure.

def heapify(l, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if the left child is larger
    if left < n and l[left] > l[largest]:
        largest = left

    # Check if the right child is larger
    if right < n and l[right] > l[largest]:
        largest = right

    # If a child is larger, swap and continue
    if largest != i:
        l[i], l[largest] = l[largest], l[i]
        heapify(l, n, largest)


def build_heap(l): # build a max heap
    n = len(l)

    # Start at the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(l, n, i)


def heap_sort(l):
    build_heap(l)

    for i in range(len(l) - 1, 0, -1):
        # Move maximum element to the end
        l[0], l[i] = l[i], l[0]

        # Restore heap property in remaining elements
        heapify(l, i, 0)

    return l


print("Heap sort:", heap_sort([3, 2, 1, 4, 5]))


# 9. radix sort [O(n log n)]------------------------------------------------------------
# radix sort is a non-comparative integer sorting algorithm 
# that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.

def radix_sort(l):
    max_num = max(l)
    exp = 1
    while max_num // exp > 0:
        counting_sort(l, exp)
        exp *= 10
    return l

print("radix sort",radix_sort([3, 2, 1, 4, 5]))

# 10. bucket sort [O(n log n)]------------------------------------------------------------
# bucket sort is a sorting technique that sorts the elements by first dividing the elements into several groups called buckets.

def bucket_sort(l):
    max_num = max(l)
    bucket = [[] for _ in range(max_num + 1)]
    for i in l:
        bucket[i].append(i)
    return [item for sublist in bucket for item in sublist]

print("bucket sort",bucket_sort([3, 2, 1, 4, 5]))


# 11. counting sort [O(n log n)]------------------------------------------------------------
# counting sort is a sorting technique that sorts the elements by counting the number of occurrences of each unique element in the list.

def counting_sort(l):
    max_num = max(l)
    count = [0] * (max_num + 1)
    for i in l:
        count[i] += 1
    return [item for item in count for _ in range(item)]

print("counting sort",counting_sort([3, 2, 1, 4, 5]))


# 12. shell sort [O(n log n)]------------------------------------------------------------
# shell sort is a sorting technique that sorts the elements by comparing the elements that are far apart and then gradually reducing the gap between the elements.

def shell_sort(l):
    gap = len(l) // 2
    while gap > 0:
        for i in range(gap, len(l)):
            temp = l[i] 
            j = i
            while j >= gap and l[j - gap] > temp:
                l[j] = l[j - gap]
                j -= gap
            l[j] = temp
        gap //= 2
    return l

print("shell sort",shell_sort([3, 2, 1, 4, 5]))

# 13. tree sort [O(n log n)]------------------------------------------------------------
# tree sort is a sorting technique that sorts the elements by building a binary search tree and then traversing the tree in order.

def tree_sort(l):
    tree = build_tree(l)
    return traverse_tree(tree)

print("tree sort",tree_sort([3, 2, 1, 4, 5]))


# 14. pigeonhole sort [O(n log n)]------------------------------------------------------------  
# pigeonhole sort is a sorting technique that sorts the elements by first dividing the elements into several groups called pigeonholes.

def pigeonhole_sort(l):
    min_num = min(l)
    max_num = max(l)
    range_of_elements = max_num - min_num + 1
    holes = [0] * range_of_elements
    for i in l:
        holes[i - min_num] += 1
    return [item for item in holes for _ in range(item)]

print("pigeonhole sort",pigeonhole_sort([3, 2, 1, 4, 5]))


# 15. cycle sort [O(n log n)]------------------------------------------------------------
# cycle sort is a sorting technique that sorts the elements by dividing the list into several cycles.

def cycle_sort(l):
    for cycle_start in range(len(l)):
        item = l[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, len(l)):
            if l[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == l[pos]:
            pos += 1
        l[pos], item = item, l[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(l)):
                if l[i] < item:
                    pos += 1    
    return l

print("cycle sort",cycle_sort([3, 2, 1, 4, 5]))


# 16. cocktail shaker sort [O(n^2)]------------------------------------------------------------
# cocktail shaker sort is a variation of bubble sort that sorts the list by repeatedly passing through the list in both directions.

def cocktail_shaker_sort(l):
    for i in range(len(l) // 2):
        for j in range(i, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j] 
    return l

print("cocktail shaker sort",cocktail_shaker_sort([3, 2, 1, 4, 5]))


# 17. comb sort [O(n^2)]------------------------------------------------------------
# comb sort is a sorting technique that sorts the elements by comparing the elements that are far apart and then gradually reducing the gap between the elements.

def comb_sort(l):
    gap = len(l) # initialize the gap to the length of the list
    shrink = 1.3
    while gap > 1:
        gap = int(gap / shrink)
        for i in range(len(l) - gap):
            if l[i] > l[i + gap]:
                l[i], l[i + gap] = l[i + gap], l[i]
    return l

print("comb sort",comb_sort([3, 2, 1, 4, 5]))


# 18. gnome sort [O(n^2)]------------------------------------------------------------   
# gnome sort is a sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

def gnome_sort(l):
    i = 0
    while i < len(l):
        if i == 0 or l[i] >= l[i - 1]:
            i += 1
        else:
            l[i], l[i - 1] = l[i - 1], l[i]
            i -= 1
    return l
print("gnome sort",gnome_sort([3, 2, 1, 4, 5]))


# 19. stooge sort [O(n^2)]------------------------------------------------------------   
# stooge sort is a sorting algorithm that works by recursively dividing the list into three parts, sorting the first two-thirds, sorting the last two-thirds, and then sorting the entire list.

def stooge_sort(l):
    if len(l) <= 1:
        return l
    if l[0] > l[-1]:
        l[0], l[-1] = l[-1], l[0]
    return stooge_sort(l[:-1]) + [l[-1]] + stooge_sort(l[:-1])
print("stooge sort",stooge_sort([3, 2, 1, 4, 5]))

# 20. bitonic sort [O(n log n)]------------------------------------------------------------   
# bitonic sort is a sorting algorithm that works by repeatedly sorting the list in a bitonic manner.

def bitonic_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = bitonic_sort(l[:mid])
    right = bitonic_sort(l[mid:])
    return merge(left, right)
print("bitonic sort",bitonic_sort([3, 2, 1, 4, 5]))


# 21. pigeonhole sort [O(n log n)]------------------------------------------------------------   
# pigeonhole sort is a sorting technique that sorts the elements by first dividing the elements into several groups called pigeonholes.

def pigeonhole_sort(l):
    min_num = min(l)
    max_num = max(l)
    range_of_elements = max_num - min_num + 1
    holes = [0] * range_of_elements
    for i in l:
        holes[i - min_num] += 1
    return [item for item in holes for _ in range(item)]
print("pigeonhole sort",pigeonhole_sort([3, 2, 1, 4, 5]))





