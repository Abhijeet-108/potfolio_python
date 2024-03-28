import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png",width=250)

with col2:
    st.title("Abhijeet.")
    content = """I am techno main Salt Lake student pursuing a B-tech in Artificial Intelligence and Machine Learning.
     I am enthusiastic learner and active listener. I am always curious about new technology in the industry .I know programming language like Python Cpp etc.
     My interest including web development, ethical hacking ,game development, Android and robotic."""
    st.info(content)

