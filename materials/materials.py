import streamlit as st
from ._first import manage as mn1
from ._second import material0612 as mt0612
from ._third import material0710 as mt0710
from ._fourth import material0731 as mt0731
from ._fifth import material1016 as mt1016

def materials():

    page = st.sidebar.selectbox('発表資料',['10/16資料','7/31資料','7/10資料','6/12資料','5/15資料'])

    if page == '5/15資料':
        
        mn1.manager()

    if page == '6/12資料':

        mt0612.material_today()
    
    if page == '7/10資料':

        mt0710.material_today()

    if page == '7/31資料':

        mt0731.material_today()

    if page == '10/16資料':

        mt1016.material_today()