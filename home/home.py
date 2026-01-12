import streamlit as st

def home():
    
    st.title('ホーム画面')

    st.header('ページ紹介')

    st.subheader('・top')
    st.text('ここ')

    #st.subheader('・generategraph')
    #st.text('各種モデルのランダムグラフを生成できます')

    st.subheader('・MSTsearch')
    st.text('最小木探索ができます。')

    st.subheader('・MLconverter')
    st.text('隣接リストを隣接行列に、隣接行列を隣接リストに変換できます\n※入力出力どちらもcsvファイル')

    st.subheader('・materials')
    st.text('発表用資料置き場')

    if st.button('ふうせん'):
        st.balloons()

    