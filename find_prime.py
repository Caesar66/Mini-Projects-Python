import math
import random

def fermat(p):
	return True if pow(a, p-1, p) == 1 else False

def millerRabin(p, k=50):
	d = p-1
	r = 0

	while d%2 == 0 and d != 0:
		d = d//2
		r += 1
	
	for i in range(k):
		composite = True
		a = random.randint(2, p-2)
		x = pow(a, d, p)
		if x == 1 or x == p-1:
			continue
		else:
			for j in range(r-1):
				x = pow(x, 2, p)
				if x ==  p-1:
					composite = False
					break
		if composite == False:
			continue
		return False
	return True

#print(millerRabin(1759*pow(2,7284439)-1))
print(millerRabin(1759))
