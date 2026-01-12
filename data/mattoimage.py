import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def csvtomat(filepath):

    array = np.loadtxt(filepath)

    

def mattoimage(numarray):
    
    G = nx.from_numpy_array(numarray)

    edge_labels = {(i,j): w['weight'] for i,j,w in G.edges(data = True)}

    pos = nx.planar_layout(G)
    nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels)
    nx.draw_networkx(G,pos=pos, with_labels=False)

    plt.savefig("graphexample.png")
