import streamlit as st
from text_files.about_me import about_me_info
from text_files.skills import skills_title, skills, skills_description
from text_files.education import display_education

def display_about_page(language):
    st.title("Claucio Antonio Rank Filho")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('contents/images/profile_picture.png', width=200)
    with col2:
        st.title(about_me_info[language]["title"])
        st.write(about_me_info[language]["description"])

    # Skills
    st.title(skills_title[language])
    st.write(skills_description[language])

    # Work Experience


    # Education
    st.title("Education")
    education_info = display_education(language)
    st.write(education_info)
