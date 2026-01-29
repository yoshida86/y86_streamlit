def randprim(G,Elist,A,startv,k):

    n = len(Elist) #辺数
    order = len(A) #頂点数
    Searchlist = [] #探索候補
    lenSearch = 0
    indexlist = [-1 for i in range(n)] #各辺のSearchlist上での添え字
    Vflag = [0 for i in range(order)] 
    ret = [0 for i in range(n)]
    vcount = 0

    #探索開始頂点の探索
    Vflag[startv] = 1
    vcount += 1
    for e in A[startv]:
        if G[e] == 1:
            Searchlist.append(e)
            indexlist[e] = lenSearch
            lenSearch += 1
    
    #全域木になるまで探索する
    while vcount < order:

        if len(Searchlist) < k:
            choicee = copy.deepcopy(Searchlist)
        else:
            choicee = random.sample(Searchlist,k)
        e = choicee[0]
        for i in range(1,len(choicee)):
            if Elist[e][2] > Elist[choicee[i]][2]:
                e = choicee[i]
       
       #探索候補から探索した辺を削除
        if len(Searchlist) == 1:
            Searchlist.pop()
            lenSearch -= 1
        else:
            Searchlist[indexlist[e]] = Searchlist[-1]
            indexlist[Searchlist[-1]] = indexlist[e]
            Searchlist.pop()
            lenSearch -= 1

        #頂点を探索
        if Vflag[Elist[e][0]] != 1:
            Vflag[Elist[e][0]] = 1
            v = Elist[e][0]
        else:
            Vflag[Elist[e][1]] = 1
            v = Elist[e][1]
        vcount += 1
        ret[e] = 1

        #辺を探索候補に追加あるいは削除
        for edge in A[v]:
            if G[edge] == 1:
                if Vflag[Elist[edge][0]] == 0 
                or Vflag[Elist[edge][1]] == 0: #向かう先が未探索
                    Searchlist.append(edge)
                    indexlist[edge] = lenSearch
                    lenSearch += 1
                else: #向かう先が探索済
                    if e != edge:
                        Searchlist[indexlist[edge]] = Searchlist[-1]
                        indexlist[Searchlist[-1]] = indexlist[edge]
                        Searchlist.pop()
                        lenSearch -= 1

    return ret