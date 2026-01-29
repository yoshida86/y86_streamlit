import pandas as pd
from . import prim
from . import primlist

def callprim(graph,form):

    G = graph.values.tolist()

    if form == '隣接行列':
        MST,operation = prim.Prim(G)
    if form == '隣接リスト':
        MST,operation = primlist.Prim(G)

    return MST,operation

