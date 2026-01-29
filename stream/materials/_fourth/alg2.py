import streamlit as st

def alg():

    st.header(':red[2.アルゴリズム動かしてみた後編]',divider="red")

    st.write('後編では、本入手後、改めて構想を練り直したアルゴリズムを動かしている。')

    st.subheader('・手順')
    with st.container(border=True):
        st.write("""1.連結グラフのエッジリストを用意  
                    2.エッジリストに対して、個体数n回だけbfsを行い、個体群をつくる(個体は辺の有無を表すベクトルで表現)  
                    3.個体群からルーレット選択を使い二つ選び、ベクトルの和を取り、グラフを生成。  
                    4.生成したグラフに対し、bfsを行う。  
                    5.bfsしたグラフを次世代の個体群に加える。  
                    6.3から6を、個体数分繰り返し、次世代の個体群を作る。  
                    7.指定した世代数に達していなければ、3に戻り、次の世代を作る。達していれば終了。""")
        
    st.subheader("注意点")
    st.write("""(1)プロトタイプとの違いとして、  
                ・一つの個体群に対し入れ替えを行っていたのを、一斉に世代交代するよう変更  
                ・良い個体ほど親個体に選ばれやすくなる選択方法に変更  
                があげられる。  
                (2)突然変異に関しては、まだ実装できていない。（今後の目標）  
                (3)親個体の選択には、トーナメント選択を用いた。  
                トーナメント選択は、個体群から指定した個数だけランダムにとってきて、その中で最も良い個体を親とする方法である。
             """)
    
    
        
    st.subheader("動作確認")
    st.write("先ほどと同様、小さいグラフで動作確認")

    st.image('images/evo2test/origin_BA.png')
    st.caption('こんなグラフ')

    col1, col2 = st.columns(2)

    with col1:
        st.write("最適解")
        st.image('images/evo2test/exact_BA.png')

    with col2:
        st.write("探索した解")
        st.image('images/evo2test/best_BA.png')

    st.image('images/evo2test/flow_BA.png')
    st.caption("最良スコアの推移はこんな感じ")

    st.write("多分ちゃんと動いているとして話を進める。")

    st.subheader(":red[実験]")
    st.divider()
    st.write("""こちらも実験してみる。  
                ・使うモデル:エルデシュレーニー、ワッツストロガッツ、BA  
                ・頂点数:50  
                ・辺の数:約300  
                でグラフを生成し、  
                ・個体数50  
                ・世代数500  
                でそれぞれにアルゴリズムを動かす。""")
    
    st.write(":red[結果]")
    
    col1, col2 = st.columns(2)

    with col1:
        st.image('images/evo2/flow_erd.png')
        st.image('images/evo2/flow_BA.png')

    with col2:
        st.image('images/evo2/flow_WS.png')

    st.write(":red[考察]")
    st.write("""・爆速で局所解に突っ込んでいる。  
                ・突然変異をしていないことが一番の原因だとは思う。  
                ・選択方法とかも原因の一端を担っていそう。""")
    
    st.subheader("今後やること")
    st.write("""・突然変異実装、実験  
                ・dfs版とか、bfsとdfs混ぜた版とかの実装、実験  
                ・ルーレット選択とかをどうしたら使えるか考える。思いつき次第実装、実験  
                などなど。結構いじれる場所多そう。
             """)