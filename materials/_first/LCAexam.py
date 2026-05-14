import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pickle
from . import LCA

def LCAexam():

    st.title("最小共通祖先の例")
    st.text("スライダーで二点選択すると、最小共通祖先の色が変わります。")

    
    with open("materials/_first/RootedTree.pkl","rb") as f:
        G = pickle.load(f)

    with open("materials/_first/pos.pkl","rb") as f:
        pos = pickle.load(f)

    V1 = st.slider(
    "頂点1を選んでください",
    min_value=1,
    max_value=14,
    value=0
    )

    V2 = st.slider(
    "頂点2を選んでください",
    min_value=1,
    max_value=14,
    value=0
    )

    if V1 == V2:
        LCA.Treeplot(G,pos)
    else:
        LCA.LCAplot(G,pos,V1,V2)

    st.caption("赤:選んだ頂点　　黄:LCA")