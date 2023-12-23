import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommended_movies

# Load the data
movies_dict = pd.read_pickle('movies_dict.pkl')
movies = pd.DataFrame(movies_dict)
similarity = pd.read_pickle('similarity.pkl')

st.title('ML Model of Movie Recommendation')

# Display a select box for choosing a movie
selected_movie_name = st.selectbox(
    'Select or Type the Movie You Want',
    movies['title'].values
)

if st.button('Search'):
    # Check if a movie is selected
    if selected_movie_name:
        # Get recommendations for the selected movie
        recommendations = recommend(selected_movie_name)

        # Display the recommended movies with numbering and red color
        if recommendations:
            st.markdown(f"<p style='color:red'>Recommended movies for '{selected_movie_name}':</p>", unsafe_allow_html=True)
            for idx, recommended_movie in enumerate(recommendations, start=1):
                st.write(f"{idx}. {recommended_movie}")
        else:
            st.write("No recommendations found.")
    else:
        st.write("Please select a movie.")
