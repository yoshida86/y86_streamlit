import streamlit as st
from . import LCA
import pickle

def LCAmutation():

    st.header(':red[1.最小共通祖先(LCA)を使った突然変異]',divider="red")

    st.subheader("・最小共通祖先",divider="blue")
    st.write("""根付き木グラフ上の2頂点u,vを取ってくる。  
                u,vの共通する祖先のうち、最も根から遠いものを最小共通祖先という。  
                """)

    with open("materials/_seventh/RootedTree.pkl","rb") as f:
        G = pickle.load(f)

    with open("materials/_seventh/pos.pkl","rb") as f:
        pos = pickle.load(f)

    V1 = st.slider(
    "頂点1を選んでください",
    min_value=1,
    max_value=9,
    value=0
    )

    V2 = st.slider(
    "頂点2を選んでください",
    min_value=1,
    max_value=9,
    value=0
    )

    if V1 == V2:
        LCA.Treeplot(G,pos)
    else:
        LCA.LCAplot(G,pos,V1,V2)

    st.caption("赤:選んだ頂点　　黄:LCA")
    
    
    st.subheader("・LCAを使った突然変異",divider="blue")
    st.write("""
             現在、重みの重い辺を、軽い辺に付け替える突然変異を考えている。  
             最小全域木問題は、元のグラフが完全グラフではないため、好きに辺を加えていいわけではない。  
             木の状態を維持したまま辺を付け替えるのは、計算量のことを考えると工夫が要りそうだった。
             そこで、LCAを使うことを試みる。   
             """)
    
    with st.container(border=True):
        st.write("""
                 1.一個辺を加える。  
                 2.加えた辺の両端の点のLCAを求め、新たに出来たサイクルを発見する。  
                 3.サイクルに含まれる辺を一つ削除し、木に補正する。  
                 """)
    
    st.write("以上の手順を踏むことで、logのオーダーで突然変異を終わらせたい。")

    st.write("以下はそのためのクラス。今後拡張の予定がある(後述)ので、暫定。")

    with open('materials/_seventh/program/RootedTreeNode.py','r',encoding='utf-8') as file:
        code = file.read()
    st.code(code)

    st.caption("これを辞書型で並べて根付き木として木を表現する")
    
    with open('materials/_seventh/program/RootedTree.py','r',encoding='utf-8') as file:
        code = file.read()
    st.code(code)

    st.caption("グラフの探索と同時にinsertで根付き木を完成させ、辺を付け替える時にLCAを見つける。")

    st.write("""今回は、  
             ・加える辺:いくつか持ってきてその中で一番重みの小さいもの  
             ・消す辺:いくつか持ってきてその中で一番重みの大きいもの  
             としていて、この方法だと消す辺の方が加える辺より軽いみたいなことも起こりうる。 
             が、ほとんど起こらないと思って、一旦これで実装した。   
             (一番重い辺を記憶しておくとかも考えたが、辺を消すたびに変わるため重そう。)
             """)