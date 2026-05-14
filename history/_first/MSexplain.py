import streamlit as st

def MSexplain():

    st.header('MSTsearch')
    st.write('隣接行列のcsvを投げることで、最小全域木の探索ができるものを作ってみました。')
    st.write('matplotlibで表示できる程度のサイズであれば、元のグラフとそのグラフの全域最小木を表示するようにしてあります')
    st.write('現状、隣接リストのcsvや、クラスカル法での探索が未実装のため、今後拡張予定。')
    st.caption('...重み付きグラフの隣接リストってどう実装するのがいいんでしょう?')