import streamlit as st
import pandas as pd

def material_today():

    st.title("7月17日週報")

    st.write("BAではないグラフモデルにGAを使ってみた。")
    st.write("バラバシアルバート、ワッツストロガッツ、エルデシュレーニーの比較。")
    with st.container(border=True):
        st.write("""
                :red[実験設定]    
                - 頂点数:200  
                - 辺数:1000 
                - ターミナル数:20  
                - 個体数:50  
                - 打ち切る時間:5分(300秒)  
                - 選択法:トーナメント選択(k=3)  
                - 探索法:マルチスタートランダムプリム(開始頂点5つ)  
                - 突然変異:single_intree_mutation
                - 変異率:1%
                """)

    tab1, tab2, tab3 = st.tabs(["BA", "WS", "ER"])

    with tab1:
        st.image('images/weekly1/BAlog.png')

        with open('weekly/_first/code/BAresult.txt','r',encoding='utf-8') as file:
            code = file.read()
        st.code(code)

    with tab2:
        st.image('images/weekly1/WSlog.png')

        with open('weekly/_first/code/WSresult.txt','r',encoding='utf-8') as file:
            code = file.read()
        st.code(code)

    with tab3:
        st.image('images/weekly1/ERlog.png')

        with open('weekly/_first/code/ERresult.txt','r',encoding='utf-8') as file:
            code = file.read()
        st.code(code)

    st.write("""
             - BA以外でも変異が役に立ってなさそうなので、変異した遺伝子を残す手段の模索をしていく予定。
             - BAだけ明確に、シュタイナー木の頂点数が少ない。
             """)
    
    st.write("上の実験で使ったグラフ三種に、整数計画を用いてみた。制限時間1時間で実行した結果となっている。")

    tab1, tab2, tab3 = st.tabs(["BA", "WS", "ER"])

    with tab1:
        with open('weekly/_first/code/BAresult_pulp.txt','r',encoding='utf-8') as file:
            code = file.read()
        st.code(code)

    with tab2:
        with open('weekly/_first/code/WSresult_pulp.txt','r',encoding='utf-8') as file:
            code = file.read()
        st.code(code)

    with tab3:
        with open('weekly/_first/code/ERresult_pulp.txt','r',encoding='utf-8') as file:
            code = file.read()
        st.code(code)

    st.write("""
             - 見立て通り、BAだけ解の形がシンプルになってそうな結果が出ている。  
             - エルデシュレーニーのような、よりランダムに近いモデルでやった方がよさそう？
             """)