def dfs(G,Elist,A,startv):

    S = []
    S.append([startv,-1])
    Vflag = [0 for i in range(len(A))]
    vcount = 0
    ret = [0 for i in range(len(G))]
    order = len(A)

    while vcount < order:

        v = S.pop()
        if Vflag[v[0]] == 0:
            Vflag[v[0]] = 1
            if startv != v[0]:
                ret[v[1]] = 1
            vcount += 1

            adje = random.sample(A[v[0]],len(A[v[0]]))

            for e in adje:
                if G[e] == 1:
                    if Elist[e][0] == v[0]:
                        S.append([Elist[e][1],e])
                    else:
                        S.append([Elist[e][0],e])

    return ret