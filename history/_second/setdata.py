def genedgelist(G):

    ret = []
    for i in range(len(G)):
        for j in range(i):
            if G[i][j] != 0:
                ret.append([j,i,G[i][j]])
    
    return ret

def genadjlist(V,order):

    ret = [[] for i in range(order)]
    
    for i in range(len(V)):
        ret[V[i][0]].append(i)
        ret[V[i][1]].append(i)
    
    return ret