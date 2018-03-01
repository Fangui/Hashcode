from parsing import *

def dumb(path):
  rows, cols, vehicles, nb_rides, bonus, nb_steps, rides = readInput(path)
  output = []
  steps_array = []
  for i in range(vehicles):
    output.append([])
    steps_array.append(nb_steps)
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
    if count >= vehicles - 1:
      ride_start[pos] = 1000000000000
      count = 0
    if distances[pos] > steps_array[v]:
      v += 1
      count += 1
      continue
    output[v].append(pos)
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
