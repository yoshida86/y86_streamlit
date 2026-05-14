import streamlit as st
def MLexplain():


        
    st.header('MLconverter')
    st.write('隣接行列や隣接リストのcsvを変換できるやつを作ってみました。')
    st.write(':red[重み付き非対応。これから拡張させます。]')
    
    
    with st.container(border=True):
        st.write('・想定しているcsvの形')
        lcode,mcode = st.columns(2)

        with lcode:
                
            with open('data\_first\list.csv') as l:
                code1 = l.read()
            st.caption('隣接リスト')
            st.code(code1)
            st.caption('行の先頭に頂点番号、2要素目から隣接頂点番号')
            
            
        with mcode:
                
            with open('data\_first\matrix.csv') as m:
                code2 = m.read()
            st.caption('隣接行列')
            st.code(code2)
            st.caption('隣接行列の要素のみ')
        

    st.write(':blue[この形がスタンダードなのかわからないので、どういう形を想定するといいかフィードバックが欲しいです。]')
        
    st.divider()

    st.subheader('使い方')
    st.write('1. ぺージ"MLconverter"を開く')
    st.write('2. csvを投げる。参照でもドラッグアンドドロップでもOK')
    st.caption('※隣接行列か隣接リストかで、投げる位置が分かれているので、そこだけ注意。')
    st.write('3.変換ボタンを押して待つ')
    st.write('4.ダウンロードボタンが出てきたら、押してダウンロード')


