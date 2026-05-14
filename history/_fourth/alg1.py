import streamlit as st

def alg():

    st.header(':red[2.アルゴリズム動かしてみた前編]',divider="red")

    st.write('前編では、進化計算についての本を入手する前に考えた、いわばプロトタイプのようなアルゴリズムを動かしている。')

    st.subheader('・手順')
    with st.container(border=True):
        st.write("""1.連結グラフのエッジリストを用意  
                    2.エッジリストに対して、個体数n回だけbfsを行い、個体群をつくる。　　
                    (個体は辺の有無を表すベクトルで表現)  
                    3.個体群からランダムに二つ選び、ベクトルの和を取り、グラフを生成。  
                    4.生成したグラフに対し、bfsを行う。  
                    5.bfs後のグラフと、個体群中で評価が最悪の木を比較、bfs後のグラフの方が評価が良いなら、最悪の木と入れ替える形で個体群に加える。  
                    6.3から6を、世代数分繰り返す。""")

        st.caption("木の評価は、辺の重みの総和で行っている。")

    st.subheader('動作確認')
    st.divider()
    st.write("""とりあえず、小さめのグラフを生成して動作確認。  
                確実に連結グラフになってくれるBAモデルで検証する。""")
    
    st.image('images/evo1test/origin_BA.png')
    st.caption('こんなグラフ')

    col1, col2 = st.columns(2)

    with col1:
        st.write("最適解")
        st.image('images/evo1test/exact_BA.png')

    with col2:
        st.write("探索した解")
        st.image('images/evo1test/best_BA.png')

    
    st.image('images/evo1test/flow_BA.png')
    st.caption("最良スコアの推移はこんな感じ")
    st.write("それっぽい結果を得られたので、ちゃんと動いているとして話を進める。")
    
    st.subheader(":red[実験]")
    st.divider()
    st.write("""せっかく作ったので、少し実験してみる。今回は、  
                ・使うモデル:エルデシュレーニー、ワッツストロガッツ、BA  
                ・頂点数:50  
                ・辺の数:約300  
                でグラフを生成し、  
                ・個体数50  
                ・世代数5000  
                でそれぞれにアルゴリズムを動かす。""")
    
    st.write(":red[結果]")
    
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/evo1/flow_erd.png')
        st.image('images/evo1/flow_BA.png')

    with col2:
        st.image('images/evo1/flow_WS.png')

    st.write(":red[考察]")
    st.write("・パッと見、モデルごとに大きな差は見られなかった。あまりモデルによる影響を受けない？")
    st.write("・最後の方の世代は、局所解に陥っていると思われる。")


                