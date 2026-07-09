import streamlit as st
import pandas as pd

def material_today():

    st.title("7月10日資料")

    with st.sidebar:

        page = st.radio("目次",["1.不要な枝の剪定","2.突然変異","3.実験","4.シュタイナー木用線形計画","5.アイデア,今後"])

    if page == "1.不要な枝の剪定":
        prune()

    if page == "2.突然変異":
        mutation()

    if page == "3.実験":
        experiment()

    if page == "4.シュタイナー木用線形計画":
        Steiner_Linear()

    if page == "5.アイデア,今後":

        idea()

def prune():

    st.header(":red[1.不要な枝の剪定]")
    st.divider()

    st.subheader("1-1.不要な枝")
    st.write("""
            シュタイナー木には、明らかに不要な枝が含まれていることがある。  
            このような枝を削除することで、より重みの和が小さいシュタイナー木を見つけることができる。 
            """)
    
    st.write(":blue[例]:以下のようなグラフがあったとする。青い頂点がターミナルとする。")
    st.write("""
             この時、赤で示した頂点と辺を削除しても、木はシュタイナー木のままである。  
             つまり、赤い頂点と辺は不要といえる。
             """)

    st.image('images/steinerexample/prune.png')




    st.divider()
    st.subheader("1-2.不要な枝を剪定するアルゴリズム")
    st.write("""
             実際に不要な枝を消すアルゴリズムを考える。  
             以下のような手順で操作をすることで、不要な枝を剪定することができる。
            """)

    with st.container(border=True):
        st.write("""
                 :red[手順]  
                 :red[1.]シュタイナー木中の、次数が1かつターミナルでない頂点を全てキューQに加える。  
                 :red[2.]Qが空になるまで、以下の操作a,b,cを繰り返す。  
                 -a.Qから頂点vを取り出す。  
                 -b.頂点vと、つながっている辺を削除する。  
                 -c.操作bによって、新たに次数1かつターミナルでない頂点が生まれたら、それをQへ加える。  
                 """)

    st.write("次数1かつターミナルでない点を消しても、連結なこと、木なこと、ターミナルが含まれることのどれにも影響しないため、この方法でシュタイナー木であることが崩れることはない。")  

def mutation():

    st.header(":red[2.突然変異]")
    st.divider()
    st.subheader("2-1.突然変異")
    st.write("""
             今回、突然変異を四通り実装してみた。一つずつ紹介していく。  
             どの突然変異も、基本的な考え方は、  
             1.シュタイナー木上の二点u,vを端点にもつ、シュタイナー木以外の頂点と辺で作ったパスPを作る。  
             2.シュタイナー木上のuvパスと、pを合わせるとサイクルになるため、uvパスから一個辺を削除。  
             となっている。
             """)

    st.divider()
    st.subheader("2-2.singlenode intree mutation")

    with st.container(border=True):
        st.write("""
                 :red[手順]  
                 :red[1.]シュタイナー木から頂点uを一つ選ぶ。  
                 :red[2.]uを始点として、シュタイナー木に含まれない頂点と辺を使い自己回避ランダムウォークをする。   
                 :red[3.]シュタイナー木とぶつかったら、ぶつかった点をvとしランダムウォーク終了。   
                 :red[4.]シュタイナー木上のuvパスから、辺を一つ削除する。  
                 """)
    
    st.divider()
    st.subheader("2-3.singlenode outtree mutation")

    with st.container(border=True):
        st.write("""
                 :red[手順]  
                 :red[1.]シュタイナー木以外から頂点wを一つ選ぶ。  
                 :red[2.]wを始点として、シュタイナー木に含まれない頂点と辺を使い2度自己回避ランダムウォークをする。   
                 :red[3.]シュタイナー木とぶつかったら、一回目のぶつかった点をu、二回目のぶつかった点をvとしランダムウォーク終了。
                 :red[4.]シュタイナー木上のuvパスから、辺を一つ削除する。  
                 """)
    st.caption("注意として、二度目のランダムウォークは、自己回避に加え、一度目のランダムウォークも回避する。")
    st.divider()

    st.subheader("2-3.doublenode intree mutation")
    with st.container(border=True):
        st.write("""
                 :red[手順]  
                 :red[1.]シュタイナー木以外から2頂点u,vを選ぶ。  
                 :red[2.]u,vを始点として、シュタイナー木に含まれない頂点と辺を使い2個同時にランダムウォーク。   
                 :red[3.]どちらかのランダムウォークが、もう一方のランダムウォークとぶつかったら、ランダムウォーク終了。
                 :red[4.]シュタイナー木上のuvパスから、辺を一つ削除する。  
                 """)
    st.caption("もう一方のランダムウォークの先端とぶつかるとは限らない。途中とぶつかった場合、はみ出ている部分のウォークはなかったことにする。")
    
    st.subheader("2-4.元のグラフを探索する突然変異")
    with st.container(border=True):
        st.write("""
                 :red[手順]  
                 :red[1.]シュタイナー木二つを交叉したものを一切考えず、大元のグラフに対して探索を行う。 
                 """)
    st.caption("改良の余地がありそう。シュタイナー木の一部分だけを破壊して、修復が済むまで元のグラフを探索するとか。")


def experiment():

    st.header(":red[3.実験]")
    st.divider()
    st.subheader("3-1.枝の剪定")
    st.write("1章で紹介した枝の剪定が、ある場合とない場合を比較してみる。")
    with st.container(border=True):
        st.write("""
                 :red[実験設定]  
                 - グラフモデル:BA  
                 - 頂点数:500  
                 - 辺数:2500 
                 - ターミナル数:20  
                 - 個体数:20  
                 - 世代数:500  
                 - 選択法:トーナメント選択(k=3)  
                 - 探索法:マルチスタートランダムプリム(開始頂点5つ)  
                 - 突然変異:single_intree_mutation
                 - 変異率:1%
                 """)
    
    st.write("データは、世代内の最高、全世代の最高、世代内の平均、世代内の最悪を取っている。")
    st.write("また、20世代目以降からデータを表示している。")    
    tab1, tab2,= st.tabs(["剪定なし", "剪定あり"])

    with tab1:
        st.image('images/mutation_exam/cut/nocut.png')

    with tab2:
        st.image('images/mutation_exam/cut/cut.png')

    st.write("""
             - 剪定の効果が絶大すぎる。こんなに変わるとは。
             - 整数計画に投げて1時間回したところ、lower boundが120くらいだったので、結構いい解が出ていると思う。
             """)
    
    st.divider()
    st.subheader("3-2.突然変異")
    st.write("突然変異四種と、突然変異がない場合を比較してみる。")
    with st.container(border=True):
        st.write("""
                 :red[実験設定]  
                 - グラフモデル:BA  
                 - 頂点数:500  
                 - 辺数:2500 
                 - ターミナル数:20  
                 - 個体数:20  
                 - 世代数:500  
                 - 選択法:トーナメント選択(k=3)  
                 - 探索法:マルチスタートランダムプリム(開始頂点5つ)  
                 - 変異率:0.01,0.05,0.1
                 """)
        
    tab1, tab2, tab3, tab4, tab5= st.tabs(["single_intree", "single_outtree", "double_intree","originalgraph","no-mutation"])

    with tab1:
        left,right = st.columns([1,1])
        with left:
            st.image('images/mutation_exam/single_intree/001.png')
            st.caption("変異率0.01")

            st.image('images/mutation_exam/single_intree/005.png')
            st.caption('変異率0.05')

        with right:
            st.image('images/mutation_exam/single_intree/01.png')
            st.caption('変異率0.1')

    with tab2:
        left,right = st.columns([1,1])
        with left:
            st.image('images/mutation_exam/single_outtree/001.png')
            st.caption("変異率0.01")

            st.image('images/mutation_exam/single_outtree/005.png')
            st.caption('変異率0.05')

        with right:
            st.image('images/mutation_exam/single_outtree/01.png')
            st.caption('変異率0.1')

    with tab3:
        left,right = st.columns([1,1])
        with left:
            st.image('images/mutation_exam/double_intree/001.png')
            st.caption("変異率0.01")

            st.image('images/mutation_exam/double_intree/005.png')
            st.caption('変異率0.05')

        with right:
            st.image('images/mutation_exam/double_intree/01.png')
            st.caption('変異率0.1')

    with tab4:
        left,right = st.columns([1,1])
        with left:
            st.image('images/mutation_exam/origingraphmutation/001.png')
            st.caption("変異率0.01")

            st.image('images/mutation_exam/origingraphmutation/005.png')
            st.caption('変異率0.05')

        with right:
            st.image('images/mutation_exam/origingraphmutation/01.png')
            st.caption('変異率0.1')

    with tab5:
        st.image('images/mutation_exam/nomutation/nomutation.png')

    st.write("""
             - 全体的に局所最適から抜けられてない印象。これについては次の章で考察。
             - originalgraphの突然変異について、特に変異率0.1は他と比べて特徴的な形をしている。  
               変異するたびに大きく適応度が揺らいでいるので、突然変異よりは強い摂動とかで使うべき？
            """)

    st.divider()
    st.subheader("3-3.局所最適から抜けられない理由考察")
    st.write("""
             実験結果では、なかなか局所から抜け出せていなかった。自分なりに考察してみた。  
             結論としては、トーナメント選択が悪さをしていると考えている。  
             突然変異をした個体は、ほかの個体より適応度が悪くなる。  
             この状態でトーナメント選択を行うと、突然変異が起きた個体はほとんど交叉の親に選ばれない。  
             その結果、突然変異した遺伝子を、次世代へ受け継ぐことができていないのではないか。
            """)
    
    st.write("解決策としてやってみようと思っていること列挙(未実装)")
    st.write(":green[・選択方法を変える]")
    st.write("""
             - ランキング選択をしてみる。  
             - 完全ランダムにk個個体を取ってきて、k個の中でランキング選択。  
              つまり、トーナメント選択とランキング選択のハイブリッド。
             """)
    
    st.write(":green[・突然変異のタイミングを変える]")
    st.write("""
             現状、交叉を終えた子個体に対して、突然変異をしている。   
             親個体に突然変異をした後交叉する、という順番にしたらどうか。
             """)
    
    st.write(":green[・悪い個体を意識的に残す]")
    st.write("""
             突然変異した個体を覚えておいて、その個体の選択の優先度を上げてみるとか。
             """)



def Steiner_Linear():

    st.header(":red[4.シュタイナー木用線形計画]")
    st.write("実装してみた(ほぼAIに丸投げ...)ので、コードと実行結果紹介")

    with open('materials/_third/pulp_test/pulp_Steiner.py','r',encoding='utf-8') as file:
        code = file.read()
    st.code(code)

    st.write("実行結果")
    with open('materials/_third/pulp_test/result.txt','r',encoding='utf-8') as file:
        code = file.read()
    st.code(code)

    st.write("試しに2時間、先ほどの実験と同じグラフに対して回してみた。")
    st.write("2時間かけて141に対し、GAは数十秒であの結果なので、やはりなかなかいいかもしれない。")
def idea():

    st.subheader("アイデアなど諸々")
    st.divider()

    st.write("""
             突然変異の遺伝子を残すための試行錯誤！
             """)