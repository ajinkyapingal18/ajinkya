import streamlit as st

st.title("Simple chatbot")

Question=st.text_input("ask your question")

if st.button("send"):
    st.write("You asked:",Question)
    st.write("answer:ajinkya")