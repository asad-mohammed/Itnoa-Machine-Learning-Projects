import streamlit as st

st.set_page_config(layout= "wide")

# Page Set Up
home_page = st.Page(page= "sections/home.py", title= "Home", icon= ":material/home:", default= True)
project_info_page = st.Page(page= "sections/project_information.py", title= "Project Information", icon= ":material/description:")
cancer_page = st.Page(page= "sections/cancer_prediction.py", title= "Cancer Prediction", icon= ":material/coronavirus:")
face_page = st.Page(page= "sections/face_detection.py", title= "Face Detection", icon= ":material/person:")
movie_page = st.Page(page= "sections/movie_recommendation.py", title= "Movie Recommendation", icon= ":material/theaters:")
music_page = st.Page(page= "sections/music_recommendation.py", title= "Music Recommendation", icon= ":material/music_note:")

# Navigation Set Up [With Sections]
pg = st.navigation(
    {
        "Main": [home_page],
        "Details": [project_info_page],
        "Projects": [cancer_page, face_page, movie_page, music_page]
    }
)

st.logo("datasets/itnoa_logo.png")
st.sidebar.markdown("""
Developed by <a href="https://www.linkedin.com/in/itnoa-mohammed-asad/" style="text-decoration: underline; color: blue;"><strong>**Mohammed Asad**</strong></a>
""", unsafe_allow_html=True)
# Run Navigation
pg.run()