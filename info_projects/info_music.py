import time
import pickle
import streamlit as st

def music_recommendation_info():
    st.title("Music Recommendation Information")

    # Introduction
    st.header("Introduction")
    st.write("""
    This music recommendation system helps users discover songs similar to a selected song.
    The model uses a precomputed similarity matrix to recommend songs based on their features.
    Additionally, the app integrates with the Spotify API to fetch and display album covers of the recommended songs.
    """)

    # Dataset
    st.header("Dataset")
    st.write("""
    The dataset used for this project contains information about various songs, including their titles and artists.
    These features are used to create a similarity matrix that helps in recommending similar songs.
    Below is a sample of the dataset:
    """)

    # Load the data
    music = pickle.load(open('models/df_music.pkl', 'rb'))
    st.dataframe(music)

    # Code Explanation
    st.header("Code Explanation")
    st.write("""
    The main steps in the code are as follows:
    1. **Load Environment Variables**: Load API keys and other environment variables using the `dotenv` package.
    2. **Retrieve Credentials**: Retrieve the Spotify API credentials from environment variables.
    3. **Initialize Spotify Client**: Initialize the Spotify client using the retrieved credentials.
    4. **Fetch Album Cover**: Define a function to fetch album covers using the Spotify API.
    5. **Recommend Songs**: Define a function to recommend songs based on the similarity matrix.
    6. **Streamlit App**: Set up the Streamlit interface for user interaction.
    7. **Display Recommendations**: Use the Spotify API to fetch and display album covers of the recommended songs.
    """)

    # API Used
    st.header("API Used")
    st.write("""
    The Spotify API is an online service that provides access to a wide range of music data, including tracks, albums, artists, and playlists.
    The API is accessible through HTTP requests, making it easy to integrate into various applications.

    **How it works:**
    1. **Authentication**: The API requires OAuth authentication. For server-to-server communication, Client Credentials Flow is used.
    2. **Search**: The API allows searching for tracks, albums, and artists using query parameters.
    3. **Fetch Album Cover**: The API returns album cover URLs, which can be used to display images in the app.

    **Advantages:**
    - Provides comprehensive music data.
    - Easy to use and integrate with various applications.
    - Reliable and frequently updated database.
    - Supports multiple types of data, including tracks, albums, and playlists.

    Example API request:
    ```
    https://api.spotify.com/v1/search?q=track:Shape+of+You%20artist:Ed+Sheeran&type=track
    ```
    """)

    # Conclusion
    st.header("Conclusion")
    st.write("""
    This music recommendation system leverages precomputed similarity matrices to provide personalized music recommendations based on user input.
    The integration with the Spotify API enhances the user experience by displaying album covers alongside the recommendations.
    This project demonstrates the power of combining machine learning techniques with external APIs to build a useful and engaging application.
    """)

    st.write("To run the model click the button below")
    if st.button(label= ":blue[**Run Music Recommendation**]"):
        st.switch_page("sections/music_recommendation.py")

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
