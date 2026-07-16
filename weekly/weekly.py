import streamlit as st
from ._first import manager as mt1

def weekly():

    page = st.sidebar.selectbox('発表資料',['7/17週報'])

    if page == '7/17週報':
        
        mt1.material_today()