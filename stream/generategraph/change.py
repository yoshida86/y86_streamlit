import numpy as np
import networkx as nx
import pandas as pd

## networkXのグラフ
## 隣接行列
## 隣接リスト
## 以上のいずれかをいずれかへ変換できる関数を集めたファイル

## networkXから変換する奴は、リストを使った形に変えるようにしている
## 隣接系からnxのグラフに変えるのは、機能がnxに備わっているのでなし

def XtoN(G):

	Nmat = []
	for i in range(nx.number_of_nodes(G)):
		tmpmat = [0 for j in range(nx.number_of_nodes(G))]
		tmplist = [n for n in G.neighbors(i)]
		for j in tmplist:
			tmpmat[j] = 1
		Nmat.append(tmpmat)
	    
	return Nmat


def XtoL(G):
	
	Nlist = []
	for i in range(nx.number_of_nodes(G)):
		Nlist.append([n for n in G.neighbors(i)])
	
	return Nlist


