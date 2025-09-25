import streamlit as st

st.header("Display Image")
st.image("./steak.jpg",caption="steak")

st.header("Display video")
video_file = open("./.mp4",'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.header("Display Audio")
Audio_file = open("./.mp3",'rb')
Audio_bytes = Audio_file.read()

st.audio(Audio_bytes)