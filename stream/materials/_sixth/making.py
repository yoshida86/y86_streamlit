import streamlit as st

def making():

    st.header(':red[1.作ったもの]',divider="red")

    st.subheader("・ランダムプリム",divider="blue")
    st.write("プリム法の加える辺をランダムにしたもの。")
    with open('materials/_sixth/program/randprim.py','r',encoding='utf-8') as file:
        code = file.read()
    st.code(code)

    st.divider()

    st.write(":red[プチ解説]")
    st.write("""プリム法と同様に、何らかのデータ構造で探索候補の辺を管理する必要がある。  
            しかも、ランダムにするうえで、  
            :green[(1)ランダムアクセスが高速  
            (2)ランダムな要素の削除が高速  
            (3)要素の値からのアクセスが高速]  
            を同時にかなえる構造が欲しい。  
            今回は、リストをうまいこと使ってなんとかした。      
            """)
    
    st.write(""":green[(1)ランダムアクセスが高速]  
             リストはランダムアクセスに強いので問題なし。  
             :green[(2)ランダムな要素の削除が高速]  
             最後尾の要素を削除したい箇所に代入した後、最後尾の要素を削除することで定数時間化。  
             :green[(3)要素の値からのアクセスが高速]  
             探索候補リストとは別に、探索候補リスト内で各辺がどの位置(添え字)にいるかを管理するリストを作り、定数時間化。  """)
    
    st.subheader("・突然変異",divider="blue")
    st.write("重みが大きい辺を付け替えるやつ。")
    with open('materials/_sixth/program/mutation.py','r',encoding='utf-8') as file:
        code = file.read()
    st.code(code)

    
