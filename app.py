# import streamlit as st

import streamlit as st
import pandas as pd
import numpy as np
import math
import random
import pickle

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    for i in movie_list:
        
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies



movie_dic = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movie_dic)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommend System')
# st.write('Hi!')
Movie_name_by_user = st.selectbox(
    "Chose Your Prefer Movie",
    movies['title'].values
)

if st.button('Recommend'):
    recommendaions = recommend(Movie_name_by_user)
    for i, index in enumerate(recommendaions):
        st.write(i+1,index)
