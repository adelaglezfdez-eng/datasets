import streamlit as st
import pandas as pd
st.title("hello world web")
st.write("hello world streamlit")
dataframe = pd.read_csv("https://raw.githubusercontent.com/adelaglezfdez-eng/datasets/refs/heads/main/titanic.csv")
st.dataframe(dataframe)
