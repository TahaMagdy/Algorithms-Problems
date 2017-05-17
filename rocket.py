#!/usr/bin/python
import math

class Rocket:
    '''
    * n is the Rocket Number
    * a is the Acceleration
    * t is the Duration -- the time of rocket working
    '''
    def __init__(self, n, a, t):
        self.n = n
        self.a = a
        self.t = t
##

def main():
    '''
        1 * Reading the rockets data into rockets[]
          * O(n)
    '''
    rocketsNumber = input("Enter the number of the rockets\n")
    i = 0
    rockets = []
    print "Enter acceleration and time:"
    for i in range (0,rocketsNumber):
        a,t = raw_input().split()
        a = float(a); t = float(t)
        obj = Rocket(i, a, t )
        rockets.append(obj)

    '''
        2 * Sorting Rockets based on acceleration.
          * O(n log n)
          * rockets has been reordered
    '''
    rockets.sort(key=lambda x: x.a, reverse=True)


    '''
        3 * Launching rockets
    '''
    distance = 0.0
    vt       = 0.0
    for p in rockets:
        print "Rocket", (p.n+1)
        vt += p.a * p.t
        distance +=  (vt * p.t) + (0.5 * p.a * p.t * p.t)

    print "Total distance", math.floor(distance/2)

if __name__ == "__main__":
    main()
