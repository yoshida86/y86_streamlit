import streamlit as st

def flo():

    st.header(':red[2.フローチャート上の各操作の計算量]',divider="red")

    st.write("""
             簡単にではあるが、計算量の評価をしたい。\n
             元のグラフの超点数をV,辺数をE、集団の要素数をN、世代数をgenとする。\n
             フローチャートはこんな感じだった。
             """)
    
    st.image('images/evomst/changeflo.jpg')
    st.image('images/evomst/flo1.jpg')
    st.image('images/evomst/flo2.jpg')
    
    st.divider()

    st.subheader('・Vから隣接リストもどきAを生成',divider="green")
    st.write('エッジリストを上から見ていくだけなので、O(E)')

    st.subheader('・元のグラフにbfsしてtを生成し、tの評価を計算',divider="green")
    st.write("""
             1.キューにすべての点が一回入って出るので、2V回\n
             2.また、最悪ですべての辺を一度見るので、E回\n
             3.評価は、辺の重みをエッジリストを使って足していくので、E回\n
             これらを足し合わせて、2V+2E回\n
             この操作はN回行われるので、O(N(V+E))
             """)
    
    
    
    st.subheader('・ランダムに木を二つ選んで足し、gを生成',divider="green")
    st.write('ベクトルにorをするだけなので、O(E)')
    st.write('この操作は世代数分やるので、O(gen*E)')

    st.subheader('・gにbfsし、評価を計算',divider="green")
    st.write("""
             gは全域木を二つ足し合わせたものだった。
             全域木の辺数はV-1なので、gの辺数も高々2(V-1)となる。\n
             このことから、bfs部分は、O(V)
             評価は、エッジリストを見るので、O(E)\n
             これらの操作は世代数分起きるので、O(gen(V+E))
             """)
    
    st.subheader('・評価を比較し、必要があれば要素を交換',divider="green")
    
    st.write("""
             評価が最悪の木を管理する手段が必要。
             メジャーなところだとヒープなので、ヒープを想定して考える。\n
             このヒープは集団の要素を管理するので、要素数はN個となる。そのため、ヒープの構築にO(NlogN)\n
             ヒープの操作は最高でgen回起こりうるので、O(gen*logN)\n
             以上を足し合わせて、O((N+gen)logN)
             """)
    
    st.divider()

    st.header(':red[まとめ]',divider="red")
    st.write("""
             以上のオーダーをすべて足し合わせると、\n
             O(E) + O(N(V+E)) + O(gen*E) + O(gen(V+E)) + O((N+gen)logN) = :red[O((N+gen)(V+E+logN))]\n
             """)
    with st.container(border=True):
        st.write("""
                 ・Nとgenは、こちらで設定できる値。\n
                 ・二乗とか、遅くなりそうなものがない。\n
                 ・一通り計算量を追った感じ、係数の部分がそんなに大きくない。\n
                  """)
            
    st.write("""
             以上の点から、結構早いんじゃね？と思ったので、この方針で実装を進める。
             実際に実装した時には、またちゃんと評価したい。
             """)
             
    






    