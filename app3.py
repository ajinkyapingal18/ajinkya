import streamlit as st

st.title("Basic Calculator")

num1=st.number_input("enter your first number",step=1,format=%d)
num2=st.number_input("enter your second number",step=2,format=%d)

Operation=st.selectbox("choose Op",["add","sub","mul","div"])

if st.button("calculator"):
    if Operation == "add":
        st.write(num1+num2)


    elif Operation == "sub":
        st.write(num1-num2)

    elif Operation == "mul":
        st.write(num1*num2)

    elif Operation == "div":
        st.write(num1/num2)

    else:
        st.write("cannot divide by zero")