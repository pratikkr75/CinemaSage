import streamlit as st
import pickle
import requests
import time

def fetch_movie_details(movie_id):
    api_key = 'fa879729aab09ad7cce01dceed717e55'
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
    data = response.json()
    poster_url = "http://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')
    release_date = data.get('release_date', 'N/A')
    genres = ', '.join([genre['name'] for genre in data.get('genres', [])])
    overview = data.get('overview', 'No overview available.')
    return poster_url, release_date, genres, overview


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

        recommended_movies = []
        recommended_movies_details = []
        for i in movie_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            poster_url, release_date, genres, overview = fetch_movie_details(movie_id)
            recommended_movies_details.append((poster_url, release_date, genres, overview))
        return recommended_movies, recommended_movies_details
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return [], []


movies = pickle.load(open('movies (1).pkl','rb'))
similarity = pickle.load(open('similarity (1).pkl','rb'))

movies_list = movies['title'].values

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies_list)

if st.button("Recommend"):
    with st.spinner('Fetching recommendations...'):
        time.sleep(1)  # simulate a delay for loading indicator
        names, details = recommend(selected_movie_name)

    if names:
        for i in range(len(names)):
            st.write("###")
            poster_url, release_date, genres, overview = details[i]
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(poster_url)
            with col2:
                st.text(f"Title: {names[i]}")
                st.text(f"Release Date: {release_date}")
                st.text(f"Genres: {genres}")
                st.write(f"Overview: {overview}")
    else:
        st.warning("No recommendations found.")