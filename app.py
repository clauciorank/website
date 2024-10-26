import streamlit as st
from pagina import about_page
from pagina import personal_projects
import os

st.set_page_config(page_title="Claucio Antonio Rank Filho")

navigation = [
    "About",
    "Personal Projects/Blog",
    "Events",
    "Contact"
]

language = st.sidebar.selectbox("Select language", options=["English", "Portuguese"])

st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", navigation)

if page == "About":
    about_page.display_about_page(language)

elif page == "Personal Projects/Blog":
    print('app file')
    print(os.getcwd())
    personal_projects.display_personal_projects(language)