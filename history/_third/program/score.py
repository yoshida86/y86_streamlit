def score(tree,V):

    ret = 0

    for i in range(len(tree)):

        if tree[i] == 1:
            ret += V[i][2]
    
    return ret