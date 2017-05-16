#!/usr/bin/python

# n is the Rocket Number
# a is the Acceleration
# t is the Duration -- the time of rocket working
class Rocket:


    ##
    def __init__(self, n, a, t):
        self.n = n
        self.a = a
        self.t = t
        init_velocity = 0

    ##
    # Calculate the distance that is cut with this rocket
    def traveled_distance(self, rocket):
        return (self.init_velocity * self.t) + (0.5 * self.a * self.t * self.t)

    ##
    # Calculate the final velocity of the ship after launching this rocket
    def final_velocity(self):
        return self.init_velocity + (self.a * self.t)
###
#END CLASS Rocket
###



#TESTING
obj = Rocket(2,3,4)
obj.init_velocity = 0
print obj.traveled_distance( obj)
print obj.final_velocity()
