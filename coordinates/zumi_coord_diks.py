from zumi.zumi import Zumi
import time
import math

from collections import defaultdict
from heapq import *


zumi = Zumi()

current_x = 0
current_y = 0

# file = open("speed_prediction.txt","r")
# data = file.readlines()
# speed_set = int(data[0])
# speed_cm_sec  = float(data[1])
# slope_int = float(data[2])

speed_set = 40
speed_cm_sec  = 15.24
slope_int = 2.54

print("speed" , speed_set)
print("speed cm/s ",speed_cm_sec)
print("slope int ", slope_int)


def dijkstra(edges, f, t):
   
    g = defaultdict(list)
    locations_list =[]
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            #path = (v1, path)
            path += (v1, )
            locations_list.append(v1)
            
            if v1 == t: return cost, path, locations_list

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")

def move_cm(distance,angle):
    global speed_set,speed_cm_sec,slope_int
    speed = speed_set
    slope = speed_cm_sec
    y_intercept = slope_int
    
    # this is the speed Zumi 
    #travels at, in centimeters per second
    
    #how much time in seconds 
    #it takes to travel the distance in inches
    duration = (distance - y_intercept)/slope
    
    #make sure if there is no distance only turn
    if(distance<0.1):
        zumi.turn(angle)
    #if there is a distance go at speed 40 at that angle
    else:
        time_start = time.time()
        time_elapsed = 0
        zumi.forward(speed,duration,angle) 
#         while(duration > time_elapsed):
#             time_elapsed = time.time()-time_start            
#             zumi.go_straight(speed,angle)
        zumi.hard_brake()
               
def move_to_coordinate(desired_x,desired_y):
    
    global current_x, current_y
    time_start = time.time()
    dx = desired_x - current_x
    dy = desired_y - current_y
    
    #find the angle
    angle = math.degrees(math.atan2(dy,dx)) 
    
    #find the distance to the coordinate
    distance = math.hypot(dx,dy)
    
    #update the coordinates
    current_x = desired_x
    current_y = desired_y
    
    #print(" ang = ", angle, " dist = ",distance)
    
    zumi.turn(angle)
    move_cm(distance,angle)
    time_elapsed = time.time()-time_start
    return time_elapsed



'''
Mini Map

G - H - I
|   |   |
D - E - F
|   |   |
A - B - C

'''

l_road = 43
#length of road in centimeters

edges = [
    ("A", "D", l_road),
    ("A", "B", l_road),
    ("B", "E", l_road),
    ("B", "C", l_road),
    ("C", "F", l_road),
    ("D", "E", l_road),
    ("D", "G", l_road),
    ("E", "H", l_road),
    ("G", "H", l_road),
    ("E", "F", l_road),
    ("F", "I", l_road),
    ("H", "I", l_road),]

starting_location = "A"
ending_location = "F"

cost, ed, l = dijkstra(edges, starting_location, ending_location)
print (starting_location," start , ", ending_location, " end")
print("path",l)



# print (dijkstra(edges, "A", "F"))
# print ("F -> G:")
# print (dijkstra(edges, "F", "G"))

# zumi.mpu.calibrate_MPU()
# zumi.reset_gyro()

# current_x = 0
# current_y = 0

# #43 cm

# move_to_coordinate(0,30)
# move_to_coordinate(30,30)
# move_to_coordinate(30,0)
# move_to_coordinate(0,0)

# move_to_coordinate(l_road,0)
# move_to_coordinate(l_road,l_road)
# move_to_coordinate(2*l_road,l_road)
# move_to_coordinate(2*l_road,2*l_road)
# move_to_coordinate(3*l_road,2*l_road)
# move_to_coordinate(3*l_road,3*l_road)

# move_to_coordinate(10,10)
# move_to_coordinate(0,10)
# move_to_coordinate(0,0)

