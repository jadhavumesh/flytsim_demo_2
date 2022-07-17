!/usr/bin/env python
import time
from flyt_python import api
drone = api.navigation(timeout=120000) # instance of flyt droneigation class

#at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print 'taking off'
drone.take_off(10.0)

#All 3 sides are of same lenth i.e 10m, it means it's an equilateral triangle.
#height of equi.triangle, h = 1/2 (under root3 * a(side length)) = 1/2 * (under root 3 * 10) = 8.66 OR we can simple use pythagorus theorem

print ' going along the setpoints'
drone.position_set(8.66,5,5,relative=True)
drone.position_set(-8.66,5,0,relative=True)
drone.position_set(0,-10,0,relative=True)

print 'Landing'
drone.land(async=False)

#shutdown the instance
drone.disconnect()
 
