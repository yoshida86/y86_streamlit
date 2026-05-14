import streamlit as st

def BA():

    st.header(':red[2.BAモデル用の探索、突然変異模索]',divider="red")

    st.write("""前回、二つの木を足したグラフに探索を行い、新たに木を作る遺伝的アルゴリズムを作った。  
                今回はBAモデルを中心に、探索方法や突然変異方法を考えてみる。""")

    st.write('BAモデルの特徴といえば、やはりハブの存在なので、ハブをどうこうする方針で考えてみる。')

    st.subheader('突然変異の模索',divider="blue")
    st.write(':red[・ハブから伸びる辺を全部復活させる方法]')
    st.write("""BAグラフから部分木を作るとなると、多様性に貢献しそうなのはやはりハブ。   
                ハブから伸びる辺の組み合わせ次第で、まったく別の木ができそう。  
                そこで、二つのビット列を足し合わせたグラフに対し、  
                :red[ランダムなハブを一つ選び、そこから伸びる辺を全部復活させる]   
                という処理をしてから、BFSやDFSで木にする方法を試してみる。
                """)
    
    st.write("動かしてみる。")

    with st.container(border=True):
        st.write(":red[実験設定]")
        st.write("""・ネットワークモデル:BAモデル  
                    ・頂点数:50  
                    ・BAのパラメータ:4  
                    ・重み:81~100の整数値からランダム  
                    ・探索方法:BFS,DFS,BFSとDFSからランダムの三通り  
                    ・突然変異率:5,10,20,50%の四通り  
                """)
    
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.write("BFS版")
        st.image('images/evo4test/flow_BA_BFS.png')

        st.write("BFS,DFS5割ずつ版")
        st.image('images/evo4test/flow_BA_MIX.png')

    with col2:
        st.write("DFS版")
        st.image('images/evo4test/flow_BA_DFS.png')
    
    st.caption("変異率5%の結果を代表して貼っている。変異率変えても全然変化がなかった")
    
    st.write("以下、ちょっとした考察")
    st.write("""・若干マシになったが、微妙。  
                ・BAモデルにBFSをすると、ハブを探索した時、そこから伸びる辺をほとんど網羅することになるので、解の多様性的には良くないかも。  
                ・DFSはBAだからとかじゃなく、一本道に毛が生えたようなものしか出てこない気がする。こっちも良くないか。""")
    
    st.write("突然変異をいじるのと同等かそれ以上に、探索方法が重要な感じがしたので...")

    st.subheader("・探索方法の模索",divider="blue")

    st.write(':red[・幅制限付きBFS]')
    st.write("""ちょっとした考察で、BFSは、ハブから伸びる辺をほぼ網羅してしまうのが問題と考察した。  
                →今探索している頂点から何点探索するかに制限をかけてしまえば、解が多様になるのでは？  
                """)
    
    st.write(':red[・深さ制限付きDFS]')
    st.write("""「幅制限付きBFS」と、発想はほぼ同じ。  
                探索を開始した点から伸びる探索の回数に制限をかければ、解が多様になるのでは？
                """)
    
    st.write("""幅も深さも、どの程度の制限にするかは、固定にしてもいいし、探索ごとにランダムにしてもよさそう。""")

    

    
