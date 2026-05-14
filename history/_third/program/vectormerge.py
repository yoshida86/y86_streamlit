def vectormerge(v1,v2):

    ret = []
    
    for i in range(len(v1)):
        if v1[i] == 0 and v2[i] == 0:
            ret.append(0)
        else:
            ret.append(1)

    return ret