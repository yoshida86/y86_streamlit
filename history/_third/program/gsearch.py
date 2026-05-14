from collections import deque
import random

def bfs(G,Vec,A,startv):

    Q = deque()
    Q.append([startv,-1])
    Vflag = [0 for i in range(len(A))] # 探索済みの頂点を管理
    vcount = 0
    ret = [0 for i in range(len(G))]
    order = len(A)

    while vcount < order:

        v = Q.popleft()
        if Vflag[v[0]] == 0:
            Vflag[v[0]] = 1
            if startv != v[0]:
                ret[v[1]] = 1
            vcount += 1

            adje = random.sample(A[v[0]],len(A[v[0]]))

            for e in adje:
                if G[e] == 1:
                    if Vec[e][0] == v[0]:
                        Q.append([Vec[e][1],e])
                    else:
                        Q.append([Vec[e][0],e])

    return ret