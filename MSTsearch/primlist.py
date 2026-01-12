import numpy as np
import networkx as nx
from . import prim_heap as heap

def Prim(A):
    print(A)
    MST = [[i] for i in range(len(A))]

    Vdata = {i: [float('inf'),i,-1] for i in range(len(A))}
    
    N = [-1 for i in range(len(A))]
    
    U = heap.Heap()

    s = 0
    Vdata[s][2] = 0
    for i in range(1,len(A[s]),2):
        if A[s][i] == "":
            break
        Vdata[int(A[s][i])][0] = A[s][i+1]
        N[int(A[s][i])] = s
        U.insert(Vdata[int(A[s][i])])

    while(len(U.data)!=0):

        w = U.deletemin()
        MST[w[1]].append(N[w[1]])
        MST.append(w[0])
        MST[N[w[1]]].append(w[1])
        MST.append(w[0])

        for j in range(1,len(A[w[1]]),2):
            if A[w[1]][j] == "":
                break
            if A[w[1]][j] != 0:
                tmpnode = int(float(A[w[1]][j]))
                if int(float(A[w[1]][j+1])) < Vdata[tmpnode][0]:
                    if Vdata[tmpnode][2] == -1:
                        Vdata[tmpnode][0] = float(A[w[1]][j+1])
                        N[tmpnode] = w[1]
                        U.insert(Vdata[tmpnode])
                    else:
                        Vdata[tmpnode][0] = float(A[w[1]][j+1])
                        N[tmpnode] = w[1]
                        U.update(Vdata[tmpnode][2])

    
    return MST,U.opecount
