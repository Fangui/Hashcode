#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:15:26 2018

@author: damien
"""

class Voiture():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.run = False
        self.step = 0
        self.map = []
        self.rides = []
        
    def actualize(self):
        self.step -= 1
        if (self.step == 0):
            self.run = False
        
    def setRide(self, x, y, step, index):
        self.x = x
        self.y = y
        self.step = step
        self.run = True
        self.rides.append(index)

    def compute(self, rides, step, bonuspt):
        for j in range (len(rides)):
            if (rides[j] == []):
                continue
            start_dist = abs(self.x - rides[j][0]) + abs(self.y - rides[j][1])
            dist = abs(rides[j][0] - rides[j][2]) + abs(rides[j][1] - rides[j][3])
            tmp = rides[j][4] - start_dist + step
            time = 0
            if (tmp > 0):
                time = dist + start_dist + tmp
            else:
                time = dist + start_dist
            if (time + step > rides[j][5]):
                self.append(-999999999)
            bonus = (time + step - rides[j][5]) * bonuspt
            res = (dist + bonus) - time
            self.append(res)
            
    

def build_matrix(ctx):
    rides = ctx[6]
    voitures = []
    for i in range(ctx[2]):
        voitures.append(Voiture())
    for step in range(ctx[5]):
        for voiture in voitures:
            voiture.acutalize()
            if voiture.run == False:
                continue
            voiture.compute(rides, step, ctx[4])
            index = voiture.map.index(min(voiture.map))
            if (voiture.map[index] == -999999999):
                continue
            ride = rides[index]
            start_dist = abs(voiture.x - ride[0]) + abs(voiture.y - ride[1])
            dist = abs(ride[0] - ride[2]) + abs(ride[1] - ride[3])
            tmp = ride[4] - start_dist + step
            time = 0
            if (tmp > 0):
                time = dist + start_dist + tmp
            else:
                time = dist + start_dist
            voiture.set(ride[2], ride[3], time, index)
            rides[index] = []
    res = []
    for voiture in voitures:
        res.append(voiture.rides)
    return res