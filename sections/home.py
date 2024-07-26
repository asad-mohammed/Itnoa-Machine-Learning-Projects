import streamlit as st

st.title("My Machine Learning Projects")

# Including Font Awesome
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<i class="fas fa-diagnoses fa-3x"></i>', unsafe_allow_html=True)
    st.page_link("sections/cancer_prediction.py", label=  "##### :blue[**Cancer Prediction**]")
    st.write("Predicts the likelihood of cancer based on user-provided medical features.")
    
    st.write("\n")

    st.markdown('<i class="fas fa-music fa-3x"></i>', unsafe_allow_html=True)
    st.page_link("sections/music_recommendation.py", label=  "##### :blue[**Music Recommendation**]")
    st.write("Suggests songs based on user-selected music, with album covers via the Spotify API.")


with col2:
    st.markdown('<i class="fas fa-user-secret fa-3x"></i>', unsafe_allow_html=True)
    st.page_link("sections/face_detection.py", label=  "##### :blue[**Face Detection**]")
    st.write("Detects faces in images captured via camera or uploaded by the user.")

    st.write("\n")

    st.markdown('<i class="fa-regular fa-file-lines fa-3x"></i>', unsafe_allow_html=True)
    st.page_link("sections/project_information.py", label=  "##### :blue[**Project Information**]")
    st.write("Detailed insights into Machine Learning projects.")



with col3:
    st.markdown('<i class="fas fa-film fa-3x"></i>', unsafe_allow_html=True)
    st.page_link("sections/movie_recommendation.py", label=  "##### :blue[**Movie Recommendation**]")
    st.write("Recommends movies based on user-selected movie, with posters via OMDB API.")

