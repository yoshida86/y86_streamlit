import streamlit as st
import networkx as nx
from . import generateGil as gil
#from . import generateWat as wat
#from . import generateAlb as alb
#from . import generateErd as erd

def generategraph():
	
    st.title('ランダムグラフ生成')
    
    st.text('生成したグラフは、csvファイルでダウンロードできるようにする予定')

    st.text('辺数は、連結性の確保のため若干増える場合あり')
    
    st.divider()
    
    model = st.selectbox(
        'randomgraph model',
        ['Gilbert',
        'Watts and Strogatz',
        'Barabasi Albert',
        'erdos renyi']
    )

    

    if model == 'Gilbert':
        
        gil.Gilbert()

