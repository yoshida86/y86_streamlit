import streamlit as st
from . import LCAmutation
from . import mutation
from . import mutation2

def manager():
    
    chapter = st.sidebar.selectbox("章選択",['目次','LCAを使った突然変異','突然変異の拡張','突然変異の拡張2'])
    
    st.title('1/30資料')
    st.divider()

    if chapter == '目次':
        st.write('LCAを使った突然変異とその拡張')

        st.divider()
        
        leftspace,maintext,rightspace = st.columns([2,3,2])

        with maintext:
            with st.expander('目次',expanded = True):
                st.write('1.LCAを使った突然変異')
                st.write('2.突然変異の拡張')
                st.write('3.突然変異の拡張2')

    if chapter == 'LCAを使った突然変異':
        
        LCAmutation.LCAmutation()

    if chapter == '突然変異の拡張':

        mutation.mutation()

    if chapter == '突然変異の拡張2':

        mutation2.mutation()