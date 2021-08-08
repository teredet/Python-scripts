def reverse_string(s):
    '''
    Takes a String and returns it back to front.
    '''
    return "".join(reversed(s))


if __name__ == "__main__":
    s = input()
    print(reverse_string(s))