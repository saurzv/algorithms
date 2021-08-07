# Merge Sort
# divide and conquer algorithm for sorting an array
# T(n) = O(nlog(n))

def merge(left, right, arr):
	res = []
	i,j,k = 0,0,0

	while k < len(left) and k < len(right):
		if left[i] > right[j] :
			arr[k] = right[j]
			j += 1
		else :
			arr[k] = left[i]
			i += 1
		k += 1

	p = 0
	while i < len(left) :
		arr[k] = left[i]
		i += 1
		k += 1

	p = 0
	while j < len(right) :
		arr[k] = right[j]
		j += 1
		k += 1
	

def merge_sort(arr):
	
	if len(arr) > 1 :
		half = len(arr) // 2
		l = arr[:half]
		r = arr[half:]
		merge_sort(l)
		merge_sort(r)
		merge(l,r,arr)