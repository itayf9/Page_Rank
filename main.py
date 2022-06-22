import numpy as np
import pandas as pd

import Graph as Gr
import random
import math

if __name__ == '__main__':
    G = Gr.Graph(2**12)
    q = 1/(2**12)

    ''' add edges - first graph family
        for each edge (i,j), the probability of (i,j) to be added is 'q' 
        we can select different values for 'q' '''
    for i in range(G.vSize):
        for j in range(G.vSize):
            if G.isProbHit(q):
                G.add(i+1, j+1)

    ''' add edges - second graph family
        for each edge(i,j), the probability of (i,j) to be added is qArr[j] 
        we can select qArr of qArrSQRT '''
    # qArr= [ 1/ (i+1) for i in range(G.vSize) ]
    # qArrSQRT = [1 / math.sqrt(i + 1) for i in range(G.vSize)]
    # for i in range(G.vSize):
    #     for j in range(G.vSize):
    #         if G.isProbHit(qArr[j]):
    #             G.add(i + 1, j + 1)


    ''' random walks with 'e' stopping parameter'''
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

    # calculates the number of vertices with stable ranking
    dPrevSeries = pd.Series(dprev)
    dPrevSeries.sort_values(inplace=True, ascending=False)
    dSeries = pd.Series(d)
    dSeries.sort_values(inplace=True, ascending=False)
    i=0
    for x, y in zip(np.array(dPrevSeries.index),np.array(dSeries.index)):
        if x==y:
            i+=1
        else:
            break
    print(dPrevSeries)
    print(dSeries)
    print(i)



    ''' random walks with 'k' stopping parameter'''
    # ''' init parameters'''
    # K = [0.5, 0.25, 0.125, 0.0625, 0.03125]
    # p = K[0]
    # N = int(1 / p)
    # k = int(1/K[4])
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
    # while (not np.all(np.equal(np.array(dTopK.index), (np.array(dprevTopK.index))))) and (t < 8000000):
    #
    #     print("________________t=", t, "________________")
    #     # print((dSeries.where(dSeries.notna()))[:k])
    #     # print("________________end of t=", t, "________________")
    #     print(np.linalg.norm(d - dprev))
    #
    #     dprev = d.copy()
    #     dprevTopK = dTopK.copy()
    #     t *= 2
    #     d = G.pageRank(N, t, p)
    #     dSeries = pd.Series(d)
    #     dSeries.sort_values(inplace=True, ascending=False)
    #     dTopK = dSeries[:k].copy()
    #
    # print("________________t=", t, "________________")
    # print((dSeries.where(dSeries.notna()))[:k])
    # print("________________end of t=", t, "________________")
    #
    # print(np.linalg.norm(d - dprev))



