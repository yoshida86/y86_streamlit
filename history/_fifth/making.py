import streamlit as st

def making():

    st.header(':red[1.作ったもの]',divider="red")

    st.subheader("・ルーレット選択")
    with open('materials/_fifth/program/roulette.py','r',encoding='utf-8') as file:
        code1 = file.read()
    st.code(code1)
    st.caption("親を二つ選んでいるだけで、前後半でやってることは同じ")

    st.subheader("・DFS")
    with open('materials/_fifth/program/dfs.py','r',encoding='utf-8') as file:
        code2 = file.read()
    st.code(code2)

 