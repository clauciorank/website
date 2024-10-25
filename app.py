import streamlit as st
from pagina import about_page

st.set_page_config(page_title="Claucio Antonio Rank Filho")


st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["About", "Projects", "Contact"])

language = st.sidebar.selectbox("Select language", options=["English", "Portuguese"])

if page == "About":
    about_page.display_about_page(language)