import streamlit as st
from . import making
from . import BA
from . import idea

def manager():
    
    chapter = st.sidebar.selectbox("章選択",['目次','作ったもの','BAモデル用の探索、突然変異模索','未実装のアイデアまとめ'])
    
    st.title('11/14資料')
    st.divider()

    if chapter == '目次':
        st.write('BAモデルに色々アプローチしてみる回')

        st.divider()
        
        leftspace,maintext,rightspace = st.columns([2,3,2])

        with maintext:
            with st.expander('目次',expanded = True):
                st.write('1.作ったもの')
                st.write('2.BAモデル用の探索、突然変異模索')
                st.write('3.未実装のアイデアまとめ')

    if chapter == '作ったもの':
        
        making.making()

    if chapter == 'BAモデル用の探索、突然変異模索':

        BA.BA()

    if chapter == '未実装のアイデアまとめ':

        idea.idea()