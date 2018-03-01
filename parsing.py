def readInput(path):
    f = open(path)
    rows, cols, vehicles, nb_rides, bonus, nb_steps = [int(i) for i in f.readline().split(' ')]
    rides = [];
    
    for i in range(nb_rides):
        rides.append([int(i) for i in f.readline().split(' ')])
    
    f.close()
    return rows, cols, nb_rides, rides
