import streamlit as st

def prog():

    st.header(':red[進捗報告]',divider='red')

    st.write("""
             ・エッジリストと隣接リストもどきを使ったbfs
             """)

    with open('materials/_third/program/gsearch.py','r',encoding='utf-8') as file:
        code1 = file.read()
    st.code(code1)

    st.caption("探索するグラフのベクトル、エッジリスト、隣接リストもどき、探索を開始する頂点を受け取る。探索後のグラフのベクトルを配列で返す。")

    st.divider()

    st.write("""
             ・評価の計算と、全域木二つを足すやつ
             """)
    
    with open('materials/_third/program/score.py','r',encoding='utf-8') as file:
        code2 = file.read()
    st.code(code2)
    st.caption("グラフのベクトルで1が立っている辺の重みだけを足していく")

    

    with open('materials/_third/program/vectormerge.py','r',encoding='utf-8') as file:
        code3 = file.read()
    st.code(code3)
    st.caption("ベクトルの各要素に、if文を使ってorの演算をしている")

    st.divider()

    st.subheader(":red[今後の予定]",divider="red")
    st.write("""
             ・最小全域木の遺伝的アルゴリズムを動くところまで持ってく。\n
             その後、いろいろマイナーチェンジして比較する。\n
             ・streamlitをdeployしてみたい。\n
             ・重みなしのエッジリストに重みをつけるプログラムを作りたい。
             """)
