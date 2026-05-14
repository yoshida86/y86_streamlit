import streamlit as st

def change():

    st.header(':red[1.前回からの変更点]',divider="red")

    st.write('前回のフローチャートからわずかに変えた部分があるので紹介。')
    st.write('前回は、最初に受け取るデータを隣接行列としていた。')
    st.write('しかし、そこから辺のリストを作る操作があり、であれば最初から辺のリストを受け取ってしまいたい。')
    st.write('そこで、受け取るデータをエッジリストに変更した。')

    st.image('images/evomst/changeflo.jpg')

    