import streamlit as st
import pandas as pd
from . import callprim as callp
from . import mattoimage as mai
import networkx as nx
import numpy as np

def MSTsearch():

    st.title('MSTsearch')

    st.text('隣接行列か、隣接リストのcsvを使って、全域最小木の探索ができます')

    form = st.selectbox('csvの形を選択',['隣接リスト','隣接行列'])

    importgraph = st.file_uploader('csvを入力')
    
    alg = st.selectbox(
        '最小木探索のアルゴリズムを選択',
        ['prim']
    )

    if st.button('実行'):
        if alg == 'prim': 
            
            st.divider()
            G = pd.read_csv(importgraph,header=None,na_filter=False)
            
            MST,operation = callp.callprim(G,form)

            if form == '隣接行列':
                G = G.to_numpy()
                MST = np.array(MST)
                graph = nx.Graph(G)

            if form == '隣接リスト':
                MST = nx.read_adjlist(MST)
                graph = nx.read_adjlist(importgraph)
                



            pos = nx.arf_layout(graph)
            mai.graphimage(graph,pos)
            
            MSTnx = nx.Graph(MST)
            mai.MSTimage(MSTnx,pos)

            before,after= st.columns(2)
            
            with before:
                st.caption('元のグラフ')
                st.image('graph.png')
            
            with after:
                st.caption('最小全域木')
                st.image('MST.png')
            
            st.write(f"ヒープの操作回数: {operation}")
    


    
