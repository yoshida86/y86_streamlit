import streamlit as st
from . import making
from . import randp

def manager():
    
    chapter = st.sidebar.selectbox("章選択",['目次','作ったもの','ランダムプリム'])
    
    st.title('12/12資料')
    st.divider()

    if chapter == '目次':
        st.write('BAモデルに色々アプローチしてみる回')

        st.divider()
        
        leftspace,maintext,rightspace = st.columns([2,3,2])

        with maintext:
            with st.expander('目次',expanded = True):
                st.write('1.作ったもの')
                st.write('2.ランダムプリム実験')

    if chapter == '作ったもの':
        
        making.making()

    if chapter == 'ランダムプリム':

        randp.randp()