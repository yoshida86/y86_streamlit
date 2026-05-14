import streamlit as st

def primexp():

    st.header(':red[1-2.プリム法]')

    st.text('最小全域木探索アルゴリズムの一つ。')
        
    with st.container(border=True):
        st.subheader('手順')
        st.text('(0.全ての頂点の木までの距離を、∞で初期化する。)')
        st.text('1. 作成中の木との距離が最も近い点を木に加える。\n  (最初はどの点でも可)')
        st.text('2. 加えた点と辺で結ばれた点の、木までの距離を更新する。')
        st.text('3. 1と2を、全ての点を木に加えるまで繰り返す。')

    st.write('例:')
    st.image('images/prkrexample/prim.png')
    st.caption('木に加えた頂点を緑、辺をオレンジに塗っている')

        
        
