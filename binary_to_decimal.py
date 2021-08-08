def BinaryToDecimal(binary):
    '''
    Takes a 2-based number and returns a 10-based number.
    '''
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal


if __name__ == "__main__":
    binary = input('Enter a number: ')
    print(BinaryToDecimal(binary))