import streamlit as st
import time


st.header("Status bar")
st.caption("progress bar display")
st.progress(50)

my_bar = st.progress(0)
for i in range(1,101):
    time.sleep(0.05)
    my_bar.progress(i)
print("------------------------")
def bar_progress():
    for i in range(1,101):
        time.sleep(0.05)
        my_bar.progress(i)


with st.spinner("Some thing in progress"):
    my_bar = st.progress(0)
    bar_progress()

    
    