import streamlit as st

def krusexplain():

    st.header(':red[1-3.クラスカル法]')
    
    st.text('最小全域木探索アルゴリズムの一つ。')
        
    with st.container(border=True):
        st.subheader('手順')
        st.text('1.全ての辺を距離昇順でソートする')
        st.text('2.ソート列の先頭の辺を取り出し、それを加えることでサイクルができないなら、\n    両端の点と共に木に加える')
        st.text('3.2を、全ての頂点が木に含まれるまで繰り返す')

    st.write('例:')
    st.image('images/prkrexample/kruskal.png')
    
