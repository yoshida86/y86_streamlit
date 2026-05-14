import streamlit as st
from . import change
from . import flo
from . import prog

def manager():
    
    chapter = st.sidebar.selectbox("章選択",['目次','前回からの変更点','フローチャート上の各操作の計算量','進捗報告'])
    
    st.title('7/18資料')
    st.divider()

    if chapter == '目次':
        st.write('遺伝的アルゴリズムでMSTを近似したい話の進捗報告回')

        st.divider()
        
        leftspace,maintext,rightspace = st.columns([2,3,2])

        with maintext:
            with st.expander('目次',expanded = True):
                st.write('1.前回からの変更点')
                st.write('2.フローチャート上の各操作の計算量')
                st.write('3.進捗報告')

    if chapter == '前回からの変更点':
        
        change.change()

    if chapter == 'フローチャート上の各操作の計算量':

        flo.flo()

    if chapter == '進捗報告':

        prog.prog()