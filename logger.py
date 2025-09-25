import streamlit as st
import time

st.header("st.info")
st.info("Information display info")

st.header("st.success")
st.success("Information display success")

st.header("st.warning")
st.warning("Information display warning")

st.header("st.error")
st.error("Information display error")

time.sleep(2)
st.balloons()