def Roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        root = -b / (2 * a)
        return f'''
        Discriminant = {discriminant}
        Root = {root}
        '''

    elif discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return f'''
        Discriminant = {discriminant}
        Root 1 = {root1}
        Root 2 = {root2}
        '''

    elif discriminant < 0:
        return f'''
        Discriminant = {discriminant}
        No real root.
        '''


#if __name__ == "__main__":
#    a, b, c = (input("For quadratic function 'f(x) = ax^2 + bx + c' enter a, b, c (separated by ' '): ")).split()
#    a, b, c = int(a), int(b), int(c)
#    print(Roots(a, b, c))

if __name__ == "__main__":
    num = (input("For quadratic function 'f(x) = ax^2 + bx + c' enter a, b, c (separated by ' '): ")).split()
    a, b, c = [int(i) for i in num]
    print(Roots(a, b, c))