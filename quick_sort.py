# Quick Sort
# Sorts a given array in acending order
# T(n) = O(nlog(n)) <-- best case
# T(n) = O(n^2) <-- worst case

from random import randint

def quick_sort(arr):
    ''' Sorts a given array in acending order '''

    n = len(arr)
    if len(arr) > 1 :
        r = randint(0,n-1)
        # select a pivot point randomly
        pivot = arr[r]
        a, c = [], []

        # divides items w.r.t pivot point
        for i in range(n) :
            if i == r :
                continue
            if arr[i] < pivot :
                a.append(arr[i])
            else :
                c.append(arr[i])

        # recursively sort left and right part
        quick_sort(a)
        quick_sort(c)

        # join the sorted left, pivot and right part
        k = 0
        for i in a :
            arr[k] = i
            k += 1

        arr[k] = pivot
        k += 1

        for i in c :
            arr[k] = i
            k += 1

""" 
arr = [10, 4, 2, 1, 9, 7, 0, -1, 2, 23]
quick_sort(arr)
print(arr)
works fine, prints: [-1, 0, 1, 2, 2, 4, 7, 9, 10, 23]
"""