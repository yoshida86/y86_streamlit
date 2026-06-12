import streamlit as st

def rintro():

    st.header(':red[1.R言語]')

    st.subheader(':red[1-1.Rのインストール]')
    st.markdown('Rは、CRAN(Comprehensive R Archive Network)のウェブページから入手できる。')
    st.markdown('CRANのウェブページ: https://cran.r-project.org/')
    st.markdown('ミラーサイトが色々ある。その中から何となく信用できそうなところを使ってインストールすればOK')
    st.code('> print("HELLO WORLD!") \n [1] "HELLO WORLD!"')
    st.caption('恒例行事')

    st.divider()
    
    st.subheader(':red[1-2.パッケージのインストール]')
    st.markdown('Rには、pythonのように、パッケージが色々存在する。')
    st.markdown('ひとまず今回は、ネットワーク解析に便利なsna、igraph、statnetというパッケージをインストールしてみる。')
    st.markdown('インストールは以下のコードで行える。()内の名称を変えることで、別のパッケージもインストールできる。')
    st.code("install.packages('statnet')")

    st.divider()

    st.subheader(':red[1-3.四則演算等、基本的な操作]')
    st.markdown('四則演算などは、大抵のプログラミング言語と同様。')
    with open('history/_second/test.R','r',encoding='utf-8') as file:
        data = file.read()
    st.code(data)
    st.markdown('特徴的だと感じたのは挿入操作。')
    st.markdown('例えばaに1を代入したいときは、=ではなく、<-を用いて、以下のように書く。')
    st.code('a <- 1')
    st.markdown('これを使って、それっぽく操作を書くとこんな感じ。')
    st.code('> a <- 1 \n> b <- 2 \n> a + b \n[1] 3')

    st.divider()
    
    st.subheader(':red[1-4.Rの特徴]')
    st.markdown('Rの特徴として、変数を、ベクトルや行列の形でもつ機能がある点があげられる。')
    st.markdown('例えば以下のようなコードで、横ベクトル(1,2,3)のデータをもてる。')
    st.code('v <- c([1,2,3])')
    st.write('また、以下のようなコードで、一行目(1,2,3)、二行目(4,5,6)の行列のデータをもてる')
    st.code("m <- matrix(c(1,2,3,4,5,6),nrow=2,ncol=3,byrow=TRUE)")
    st.markdown('ここで、nrowとncolは行列の行数と列数、byrowはTRUEにすることで、成分を行方向に並べることができる。')
    st.markdown('行列の転置をt(m)で取ってきたり、行列の積の演算子%*%もあったりなど、行列に対する操作もいろいろ用意されている。')

    st.divider()

    st.write('参考文献:')
    st.write('鈴木努、「ネットワーク分析 第2版 (Rで学ぶデータサイエンス 8)」、金明哲編、共立出版')





    