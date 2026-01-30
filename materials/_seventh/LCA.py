import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pickle


def Treeplot(G,pos):

    fig, ax = plt.subplots()
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=500,
        ax=ax
    )

    st.pyplot(fig)


def LCAplot(G,pos,V1,V2):

    LCA = nx.lowest_common_ancestor(G, V1, V2)

    node_colors = []
    for n in G.nodes():
        if n == LCA:
            node_colors.append("yellow")
        elif n == V2 or n == V1:
            node_colors.append("red")
        else:
            node_colors.append("tab:blue")

    fig, ax = plt.subplots()
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=500,
        ax=ax
    )

    st.pyplot(fig)