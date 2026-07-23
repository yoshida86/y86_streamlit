import streamlit as st
import pandas as pd

def material_today():

    st.title("7月24日週報")

    st.header("突然変異遺伝子残す模索")
    with st.container(border=True):
        st.write("""
                1.アイデア紹介  
                1-1.突然変異後の適応度補正  
                1-2.交叉に突然変異を組み込む  
                1-3.選択方法変更(次回以降実験)  
                2.実験
                """)

    st.header("1.アイデア紹介")

    st.subheader("1-1.突然変異後の適応度補正")
    st.write("""
            突然変異が起きた個体が選ばれやすくなるよう、一時的に適応度に補正をかける。  
            今回は適応度に倍率をかけている。  
            突然変異直後に0.1倍、その後一世代経過ごとに0.2,0.3,...と徐々に補正を元に戻していく。
            """)
    st.caption("10世代の間補正がかかり続けるのはやりすぎ？補正がかかった個体ばかりになるかも？改良の余地あり")

    st.write("・実装")
    with open('weekly/_second/code/mutationbonus.py','r',encoding='utf-8') as file:
        code = file.read()
    st.code(code)

    st.divider()

    st.subheader("1-2.交叉に突然変異を組み込む")
    st.write("""
            これまで、  
            「親1、親2を交叉して子を作る→子を突然変異する」  
            だったのを、  
            「親1を突然変異させる→親1、親2を交叉して子を作る」  
            に変える。  
            これにより、無理やり次世代に変異した遺伝子を残す。
            """)

    st.divider()

    st.subheader("1-3.選択方法変更(次回以降実験)")
    st.write("""
                トーナメント選択に問題あり？と考えたので、変えてみたい。  
                - トーナメント選択
                - ランキング選択  
                - 上記二つのハイブリッド
                - (良い比重の入れ方が見つかれば)ルーレット選択  
                辺りを比較実験したい。
                """)
    st.caption("今回の実験では、ランキング選択を採用している。")

    
    st.divider()

    st.subheader("2.実験")
    st.write("1-1と1-2で紹介したアイデアを比較する。両方取り入れたものもやってみる。")
    st.write("同じ条件でやったものを三つずつ載せている。")
    with st.container(border=True):
        st.write("""
                :red[実験設定]  
                - グラフモデル:エルデシュレーニー  
                - 頂点数:200  
                - 辺数:1000 
                - ターミナル数:20  
                - 個体数:20  
                - 世代数:5000  
                - 選択法:ランキング選択 
                - 探索法:マルチスタートランダムプリム(開始頂点5つ)  
                - 突然変異:single_intree_mutation
                - 変異率:1%
                """)

    tab1, tab2, tab3 = st.tabs(["1-1", "1-2", "両方"])

    with tab1:
        st.image('images/weekly2/mutation_bonus.png')
        st.image('images/weekly2/mutation_bonus2.png')
        st.image('images/weekly2/mutation_bonus3.png')


    with tab2:
        st.image('images/weekly2/premutation.png')
        st.image('images/weekly2/premutation2.png')
        st.image('images/weekly2/premutation3.png')

    with tab3:
        st.image('images/weekly2/premutation_bonus.png')
        st.image('images/weekly2/premutation_bonus2.png')
        st.image('images/weekly2/premutation_bonus3.png')

    st.write("""
             - どの方法も、局所最適から抜けられている印象。 
             - 「1-1」だけworst(赤い線)が濃ゆい。その上で世代内平均が極端に悪くなることも無さそうなので、「1-1」が一番いい感じに変異できてそう。 
             - 一度も局所から動かなかった「1-2」と「両方」の2枚目も、なんとなく形が違う気がする。  
             -「両方」の方は、変異の遺伝子が残りすぎてる？両方採用するのはやりすぎかもしれない。
             """)

    st.subheader("次回以降予定")
    st.write("・選択方法の比較")
    st.write("・突然変異後補正の改良")
    st.write("・ちゃんと突然変異が機能したので、強い摂動などなど導入してみてもいい？")