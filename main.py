import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("プログレスバーの表示")
"Start!!"

latest_interaction=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_interaction.text(f"Interaction {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!!!"

left_column,right_column=st.beta_columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_column.wright("ここは右カラム")

expander1=st.beta_expander("問い合わせ１")
expander1.wright("問い合わせ1の解答")
expander2=st.beta_expander("問い合わせ2")
expander2.wright("問い合わせ2の解答")
expander3=st.beta_expander("問い合わせ3")
expander3.wright("問い合わせ3の解答")