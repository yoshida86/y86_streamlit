import streamlit as st
import networkx as nx
import numpy as np
import pandas as pd
from . import change as ch

def Gilbert():
    
    n = st.slider('頂点数',1,100000)
    
    p = st.slider('辺の生成確率',0.00,1.00)

    datatype = st.selectbox('取得するデータ型',['隣接行列','隣接リスト','networkXのグラフ原型'])

    if st.button('生成'):
        
        Gx = nx.gnp_random_graph(n,p)

        if datatype == '隣接行列':
            
            matrix = ch.XtoN(Gx)
            

            if st.download_button(label = 'download csv',
                                  data = bin,
                                  file_name = 'graph.bin'):
                a=a




        

        