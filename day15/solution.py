import sys

arg = sys.argv[1]

with open(arg, 'r') as f:
    entry = f.readlines()

#print(entry)

def manhattan(c1,c2):
    rgx = abs(c1[0] - c2[0])
    rgy = abs(c1[1] - c2[1])
    return rgx + rgy


sensors = set()
beacons = set()
non_beacons = set()
global row 
row = 2000000

def add_manhattan(sensor, distance, non_beacons):
    x, y = sensor
    for xx in range(distance+1):
        c1 = (x+xx, row)
        c2 = (x-xx, row)
        c3 = (x+xx, row)
        c4 = (x-xx, row)
        for c in [c1,c2,c3,c4]:
            d = manhattan(c, sensor)
            if d <= distance and c != sensor:
                non_beacons.add(c)


for line in entry:
    line = line.split(" ")
    sensor_x, sensor_y, beacon_x, beacon_y = line[2], line[3], line[8], line[9]
    sensor_x = sensor_x.split("=")[1].split(",")[0]
    sensor_y = sensor_y.split("=")[1].split(":")[0]
    beacon_x = beacon_x.split("=")[1].split(",")[0]
    beacon_y = beacon_y.strip().split("=")[1]
    sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)
    sensor = (sensor_x, sensor_y)
    beacon = (beacon_x, beacon_y)
    sensors.add(sensor)
    beacons.add(beacon)
    dist = manhattan(sensor,beacon)
    #add_manhattan(sensor, dist, non_beacons)
    print("sensor: {} beacon: {} dist: {}".format(sensor,beacon,dist))
    if sensor in non_beacons:
        non_beacons.remove(sensor)
    if beacon in non_beacons:
        non_beacons.remove(beacon)


num = len([c for c in non_beacons if c[1] == row])
print(num)

#### PART 2 ###
edge = 4000000
b = [x for x in beacons if x[0] >= 0 and  x[1] >= 0 and x[0] <= edge and x[1] <= edge]
print(b) 
