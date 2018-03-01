from parsing import *

def dumb(path):
  rows, cols, vehicles, nb_rides, bonus, nb_steps, rides = readInput(path)
  output = []
  for i in range(vehicles):
    output.append([])
  ride_start = []
  for ride in rides:
    distance = abs(ride[2] - ride[0]) + abs(ride[3] - ride[1])
    ride_start.append(ride[5])
  v = 0
  for i in range(nb_rides):
    if v >= vehicles:
      v = 0
    pos = ride_start.index(min(ride_start))
    output[v].append(pos)
    ride_start[pos] = 1000000000000
    v += 1
  createOutput(path, output)

dumb("a_example.in")
dumb("b_should_be_easy.in")
dumb("c_no_hurry.in")
dumb("d_metropolis.in")
dumb("e_high_bonus.in")
