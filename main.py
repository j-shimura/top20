import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title("上限電圧、下限電圧 プロットApp")

st.write("インポートするCSVの注意点")

img = Image.open("image2.png")
st.image(img, caption="CSVに関する注意事項", use_column_width=True)

uploaded_file = st.file_uploader("CSVファイルのアップロード", type={"csv", "txt"})
if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
#st.write(uploaded_df)

if uploaded_file:
    # メインとなるCSV
    dat1 = uploaded_df
    # 編集用のCSV
    dat2 = uploaded_df
    st.write("アップロードしたCSVファイル")
    # アップロードしたCSVファイルを表示
    dat1

    # テキスト入力
    target = st.text_input('特徴量選択（例：ci）')
    # テキストを入力したら実行開始
    if target:

        st.write("目的の特徴量を軸に昇順にCSVを変換")
        # 特徴量Ciを軸に昇順に変換
        df = dat2.sort_values(target, ascending=False)
        # 選択した特徴量を軸に昇順に変換したCSVを表示
        df
        
        # 変数に格納
        vu = dat1["vu"]
        vl = dat1["vl"]
        time = dat1["time"]

        # 軸となる行数リスト
        column_lis = list(df.iloc[0:20,0])
        #column_lis

        st.write("上限電圧と下限電圧をプロットした画像の表示")

        # 上限電圧と下限電圧の上位20をプロットで表示 
        for i in range(20):
            plt.rcParams['figure.figsize'] = (40, 20)
            fig = plt.figure()
            x = column_lis[i] - 6
            y = column_lis[i] + 6
            plt.title("feature" + " " + "%02.f"%(i+1) + " " + "rank", fontsize=32)
            plt.scatter(time[x:y], vu[x:y])
            plt.scatter(time[x:y], vl[x:y])
            st.pyplot(fig)