import streamlit as st
from . import rintro as ri
from . import evoexp as ev

def manager():
    
    chapter = st.sidebar.selectbox("章選択",['目次','R言語','進化計算でMSTを近似する'])
    
    st.title('6/27資料')
    st.divider()

    if chapter == '目次':
        st.write('R言語の簡単な紹介と、進化計算を使ってMSTを近似したい話です。')

        st.divider()
        
        leftspace,maintext,rightspace = st.columns([2,3,2])

        with maintext:
            with st.expander('目次',expanded = True):
                st.write('1.R言語')
                st.write('2.進化計算でMSTを近似する')

    if chapter == 'R言語':
        
        ri.rintro()

    if chapter == '進化計算でMSTを近似する':

        ev.evoexp()