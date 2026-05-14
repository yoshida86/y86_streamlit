import streamlit as st
from ._first import manage as mn1

def materials():

    page = st.sidebar.selectbox('発表資料',['5/15資料'])

    if page == '5/15資料':
        
        mn1.manager()