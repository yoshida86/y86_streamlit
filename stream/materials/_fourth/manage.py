import streamlit as st
from . import evolution
from . import alg1
from . import alg2

def manager():
    
    chapter = st.sidebar.selectbox("章選択",['目次','進化計算アルゴリズム','アルゴリズム動かしてみた前編','アルゴリズム動かしてみた後編'])
    
    st.title('7/18資料')
    st.divider()

    if chapter == '目次':
        st.write('MSTに近い木を求めるやつ試運転の回')

        st.divider()
        
        leftspace,maintext,rightspace = st.columns([2,3,2])

        with maintext:
            with st.expander('目次',expanded = True):
                st.write('1.進化計算アルゴリズム')
                st.write('2.アルゴリズム動かしてみた前編')
                st.write('3.アルゴリズム動かしてみた後編')

    if chapter == '進化計算アルゴリズム':
        
        evolution.evolution()

    if chapter == 'アルゴリズム動かしてみた前編':

        alg1.alg()

    if chapter == 'アルゴリズム動かしてみた後編':

        alg2.alg()