from collections import defaultdict
import numpy as np
import random


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, vSize):
        self.vertices = [np.array([], dtype=int)] * vSize
        self.vSize = vSize

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self.vertices[node1-1]= np.append(self.vertices[node1-1], [node2])

    def isAdj(self, u, v):
        return True if v in self.vertices[u-1] else False

    def pageRank(self, numberOfSteps_N, numberOfIterations_t, prob_p):
        d=  np.zeros(self.vSize)

        for i in range(numberOfIterations_t):
            d[self.randomWalk(numberOfSteps_N, prob_p) - 1] +=1

        d/= numberOfIterations_t
        d= np.around(d, decimals=3)

        return d

    def randomWalk(self, numberOfSteps_N, prob_p):
        currentVertex = random.randint(1, self.vSize)

        for i in range(numberOfSteps_N):
            if not self.isProbHit(prob_p): # 1-p
                countNumOfNeighbors = self.vertices[currentVertex-1].size

                if countNumOfNeighbors != 0:
                    randSelectNeighbor = random.randint(0, countNumOfNeighbors-1)
                    currentVertex = self.vertices[currentVertex-1][randSelectNeighbor]

            else: # p
                currentVertex = random.randint(1, self.vSize)


        return currentVertex



    def isProbHit(self,prob_p):
        currentRand = random.random()

        return True if currentRand < prob_p else False
