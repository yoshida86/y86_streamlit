import streamlit as st

def fiboexplain():

    st.header(':red[1-5.フィボナッチヒープ]')
    st.write('プリム法をより高速に実行する事が期待できるデータ構造。')
    st.write('元々は、最短経路問題の、ダイクストラ法を高速化するため考案されたもの...らしい。')
    st.caption('言われてみれば、プリム法とダイクストラ法は、やることがかなり似ている。')

    st.divider()

    st.subheader('・通常のヒープ')
    st.write('通常のヒープはこんなのだった。')
    st.image('.\images\_fiboheap\_fibo-1.png')
    st.write('・親ノードの値は、必ず子ノードの値より小さい')
    st.write('・一番上のノードを根といい、根にはヒープ内で最小の値をもつノードが来る')
    st.write('・一つのノードに対し、子ノードは二つまで')
    st.write('・各階層を左から順に並べていくことで、配列での表現が可能')
    

    st.divider()
    st.subheader('・概要')

    st.write('通常のヒープは、ノードの挿入や値の更新があったとき、そのノードを:red[「適切な位置に移動させる処理」]を行う。')
    st.write('フィボナッチヒープは、この:red[「適切な位置に移動させる処理」]をある種後回しにすることで、挿入や値の更新を、定数時間で行えるようにしたものである。')
    st.write('後回しにした操作は、最小値を取り出すときにまとめて行う。そのため、長いこと最小値取り出しが起こらないと、後回しにしたツケがまわってきて、逆に遅くなることがある点に注意が必要。')
    st.write('プリム法は、挿入や値の更新と、最小値取り出しがバランスよく起こることから、フィボナッチヒープを用いるのに適していると考えられる。')

    st.divider()

    st.subheader('・基本的な構造')
    st.write('「親の値が子の値よりも必ず小さくなる木構造」のことを、ヒープ構造ということにする。')
    st.write('また、説明する上で都合がいいので、根の子がn個のヒープを、H(n)と呼ぶことにする。')
    st.write('フィボナッチヒープのヒープ構造には、根が持つ子の数に応じて、テンプレート的な形がある。')
    st.image('.\images\_fiboheap\_fibo0.png')
    st.caption('例えばH(3)は、H(2)の根に、H(2)をくっつけている。このように、H(n+1)は、H(n)の根に、H(n)をくっつけた形がテンプレートとなる。')
    
    st.write('')
    st.write('"root":根となるノードを入れるリスト')
    st.write('"min":最小のノードを指すポインタ')
    
    st.image('.\images\_fiboheap\_fibo1.png')
    
    st.write('リスト"root"に入っている各根から、それぞれヒープ構造がぶら下がっているイメージ。')
    st.write('通常のヒープと違い、根が一個とか、子ノードは二つまでみたいな制約がない。')


    st.divider()
    
    st.subheader('・フィボナッチヒープの操作')
    st.write('プリム法にフィボナッチヒープを使う際、行う操作は、')
    st.write('(1)挿入(insert)')
    st.write('(2)最小値取り出し(delete-min)')
    st.write('(3)値の更新(decrease-key)')
    st.write('以上三つなので、順に見ていく。')

    st.divider()

    st.subheader('(1)挿入')
    with st.container(border=True):
        st.write(':red[手順]')
        st.write('1."root"に値を挿入する。')
        st.write('2.必要があれば、"min"を更新する。')
    

    st.write('1.')
    st.image('.\images\_fiboheap\_fibo2.png')
    st.caption('値1をrootに挿入')

    st.caption('3は2より大きいので、minの更新は必要ない')

    st.divider()

    st.subheader('(2)最小値取り出し')
    with st.container(border=True):
        st.write(':red[手順]')
        st.write('1.取り出したノードの子だったノードたちを全てrootに加える。')
        st.write('2.minのノードを取り出す。')
        st.write('3.rootから伸びるヒープ構造を全て確認し、もしH(k)が2個あったなら、それらを合成しH(k+1)を作成する。これを、「H(k)が複数個ある」が一切無くなるまで繰り返す。')
        st.write('※合成するときは、二つの根のうち、値の小さい方を根にする。')
        st.write('4.minを更新する。')

    st.image('.\images\_fiboheap\_fibo3.png')
    st.caption('minの子だった、6と10のノードをrootに加える')
    st.image('.\images\_fiboheap\_fibo4.png')
    st.caption('minだった2を取り出す')
    st.image('.\images\_fiboheap\_fibo5.png')
    st.caption('H(0)とH(1)が二つあるので、合成して、H(1)とH(2)を作る')
    st.image('.\images\_fiboheap\_fibo6.png')
    st.caption('合成したらH(2)が二つ出てきたので、合成してH(3)にする')
    st.image('.\images\_fiboheap\_fibo7.png')
    st.caption('被りが無くなったので、合成を終了して、minを更新する')

    st.divider()

    st.subheader('(3)値の更新')
    with st.container(border=True):
        st.write('操作の対象となっているノードをvとし、vの親ノードをpとする。')
        st.write(':red[手順]')
        st.write('1.値の更新があったノードをvとする。')
        st.write('2.vをrootに加え、もしvに印がついていれば印を外す。')
        st.write('3.pに印が、')
        st.write('i)ついていなかった時、pに印をつける。')
        st.write('ii)ついていた時、pをvとし、vに対して2～3を行う。')
        st.write('4.minを更新し、終了')

    st.image('.\images\_fiboheap\_fibo8.png')
    st.caption('元々8だった値が1になった。これをv、親をpとする')
    st.image('.\images\_fiboheap\_fibo9.png')
    st.caption('vをrootに加える')
    st.image('.\images\_fiboheap\_fibo10.png')
    st.caption('pに印がついていないので、印をつける')
    st.image('.\images\_fiboheap\_fibo11.png')
    st.caption('minを更新する')

    st.divider()

    st.write('参考資料:')
    st.write('Kevin Wayne "Fibonacci Heaps" 2007')
    st.write('https://www.cs.princeton.edu/~wayne/teaching/fibonacci-heap.pdf')

