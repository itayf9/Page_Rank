import numpy as np
import pandas as pd

import Graph as Gr
import random
import math

if __name__ == '__main__':
    G = Gr.Graph(2**12)
    q = 1/(2**12)

    ''' add edges
    for i in range(G.vSize):
        for j in range(G.vSize):
            if G.isProbHit(q):
                G.add(i+1, j+1)
    '''

    qArr= [ 1/ (i+1) for i in range(G.vSize) ]
    #qArrSQRT = [1 / math.sqrt(i + 1) for i in range(G.vSize)]
    print(qArr)
    for i in range(G.vSize):
        for j in range(G.vSize):
            if G.isProbHit(qArr[j]):
                G.add(i + 1, j + 1)

    '''
    for k in range(114335747):
        i = random.randint(1, G.vSize)
        j = random.randint(1, G.vSize)
        G.add(i, j)
    '''

    ''' init parameters'''
    E = [0.5, 0.25, 0.125, 0.0625, 0.03125]
    p = E[0]
    N= int(1/p)
    dprev= np.zeros(G.vSize)

    ''' apply page rank'''
    t = 2
    d = G.pageRank(N, t, p)

    print(np.linalg.norm(d - dprev))
    while (np.linalg.norm(d-dprev) > E[0]):

        print("________________t=", t, "________________")

        for i in range(d.size):
            if not d[i] == 0:
                print(i, " : ", d[i], " : num of neighbors= ", G.vertices[i].size)

        print("________________end of t=", t, "________________")

        dprev = d.copy()
        t *= 2
        d = G.pageRank(N, t, p)

        print(np.linalg.norm(d - dprev))




    # ''' init parameters'''
    # K = [0.5, 0.25, 0.125, 0.0625, 0.03125]
    # p = K[0]
    # N = int(1 / p)
    # k = int(1/K[0])
    # #dprev = np.zeros(G.vSize)
    # #dprevTopK = dprev[:k].copy()
    #
    # ''' apply page rank'''
    # t = 2
    # dprev = G.pageRank(N, t, p)
    # dPrevSeries = pd.Series(dprev)
    # dPrevSeries.sort_values(inplace=True, ascending=False)
    #
    # dprevTopK = dPrevSeries[:k].copy()
    #
    # t*=2
    # d = G.pageRank(N, t, p)
    # # d[::-1].sort()
    # dSeries = pd.Series(d)
    # dSeries.sort_values(inplace=True, ascending=False)
    #
    # dTopK = dSeries[:k].copy()
    #
    # while not dTopK.equals(dprevTopK):
    #
    #     print("________________t=", t, "________________")
    #     print((dSeries.where(dSeries.notna()))[:k])
    #     print("________________end of t=", t, "________________")
    #
    #     dprev = d.copy()
    #     dprevTopK = dTopK.copy()
    #     t *= 2
    #     d = G.pageRank(N, t, p)
    #     dSeries = pd.Series(d)
    #     dSeries.sort_values(inplace=True, ascending=False)
    #     dTopK = dSeries[:k].copy()




