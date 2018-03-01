from algo import *

def readInput(path):
  f = open(path, "r")
  rows, cols, vehicles, nb_rides, bonus, nb_steps = [int(i) for i in f.readline().split(' ')]
  rides = [];

  for i in range(nb_rides):
      rides.append([int(i) for i in f.readline().split(' ')])

  f.close()
  return rows, cols, vehicles, nb_rides, bonus, nb_steps, rides

def createOutput(path, rides):
  f = open(path.split('.')[0] + ".out", "w")
  for ride in rides:
    f.write(str(len(ride)) + ' ')
    for i in range(len(ride)):
      f.write(str(ride[i]))
      if i < len(ride) - 1:
        f.write(' ')
    f.write('\n')

createOutput("a_example.in", build_matrix(readInput("a_example.in")))
createOutput("b_should_be_easy.in", build_matrix(readInput("b_should_be_easy.in")))
createOutput("c_no_hurry.in", build_matrix(readInput("c_no_hurry.in")))
createOutput("d_metropolis.in", build_matrix(readInput("d_metropolis.in")))
createOutput("e_high_bonus.in", build_matrix(readInput("e_high_bonus.in")))
