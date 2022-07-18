import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]  
    distances = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, recommended_movies_poster

similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('type your movie',movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    # for i in recommendations:
    #     movie_id = i[0]
        # fetch poster from api
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    # st.write(i)