def InchToCentimeters(foot, inch):
    '''
    Accepts pounds and inches. Returns the equivalent in centimeters.
    '''
    foot = int(foot)
    inch = int(inch)
    inch += foot * 12
    res = inch * 2.54
    return round(res, 2)


if __name__ == "__main__":
    foot, inch = input("Enter foot and inch (separated by ' '): ").split(" ")
    print(f"\n {InchToCentimeters(foot, inch)} centimeters \n")