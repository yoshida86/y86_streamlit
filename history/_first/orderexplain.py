import streamlit as st

def orderexplain():
    st.header(':red[1-4.プリムとクラスカルの計算量]')
    st.write('以下、頂点数をV、辺数をEとする。')
    st.subheader(':orange[・プリム法の計算量]')
    st.markdown('ヒープを使って実装した場合を考える。')
    st.markdown('プリム法の操作は、大きく分けて、')
    st.markdown('(1)ヒープへの挿入と最小値取り出し')
    st.markdown('(2)ヒープ内の要素の値(頂点の木までの距離)の更新')
    st.markdown('の二種類。')
    st.markdown('・1について、必ず全ての頂点がヒープへの挿入と取り出しを一度ずつ経験するため、')
    st.latex('O(V \log V)')
    st.markdown('・2について、一つの辺によって起こる更新は一度きりで、更新回数が辺の数で抑えられるので、')
    st.latex('O(E \log V)')
    st.markdown('以上から、ヒープを用いたプリム法のオーダーは、')
    st.latex('O(V \log V + E \log V) = O(E \log V)')
    with st.container(border=True):
        st.markdown('フィボナッチヒープというデータ構造を使えば、より高速にできることが知られている。')
        st.markdown('フィボナッチヒープについては後述。')

    st.subheader(':orange[・クラスカル法の計算量]')
    st.markdown('一般に使えるソート方法(O(ElogE)のもの)を使用した場合を考える')
    st.markdown('クラスカル法の操作は、大きく分けて、')
    st.markdown('(1)全ての辺を重み順にソート')
    st.markdown('(2)頂点がどの部分木に属するかの管理')
    st.markdown('の二種類。')
    st.markdown('(1)について、単純にソートなので、')
    st.latex('O(E \log E)')
    st.markdown('(2)について、木構造を使って部分木の集合を表現することで、')
    st.markdown('頂点がどの部分木に属するかの探索をO(logV)で行うことができる。')
    st.markdown('その操作を辺の数だけ行うので、')
    st.latex('O(E \log V)')
    st.markdown('以上から、クラスカル法のオーダーは、')
    st.latex('O(E \log E + E \log V) = O(E \log E)')
    

