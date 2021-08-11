# Binary Search
# Find the index k of a key in a sorted array
# T(n) = O(logn)

def binary_search(arr, key) :
	l = len(arr)
	s, e = 0, l-1
	while s<e:
		mid = (s+e)//2
		if arr[mid] == key :
			return mid
		if arr[mid] > key :
			e = mid-1
		else :
			s = mid+1
	return -1

# print(binary_search([1,2,3,4,5], 3))
# works fine, prints 2