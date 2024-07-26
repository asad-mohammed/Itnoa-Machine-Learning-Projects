import streamlit as st
import pandas as pd
import time


def movie_recommendation_info():
    st.title("Movie Recommendation Information")

    # Introduction
    st.header("Introduction")
    st.write("""
    This movie recommendation system helps users find movies similar to a given movie title. 
    The model uses a combination of genres, keywords, tagline, cast, and director to determine movie similarity.
    The system leverages TF-IDF Vectorization and Cosine Similarity for feature extraction and similarity computation, respectively.
    Additionally, the app integrates with the OMDB API to fetch and display movie posters.
    """)

    # Dataset
    st.header("Dataset")
    st.write("""
    The dataset used for this project contains information about various movies, including their genres, keywords, tagline, cast, and director.
    These features are combined to create a comprehensive representation of each movie for the recommendation system.
    Below is a sample of the dataset:
    """)
    
    # Load the data
    movies_data = pd.read_csv('datasets/movies.csv')
    st.write(movies_data)

    # Code Explanation
    st.header("Code Explanation")
    st.write("""
    The main steps in the code are as follows:
    1. **Load Environment Variables**: Load API keys and other environment variables using the `dotenv` package.
    2. **Load and Preprocess Data**: Load the movie dataset and fill missing values in the selected features.
    3. **Combine Features**: Combine genres, keywords, tagline, cast, and director into a single string for each movie.
    4. **Feature Extraction**: Use TF-IDF Vectorization to convert text data into feature vectors.
    5. **Compute Similarity**: Calculate the cosine similarity between movie feature vectors.
    6. **Get Movie Poster**: Define a function to fetch movie posters from the OMDB API.
    7. **Streamlit App**: Set up the Streamlit interface for user interaction.
    8. **Movie Recommendation**: Use the cosine similarity scores to recommend movies similar to the selected or entered movie.
    """)

    # OMDB API
    st.header("OMDB API")
    st.write("""
    The OMDB (Open Movie Database) API is an online service that provides detailed information about movies and TV shows. 
    It includes data such as movie posters, plot summaries, cast and crew details, and much more. 
    The API is accessible through HTTP requests, making it easy to integrate into various applications.

    **How it works:**
    1. **Request**: The API request is made using the movie title and API key.
    2. **Response**: The API returns a JSON response containing the movie details.
    3. **Poster URL**: The poster URL is extracted from the JSON response to display the movie poster.

    **Advantages:**
    - Provides comprehensive movie and TV show data.
    - Easy to use and integrate with various applications.
    - Reliable and frequently updated database.
    - Supports multiple languages and regions.

    Example API request:
    ```
    http://www.omdbapi.com/?t=Inception&apikey=your_api_key
    ```
    """)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    This movie recommendation system leverages TF-IDF Vectorization and Cosine Similarity to provide personalized movie recommendations based on user input.
    The integration with the OMDB API enhances the user experience by displaying movie posters alongside the recommendations.
    This project demonstrates the power of combining natural language processing techniques with external APIs to build a useful and engaging application.
    """)

    st.write("To run the model click the button below")
    if st.button(label= ":blue[**Run Movie Recommendation**]"):
        st.switch_page("sections/movie_recommendation.py")

    # Back to Top Button
    js = '''
    <script>
        var body = window.parent.document.querySelector(".main");
        console.log(body);
        body.scrollTop = 0;
    </script>
    '''

    if st.button(label= ":blue[**Back to top**]"):
        temp = st.empty()
        with temp:
            st.components.v1.html(js)
            time.sleep(.5) # To make sure the script can execute before being deleted
        temp.empty()
