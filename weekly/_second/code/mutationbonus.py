def get_mutation_bonus(mutation_flag,parent1,parent2):
	
	#初期化
	mutation_bonus = 1
	
	#親個体の少なくともどちらかの補正が1でない時、補正値=低い方の補正値+0.1
	mutation_parent = min(parent1,parent2,key=lambda ind: ind.mutation_bonus)
	if mutation_parent.mutation_bonus != 1:
		mutation_bonus = mutation_parent.mutation_bonus + 0.1
	
	#直前で突然変異が起きていたら問答無用で0.1
	if mutation_flag == 1:
		mutation_bonus = 0.1

	return mutation_bonus