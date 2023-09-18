import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Selecting the page (Predict or Explore) using Streamlit's sidebar
page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

# Display the respective page based on the selection
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()