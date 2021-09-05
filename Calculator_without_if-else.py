import operator

def calc_without_if_else(num1, num2, oper):
    '''
    num1, num2 - int\n
    oper - string\n
    Implementation of a calculator without if-else.
    '''
    action = {
    "+" : operator.add,
    "-" : operator.sub,
    "/" : operator.truediv,
    "*" : operator.mul,
    "**" : pow
    }
    
    return action[oper](number1, number2)

if __name__ == "__main__":
    oper = input("Enter operator [+ - / * **]: ")
    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    print(calc_without_if_else(number1, number2, oper))