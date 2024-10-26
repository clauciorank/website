import os

import streamlit as st

from blog_posts.blog_posts_references import blog_posts

def display_personal_projects(language):
    st.title("Personal Projects/Blog")
    print('projects_file')
    print(os.getcwd())
    for post in blog_posts:
        with st.expander(f"{post[language]['title']}"):
            st.markdown(open(post[language]['file'], 'r').read(), unsafe_allow_html=True)