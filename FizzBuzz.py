# basic varsion

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number

for number in range(1, 101):
    print(fizzbuzz(number))

# advanced version

for n in range(1, 101):
    print("Fizz"*(not n % 3) + "Buzz"*(not n % 5) or n)