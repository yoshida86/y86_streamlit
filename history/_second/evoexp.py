import streamlit as st

def evoexp():

    st.header(':red[2.進化計算でMSTを近似したい]')

    st.write('遺伝的アルゴリズムを使って、全域最小木の近似解を求めてみたい。')
    st.write('ということで、話を整理して実装の準備をする。')

    st.divider()

    st.subheader(':red[2-1.現在構想している手順]')
    with st.container(border=True):
        st.write(':red[手順:]')
        st.write('1.bfsで元のグラフを探索して適当に木を作る。これを、bfsの条件を変えつつ繰り返すことで、適当に作った木の集合Tを用意する。')
        st.write('2.Tの中から何かしらの方法で二つ選び、その二つの木に含まれる辺のみをすべて含んだ、新たな全域部分グラフGを作る。')
        st.write('3.Gをbfsで探索して適当に木を作り、Tの中で最も優秀でない木と比較。それより優秀なら、それと入れ替える形でTに加える。')
        st.write('4.2と3を十分な回数繰り返し、MSTの近似を行う。')

    st.divider()

    st.subheader(':red[2-2.手順の整理]')

    st.write('手順中で色々あいまいな部分があるので、一つ一つ挙げながら整理する。')

    st.write(':green[・bfsをする際のランダム性の確保]')
    st.write('探索を開始する点を変える。また、隣接している点のうち、どの点から探索するかをランダムにすることで、ランダム性を確保できるのではないか。')
    st.write(':green[・Tから2つ選ぶ方法]')
    st.write('ひとまず完全ランダムに選ぶ方法で実装してみる予定。')
    st.write(':green[・ここでいう「優秀な木」の評価基準]')
    st.write('MSTの特徴から、一番直感的なのは辺の重みの総和での評価なので、まずはそれで評価をする方法で実装する。この場合、スコアは低いほど優秀ということになる。')
    st.write(':green[・T中のグラフの表現方法]')
    st.write('辺の有無をブール値で表す、ベクトルで表現する。')

    st.divider()

    st.subheader(':red[2-3.実装方法の整理]')
    st.write('・元のグラフに含まれない辺は考えなくてよい。よって、元のグラフを表現すると、すべての要素が1となるようなベクトルを用意するのが効率的と思われる。')
    st.write('・ベクトルの何番目の要素が、どの辺を表すのかの対応表が必要なため、隣接行列から対応表を生成する関数も実装する必要がある。')
    st.write('・bfsをするにあたって、頂点から伸びている辺をまとめた、隣接リストもどきも必要そう。これを生成する関数も用意したい。')
    
    st.divider()

    st.subheader(':red[2-4.ここまでのまとめ]')
    st.write('フローチャートにしてみた。')
    st.image('images/evomst/fro1.png')
    st.image('images/evomst/fro2.png')
    st.image('images/evomst/fro3.png')

    st.divider()

    st.subheader(':red[2-5.進捗]')
    st.write('とりあえず、隣接行列から対応表と隣接リストもどきを作るところまで実装。')
    with open('history/_second/setdata.py','r',encoding='utf-8') as file:
        code = file.read()
    st.code(code)

    st.divider()

    st.subheader('今後やりたいこと')
    st.write('・bfsと進化計算部分を実装して、一旦完成させたい。')
    st.write('探索方法をdfsにしたりなど、色々条件を変えたバージョンの実装。')
    st.write('・遺伝的アルゴリズムの、突然変異的な話を全く盛り込めていない。ある程度形が整ったら、そういう話も盛り込んでいきたい。')
    