import operator

oper = input("Enter operator [+ - / * **]: ")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

action = {
 "+" : operator.add,
 "-" : operator.sub,
 "/" : operator.truediv,
 "*" : operator.mul,
 "**" : pow
}
 
print(action[oper](number1, number2))

