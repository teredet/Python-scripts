import time

def timer(func):
    '''Tis is decorator that print time to perform a function'''
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print('func takes', end - start, 'seconds')

    return wrapper



if __name__ == "__main__":
    @timer
    def calc(x, y):
        print(x*y)

    calc(5, 2)