import streamlit as st
import time

place_holder = st.empty()

for i in range(3,-1,-1):
    place_holder.write(i)
    time.sleep(5)

place_holder = st.empty()