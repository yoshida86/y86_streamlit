import streamlit as st
from . import mstexplain as mstexp
from. import primexplain as prexp
from . import krusexplain as krexp
from . import MLexplain as ML
from . import MSexplain as MS
from . import orderexplain as order
from . import fiboexplain as fibo
def manager():
    
    chapter = st.sidebar.selectbox("章選択",['目次','1.最小全域木探索','1-5.フィボナッチヒープ','2.streamlit成果紹介'])
    
    st.title('6/6資料')
    st.divider()

    if chapter == '目次':
        st.write('streamlit触ってみたよ!の回です。')
        st.write('色々試してます。')

        st.divider()
        
        leftspace,maintext,rightspace = st.columns([2,3,2])

        with maintext:
            with st.expander('目次',expanded = True):
                st.write(':red[1.最小全域木探索]')
                st.write('1-1.最小全域木')
                st.write('1-2.プリム法')
                st.write('1-3.クラスカル法')
                st.write('1-4.プリムとクラスカルの計算量')
                st.write('1-5.フィボナッチヒープ')
                st.write(':red[2.streamlit成果紹介]')
                st.write('2-1.MSTsearch')
                st.write('2-2.MLconverter')

        
    ##1章
    if chapter == '1.最小全域木探索':
        mstexp.mstexp()
        st.divider()
        prexp.primexp()
        st.divider()
        krexp.krusexplain()
        st.divider()
        order.orderexplain()
        st.divider()

    if chapter == '1-5.フィボナッチヒープ':   
        fibo.fiboexplain()

    ##2章
    if chapter == '2.streamlit成果紹介':

        st.subheader('2.streamlit成果紹介')
        MS.MSexplain()
        st.divider()
        ML.MLexplain()
