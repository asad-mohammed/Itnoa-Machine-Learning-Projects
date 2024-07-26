import streamlit as st
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from PIL import Image
from io import BytesIO

def movie_recommendation():

    # Load the data
    movies_data = pd.read_csv('datasets/movies.csv')
    movies_list = movies_data['title'].values

    # Preprocess the data
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')

    combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)

    similarity = cosine_similarity(feature_vectors)

    # Function to get movie poster from OMDB API
    def get_poster_url(title):
        api_key = st.secrets["OMDB_API_KEY"]
        search_url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'
        response = requests.get(search_url)
        data = response.json()
        if 'Poster' in data and data['Poster'] != 'N/A':
            return data['Poster']
        return None

    # Streamlit app
    st.title('Movie Recommendation')

    option = np.append(movies_list, ["Enter your own movie name"])
    movie_name = st.selectbox("**Select a movie from the list or Enter your own:** (Select the option 'Enter your own movie name' to enter your own)", options=option, index=None)

    if movie_name == "Enter your own movie name":
        movie_name = st.text_input('**Enter a movie name:** (Press Enter before clicking the recommend button)')

    if st.button('Recommend'):
        list_of_all_titles = movies_data['title'].tolist()
        find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
        if find_close_match:
            close_match = find_close_match[0]
            index_of_the_movie = movies_data[movies_data.title == close_match].index[0]
            similarity_score = list(enumerate(similarity[index_of_the_movie]))
            sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
            st.write('Movies suggested for you:')
            cols = st.columns(5)
            for i, movie in enumerate(sorted_similar_movies[1:6]):
                index = movie[0]
                title_from_index = movies_data.iloc[index]['title']
                poster_url = get_poster_url(title_from_index)
                with cols[i]:
                    if poster_url:
                        try:
                            image = Image.open(BytesIO(requests.get(poster_url).content))
                            st.image(image, caption=title_from_index, use_column_width=True)
                        except Exception as e:
                            st.write(title_from_index)
                            st.warning(f"Failed to load image: {e}")
                    else:
                        st.write(title_from_index)
        else:
            st.write('No matching movies found.')

movie_recommendation()
