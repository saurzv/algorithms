# Selection
# finds k-th smallest element in an array.
# T(n) = O(n)

from random import randint

def selection(arr, k) :
	v = arr[randint(0, len(arr)-1)]
	print(v)
	sl, sv, sr = [], [], []

	for i in arr :
		if i < v :
			sl.append(i)
		elif i == v :
			sv.append(i)
		else :
			sr.append(i)

	if k < len(sl) :
		return selection(sl,k)
	if len(sl) < k <= len(sl)+len(sv) :
		return v
	if k > len(sl)+len(sv) :
		return selection(sr, k - len(sl) - len(sv))

print(selection([1,4,5,10,19,5,29,3], 4))