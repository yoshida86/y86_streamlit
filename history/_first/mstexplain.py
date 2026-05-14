import streamlit as st
import networkx as nx
import matplotlib as plt
import numpy as np

def mstexp():

    
    st.header(':red[1-1.最小全域木]')
    st.write('以下、グラフは重み付きの無向グラフとする。')
    st.subheader('全域木')
    st.write('元のグラフのすべての頂点を含み、かつサイクルをもたないような部分グラフを、:red[全域木]という。')
    st.write('一般にグラフが与えられたとき、全域木は一意に定まらず、複数存在する。')
    st.subheader('最小全域木')
    st.write('あるグラフの全域木のうち、辺の重みの総和が最小な全域木を:red[最小全域木]という。')
        