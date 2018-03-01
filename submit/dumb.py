from parsing import *

def distanceTP(a, b, c, d):
  return abs(c - a) + abs(d - b)

def dumb(path):
  rows, cols, vehicles, nb_rides, bonus, nb_steps, rides = readInput(path)
  output = []
  steps_array = []
  vehicles_pos = []
  for i in range(vehicles):
    output.append([])
    steps_array.append(nb_steps)
    vehicles_pos.append([0, 0, True, -1])
  ride_start = []
  distances = []
  count = 0
  for ride in rides:
    distance = abs(ride[2] - ride[0]) + abs(ride[3] - ride[1])
    distances.append(distance)
    ride_start.append(ride[5])
  v = 0
  for i in range(nb_rides):
    if v >= vehicles:
      v = 0
    pos = ride_start.index(min(ride_start))
    if count == 0:
      dst = 100000000000
      start_pos = [rides[pos][0], rides[pos][1]]
      for j in range (len(vehicles_pos)):
        if dst > distanceTP(start_pos[0], start_pos[1], vehicles_pos[j][0], vehicles_pos[j][1]):
          v = j
          dst = distanceTP(start_pos[0], start_pos[1], vehicles_pos[j][0], vehicles_pos[j][1])
    output[v].append(pos)
    vehicles_pos[v][0] = rides[pos][2]
    vehicles_pos[v][1] = rides[pos][3]
    vehicles_pos[v][2] = False
    vehicles_pos[v][3] = ride_start[pos]
    vehicles
    ride_start[pos] = 1000000000000
    steps_array[v] -= distances[pos]
    count = 0
    v += 1
  createOutput(path, output)

dumb("a_example.in")
dumb("b_should_be_easy.in")
dumb("c_no_hurry.in")
dumb("d_metropolis.in")
dumb("e_high_bonus.in")
