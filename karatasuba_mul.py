# divide and conquer algorithm for multiplication.
# T(n) = O(n^1.59)

def mul(x, y):
	n = max(len(str(x)), len(str(y)))
	if n < 10 :
		return x*y

	half = n//2

	a = x // (10**half)
	b = x % (10**half)
	c = y // (10**half)
	d = y % (10**half)

	p1 = mul(a,b)
	p2 = mul(c,d)
	p3 = mul(a+b,c+d)

	return (10**n)*p1 + (p3-p2-p1)*(10**half) + p2