import streamlit as st
import pandas as pd
import time

side_bar = st.sidebar

side_bar.header("This side bar")
side_bar.caption("element that we need to be added in side bar")

st.write("This is main page")

df = pd.read_csv("./train.csv")
st.dataframe(df)

columns = df.columns.to_list()
st.info(columns)

#create wedget select bar

select_column = side_bar.selectbox("select column you want to display",columns)
st.dataframe(df[[select_column]])

col1,col2,col3 = st.columns(3)

with col1:
    st.image("./steak.jpg")

with col2:
    st.dataframe(df[[select_column]])


st.write("st.expander")
with st.expander("some explanization about work"):
    st.write("india is more powerful country than other nations in the wordcccccbcgttvneecgbdgcibcrllnbhlidedfighjhjlbh" \
    "")
    st.code("""
            import numpy as np""")