import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,empty_col , col2 = st.columns([1.5,0.5,1.5])

with col1:
    st.image("images/photo.png",width=250)

with col2:
    st.title("Abhijeet.")
    content = """I am techno main Salt Lake student pursuing a B-tech in Artificial Intelligence and Machine Learning.
     I am enthusiastic learner and active listener. I am always curious about new technology in the industry .I know programming language like Python Cpp etc.
     My interest including web development, ethical hacking ,game development, Android and robotic."""
    st.info(content)

col3, empty_col1 , col4 = st.columns([1.5,0.5,1.5])

file = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in file[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index,row in file[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])