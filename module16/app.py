import streamlit
import streamlit as st

def main():
    st.title("Hello world")
    st.button("Click Here")
    if st.button("Click Me"):
        st.write("Button Clicked")
    if st.checkbox("Click"):
        st.write("Ticked")
    user_input = st.text_input("enter text", " ")
    st.write("you wrote", user_input,)
    age = st.number_input("Enter your age:", min_value=0 , max_value=100)
    st.write(f"your age is: {age}")

if __name__ == "__main__":
    main()

