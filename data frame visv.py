import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("train.csv")

st.header('st dataframe')
st.caption("Display a dataframe as an interative table")
st.dataframe(data = df)

st.header('st table')
st.caption("Display a dataframe")
st.table(data = df.head(5))

st.header('st Json')
st.caption("Display a dataframe as json")

json_value = df.head(5).to_dict()
st.json(json_value)