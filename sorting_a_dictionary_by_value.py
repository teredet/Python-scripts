def sort_by_value(xs):
    '''
    Takes in an unsorted dictionary and returns the sorted version by value.
    '''
    return sorted(xs.items(), key=lambda x: x[1])

if __name__ == "__main__":
    xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
    print(sort_by_value(xs))