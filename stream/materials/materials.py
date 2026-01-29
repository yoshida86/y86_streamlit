import streamlit as st
from ._first import manage as mn1
from ._second import manage as mn2
from ._third import manage as mn3
from ._fourth import manage as mn4
from ._fifth import manage as mn5
from ._sixth import manage as mn6

def materials():

    page = st.sidebar.selectbox('発表資料',['12/12資料','11/14資料','10/24資料','7/18資料','6/27資料','6/6資料'])

    if page == '6/6資料':
        
        mn1.manager()

    if page == '6/27資料':
        
        mn2.manager()

    if page == '7/18資料':

        mn3.manager()

    if page == '10/24資料':

        mn4.manager()

    if page == '11/14資料':

        mn5.manager()

    if page == '12/12資料':

        mn6.manager()