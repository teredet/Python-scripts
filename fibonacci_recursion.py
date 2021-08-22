import time
from functools import lru_cache

# basic
# very slow
def recursiveFib(n):
	'''
	Takes a number in the sequence of Fibonacci numbers and returns its value.
	'''
	if n < 0:
		print("Incorrect input")
        
	elif n == 0:
		return 0
        
	elif n == 1 or n == 2:
		return 1

	else:
		return recursiveFib(n-1) + recursiveFib(n-2)

# basic with cache
# More faster. But have trable with "RecursionError: maximum recursion depth exceeded".
# It happens if you try to calculate number that higher than 500
@lru_cache()
def recursiveFibCached(n):
	'''
	Takes a number in the sequence of Fibonacci numbers and returns its value.
	'''
	if n < 0:
		print("Incorrect input")
        
	elif n == 0:
		return 0
        
	elif n == 1 or n == 2:
		return 1

	else:
		return recursiveFibCached(n-1) + recursiveFibCached(n-2)



if __name__ == "__main__":
	x = int(input('Enter the number: '))
	type_f = input("Enter type ([R]ecursive, [C]ache recursive):").upper()
	start_time = time.time()
	if type_f == 'R':
		print(recursiveFib(x))
	elif type_f == 'C':
		print(recursiveFibCached(x))

	print(f"--- {time.time() - start_time} seconds ---")
