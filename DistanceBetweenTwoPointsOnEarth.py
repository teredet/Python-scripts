import math

def DistanceBetweenTwoPointsOnEarth(t1, g1, t2, g2):
    '''
    The function calculates the distance between two points on Earth. The result is returned in kilometers.\n
    
    Keyword arguments:\n
    t1 - latitude of point A\n
    g1 - longitude of point A\n
    t2 - latitude of point B\n
    g2 - longitude of point B
    '''
    t1 = math.radians(float(t1))
    t2 = math.radians(float(t2))
    g1 = math.radians(float(g1))
    g2 = math.radians(float(g2))

    distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

    return round(distance, 2)

if __name__ == "__main__":
    t1, g1, t2, g2 = input("\nEnter the latitude and longitude of two points on the Earth’s (separated by ' '): ").split(" ")
    print(f"\nDistance = {DistanceBetweenTwoPointsOnEarth(t1, g1, t2, g2)} km.\n" )