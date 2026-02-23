import streamlit as st

st.markdown("""
<style>
            
            .stButton > button
            {
            background-color:"green";
            color:"white;
            border-radius:50%;
            }

<style/>          



""",unsafe_allow_html=True)


name=st.text_input("enter your name")
DOB=st.date_input("enter dob")
age=st.age_input("enter your age")
add=st.add_input("enter your address")




st.title("welcome to basic straemlit app")


age =st.slider("select your age",1,100)
city=st.selectbox("select your city",["delhi","mumbai","nashik"])

if st.button("show details"):
    st.write("age",age)
    st.write("city",city)