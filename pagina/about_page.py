import streamlit as st

# Information dictionary with translations
about_me_info = {
    "English": {
        "title": "About Me",
        "description": (
            "Welcome! I'm Your Name, a Data Scientist with a background in physiology and a passion for automation and AI. "
            "I specialize in data analysis, machine learning, and have a strong interest in applied AI solutions."
        )
    },
    "Portuguese": {
        "title": "Sobre Mim",
        "description": (
            "Bem-vindo! Sou Seu Nome, um Cientista de Dados com formação em fisiologia e paixão por automação e IA. "
            "Eu me especializo em análise de dados, aprendizado de máquina e tenho um forte interesse em soluções de IA aplicadas."
        )
    }
}

def display_about_page(language):
    st.title("Claucio Antonio Rank Filho")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('contents/images/profile_picture.png', width=200)
    with col2:
        st.title(about_me_info[language]["title"])
        st.write(about_me_info[language]["description"])

    st.header("Skills")

    st.write(
        "I have experience with the following tools and technologies:"
    )

    st.write(
        "- **Programming Languages**: Python, SQL"
    )

    st.write(
        "- **Data Analysis Libraries**: Pandas, Numpy, Scipy, Scikit-learn, Statsmodels"
    )

    st.write(
        "- **Data Visualization Libraries**: Matplotlib, Seaborn, Plotly, Streamlit"
    )
