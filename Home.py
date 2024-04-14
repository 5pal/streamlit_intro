import streamlit as st

st.title("Hello, world!")
st.subheader("Hello, world!")
st.markdown(
    """
  ### I Love it
  ## This is my first time
  ### Markdown in streamlit
  #### Ever
"""
)

st.write("Hello, *World!* :sunglasses:")

st.selectbox("Select a Model", ("GPT-3", "GPT-4"))
