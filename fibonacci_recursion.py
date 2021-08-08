def Fibonacci(n):
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
		return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == "__main__":
	x = int(input('Enter the number: '))
	print(Fibonacci(x))
