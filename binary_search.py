# Binary Search
# Find the index k of a key in a sorted array
# T(n) = O(logn)

def binary_search(arr, key):
	n = len(arr)
	k,b = 0,n//2
	while True:
		while k+b < n and arr[k+b] <= key :
			k += b
		b //= 2
		if b < 1 :
			break
	if(arr[k] == key):
		return k
	return k

# print(binary_search([1,2,3,4,5], 3))
# works fine, prints 2