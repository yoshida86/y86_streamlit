import random
import copy


def mutation(Elist,tree,A):
	
	treeedges = []
	for treeE in range(len(tree)):
		if tree[treeE] == 1:
			treeedges.append(treeE)

	mutedges = random.sample(treeedges,5)
	mutedge = mutedges[0]
	for mute in mutedges:
		if Elist[mutedge][2] < Elist[mute][2]:
			mutedge = mute
	
	tree[mutedge] = 0
	print(mutedge)
	connectV = mutbfs(tree,Elist,A,0) ##bfsで連結成分探し

	searchE = []
	for i in range(len(Elist)):
		if connectV[Elist[i][0]] != connectV[Elist[i][1]]:
			searchE.append(i)

	if len(searchE) < 5:
		choicee = copy.deepcopy(searchE)
	else:
		choicee = random.sample(searchE,5)
	adde = choicee[0]
	for i in range(1,len(choicee)):
		if Elist[adde][2] > Elist[choicee[i]][2]:
			adde = choicee[i]
	
	tree[adde] = 1

	return tree