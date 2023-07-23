import math
import sys

def computeArea(r):
    return(math.pi * r * r)

radius = float(input("Enter radius in feet: ")) 

sys.stdout.write("The radius you provided was " + format(radius, '.2f') + " feet and the area is about " + format(computeArea(radius), '.2f') + " sq feet")
