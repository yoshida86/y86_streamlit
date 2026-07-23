import streamlit as st
from ._first import manager as mt1
from ._second import manager as mt2

def weekly():

    page = st.sidebar.selectbox('発表資料',['7/24週報','7/17週報'])

    if page == '7/17週報':
        
        mt1.material_today()

    if page == '7/24週報':

        mt2.material_today()