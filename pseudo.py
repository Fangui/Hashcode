#!/usr/bin/python

for i in range(nb_step):
    to_change = []
    prv = cars

    while (len(to_change) > 0):
        for v in cars:
            if v.run:
                continue
            v.step = min(rides)
        
        tmp = cars
        for i in range(len(cars)):
            for j in range(len(cars)):
                if (i == j):
                    continue
                if (tmp[i].x == tmp[j].x 
                    and tmp[i].y == tmp[j].y):
                    if (tmp[i].step < tmp[j].step):
                        to_change.append(tmp[i])
                    else
                        to_change.append(tmp[j])

        if (len(to_change) == len(prv))
            break
        else
            prv = to_change
