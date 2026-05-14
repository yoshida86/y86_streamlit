import streamlit as st
from . import streamexp as stex
from . import LCAexam 
def manager():
    
    chapter = st.sidebar.selectbox("章選択",['streamlit','LCAexam'])
    
    st.title('5/15資料')
    st.divider()

    if chapter == 'streamlit':

        stex.streamexp()

    if chapter == 'LCAexam':

        LCAexam.LCAexam()