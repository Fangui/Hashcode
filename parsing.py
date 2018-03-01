def readInput(path):
  f = open(path, "r")
  rows, cols, vehicles, nb_rides, bonus, nb_steps = [int(i) for i in f.readline().split(' ')]
  rides = [];

  for i in range(nb_rides):
      rides.append([int(i) for i in f.readline().split(' ')])

  f.close()
  return rows, cols, vehicles, nb_rides, bonus, nb_steps, rides

#def createOutput(rides):
#  f = open("toto", "w")
