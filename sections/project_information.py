import streamlit as st
from streamlit_option_menu import option_menu
from info_projects import info_cancer
from info_projects import info_face
from info_projects import info_movie
from info_projects import info_music

def project_information():
    st.title("Project Information")

    selected = option_menu(
        menu_title=None,
        options = ["Cancer Prediction", "Face Detection", "Movie Recommendation", "Music Recommendation"],
        icons=["virus2", "person-bounding-box", "film", "music-note-beamed"],
        orientation="horizontal"
    )
    
    if selected == "Cancer Prediction":
        info_cancer.cancer_prediction_info()
    elif selected == "Face Detection":
        info_face.face_detection_info()
    elif selected == "Movie Recommendation":
        info_movie.movie_recommendation_info()
    elif selected == "Music Recommendation":
        info_music.music_recommendation_info()

project_information()