import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your E-mail")
    raw_message = st.text_area("Your messages")
    message = raw_message + "\n" + user_email

    buttom = st.form_submit_button("Submit")
    if buttom:
        send_email(message)
        st.info("Your email sent successfully!!")

