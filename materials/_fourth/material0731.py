import streamlit as st
import pandas as pd

def material_today():

    st.title("7月24日資料")

    st.header("実験回")
    with st.container(border=True):
        st.write("""
                1.お詫び  
                2.適法度補正色々  
                3.実験  
                3-1.選択方法×適応度補正の比較実験  
                3-2.突然変異方法の比較実験  
                """)

    st.header("1.お詫び")

    st.write("前回までの週報の実験設定の部分、突然変異率を1%と記載していましたが、正しくは10%です。すみません。今回も実験は10%で行っています。")

    st.write("今回、実験結果がだいぶ散らかっていて見づらいかもしれません。")

    st.divider()

    st.subheader("2.適応度補正色々")

    st.write("比較実験で使った適応度補正の紹介。")
    with st.container(border = True):
        st.latex("f_{correct} = f_{best} - (f_{best} - f_{ind}) * bonus ")
    st.write("""
             bonusの値は、  
             - 0.1から0.1ずつ上げる。  
             - 0.1から2倍ずつしていく。(0.1,0.2,0.4,0.8,1)  
             - 0から0.2ずつ上げる。  
             を試してみた。
             """)
    st.caption("「突然変異後極端に適応度が悪くなることを考えると、変異直後はbonus=0にしないと全然選ばれない」ということにもっと早く気付くべきだった...。")



    st.divider()

    st.subheader("3.実験")
    st.subheader("3-1.選択方法×適応度補正の比較実験")
    st.write("適応度は親個体選択と密接に関わりがあるので、選択方法と適応度補正の組み合わせを網羅的に試してみた。")
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
                - 探索法:マルチスタートランダムプリム(開始頂点5つ)  
                - 突然変異:single_intree_mutation  
                - 変異率:10%  
                - トーナメントの選択数:4
                """)

    tab1, tab2, tab3 = st.tabs(["0.1+0.1", "0.1*2", "0+0.2"])

    with tab1:
        subtab1, subtab2, subtab3 = st.tabs(["トーナメント","ランキング","トーナメントランキング"])
        with subtab1:
            st.image('images/material0731/corrects/bestminus/tornament/tornament1.png')
            st.image('images/material0731/corrects/bestminus/tornament/tornament2.png')
            st.image('images/material0731/corrects/bestminus/tornament/tornament3.png')
        with subtab2:
            st.image('images/material0731/corrects/bestminus/ranking/ranking1.png')
            st.image('images/material0731/corrects/bestminus/ranking/ranking2.png')
            st.image('images/material0731/corrects/bestminus/ranking/ranking3.png')
        with subtab3:
            st.image('images/material0731/corrects/bestminus/toran/toran1.png')
            st.image('images/material0731/corrects/bestminus/toran/toran2.png')
            st.image('images/material0731/corrects/bestminus/toran/toran3.png')


    with tab2:
        subtab1, subtab2, subtab3 = st.tabs(["トーナメント","ランキング","トーナメントランキング"])
        with subtab1:
            st.image('images/material0731/corrects/baibai/tornament/tornament1.png')
            st.image('images/material0731/corrects/baibai/tornament/tornament2.png')
            st.image('images/material0731/corrects/baibai/tornament/tornament3.png')
        with subtab2:
            st.image('images/material0731/corrects/baibai/ranking/ranking1.png')
            st.image('images/material0731/corrects/baibai/ranking/ranking2.png')
            st.image('images/material0731/corrects/baibai/ranking/ranking3.png')
        with subtab3:
            st.image('images/material0731/corrects/baibai/toran/toran1.png')
            st.image('images/material0731/corrects/baibai/toran/toran2.png')
            st.image('images/material0731/corrects/baibai/toran/toran3.png')

    with tab3:
        subtab1, subtab2, subtab3 = st.tabs(["トーナメント","ランキング","トーナメントランキング"])
        with subtab1:
            st.image('images/material0731/corrects/bestminusfromzero/tornament/tornament1.png')
            st.image('images/material0731/corrects/bestminusfromzero/tornament/tornament2.png')
            st.image('images/material0731/corrects/bestminusfromzero/tornament/tornament3.png')
        with subtab2:
            st.image('images/material0731/corrects/bestminusfromzero/ranking/ranking1.png')
            st.image('images/material0731/corrects/bestminusfromzero/ranking/ranking2.png')
            st.image('images/material0731/corrects/bestminusfromzero/ranking/ranking3.png')
        with subtab3:
            st.image('images/material0731/corrects/bestminusfromzero/toran/toran1.png')
            st.image('images/material0731/corrects/bestminusfromzero/toran/toran2.png')
            st.image('images/material0731/corrects/bestminusfromzero/toran/toran3.png')

    st.write("""
             - 0.1から0.1ずつ足すやつは、補正がかかった個体数が20(全個体)で張り付いている。選びすぎ。  
             - 2章でcaptionを使って書いた通り、0から始めたやつが強い。 
             - その中でも、トーナメントとランキングのハイブリッドは、個体数が上にも下にも張り付いたり偏ったりしてなくていい感じな印象。
             ・トーナメントの選択個数を変えて実験してみる？ 
             - 元々、トーナメント選択だと変異個体が選ばれないというきっかけで始めた補正だった。今回はトーナメント選択が変異個体を選びすぎるという逆転現象が起きている。  
               どのみちトーナメントの性能はあまり良くないが、同じ選択方法でこうも結果が変わるのは面白いと思った。   
             """)

    st.subheader("3-2.突然変異の比較")
    st.write("""
                突然変異がまともに機能した記念、改めて比較実験。  
                上記実験で一番いい感じだった、0+0.2とトーナメントランキングの組み合わせで固定し、突然変異三種を比較。
                """)

    with st.container(border=True):
        st.write("""
                :red[実験設定]  
                - グラフモデル:エルデシュレーニー  
                - 頂点数:200  
                - 辺数:1000  
                - ターミナル数:20  
                - 個体数:20  
                - 世代数:5000  
                - 探索法:マルチスタートランダムプリム(開始頂点5つ)  
                - 突然変異:single_intree,single_outtree,double_intree  
                - 変異率:10%  
                - トーナメントの選択数:4
                """)

    tab1, tab2, tab3 = st.tabs(["single_in", "single_out", "double_in"])

    with tab1:
        st.image('images/material0731/mutations/singlein/singlein1.png')
        st.image('images/material0731/mutations/singlein/singlein2.png')
        st.image('images/material0731/mutations/singlein/singlein3.png')

    with tab2:
        st.image('images/material0731/mutations/singleout/singleout1.png')
        st.image('images/material0731/mutations/singleout/singleout2.png')
        st.image('images/material0731/mutations/singleout/singleout3.png')

    with tab3:
        st.image('images/material0731/mutations/doublein/doublein1.png')
        st.image('images/material0731/mutations/doublein/doublein2.png')
        st.image('images/material0731/mutations/doublein/doublein3.png')

    st.write("""
             - どれも同じくらい機能してそう。やってることの本質は同じだから大差なし？  
             - 何か差が出るような比較方法が欲しいところ。
            """)

    st.subheader("次回以降予定")
    st.write("・補正方法もうちょいなんかありそう。")
    st.write("・突然変異比較方法募集中。")
    st.write("・強い摂動。元のグラフ探索するやつと、補グラフ探索するやつ比較。")
    st.write("・最良個体をそのまま残すやつ実装。")
    st.write("・トーナメントランキング選択の個体選択数を変えて実験してみる。")