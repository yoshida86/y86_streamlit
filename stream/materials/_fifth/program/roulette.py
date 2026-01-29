def roulette(scoreboard):

    scoresum = 0

    for s in scoreboard:
        scoresum += 1/s
    
    dart1 = random.uniform(0,scoresum)
    parent1 = 0
    tmp = 0
    for s in scoreboard:
        tmp += 1/s
        if tmp >= dart1:
            break
        parent1 += 1

    
    #while文に入るための初期化
    dart2 = dart1
    while dart2 == dart1:

        dart2 = random.uniform(0,scoresum)
        parent2 = 0
        tmp = 0
        for s in scoreboard:
            tmp += 1/s
            if tmp >= dart2:
                break
            parent2 += 1
    
    return parent1,parent2