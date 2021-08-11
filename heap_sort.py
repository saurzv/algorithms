# Heap Sort
# Sort the array in increasing order
# T(n) = O(nlog(n))

'''
build_heap() call in heap_sort() will take O(n) times.
for loop in in heap_sort() calls max_heapify() O(n) times
each call takes O(log(n)) time
so total time: O(n) * O(log(n)) + O(n) = O(nlog(n))
'''

def max_heapify(arr, n, i = 0) :
    ''' fix the max heap property at one node '''

    max = i     # index of maximum element of node
    l = 2*i + 1     # left child
    r = 2*i + 2     # right child

    # change max to l if it is greater than max
    if l < n and arr[max] < arr[l] :
        max = l
    
    if r < n and arr[max] < arr[r] :
        max = r
    
    # if max is changed, swap the max for the new max
    if max != i :
        arr[max], arr[i] = arr[i], arr[max]
        # call to fix the max heap property of child node, if any
        max_heapify(arr, n, max)

def build_heap(arr, n) :
    ''' Builds a max heap from an array '''

    # only calls for nodes from index n/2 and above, because below that every element is a leaf
    for i in range(n//2, -1, -1) :
        max_heapify(arr, n, i)

def heap_sort(arr) :
    ''' Sort an unsorted array '''

    n = len(arr)
    # puts the largest element at index 0
    build_heap(arr, n)
    
    for i in range(n-1, 0, -1) :
        # move the largest element to the end
        arr[0], arr[i] = arr[i], arr[0]
        n -= 1
        # puts the next largest element at index 0
        max_heapify(arr, n, 0)

""" a = [10, 3, 4, 1, 5, 2, 7]
heap_sort(a)
print(a)
works fine, prints [1, 2, 3, 4, 5, 7, 10] """