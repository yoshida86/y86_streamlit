import streamlit as st

def streamexp():

    st.title(":red[streamlit]")
    
    st.subheader("webアプリを作れるpythonのライブラリ")

    st.divider()

    st.text("他のpythonのライブラリ同様、インストールして使う。")

    st.code("pip install streamlit")

    st.text("下を入力すると、サンプルを起動できる。")

    st.code("streamlit hello")

    st.text("")

    st.title("タイトル")
    st.header("ヘッダー")
    st.subheader("サブヘッダー")
    st.text("テキスト")
    st.caption("キャプション")
    
    fusen = st.button("ボタン")

    st.title(":rainbow[rainbow]")

    if fusen == True: 
        st.balloons()

    st.text("重い実験はstreamlit側が悲鳴を上げるためできないが、小さな例で試したりするときは、実験の過程や結果を視覚的に表示できて便利だったり。")